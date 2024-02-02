import folium
from geopy.geocoders import Nominatim
m = folium.Map(location=[55.7558, 37.6176], zoom_start=10)
b = Nominatim(user_agent="stadium_locator")
c = {
    "Спартак": "Спартак, Москва, Россия",
    "Динамо": "Динамо, Москва, Россия",
    "Лужники": "Лужники, Москва, Россия"
}
for d, x in c.items():
    x = b.geocode(x)
    if x:
        y, j = x.latitude, x.longitude
        folium.Marker([y, j], popup=d).add_to(m)
m.save("stadioni.html")