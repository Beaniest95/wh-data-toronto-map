import folium
import glob
import json

class GoogleMapDrawer():
    def __init__(self, google_variable):
        self.google_variable = google_variable
        self.map_object = folium.Map(
            location=google_variable.toronto_center_coordinates,
            # control_scale=True,
            zoom_start=google_variable.map_zoom_size,
            tiles=google_variable.map_tiles,
            attr=google_variable.map_attribute_name,
        )
        self.file_path=google_variable.file_path
        self.enriched_path_suffix=google_variable.enriched_path_suffix
        self.file_format=google_variable.file_format
        self.map_file_path=google_variable.map_file_path
        self.map_path_suffix=google_variable.map_path_suffix
        self.map_file_name=google_variable.map_file_name
        self.map_file_format=google_variable.map_file_format

    def _add_polyline(self):
        map_polyline = folium.PolyLine(locations=self.google_variable.polyline, weight=5)
        self.map_object.add_child(map_polyline)

    def _add_feature_group(self, category, data):
        feature_group = folium.FeatureGroup(name=category).add_to(self.map_object)
        for row in data:
            if row.get('lat') and row.get('lng') and row.get('url') and row.get('name') and row.get('address'):
                icon=folium.Icon(color='white', icon=self.google_variable.marker_style[category][1], icon_color=self.google_variable.marker_style[category][0], prefix='fa')
                feature_group.add_child(
                    folium.Marker(
                        (row['lat'], row['lng']),
                        popup=f"<a href={row['url']}>{row['name']} ({row.get('grade', '')})</a>",
                        tooltip=row['address'],
                        icon=icon
                    )
            )

    def _extract_and_draw(self):
        for json_file_path in glob.glob(f"{self.file_path}/{self.enriched_path_suffix}/*.{self.file_format}"):
            category = json_file_path.split('canada_toronto_')[-1].split(f'.{self.file_format}')[0]
            with open(json_file_path, 'r') as file:
                data = json.load(file)
                self._add_feature_group(category, data)

        folium.LayerControl().add_to(self.map_object)

    def draw_map(self):
        self._add_polyline()
        self._extract_and_draw()

    def save_html(self):
        save_path = f"{self.map_file_path}/{self.map_path_suffix}/{self.map_file_name}.{self.map_file_format}"
        self.map_object.save(save_path)

    def run(self):
        self.draw_map()
        self.save_html()
