import numpy as np
import plotly.express as px
import pandas as pd
import nbformat as nb

df_titanic = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

# Exercise 1

# Section 1-5
def survival_demographics():

    age_bins = [0, 12, 19, 59, 110]
    age_labels = ['Child', 'Teen', 'Adult', 'Senior']

    df_titanic['age_group'] = pd.cut(df_titanic['Age'], 
                                        bins = age_bins, 
                                        labels = age_labels,
                                        include_lowest = True)
    
    df_grouped = df_titanic.groupby(['age_group', 'Sex', 'Pclass']).agg(
        n_passengers = ('Survived', 'size'),
        n_survivors = ('Survived', 'sum'),
        survival_rate = ('Survived', lambda x: (x.sum() / x.size) * 100)
    ).reset_index()

    df_grouped = df_grouped.rename(columns = {'Pclass': 'pclass'})

    sorted_df_grouped = df_grouped.sort_values(by = ['age_group', 'Sex'])
    
    return sorted_df_grouped.reset_index(drop = True)

# Section 6: See app.py

# Section 7
def visualize_demographic():
    age_bins = [0, 12, 19, 59, 110]
    age_labels = ['Child', 'Teen', 'Adult', 'Senior']

    df_titanic['age_category'] = pd.cut(df_titanic['Age'], 
                                        bins = age_bins, 
                                        labels = age_labels,
                                        include_lowest = True)
    
    df_grouped = df_titanic.groupby(['age_category', 'Sex']).agg(
        avg_survival_rate = ('Survived', 'mean')
    ).reset_index()

    df_grouped['avg_survival_rate_pct'] = df_grouped['avg_survival_rate'] * 100

    fig = px.bar(df_grouped, 
                 x = "age_category", 
                 y = "avg_survival_rate_pct", 
                 color = "Sex", 
                 barmode="group",
                 labels = {'age_category':'Age Category',
                           'avg_survival_rate_pct':'Average Survival Rate (%)'
                           },
                           title = "Average Survival Rate by Age Category and Sex",
                           color_discrete_sequence = ["#4b99d0", '#ff7f0e']
                           )
    return fig

# Exercise 2

# Section 1-3
def family_groups():
    df_titanic['family_size'] = df_titanic['SibSp'] + df_titanic['Parch'] + 1

    df_grouped = df_titanic.groupby(['family_size', 'Pclass']).agg(
        n_passengers = ('Survived', 'size'),
        avg_fare = ('Fare', lambda x: (x.sum() / x.size)),
        min_fare = ('Fare', 'min'),
        max_fare = ('Fare', 'max')
    ).reset_index()

    sorted_df_grouped = df_grouped.sort_values(by = ['Pclass', 'family_size'])
    
    return df_grouped

# Section 4
def last_names():
    last_names = df_titanic['Name'].str.split(',').str[0]
    return last_names.value_counts()

# Section 5
def visualize_families():
    fig = px.histogram(df_titanic, 
                       x = 'Age', 
                       y = 'Fare', 
                       color = 'Sex', 
                       histfunc='avg',
                       labels = {'avg of Fare' : 'Average Fare'
                           },
                           title = "Average Fare by Age for each Sex",
                           color_discrete_sequence = ["#4b99d0", '#ff7f0e']
                           )
    return fig