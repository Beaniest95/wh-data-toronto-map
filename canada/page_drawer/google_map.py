import folium
from folium.features import CustomIcon
import glob
import json

class GoogleMapDrawer():
    def __init__(self, google_variable):
        self.google_variable = google_variable
        self.file_path=google_variable.file_path
        self.enriched_path_suffix=google_variable.enriched_path_suffix
        self.file_format=google_variable.file_format
        self.map_file_path=google_variable.map_file_path
        self.map_path_suffix=google_variable.map_path_suffix
        self.map_file_name=google_variable.map_file_name
        self.map_file_format=google_variable.map_file_format


    def init_map(self):
        self.map_object = folium.Map(
            location=self.google_variable.toronto_center_coordinates,
            zoom_start=self.google_variable.map_zoom_size,
            tiles=self.google_variable.map_tiles,
            attr=self.google_variable.map_attribute_name,
        )

    def _add_polyline(self):
        map_polyline = folium.PolyLine(locations=self.google_variable.polyline, weight=5)
        self.map_object.add_child(map_polyline)




    def _add_icons(self, feature_group, icon_name, color, icon_data):
        for row in icon_data:
            if row.get('lat') and row.get('lng') and row.get('url') and row.get('name') and row.get('address'):
                icon=folium.Icon(color=color, icon='location-dot', icon_color=color, prefix='fa')
                feature_group.add_child(
                    folium.Marker(
                        (row['lat'], row['lng']),
                        popup=f"<a href={row['url']} target='_blank'>{row['name']} ({row.get('grade', '')}) </a>",
                        tooltip=row['address'],
                        icon=icon
                    )
            )

    def _extract_and_draw(self, data):
        for icon_name, color in data.items():
            feature_group = folium.FeatureGroup(name=f'{icon_name} ({color})').add_to(self.map_object)
            with open(f"{self.file_path}/{self.enriched_path_suffix}/canada_toronto_{icon_name}.{self.file_format}") as file:
                icon_data = json.load(file)
                self._add_icons(feature_group, icon_name, color, icon_data)

        folium.LayerControl().add_to(self.map_object)

    def save_html(self, category):
        save_path = f"{self.map_file_path}/{self.map_path_suffix}/{category}.{self.map_file_format}"
        self.map_object.save(save_path)

    def run(self):
        for category, data in self.google_variable.map_category.items():
            self.init_map()
            self._add_polyline()
            self._extract_and_draw(data)
            self.save_html(category)
