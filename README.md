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

## Data Sets used

* data (directory not shared in this repository)
    * PISCOp_h_non-DBC_2015.nc
        * [Details on the article](https://www.sciencedirect.com/science/article/pii/S2352340922007776?via%3Dihub)
        * [URL where the dataset is hosted.](https://figshare.com/articles/dataset/SATc/17148416?backTo=/collections/Development_of_high-resolution_hourly_gridded_precipitation_dataset_over_Peru/5743166)
    * qc00000230.txt
        * Precipitation data for station "La Esperanza", Perú/Piura/Paita/Colan
        * URL where the dataset can be downloaded previous
          registration [Senhami](https://www.senamhi.gob.pe/site/descarga-datos/)
    
