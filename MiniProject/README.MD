# Mini-Project
## Introduction
### Author
Created by Haozhi Li @ QMUL
Stu. Number: 180377538
Email: haozhi.li@se18.qmul.ac.uk

### App Functionality Description
The web app captures local current air quality data from external API [breezometer.com](https://breezometer.com/products/air-quality-api) through GET method, which will be stored in a cloud Cassandra database.
The data report will be formatted as JSON file, for example:
```json
{
  "data": {
    "data_available": true,
    "datetime": "2019-03-28T14:00:00Z",
    "indexes": {
      "baqi": {
        "aqi": 52,
        "aqi_display": "52",
        "category": "Moderate air quality",
        "color": "#F2FA05",
        "display_name": "BreezoMeter AQI",
        "dominant_pollutant": "pm25"
      }
    }
  },
  "error": null,
  "metadata": null
}
```
You could find these data in the route _/airqualitychart_

And there is a CQL (Cassandra Query Language) query inside the application that could sort out the AQI number of a certain datetime. Just simply enter the route /airqualitychart/<datetime> you would get a json formatted output(for example):
```json
{
  "2019-03-28T13:00:00Z": 52
}
```
*You could either get a text-style output, simply by going to another site: 35.239.178.220/airqualitychart/<datetime>*

## Cloud Deployment status
Number of nodes in cluster: 3
Database scale in cluster: 4 
Replication factor of keyspace: 2

## API Usage
**Restful API:**

Current air quality data:
http://35.224.38.13/airqualitychart/

AQI data at a certain time:(Example tamplate)
http://35.239.178.220/airqualitychart/2019-03-28T12:00:00Z

***NOTICE***
The format of _datetime_ should be:
_YYYY-MM-DD_ T _HH:MM:SS_ Z
where Z means zulu (Greenwich Mean Time).

**REST Methods:**
GET, POST, PUT, DELETE

## Acknowledgement

### Technical Support
[Google Cloud Platform](https://cloud.google.com)
[Restful API Tutorial](https://restfulapi.net/rest-put-vs-post/)
[Cassandra CQL docs](https://docs.datastax.com/en/dse/6.7/cql/index.html)
[Breezometer API](https://docs.breezometer.com/api-documentation/air-quality-api/v2/)

### Lecturers, Tutors
[Dr. Arman](http://www.eecs.qmul.ac.uk/~khouzani/)
[Dr. Felix](http://www.eecs.qmul.ac.uk/profiles/cuadradofelix.html)

## Further development
1. Insert data into database directly from external API
2. SSL protocol