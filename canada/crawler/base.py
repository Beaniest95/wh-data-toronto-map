# %%
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from abc import abstractmethod

class WebCrawler:
    def __init__(self, url:str, input_string:str):
        self._url = url
        self._input_string = input_string
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    @classmethod
    @abstractmethod
    def search(cls) -> str:
        return NotImplementedError()
