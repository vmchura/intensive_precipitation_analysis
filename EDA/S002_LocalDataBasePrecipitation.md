# Local Data Base of Piura's precipitation

Since the precipitation is acquired from different sources, I've decided to create a database to gather all
precipitation sources in a single database, process them into a single one and use it for further analysis.

```sql
DROP TABLE IF EXISTS enso_past_events;
DROP TABLE IF EXISTS equatorial_average_temperature_monthly;
DROP TABLE IF EXISTS master_precipitation;
DROP TABLE IF EXISTS oni_monthly;
DROP TABLE IF EXISTS raw_precipitation;
DROP TABLE IF EXISTS target_precipitation;
DROP TABLE IF EXISTS sst_weekly;


CREATE TABLE enso_past_events (
    year_id integer NOT NULL PRIMARY KEY,
    year_enso_type text NOT NULL
);

CREATE TABLE equatorial_average_temperature_monthly (
    event_calendar_date date NOT NULL PRIMARY KEY,
    e130_w80 double precision NOT NULL,
    e160_w80 double precision NOT NULL,
    w180_w100 double precision NOT NULL
);

CREATE TABLE master_precipitation (
    event_calendar_date date NOT NULL PRIMARY KEY,
    precipitation_number double precision NOT NULL
);

CREATE TABLE oni_monthly (
    event_calendar_date date NOT NULL PRIMARY KEY,
    total_oni double precision NOT NULL,
    anomaly_oni double precision NOT NULL
);

CREATE TABLE raw_precipitation (
    event_calendar_date date NOT NULL,
    source_id character varying(40) NOT NULL,
    precipitation_number double precision NOT NULL,
    PRIMARY KEY (event_calendar_date, source_id)
);

CREATE TABLE sst_weekly (
    event_calendar_date date NOT NULL PRIMARY KEY,
    nino12_sst double precision NOT NULL,
    nino12_var double precision NOT NULL,
    nino3_sst double precision NOT NULL,
    nino3_var double precision NOT NULL,
    nino34_sst double precision NOT NULL,
    nino34_var double precision NOT NULL,
    nino4_sst double precision NOT NULL,
    nino4_var double precision NOT NULL
);

CREATE TABLE target_precipitation (
    calendar_date date NOT NULL PRIMARY KEY,
    target_high_precipitation double precision NOT NULL
);
```