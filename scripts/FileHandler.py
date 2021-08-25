import pandas as pd
from log import logger
import logging
import logging.handlers

from project_config import Config

class FileHandler():

  def __init__(self):
    self._logger = logging

  def csv_file_save(self, df, name, index=False):
    try:
      path = Config.Data_path / str(name + '.csv')
      df.to_csv(path, index=index)
      self._logger.info(f"{name} file saved successfully in csv format")
    except Exception:
      self._logger.exception(f"{name} save failed")


  def csv_file_read(self, name, missing_values=[]):
    try:
      path = Config.Data_path / str(name + '.csv')
      df = pd.read_csv(path, na_values=missing_values)
      self._logger.info(f"{name} file read successfully")
      return df
    except FileNotFoundError:
      self._logger.exception(f"{name} not found")

