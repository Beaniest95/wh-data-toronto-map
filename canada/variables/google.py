from dataclasses import dataclass
from typing import Any, Dict, Iterable, List, Optional

@dataclass
class GoogleMapVariables:
    api_key: str
    file_path: str
    raw_path_suffix: str
    enriched_path_suffix: str
    file_format: str

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

    @classmethod
    def get(cls) -> "GoogleMapVariables":
        return cls(
            api_key='add key here'
            file_path = "./results/json",
            raw_path_suffix = "google/raw",
            enriched_path_suffix = "google/enriched",
            file_format = "json",

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
                'Nv2PK tH5CWc THOPZb'
            ],
            end_line_result_class_list=[
                'lXJj5c Hk4XGb',
                'PbZDve'
            ],
            skip_line_result_class_list=[
                'fp2VUc',
                'z7i0C m6QErb',
                'm6QErb tLjsW'
            ],

            search_string=[
                # 'toronto hospital',

                # 'toronto bank',

                # 'toronto fitness center',

                # 'toronto church',

                # 'toronto metro',
                # 'toronto walmart',
                # 'toronto freshco',
                # 'toronto costco',

                'canada toronto coin laundry',
                'canada toronto costco'
                'canada toronto freshco'
            ]
        )



            # else:
                # raise ValueError("ENVIRONMENT environment variable should be in ('production', 'staging')")
