import numpy as np
import plotly.express as px
import pandas as pd

df_titanic = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

# Exercise 1

# Section 1-5
def survival_demographics():

    age_bins = [0, 12, 19, 59, 110]
    age_labels = ['Child', 'Teen', 'Adult', 'Senior']

    df_titanic['age_category'] = pd.cut(df_titanic['Age'], 
                                        bins = age_bins, 
                                        labels = age_labels,
                                        include_lowest = True)
    
    df_grouped = df_titanic.groupby(['age_category', 'Sex', 'Pclass']).agg(
        n_passengers = ('Survived', 'size'),
        n_survivors = ('Survived', 'sum'),
        survival_rate = ('Survived', lambda x: (x.sum() / x.size) * 100)
    ).reset_index()

    sorted_df_grouped = df_grouped.sort_values(by = ['age_category', 'Sex'])
    
    return sorted_df_grouped.reset_index(drop = True)

#def survival_demographics()