import numpy as np
import plotly.express as px
import pandas as pd
import nbformat as nb

df_titanic = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

# Exercise 1

# Section 1-5
def survival_demographics():
     '''
    Function to produce a table with
    various aggregated columns.

    Parameters:
    No input parameters.

    Return value:
    A table including the various columns
    produced within the function.
    '''
    # Create the bins for the age_groups.
    age_bins = [0, 12, 19, 59, 110]

    # Create the labels for the age_groups.
    age_labels = ['Child', 'Teen', 'Adult', 'Senior']

    # Cut the 'Age' column by the age_groups bins.
    df_titanic['age_group'] = pd.cut(df_titanic['Age'], 
                                        bins = age_bins, 
                                        labels = age_labels,
                                        include_lowest = True)
    
    # Generating the table.
    df_grouped = df_titanic.groupby(['age_group', 'Sex', 'Pclass']).agg(
        n_passengers = ('Survived', 'size'),
        n_survivors = ('Survived', 'sum'),
        survival_rate = ('Survived', lambda x: (x.sum() / x.size) * 100)
    ).reset_index()

    # Trying to change column name to satisfy the autograder, it
    # didn't really work.
    df_grouped = df_grouped.rename(columns = {'Pclass': 'pclass'})

    # Sort the values so the table is a bit easier to read.
    sorted_df_grouped = df_grouped.sort_values(by = ['age_group', 'Sex'])
    
    return sorted_df_grouped.reset_index(drop = True)

# Section 6: See app.py

# Section 7
def visualize_demographic():
     '''
    Function to produce a visualization
    to answer my app.py question.

    Parameters:
    No input parameters.

    Return value:
    A bar plot of average survival rate
    by age group and sex.
    '''
    # Recall the bins since everything
    # is left in the previous function
    age_bins = [0, 12, 19, 59, 110]

    # Recall the age_labels
    age_labels = ['Child', 'Teen', 'Adult', 'Senior']

    # Recall the age_group column
    df_titanic['age_group'] = pd.cut(df_titanic['Age'], 
                                        bins = age_bins, 
                                        labels = age_labels,
                                        include_lowest = True)
    
    # Group, aggregate and find average survival rate
    df_grouped = df_titanic.groupby(['age_group', 'Sex']).agg(
        avg_survival_rate = ('Survived', 'mean')
    ).reset_index()

    # Create a new percentage column
    df_grouped['avg_survival_rate_pct'] = df_grouped['avg_survival_rate'] * 100

    # Create the bar plot
    fig = px.bar(df_grouped, 
                 x = "age_group", 
                 y = "avg_survival_rate_pct", 
                 color = "Sex", 
                 barmode="group",
                 labels = {'age_group':'Age Group',
                           'avg_survival_rate_pct':'Average Survival Rate (%)'
                           },
                           title = "Average Survival Rate by Age Group and Sex",
                           color_discrete_sequence = ["#4b99d0", '#ff7f0e']
                           )
    return fig

# Exercise 2

# Section 1-3
def family_groups():
     '''
    Function to explor the relationship
    between family size, passenger class,
    and ticket fare.

    Parameters:
    No input parameters.

    Return value:
    A sorted table of various aggregated
    and grouped columns.
    '''
    # Create the family size column
    df_titanic['family_size'] = df_titanic['SibSp'] + df_titanic['Parch'] + 1

    # Create the grouped data set with fare information
    df_grouped = df_titanic.groupby(['family_size', 'Pclass']).agg(
        n_passengers = ('Survived', 'size'),
        avg_fare = ('Fare', lambda x: (x.sum() / x.size)),
        min_fare = ('Fare', 'min'),
        max_fare = ('Fare', 'max')
    ).reset_index()

    # Sort the output table by Pclass and family_size
    sorted_df_grouped = df_grouped.sort_values(by = ['Pclass', 'family_size'])
    
    return df_grouped

# Section 4
def last_names():
     '''
    Function to extract the last
    names of each passenger.

    Parameters:
    No input parameters.

    Return value:
    A pandas series with last name
    count as the value and the last 
    name as the index.
    '''
    # Use string split to extract the last names.
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