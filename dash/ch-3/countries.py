import pandas as pd
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

poverty_data = pd.read_csv('data/PovStatsData.csv')
regions = ['East Asia & Pacific', 'Europe & Central Asia',           'Fragile and conflict affected situations', 'High income', 'IDA countries classified as fragile situations', 'IDA total', 'Latin America & Caribbean', 'Low & middle income', 'Low income', 'Lower middle income', 'Middle East & North Africa', 'Middle income', 'South Asia', 'Sub-Saharan Africa', 'Upper middle income', 'World']

population_df = poverty_data[~poverty_data['Country Name'].isin(regions) & (poverty_data['Indicator Name'] == 'Population, total')]

def plot_countries_by_population(year):
    year_df = population_df[['Country Name', year]].sort_values(year, ascending=False)[:20]
    fig = go.Figure()
    fig.add_bar(x=year_df['Country Name'], y=year_df[year])
    fig.layout.title=f'Top twenty countries by population - {year}'
    fig.show()

#plot_countries_by_population('2016')

