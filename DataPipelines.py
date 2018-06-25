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
        _datasource = None

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

    def import_data_source(self):
        """connect to data source"""
        try:
            r = requests.get(url=self._datasource)
            if r.status_code == 200:
                print("Successfully connected: status[{}]".format(r.status_code))
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
    web_pipeline.import_data_source()
        
        
if __name__=='__main__':
    main()


    
