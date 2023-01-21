# %%
import folium
print(f"folium Version: {folium.__version__}")
# %%
####################
# GET TORONTO MAP  #
####################
# %%
# 위도, 경도
# Left Upper  : 43.767695, -79.550735
# Left Lower  : 43.592222, -79.550735
# Right Upper : 43.767695, -79.240054
# Right Lower : 43.592222, -79.240054
# %%
print((-79.550735+-79.240054)/2)
# %%
# CENTER
lat, lon = 43.6799585, -79.395395
# 줌 크기
zoom_size = 10
# %%
# 구글 지도 타일 설정
tiles = "http://mt0.google.com/vt/lyrs=m&hl=ko&x={x}&y={y}&z={z}"
# 속성 설정
attr = "Google"
# 지도 객체 생성
m = folium.Map(location = [lat, lon],
               zoom_start = zoom_size,
               tiles = tiles,
               attr = attr)
# %%
m
# %%
folium.Marker([37.504811111562, 127.025492036104],
              popup="판교역",
              tooltip="판교역 입구",
              icon=folium.Icon('red', icon='star'),
            ).add_to(m)
# %%
m
# %%
folium.CircleMarker([37.504811111562, 127.025492036104],
                    color='tomato',
                    radius = 50,
                    tooltip='판교역 상권').add_to(m)
m
# %%
# @see : https://teddylee777.github.io/visualization/folium
# %%
coordinates = [
    # [42.3581, -71.0636],
    # [42.82995815, -74.78991444],
    # [43.17929819, -78.56603306],
    # [43.40320216, -82.37774519],
    # [43.49975489, -86.20965845],
    # [41.4338549, -108.74485069],
    # [40.67471747, -112.29609954],
    # [39.8093434, -115.76190821],
    # [38.84352776, -119.13665678],
    # [37.7833, -122.4167],
    [43.749391, -79.638496],
    [43.855409, -79.170128],
    [43.813431, -79.151355],
    [43.793108, -79.117096],
    [43.619748, -79.321244],
    [43.583384, -79.542757],
    [43.626882, -79.564345],
    [43.646242, -79.608460],
    [43.665257, -79.587341],
    [43.749391, -79.638496],
]

# Create the map and add the line
m = folium.Map(location=[43.6799585, -79.395395], zoom_start=10)
my_PolyLine=folium.PolyLine(locations=coordinates,weight=5)
m.add_child(my_PolyLine)
# m.save('line_example_newer.html')
# %%
API_KEY = "AIzaSyBr6Sz3AaNGWZpgL_faYsZBboH63E-DLE0"
# %%
import googlemaps
# %%
a=googlemaps.Client(
  key=API_KEY
)
address = "2525 St Clair Ave W"
# %%
t = a.geocode(address)
# %%
t[0].keys()
# %%
lat = t[0]['geometry']['bounds']['northeast']['lat']
lng = t[0]['geometry']['bounds']['northeast']['lng']
# %%
t = a.place("ChIJpTvG15DL1IkRd8S0KlBVNTI")
# %%
import json
# %%
with open("./test.json", "w") as f:
    f.write(json.dumps(t, indent=4))
# %%
import requests
import json
# url variable store url
url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

# The text string on which to search
query = "Toronto Walmart"

# get method of requests module
# return response object
r = requests.get(url + 'query=' + query +
                        '&key=' + API_KEY + '&pagetoken=' + 'ARywPAK1A4MtgrFHAASzQMYodkgqBuupuQr0lU1zLuDN25iJwZtoepCj5TpYmxnBMg_yxx1plPVMsmqkhiAzjj2T1UAWzVSegjU5QIyR9ByonfZjnuBH5Vm4PkK-zv7vjQJTvQwobZP2ymG_KjoCFd1bpHhNIWdIioJy61eQWRfPLzOiVDen-V0ypGalvazIbbf6FYicqwOlBnb6D2MnyNdZallAJhG-sIWl2nO6IG8xkWahuDZY6qjI8_EcLsf_rJZFWocccCnD9hl-zH7xYi34CGWD0GZTMYUWPodctd873_okaWRO4VdsEBkG5R8jfcbtg4BswVjRSp5DJY7BspUzIBWVxVzte4Wdbhk_LmqUpFKWsD3F6OBUYVYoA4ArMLreUqtT2iDaKggOOLqMgA')

# %%
result = r.json()
# %%
result.keys()
# %%
result["results"][0]
# %%
a = result["next_page_token"]
# %%
requests.get(url + 'query=' + query +
                        '&key=' + API_KEY + '&pagetoken='+a)
# %%
map = folium.Map(location=[37.5502, 126.982], zoom_start=11)

for n in seoul_df_raw.index:
    folium.Marker(
        [seoul_df_raw['lat'][n],seoul_df_raw['lng'][n]],
        radius = 10,
        color='#3186cc',
        fill_color='#3186cc',
        fill=True,
        tooltip  = ('<b>- 지역</b>: ' + seoul_df_raw['지역'][n] + " " + seoul_df_raw['도시명'][n] + '<br>' +
                 '<b>- 상호명</b>: ' + seoul_df_raw['식당상호'][n] + '<br>' +
                 '<b>- 대표메뉴</b>: ' + seoul_df_raw['대표 메뉴'][n] + '<br>' +
                   '<b>- 추천사유</b>: ' + seoul_df_raw['추천사유'][n])
    ).add_to(map)
map

2525 St Clair Ave W"
