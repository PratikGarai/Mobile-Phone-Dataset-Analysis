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

def make(n):
    from MainApp.qp import stateSaver as state

    state()
    os.chdir(os.path.join(PROJECT_DIR,'media','data'))
    df=pd.read_csv("local.csv")
    os.chdir(os.path.join(PROJECT_DIR,'media','html'))

    if n==1:
        data = px.bar(data,x="Processor",y="Price",title="Price vs Processor Core")

    elif n==2:
        data = px.bar(data,x="Screen size (inches)",y="Resolution y",color="Resolution x")

    elif n==3:
        fig=go.Figure()
        for x in list(df['OS'].unique()):
            fig.add_trace(go.Box(y=df["Price"][df["OS"]==x],name=x))
        fig.update_layout(title_text="Mean Price of each OS",)
        data=fig

    elif n==4:
        data=px.scatter(df,x="RAM",y="Price",color="OS",title="Price vs RAM for each OS")

    elif n==5:
        data = px.pie(data,values="Internal storage (GB)",names="Processor",title="Internal Storage vs Processor Core")
    
    pyo.plot(data,filename='graphplate.html',auto_open=False)
    os.chdir(PROJECT_DIR)

    return 0
