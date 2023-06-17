import sys
import pandas as pd
from pykml import parser
from turfpy.measurement import boolean_point_in_polygon
from geojson import Point, MultiPolygon, Feature, Polygon
from datetime import datetime
import re

def convert_datetime(date):
    year, month, day, hour, minute, second = list(map(int, re.findall(r'\d+', date)))
    return datetime(year, month, day, hour, minute, second)

def main(kml_path, csv_path):
    with open(kml_path, 'r', encoding='utf-8') as f: 
        doc = parser.parse(f).getroot()

    location = str(doc.Document.Placemark.Polygon.outerBoundaryIs.LinearRing.coordinates).replace('\n', '').replace('\t', '')
    location = location.split(' ')[:-1]
    location = [tuple(map(float, item.split(',')[:2])) for item in location]
    print(location)

    point = Feature(geometry=Point([140.95, 43.2]))
    polygon = Feature(geometry=Polygon([location]))

    df_ais = pd.read_csv(csv_path)
    df_ais['is_in_polygon'] = [boolean_point_in_polygon(Feature(geometry=Point(list(point))), polygon) for point in list(df_ais[['LON', 'LAT']].values)]
    df_ais['BaseDateTime'] = df_ais['BaseDateTime'].map(convert_datetime)
    
    vessels_in_polygon = []
    
    df2 = df_ais[(datetime(2023, 1, 1) <= df_ais['BaseDateTime']) & (df_ais['BaseDateTime'] < datetime(2023, 1, 2))]
    
    for imo in df2['MMSI'].unique():
        df_imo = df2[df2['MMSI'] == imo]
        if df_imo['is_in_polygon'].any():
            vessels_in_polygon.append(imo)
    
    print(imo)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <kml_file> <csv_file>")
    else:
        kml_file = sys.argv[1]
        csv_file = sys.argv[2]
        main(kml_file, csv_file)