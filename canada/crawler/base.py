# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from abc import abstractmethod
from typing import Any, Dict, Iterable, List, Optional

class WebCrawler:
    def __init__(self, url:str, input_string:str):
        self._url = url
        self._input_string = input_string
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    @classmethod
    @abstractmethod
    def search(cls):
        return NotImplementedError()

    @classmethod
    @abstractmethod
    def crawl(cls) -> List[Dict[str, Any]]:
        return NotImplementedError()

    @classmethod
    @abstractmethod
    def scroll_down(cls):
        return NotImplementedError()

    @classmethod
    @abstractmethod
    def format(cls) -> List[Dict[str, Any]]:
        return NotImplementedError()

    def get_parsed_info(self, element, parse_type):
        if parse_type is None:
            raise ValueError('parse type is not available')
        if parse_type == 'text':
            return element.text
        elif parse_type == 'class':
            return element.get_attribute('class')
        elif parse_type == 'aria_label':
            return element.get_attribute('aria-label')
        elif parse_type == 'href':
            return element.get_attribute('href')
        else:
            return None

    def quit(self):
        self.driver.quit()
