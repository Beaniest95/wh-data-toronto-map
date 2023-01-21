from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional, Tuple
from secret import GOOGLE_MAP_API_KEY

@dataclass
class GoogleMapVariables:
    ######################
    #  Crawler Variable  #
    ######################
    url: str
    searchbox_selector: str
    searchbutton_selector: str
    scroll_xpath: str
    valid_result_xpath: str
    url_link_xpath: str
    name_xpath: str
    grade_xpath: str
    address_xpath: str
    valid_result_class_list: List[str]
    end_line_result_class_list: List[str]
    skip_line_result_class_list: List[str]
    search_string: List[str]

    #####################
    #  Mapper Variable  #
    #####################
    api_key: str
    file_path: str
    raw_path_suffix: str
    enriched_path_suffix: str
    file_format: str

    #####################
    #  Drawer Variable  #
    #####################
    marker_style: Dict[str, Tuple[str,str]]
    polyline: List[List[float]]
    toronto_center_coordinates: List[float]
    map_zoom_size: int
    map_tiles: str
    map_attribute_name: str
    map_file_path: str
    map_path_suffix: str
    map_file_name: str
    map_file_format: str

    @classmethod
    def get(cls) -> "GoogleMapVariables":
        return cls(
            ######################
            #  Crawler Variable  #
            ######################
            url="https://www.google.com/maps?hl=en",
            searchbox_selector="#searchboxinput",
            searchbutton_selector="#searchbox-searchbutton",
            scroll_xpath="/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]",
            valid_result_xpath='//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[{index}]/div',
            url_link_xpath='//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[{index}]/div/a',
            name_xpath='//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[{index}]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[1]/div[2]/span',
            grade_xpath='//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[{index}]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[3]/div/span[2]/span[2]/span[1]',
            address_xpath='//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[{index}]/div/div[2]/div[2]/div[1]/div/div/div[2]/div[4]/div[1]/span[2]/jsl/span[2]',
            valid_result_class_list=[
                'Nv2PK THOPZb CpccDe',
                'Nv2PK tH5CWc THOPZb',
                'Nv2PK Q2HXcd THOPZb',
            ],
            end_line_result_class_list=[
                'lXJj5c Hk4XGb',
                'PbZDve',
                ''
            ],
            skip_line_result_class_list=[
                'fp2VUc',
                'z7i0C m6QErb',
                'm6QErb tLjsW',
            ],
            search_string=[
                # 'canada toronto bank',
                # 'canada toronto hospital',

                # 'canada toronto church',

                # 'canada toronto coin laundry',
                # 'canada toronto fitness center',
                # 'canada toronto theatre',

                # 'canada toronto costco',
                # 'canada toronto walmart',
                # 'canada toronto freshco',
                # 'canada toronto best buy',
                # 'canada toronto grocery',
                # 'canada toronto shopping mall',

                # 'canada toronto restaurant',
                # 'canada toronto pizza',
                'canada toronto chipotle',
                'canada toronto bbq chicken',
                # 'canada toronto food',
            ],

            #####################
            #  Mapper Variable  #
            #####################
            api_key=GOOGLE_MAP_API_KEY,
            file_path="./results/json",
            raw_path_suffix="google/raw",
            enriched_path_suffix="google/enriched",
            file_format="json",

            #####################
            #  Drawer Variable  #
            #####################
            marker_style={
                'bank': ('blue','bank'),
                'hospital': ('blue','hospital'),

                'church': ('purple', 'church'),

                'coin_laundry': ('green', 'droplet'),
                'fitness_center': ('green', 'heart-pulse'),
                'theatre': ('green', 'film'),

                'costco': ('cyan', 'location-dot'),
                'freshco': ('blue','location-dot'),
                'walmart': ('black', 'location-dot'),
                'best_buy': ('black', 'tv'),
                'grocery': ('green', 'location-dot'),
                'shopping_mall': ('red', 'location-dot'),

                'restaurant': ('red', 'star'),
                'pizza': ('purple', 'star'),
                'chipotle': ('cyan', 'star'),
                'bbq_chicken': ('brown', 'star'),
                'food': ('green', 'star'),
            },
            polyline=[
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
            ],
            toronto_center_coordinates=[43.6799585, -79.395395],
            map_zoom_size=10,
            map_tiles="http://mt0.google.com/vt/lyrs=m&hl=ko&x={x}&y={y}&z={z}",
            map_attribute_name="Google",
            map_file_path="./results/html",
            map_path_suffix='google',
            map_file_name='toronto_google_map',
            map_file_format="html",
        )
