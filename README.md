# Air-Quality Clustering of an Italian City

Capstone Project of Post Graduate Diploma in Artificial Intelligence and Machine Learning at Asian Institute of Management.

## Data Source

Vito, S. (2008). Air Quality [Dataset]. UCI Machine Learning Repository. <https://archive.ics.uci.edu/dataset/360/air+quality>

File name: AirQualityUCI.csv
File path: ./data/AirQualityUCI.csv

## Associated Task

Clustering

## Instances of Real Data

9358
Missing Values: Yes

## Dataset Characteristics

Multivariate, Time-Series

## Dataset Information

The dataset contains 9358 instances of hourly averaged responses from an array of 5 metal oxide chemical sensors embedded in an Air Quality Chemical Multisensor Device. The device was located on the field in a significantly polluted area, at road level, within an Italian city. Data were recorded from March 2004 to February 2005 (one year)representing the longest freely available recordings of on field deployed air quality chemical sensor devices responses. Ground Truth hourly averaged concentrations for CO, Non Metanic Hydrocarbons, Benzene, Total Nitrogen Oxides (NOx) and Nitrogen Dioxide (NO2) and were provided by a co-located reference certified analyzer. Evidences of cross-sensitivities as well as both concept and sensor drifts are present as described in De Vito et al., Sens. And Act. B, Vol. 129,2,2008 (citation required) eventually affecting sensors concentration estimation capabilities. Missing values are tagged with -200 value.
This dataset can be used exclusively for research purposes. Commercial purposes are fully excluded.

## Data Dictionary

| Column Index | Column Name    | Type      | Info                                                     | Allowed Values            |
|--------------|----------------|-----------|----------------------------------------------------------|---------------------------|
| 0            |  Date          | object    | Date with format: DD/MM/YYYY                             | DD/MM/YYYY                |
| 1            |  Time          | object    | Time with format: HH.MM.SS                               | HH.MM.SS                  |
| 2            |  CO(GT)        | object    | CO concencration in mg/m^3                               | >= 0 or -200 (error)      |
| 3            |  PT08.S1(CO)   | float64   | Hourly averaged sensor response (nominally CO targeted)  | >= 0 or -200 (error)      |
| 4            |  NMHC(GT)      | float64   | Non Metanic HydroCarbons concentration in microg/m^3'    | >= 0 or -200 (error)      |
| 5            |  C6H6(GT)      | object    | Benzene concentration in microg/m^3                      | >= 0 or -200 (error)      |
| 6            |  PT08.S2(NMHC) | float64   | Hourly averaged sensor response (nominally NMHC targeted)| >= 0 or -200 (error)      |
| 7            |  NOx(GT)       | float64   | NOx concentration in ppb                                 | >= 0 or -200 (error)      |
| 8            |  PT08.S3(NOx)  | float64   | Hourly averaged sensor response (nominally NO2 targeted) | >= 0 or -200 (error)      |
| 9            |  NO2(GT)       | float64   | NO2 concentration in microg/m^3                          | >= 0 or -200 (error)      |
| 10           |  PT08.S4(NO2)  | float64   | Hourly averaged sensor response (nominally NO2 targeted) | >= 0 or -200 (error)      |
| 11           |  PT08.S5(O3)   | float64   | Ozon (O3)                                                | >= 0 or -200 (error)      |
| 12           |  T             | object    | Temperature (°C)                                         | -50 >= 0 or -200 (error)  |
| 13           |  RH            | object    | Relative Humidity (%)                                    | 0-100 or -200 (error)     |
| 14           |  AH            | object    | Absolute Humidity                                        | >= 0 or -200 (error)      |
