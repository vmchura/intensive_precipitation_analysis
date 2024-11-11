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
```