# Graph and Diagram Ploting script.
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from log import logger
import logging
import logging.handlers

from project_config import Config


class Plot():

    def __init__(self):
        self._logger = logger

    ################### PLOTTING FUNCTIONS #####################

    def plot_box(self, df:pd.DataFrame, x_col:str, title:str) -> None:
        plt.figure(figsize=(12, 7))
        sns.boxplot(data = df, x=x_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.show()

    def plot_hist(self, df:pd.DataFrame, column:str, color:str)->None:
        sns.displot(data=df, x=column, color=color, kde=True, height=4, aspect=2)
        plt.title(f'Distribution of {column}', size=20, fontweight='bold')
        plt.show()


    def plot_count(self, df:pd.DataFrame, column:str) -> None:
        plt.figure(figsize=(12, 7))
        sns.countplot(data=df, x=column)
        plt.title(f'Distribution of {column}', size=20, fontweight='bold')
        plt.show()
        
    def plot_bar(self, df:pd.DataFrame, x_col:str, y_col:str, title:str, xlabel:str, ylabel:str)->None:
        plt.figure(figsize=(6, 4))
        sns.barplot(data = df, x=x_col, y=y_col)
        plt.title(title, size=20)
        plt.xticks(rotation=45, fontsize=12)
        plt.yticks( fontsize=14)
        plt.xlabel(xlabel, fontsize=13)
        plt.ylabel(ylabel, fontsize=13)
        plt.show()

    def plot_heatmap(self, df:pd.DataFrame, title:str, cbar=False)->None:
        plt.figure(figsize=(12, 7))
        sns.heatmap(df, annot=True, cmap='viridis', vmin=0, vmax=1, fmt='.2f', linewidths=.7, cbar=cbar )
        plt.title(title, size=18, fontweight='bold')
        plt.show()

    def plot_box(self, df:pd.DataFrame, x_col:str, title:str) -> None:
        plt.figure(figsize=(12, 7))
        sns.boxplot(data = df, x=x_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.show()

    def plot_box_multi(self, df:pd.DataFrame, x_col:str, y_col:str, title:str) -> None:
        plt.figure(figsize=(12, 7))
        sns.boxplot(data = df, x=x_col, y=y_col)
        plt.title(title, size=20)
        plt.xticks(rotation=75, fontsize=14)
        plt.yticks( fontsize=14)
        plt.show()

    def plot_scatter(self, df: pd.DataFrame, x_col: str, y_col: str, title: str, hue: str, style: str) -> None:
        plt.figure(figsize=(8, 5))
        sns.scatterplot(data = df, x=x_col, y=y_col, hue=hue, style=style)
        plt.title(title, size=20)
        plt.xticks(fontsize=14)
        plt.yticks( fontsize=14)
        plt.show()


    def heat(self, df, color, size):
    
        corr = df.corr()
        mask = np.zeros_like(corr, dtype=np.bool)
        mask[np.triu_indices_from(corr)] = True
        
        plt.figure(figsize=size)
        sns.heatmap(corr, mask=mask, annot=True, cmap=color)
        plt.show()


    def scatter_feature_plot(self, df, feature1, feature2, title, fields):
    
        fig = go.Figure()
        fig.update_layout(
            title=title,
            width=600,
            height=400,
            margin=dict(
                        l=20,
                        r=20,
                        t=40,
                        b=20,
                    )
        )
        
        fig.add_trace(go.Scatter(x=df[feature1+"_"+fields[0]], 
                                y=df[feature2+"_"+fields[0]], 
                                mode="markers", 
                                name="mean",
                                ))

        fig.add_trace(go.Scatter(x=df[feature1+"_"+fields[1]], 
                                y=df[feature2+"_"+fields[1]], 
                                mode="markers", 
                                name="se",
                                ))
        fig.add_trace(go.Scatter(x=df[feature1+"_"+fields[2]], 
                             y=df[feature2+"_"+fields[2]], 
                             mode="markers", 
                             name="worst",
                             ))
        fig.show()