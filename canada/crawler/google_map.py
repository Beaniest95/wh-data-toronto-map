import time
import json
from loguru import logger
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from typing import Any, Dict, Iterable, List, Optional

from crawler.base import WebCrawler
from variables import server_variables

class GoogleMapCrawler(WebCrawler):

    def __init__(self,
        input_string:str,
        url:str = server_variables.google.url,
    ):
        super().__init__(
            url=url,
            input_string=input_string,
        )
        self.result_dataset = []
        time.sleep(5)

    @property
    def url(self):
        return self._url
    @property
    def searchbox_selector(self):
        return self._searchbox_selector
    @property
    def searchbutton_selector(self):
        return self._searchbutton_selector
    @property
    def search_string(self):
        return self._input_string.replace(" ", "+")

    def search(self):
        searchbox_selector = server_variables.google.searchbox_selector
        searchbutton_selector = server_variables.google.searchbutton_selector
        logger.info(f'searchbox selector: {searchbox_selector}')
        logger.info(f'searchbutton selector: {searchbutton_selector}')

        self.driver.get(self.url)
        time.sleep(3)

        logger.info(f'search string: {self.search_string}')
        searchbox = self.driver.find_element(By.CSS_SELECTOR, searchbox_selector)
        time.sleep(1)
        searchbox.send_keys(self.search_string)
        time.sleep(1)

        searchbutton = self.driver.find_element(By.CSS_SELECTOR, searchbutton_selector)
        time.sleep(1)
        searchbutton.click()
        time.sleep(10)

        self.scroll_down()

    def scroll_down(self):
        scroll_count = 0
        while True:
            scroll_path = self.driver.find_element(By.XPATH, server_variables.google.scroll_xpath)
            time.sleep(1)
            self.driver.execute_script("arguments[0].scrollBy(0,5000)", scroll_path)
            time.sleep(3)
            scroll_count += 1
            if scroll_count == 30:
                break

    def _get_element_by_selector(self, selector):
        return self.driver.find_element(By.CSS_SELECTOR, selector)

    def _get_element_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def _get_element_class_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath).get_attribute('class')

    def _get_line_type(self, xpath):
        try:
            line_type = self.driver.find_element(By.XPATH, xpath).get_attribute('class')
            if line_type in server_variables.google.valid_result_class_list:
                return "valid"
            elif line_type in server_variables.google.end_line_result_class_list:
                return "end"
            elif line_type in server_variables.google.skip_line_result_class_list:
                return "skip"
            else:
                logger.info(f"line type is unknown: {line_type}")
                logger.info(f"logging aria label: {self.driver.find_element(By.XPATH, xpath).get_attribute('aria-label')}")
                return "unknown"
        except Exception as e:
            logger.info(str(e))
            return "skip"


    def crawl(self):
        for i in range(3, 999):
            index = str(i)
            line_type = self._get_line_type(server_variables.google.valid_result_xpath.format(index=index))
            url, name, grade, address = None, None, None, None
            if line_type == "valid":
                try:
                    name    = self.get_parsed_info(self._get_element_by_xpath(server_variables.google.name_xpath.format(index=index)), 'text')
                    address = self.get_parsed_info(self._get_element_by_xpath(server_variables.google.address_xpath.format(index=index)), 'text')
                    url     = self.get_parsed_info(self._get_element_by_xpath(server_variables.google.url_link_xpath.format(index=index)), 'href')
                    grade   = self.get_parsed_info(self._get_element_by_xpath(server_variables.google.grade_xpath.format(index=index)), 'text')
                    self.result_dataset.append(self.format(url, name, grade, address))
                except Exception as e:
                    logger.info(f"Error has been occurred: {str(e)}")
                    self.result_dataset.append(self.format(url, name, grade, address))
            elif line_type == "skip":
                continue
            elif line_type == "end":
                logger.info(f"End Crawling: {str(i)}")
                break
            else:
                logger.info(f'Error has been occurred: line type is {line_type}')
                logger.info(f"Error has been occurred: line number is {str(i)}")
                time.sleep(60)
                break

        return self.result_dataset

    def format(self, url, name, grade, address):
        return dict(
            url = url,
            name = name,
            grade = grade,
            address = address,
        )

    def to_json(self):
        with open("results/json/google/raw/"+self.search_string.replace('+','_')+".json", "w") as f:
            json_file = json.dumps(self.result_dataset, indent=4)
            f.write(json_file)

    def run(self):
        self.search()
        self.crawl()
        self.to_json()
        self.quit()
