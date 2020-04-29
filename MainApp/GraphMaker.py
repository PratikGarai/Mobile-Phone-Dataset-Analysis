import plotly.offline as pyo
import plotly.graph_objs as go

import os, sys
import pandas as pd

PROJECT_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__),'..','..'))

sys.path.append(PROJECT_DIR)

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Proj1.settings")
django.setup()

os.environ['DJANGO_SETTINGS_MODULE']='Proj1.settings'

from MainApp.models import Phone

os.chdir(os.path.join(PROJECT_DIR,'media','html'))

df=pd.read_csv("\\DBMS_J_COMP\\media\\data\\ndtv_data_final.csv")

def make(n):
    if n==1:
        data = [go.Scatter(x=[1,2,3],y=[3,1,6])]
    elif n==2:
        data = [go.Scatter(x=[1,2,3],y=[1,2,20])]
    elif n==3:
        fig=go.Figure()
        for x in list(df['Operating system'].unique()):
            fig.add_trace(go.Box(y=df["Price"][df["Operating system"]==x],name=x))
        fig.update_layout(title_text="Mean Price of each OS",)
        data=fig
    elif n==4:
        data=px.scatter(df,x="RAM (MB)",y="Price",color="Operating system",title="Price vs RAM for each OS")
    
    pyo.plot(data,filename='graphplate.html',auto_open=False)
print(Phone.objects.count())
