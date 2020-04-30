import plotly.offline as pyo
import plotly.graph_objs as go
import plotly.express as px

import os, sys
import pandas as pd
PROJECT_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__),'..','..'))
sys.path.append(PROJECT_DIR)
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Proj1.settings")
django.setup()
os.environ['DJANGO_SETTINGS_MODULE']='Proj1.settings'
from MainApp.qp import stateSaver as state

state()
os.chdir(os.path.join(PROJECT_DIR,'media','data'))
df=pd.read_csv("local.csv")
os.chdir(os.path.join(PROJECT_DIR,'media','html'))


def make(n):
    if n==1:
        data = [go.Scatter(x=[1,2,3],y=[3,1,6])]
    elif n==2:
        data = [go.Scatter(x=[1,2,3],y=[1,2,20])]
    elif n==3:
        fig=go.Figure()
        for x in list(df['OS'].unique()):
            fig.add_trace(go.Box(y=df["Price"][df["OS"]==x],name=x))
        fig.update_layout(title_text="Mean Price of each OS",)
        data=fig
    elif n==4:
        data=px.scatter(df,x="RAM",y="Price",color="OS",title="Price vs RAM for each OS")
    
    pyo.plot(data,filename='graphplate.html',auto_open=False)
    os.chdir(PROJECT_DIR)
