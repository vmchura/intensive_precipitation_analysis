# Prediction of high precipitation on Piura / Perú

Although there are already highly accurate methods for predicting precipitation on the western side of South America, my
particular interest is in understanding why periods of intensive precipitation have become more frequent in recent years
compared to past decades.

As a secondary goal, I aim to enhance my skills in techniques used in Data Engineering and Data Science. To that end, I
will do my best to document every step of this project.

## Content

* EDA
    * S001_CompareDataSets.py
        * Script to compare complementary sources, one dataset spans from 1996 to 2015-12, and the other from 2015-01 to 2020-12.
        * The comparison focuses on overlapping days to adjust the datasets so they align on the same scale.

    * S002_LocalDataBasePrecipitation.md
      * SQL Script to create the database and tables precipitation.
    * S003_IngestRawPrecipitation.ipynb
      * Python script to ingest raw precipitation datasets into SQL table.
    * S004_ProcessPrecipitation.ipynb
      * Python script to process raw SQL table into refined precipitation SQL table.
## Data Sets used

* data (directory not shared in this repository)
    * PISCOp_h_non-DBC_2015.nc
    * PISCOp_h_non-DBC_2016.nc
    * PISCOp_h_non-DBC_2017.nc
    * PISCOp_h_non-DBC_2018.nc
    * PISCOp_h_non-DBC_2019.nc
    * PISCOp_h_non-DBC_2020.nc
        * High-resolution (0.1°) gridded dataset of hourly precipitation across Peru for the period 2015–2020.
        * [Details on the article](https://www.sciencedirect.com/science/article/pii/S2352340922007776?via%3Dihub)
        * [URL where the dataset is hosted.](https://figshare.com/articles/dataset/SATc/17148416?backTo=/collections/Development_of_high-resolution_hourly_gridded_precipitation_dataset_over_Peru/5743166)
    * qc00000230.txt; Station "La Esperanza", Perú/Piura/Paita/Colan
    * qc00000208.txt; Station "Mallares", Perú/Piura/Sullana/Marcavelica
    * qc00152101.txt; Station "Pananga", Perú/Piura/Sullana/Marcavelica
        * URL where the dataset can be downloaded previous registration [Senhami](https://www.senamhi.gob.pe/site/descarga-datos/)
    
