import plotly.offline as pyo
import plotly.graph_objs as go

import os, sys

PROJECT_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__),'..','..'))

sys.path.append(PROJECT_DIR)

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Proj1.settings")
django.setup()

os.environ['DJANGO_SETTINGS_MODULE']='Proj1.settings'

from MainApp.models import Phone


def make(n):
    if n==1:
        data = [go.Scatter(x=[1,2,3],y=[3,1,6])]
    elif n==2:
        data = [go.Scatter(x=[1,2,3],y=[1,2,20])]
    
    pyo.plot(data,filename='graphplate.html',auto_open=False)
print(Phone.objects.count())
