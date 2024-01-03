import dash
from dash.dependencies import Input, Output, State
from dash.dash import dash_table
from dash import dcc as dcc
from dash import html as html
import pyodbc
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from flask_sqlalchemy import SQLAlchemy
from flask import Flask

conn_str = 'DRIVER={SQL Server};SERVER=test-mpi.corp.iges.si;DATABASE=MPI_Storage;Trusted_Connection=yes;'
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

app = dash.Dash(__name__)

tender_layout = html.Div([
    dash_table.DataTable(
        id='tender-table',
        columns=[
            {'name': col, 'id': col} for col in ['T_ID', 'T_PublisherDate', 'T_LotNumber', 'T_SubLot', 'T_P_ID',
                                                'T_DateHourFrom', 'T_DateHourTo', 'T_Type', 'T_Power', 'T_Status',
                                                'T_TimeStampTick', 'T_UserName', 'T_Comment']
        ],
        editable=True,
        row_deletable=True,
        sort_action="native",
        sort_mode="multi",
        filter_action="native",
        page_action='none',
        style_table={'height': '300px', 'overflowY': 'auto'},
    ),
    html.Button('Add Tender', id='add-tender-button', n_clicks=0),
])