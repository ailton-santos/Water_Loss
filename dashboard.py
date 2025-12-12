import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import os
import sys

# Add parent directories to path to import zone modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'east_zone')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'south_zone')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'north_zone')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'west_zone')))

from east_zone.simulation import run_simulation as run_east_simulation
from south_zone.simulation import run_simulation as run_south_simulation
from north_zone.simulation import run_simulation as run_north_simulation
from west_zone.simulation import run_simulation as run_west_simulation

# Initialize the Dash app
app = dash.Dash(__name__)

# Define app layout
app.layout = html.Div(children=[
    html.H1(children='Water Loss Reduction Simulation Dashboard'),
    html.Hr(),

    html.Div(children='''
        This dashboard simulates the evolution of water loss percentage over time 
        before and after the implementation of IoT and modernization technologies.
    '''),
    
    html.Div([
        html.H3("Select Zone:"),
        dcc.Dropdown(
            id='zone-dropdown',
            options=[
                {'label': 'East Zone', 'value': 'east'},
                {'label': 'South Zone', 'value': 'south'},
                {'label': 'North Zone', 'value': 'north'},
                {'label': 'West Zone', 'value': 'west'}
            ],
            value='east',
            clearable=False,
            style={'width': '50%'}
        )
    ]),

    dcc.Graph(id='water-loss-graph'),
    
    html.Hr(),
    
    html.H3("Weekly Progress Overview"),
    dcc.Graph(id='all-zones-progress'),
])

@app.callback(
    Output('water-loss-graph', 'figure'),
    Input('zone-dropdown', 'value')
)
def update_graph(selected_zone):
    """
    Updates the single-zone graph based on the dropdown selection.
    """
    weeks = 50  # Number of weeks to simulate
    
    if selected_zone == 'east':
        df = run_east_simulation(weeks)
        title = "East Zone Water Loss Evolution"
    elif selected_zone == 'south':
        df = run_south_simulation(weeks)
        title = "South Zone Water Loss Evolution"
    elif selected_zone == 'north':
        df = run_north_simulation(weeks)
        title = "North Zone Water Loss Evolution"
    elif selected_zone == 'west':
        df = run_west_simulation(weeks)
        title = "West Zone Water Loss Evolution"
    else:
        df = pd.DataFrame(columns=['week', 'water_loss_percentage'])
        title = "Select a Zone"
    
    fig = px.line(df, x='week', y='water_loss_percentage', 
                  title=title, markers=True)
    
    fig.add_vline(x=weeks/2, line_dash="dash", line_color="red", annotation_text="Modernization Implemented")

    return fig

@app.callback(
    Output('all-zones-progress', 'figure'),
    [Input('zone-dropdown', 'value')]
)
def update_all_zones_graph(selected_zone):
    """
    Updates the combined graph showing all zones.
    The input is used to trigger the update, but the data is regenerated.
    """
    weeks = 50
    df_east = run_east_simulation(weeks).rename(columns={'water_loss_percentage': 'East Zone'})
    df_south = run_south_simulation(weeks).rename(columns={'water_loss_percentage': 'South Zone'})
    df_north = run_north_simulation(weeks).rename(columns={'water_loss_percentage': 'North Zone'})
    df_west = run_west_simulation(weeks).rename(columns={'water_loss_percentage': 'West Zone'})
    
    # Merge all dataframes on the 'week' column
    df_combined = pd.merge(df_east, df_south, on='week')
    df_combined = pd.merge(df_combined, df_north, on='week')
    df_combined = pd.merge(df_combined, df_west, on='week')
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(x=df_combined['week'], y=df_combined['East Zone'], mode='lines', name='East Zone'))
    fig.add_trace(go.Scatter(x=df_combined['week'], y=df_combined['South Zone'], mode='lines', name='South Zone'))
    fig.add_trace(go.Scatter(x=df_combined['week'], y=df_combined['North Zone'], mode='lines', name='North Zone'))
    fig.add_trace(go.Scatter(x=df_combined['week'], y=df_combined['West Zone'], mode='lines', name='West Zone'))

    fig.update_layout(
        title="Comparative Water Loss Evolution Across All Zones",
        xaxis_title="Week",
        yaxis_title="Water Loss Percentage (%)"
    )
    
    fig.add_vline(x=weeks/2, line_dash="dash", line_color="red", annotation_text="Modernization Implemented")
    
    return fig

# Run the server
if __name__ == '__main__':
    app.run(debug=True)

