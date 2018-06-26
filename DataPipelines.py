#!ve/bin/python3
import sys, os
import abc
from abc import ABCMeta, abstractproperty, abstractmethod
import configparser
from numpy import integer, ndarray, array, dtype
import requests

print("DataPipelines.py\n\
______________________\n\
Author: William Murphy\n\
Data Analytic Engineer\n\
Vibrant: Emotional Health")


class DataPipelinesInterface(metaclass=ABCMeta):
    """data pipelining interface"""

    @abstractmethod
    def import_data_source(self, *args, **kwargs):
        """abstract data soruce"""

    @abstractmethod
    def mapper(self, *args, **kwargs):
        """abstract mapper source"""

# --- Web Connection Implementation
class WebDataPipeline(DataPipelinesInterface):
    """Process Web data"""
    def __init__(self) -> None:
        self._datasource = None
        self.raw_data_ = tuple()
        self.byte_pos = 0
        self.FILE_SIZE = 0

    def __set__(self, datasource: str) -> None:
        """set the datasource"""
        self._datasource = datasource

    def __get__(self, ds: str) -> str:
        """get the current datasource"""
        if self._datasource is not None:
            print('Datasource:', self._datasource)
            return self._datasource
        else:
            print('No Datasouce set')

    def __delete__(self) -> None:
        """remove current datasource"""
        if self._datasource is None:
            raise AttributeError("Error: datasource has not been set")
        self._datasource = None

    def import_data_source(self, chunk_size=100):
        """connect to data source"""
        try:
            r = requests.get(url=self._datasource, stream=True)
            if r.status_code == 200:
                print("Successfully connected: status[{}]".format(r.status_code))
                for chunk in r.iter_content(chunk_size):
                    self.FILE_SIZE += chunk_size
                """
                while True:
                    self.raw_data_ = self.raw_data_ + str(r.content[self.byte_pos:chunk_size+self.byte_pos].decode('utf-8'))
                    self.byte_pos += chunk_size
                    if
                """
                #print("current chunk:\n",self.raw_data_)
                
            else:
                raise ConnectionError("Error: connection failed: status[{}]".format(r.status_code))
        except ConnectionError as e:
            print(str(e))

    def mapper(self):
        pass
        
            
        
        

def main():
    """main function"""
    # --- data
    url_ = "https://assets.datacamp.com/production/course_1939/datasets/boston.csv"
    # --- create pipeline
    web_pipeline = WebDataPipeline()
    web_pipeline.__set__(datasource=url_)
    web_pipeline.import_data_source(chunk_size=100)
    web_pipeline.import_data_source(chunk_size=100)
    print("FILE_SIZE: bytes={}".format(web_pipeline.FILE_SIZE))
        
        
if __name__=='__main__':
    main()
