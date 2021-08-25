import pandas as pd
import numpy as np
from log import logger
import logging
import logging.handlers

from project_config import Config



class data_processor():

    def __init__(self) -> None:
        self._logger = logger



    # Percentage % of total missing values in the dataset

    def total_percent_missing_data(self, df):

        # Calculate total number of cells in dataframe
        totalCells = np.product(df.shape)

        # Count number of missing values per column
        missingCount = df.isnull().sum()

        # Calculate total number of missing values
        totalMissing = missingCount.sum()

        # Calculate percentage of missing values
        

        return round(((totalMissing/totalCells) * 100), 2)

    def missing_data_per_column(self, df):
        item_list = []
        row_list = []
        new_columns=['Column', 'No. of Missing Values', '% Missing Values per column']
        total_no_data_per_column = df.shape[0]-1
        i=0
        for item in df.columns:
            no_missing_values = df[item].isna().sum()
            percentage = str(round(((no_missing_values/total_no_data_per_column) * 100), 2))+" %"
            row_list.append(item)
            row_list.append(no_missing_values)
            row_list.append(percentage)
            item_list.append(row_list)
            row_list = []

        df_data = pd.DataFrame(item_list, columns = new_columns)
        return df_data


    def drop_columns(self, df, column_list):
        df_new = df.drop(column_list, axis=1)

        return df_new

    
    def fix_outlier(self, data, column_list):
        for column in column_list:
            data[column] = np.where(data[column] > data[column].quantile(0.95), data[column].median(),data[column])
        
        return data