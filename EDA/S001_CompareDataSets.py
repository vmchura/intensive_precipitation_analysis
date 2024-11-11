import pandas as pd
from dotenv import load_dotenv
import os
import netCDF4
from matplotlib import pyplot as plt
import numpy as np
plt.rcParams['figure.figsize'] = [10, 8]

class NetCDF4PrecipitationParser:

    @staticmethod
    def find_nearest_index(array, value):
        return np.abs(array - value).argmin()
    @staticmethod
    def parse(file_name: str, year: int) -> pd.DataFrame:
        load_dotenv()
        data_path = os.getenv("EL_NINO_DATA_PATH")
        precipitation_hourly_nc = netCDF4.Dataset(f'{data_path}/{file_name}')
        latitudes = precipitation_hourly_nc.variables['latitude'][:]
        longitudes = precipitation_hourly_nc.variables['longitude'][:]
        # Latitude and longitude for La Esperanza station
        target_latitude = -4.913735
        target_longitude = -81.055118

        lat_index = NetCDF4PrecipitationParser.find_nearest_index(latitudes, target_latitude)
        lon_index = NetCDF4PrecipitationParser.find_nearest_index(longitudes, target_longitude)

        nearly_station_precipitation_hourly = precipitation_hourly_nc.variables['p'][:, lat_index, lon_index]
        nearly_station_precipitation_daily = np.sum(nearly_station_precipitation_hourly.reshape(-1, 24), axis=1)
        nearly_station_dates = np.arange(f'{str(year)}-01-01', f'{str(year+1)}-01-01', dtype='datetime64[D]')
        nearly_station_hours = precipitation_hourly_nc.variables['time'][:].data
        assert np.all(nearly_station_hours[:-1] <= nearly_station_hours[1:]), 'time is not sorted'
        assert len(nearly_station_precipitation_daily) == len(nearly_station_dates), 'not all days with data'
        return pd.DataFrame({'date':nearly_station_dates, 'daily_precipitation':nearly_station_precipitation_daily})

class SenamhiPrecipitationParser:
    @staticmethod
    def parse(file_name: str) -> pd.DataFrame:
        load_dotenv()
        data_path = os.getenv("EL_NINO_DATA_PATH")
        station_df = pd.read_csv(f'{data_path}/qc00000230.txt', header=None, delimiter=r"\s+")
        station_df.columns =['year', 'month', 'day', 'daily_precipitation', 'temp_min', 'temp_max']
        station_df = station_df.assign(date=lambda x: pd.to_datetime(x['year'].apply(str) +
                                                                     x['month'].apply(str).str.zfill(2) +
                                                                     x['day'].apply(str).str.zfill(2), format='%Y%m%d'))
        return station_df[['date', 'daily_precipitation']]

if __name__ == "__main__":
    load_dotenv()
    output_figures_path = os.getenv("FIGURE_OUTPUT")
    nearly_station_df = NetCDF4PrecipitationParser.parse('PISCOp_h_non-DBC_2015.nc', 2015)
    station_df = SenamhiPrecipitationParser.parse('qc00000230.txt')

    station_2015 = station_df[station_df['date'].dt.year == 2015]

    fig, ax = plt.subplots()
    ax = station_2015.plot(ax=ax, x='date', y='daily_precipitation', c='red', label='Precipitation registered by Station La Esperanza', marker='o',linestyle='None')
    _ = nearly_station_df.plot(ax=ax, kind='line', x='date', y='daily_precipitation', c='cyan', label='High-resolution gridded hourly precipitation close to Station La Esperanza', linestyle='solid')
    plt.title("Comparison between two different precipitation datasets for year 2015")
    fig.savefig(f'{output_figures_path}/cmp_station_nearly_station.png')   # save the figure to file
    plt.close(fig)
    print('plot generated')
