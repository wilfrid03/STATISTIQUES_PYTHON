import folium 
import geopandas 

m = folium.Map(location=[48.08, 2.55], zoom_start=8, tiles="OpenStreetMap")


m.save(".\\RESULTATS\\carte1.html")