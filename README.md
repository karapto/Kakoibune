# Kakoibune

[Locked Shields] A program that determines points inside and outside of a geofence to analyze how many vessels are staying in an area and for how long.

### Setup

This guide assumes that you have installed python 3.x on your machine, preferably python 3.7 and above.

```
$ pip install -r requirements.txt
```

### Prepare AIS Dataset

You can get it from the following link;

https://marinecadastre.gov/ais/

### Generating kml file

https://earth.google.com/web/

Click on the blue glowing icon in this image from the left menu bar 

Create a new project > Create KML file 

![google earth](img/google_earth.png)

Add Items > Draw Lines and Shapes

Press the back button in the upper left corner, press the three dots next to the trashcan, and click Export as KML file to download the kml file.

![export kml file](img/draw.png)


### Counting vessels within the geofence using AIS data

Running main.py will display the geofences you have defined and the Maritime Mobile Service Identity (MMSI) of the vessels within them.

```
$ python main.py otaru.kml AIS_2023_01_01.csv
[(140.8536424990038, 43.21877081834404), (140.9166818015721, 43.16569868534197), (141.0740979141997, 43.17610839426013), (141.0879242560119, 43.25249043367866), (141.0249118384166, 43.32024331113249), (140.8634812977587, 43.29555835250518), (140.8536424990038, 43.21877081834404)]
431159000
```
