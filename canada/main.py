from crawler.google_map import GoogleMapCrawler
from variables import server_variables

from mapper.google_map import google_map_mapper
from page_drawer.google_map import GoogleMapDrawer

if __name__ == '__main__':

    ############
    # Crawling #
    ############
    target_list = server_variables.google.search_string
    for search_string in target_list:
        crawler = GoogleMapCrawler(input_string=search_string)
        crawler.run()

    ###########
    # Mapping #
    ###########
    google_map_mapper(google_variable=server_variables.google)
    ###########
    # Drawing #
    ###########
    drawer = GoogleMapDrawer(google_variable=server_variables.google)
    drawer.run()
