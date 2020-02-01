# Windy Web Crawler
#### This application is built with scrapy and selenium

It takes places name as input to give weather forecast in commandline for 5 upcoming days

The package can be installed using pip by following command
(Python >=3.6 is required for this project)

`pip3 install windy-weather-crawler`

OR
=
`pip install windy-weather-crawler`

## Usage :
1. Create a python file with any name
2. write the following code in there

    ``from windy_crawler.run import windy_crawler
      windy_crawler()``

3. Save the file and run it

## Input :
1. You need to enter the firefox binary file path on-request

`Welcome to Windy Web Crawler`
`Please enter your full path to firefox binary in your system(default: /usr/bin/firefox) :
`
2. Then type the place

`Now select the place for weather forecast(ex. chennai, hyderabad, delhi etc... :`
3. You will get some suggestions regarding locality in that place
```
|    | Place Name                                                                     |
|----+--------------------------------------------------------------------------------|
|  0 | Hyderabad Airport OPKD                                                         |
|  1 | Hyderabad                                                                      |
|  2 | Hyderabad Pakistan                                                             |
|  3 | Hyderabad Sangareddy District                                                  |
|  4 | Hyderabad Central District, Iran                                               |
|  5 | Greater Hyderabad Municipal Corporation North Zone Medchal–Malkajgiri District |
|  6 | Greater Hyderabad Municipal Corporation West Zone Rangareddy District          |
|  7 | Greater Hyderabad Municipal Corporation South Zone Hyderabad                   |
|  8 | Greater Hyderabad Municipal Corporation Central Zone Hyderabad                 |
Please Select the Index from above table: 
```
4. On selecting the index out in tabular form will be displayed

```
#########################Weather Forecast for 5 days##############################
=>Saturday 1
| Time of Day   | Min Temp-Max Temp(C)   | Min Wind Speed-Max Wind Speed(Kt)   |
|---------------+------------------------+-------------------------------------|
| 0AM           | 5°-16°                 | 6-11                                |
| 3AM           | 9°-14°                 | 6-10                                |
| 6AM           | 9°-13°                 | 6-10                                |
| 9AM           | 5°-12°                 | 6-9                                 |
| 12PM          | 5°-20°                 | 8-15                                |
| 3PM           | 3°-25°                 | 7-18                                |
| 6PM           | 2°-24°                 | 6-14                                |
| 9PM           | 4°-19°                 | 8-11                                |
=>Sunday 2
| Time of Day   | Min Temp-Max Temp(C)   | Min Wind Speed-Max Wind Speed(Kt)   |
|---------------+------------------------+-------------------------------------|
| 0AM           | 3°-15°                 | 8-11                                |
| 3AM           | 1°-13°                 | 7-12                                |
| 6AM           | 1°-11°                 | 7-12                                |
| 9AM           | 3°-11°                 | 9-14                                |
| 12PM          | 3°-19°                 | 8-17                                |
| 3PM           | 1°-23°                 | 9-18                                |
| 6PM           | 0°-23°                 | 7-17                                |
| 9PM           | 2°-17°                 | 6-13                                |
=>Monday 3
| Time of Day   | Min Temp-Max Temp(C)   | Min Wind Speed-Max Wind Speed(Kt)   |
|---------------+------------------------+-------------------------------------|
| 0AM           | 5°-15°                 | 7-11                                |
| 3AM           | 5°-13°                 | 7-11                                |
| 6AM           | 5°-12°                 | 7-12                                |
| 9AM           | 5°-12°                 | 6-10                                |
| 12PM          | 4°-20°                 | 4-11                                |
| 3PM           | 1°-24°                 | 3-11                                |
| 6PM           | 1°-24°                 | 2-9                                 |
| 9PM           | 3°-20°                 | 2-6                                 |
=>Tuesday 4
| Time of Day   | Min Temp-Max Temp(C)   | Min Wind Speed-Max Wind Speed(Kt)   |
|---------------+------------------------+-------------------------------------|
| 0AM           | 9°-17°                 | 6-10                                |
| 3AM           | 12°-15°                | 6-10                                |
| 6AM           | 14°-16°                | 6-10                                |
| 9AM           | 14°-16°                | 6-11                                |
| 12PM          | 7°-21°                 | 9-17                                |
| 3PM           | 5°-24°                 | 9-18                                |
| 6PM           | 5°-24°                 | 7-17                                |
| 9PM           | 6°-19°                 | 7-13                                |
=>Wednesday 5
| Time of Day   | Min Temp-Max Temp(C)   | Min Wind Speed-Max Wind Speed(Kt)   |
|---------------+------------------------+-------------------------------------|
| 0AM           | 5°-16°                 | 8-12                                |
| 3AM           | 4°-14°                 | 7-12                                |
| 6AM           | 5°-12°                 | 8-12                                |
| 9AM           | 5°-12°                 | 9-14                                |
| 12PM          | 6°-19°                 | 11-20                               |
| 3PM           | 5°-23°                 | 10-21                               |
| 6PM           | 5°-23°                 | 9-20                                |
| 9PM           | 3°-18°                 | 8-16                                |
```

## Requirements:
1. Mozilla Firefox Browser
2. Python3
