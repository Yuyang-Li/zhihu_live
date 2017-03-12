# -*- coding: utf-8 -*-
"""
Created on Wed Mar 08 00:04:12 2017

@author: Lily
"""
# the analyse of data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import sys
reload(sys)
sys.setdefaultencoding('utf8')


df_end = pd.read_csv('ended.csv')
df1_end = df_end.dropna()
df_ongo = pd.read_csv('ongoing.csv')
df_all = pd.read_csv('all.csv')


# describe
def describe_data():
    df_end.describe().to_csv('des_end.csv')
    df_ongo.describe().to_csv('des_ongo.csv')


# Visualization
# box plots(???)
def box_plot(df1,df2,a):
    plt.show(sns.boxplot(df1[a],df2[a],width=0.5))

# regression analysis
def regression_analysis(df):
    print df.corr()


def regression_analysis(df,x,y):
    df1 = df.loc[:,[x,y]]
    df1 = df1.dropna()
    sns.jointplot(x,y,df1,kind='reg')
    plt.show()

def histogram(df,a):
    plt.figure()
    sns.distplot(df[a],bins=100,rug=True)
    plt.show()

histogram(df_end,'费用')