# Local Data Base of Piura's precipitation

Since the precipitation is acquired from different sources, I've decided to create a database to gather all
precipitation sources in a single database, process them into a single one and use it for further analysis.

```sql
CREATE TABLE IF NOT EXISTS  raw_precipitation (
    event_calendar_date     date,
    source_id               varchar(40) NOT NULL,
    precipitation_number    float NOT NULL,
    CONSTRAINT raw_precipitation_primary_key PRIMARY KEY(event_calendar_date, source_id));

CREATE TABLE IF NOT EXISTS  master_precipitation (
    event_calendar_date     date primary KEY,
    precipitation_number    float NOT NULL);

CREATE TABLE IF NOT EXISTS  sst_weekly (
    event_calendar_date     date primary KEY,
    nino12_sst 				float not null,
    nino12_var 				float not null,
    nino3_sst 				float not null,
    nino3_var 				float not null,
    nino34_sst 				float not null,
    nino34_var 				float not null,
    nino4_sst 				float not null,
    nino4_var 				float not null
);

CREATE TABLE IF NOT EXISTS  equatorial_average_temperature_monthly (
    event_calendar_date     date primary KEY,
    e130_w80 				float not null,
    e160_w80 				float not null,
    w180_w100 				float not null
);

CREATE TABLE IF NOT EXISTS  oni_monthly (
    event_calendar_date     date primary KEY,
    total_oni 				float not null,
    anomaly_oni 			float not null
);

CREATE TABLE IF NOT EXISTS  target_precipitation (
    calendar_date     date primary KEY,
    target_high_precipitation 				float not null
);
```