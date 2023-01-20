from crawler.google_map import GoogleMapCrawler
from variables import server_variables

from utils.google_map_helper import google_map_data_processor

if __name__ == '__main__':
    target_list = server_variables.google.search_string
    for search_string in target_list:
        crawler = GoogleMapCrawler(input_string=search_string)
        crawler.run()

    google_map_data_processor(
        api_key=server_variables.google.api_key,
        file_path=server_variables.google.file_path,
        raw_path_suffix=server_variables.google.raw_path_suffix,
        enriched_path_suffix=server_variables.google.enriched_path_suffix,
        file_format=server_variables.google.file_format,
    )
