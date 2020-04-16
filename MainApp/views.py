from django.shortcuts import render
from MainApp.forms import Phone_Form
import pandas as pd
from MainApp.models import Phone
from django.http import HttpResponse
import bs4
from MainApp import GraphMaker as gm
from MainApp.forms import Filter_Form
from MainApp.models import FilterPhone
from MainApp.qp import queryProcessor as qpf
from MainApp.qp import predictorFunc as qpp
from MainApp.models import Filter
from MainApp.forms import Filter_Form1
from MainApp.forms import Graph_Form 
from django.shortcuts import redirect
from django.core import serializers
import os

#column names
maincol = ["Name","Brand","Model","Battery","Screen Size (in inches)","Touchscreen","Resolution width","Resolution height","Processor Cores","RAM (in MB)","Storage(in GB)","Rear Camera","Front Camera","OS","Wi-Fi","Bluetooth","GPS","SIMs","3G","4G-LTE","Price (in Rs.)"]
qcol = ["Battery min","Battery max","Screen min","Screen max","Touchscreen","RWidth min","RWidth max","RHeight min","RHeight max","Cores","RAM min","RAM max","Storage min","Storage max","RCamera min","RCamera max","Fcamera min","FCamera max","OS","Wi-Fi","Bluetooth","GPS","SIM min","SIM max","3G","4G"]
pcol = ["Battery","Screen Size (in inches)","Touchscreen","Resolution width","Resolution height","Processor Cores","RAM (in MB)","Storage (in GB)","Rear Camera","Front Camera","OS","Wi-Fi","Bluetooth","GPS","SIMs","3G","4G-LTE"]

def firstPage(request):
    return redirect(main_page)

def inserter(i):
    p1 = Phone.objects.create(**i)
    p1.save()


def reseter(i):
    p1 = Phone.objects.create(
            Name = i[0], 
            Brand = i[1],
            Model = i[2],
            Battery = i[3],
            Screen = i[4],
            Touchscreen = i[5],
            Resolution_x = i[6],
            Resolution_y = i[7],
            Processor_Cores = i[8],
            RAM = i[9],
            Storage = i[10],
            Rear_Camera = i[11],
            Front_Camera = i[12],
            OS = i[13],
            Wi_Fi = i[14],
            Bluetooth = i[15],
            GPS = i[16],
            SIMs = i[17],
            H_3G = i[18],
            LTE_4G = i[19],
            Price =i[20] )
    p1.save()


def phone_form(request):
    if request.method=='POST':
        pf = Phone_Form(request.POST)
        if pf.is_valid():
            inserter(pf.cleaned_data)
            return render(request,"AllPost.html",{})
    else:
        pf = Phone_Form()
    return render(request,"Adder.html",{'form':pf, 'name':'Add a Phone', 'help':'*all fields are compulsory'})

def predict_form(request):
    if request.method=='POST':
        ff = Filter_Form(request.POST)
        if ff.is_valid():
            result = qpp(ff.cleaned_data)
            return render(request,"prediction.html",{'price':result})
    else:
        pf = Filter_Form()
    return render(request,"Adder.html",{'form':pf, 'name':'Price Predictor','help':'*parameters for prediction'})

def filter_form(request):
    if request.method=='POST':
        ff = Filter_Form1(request.POST)
        if ff.is_valid():
            result = qpf(ff.cleaned_data)
            result = serializers.serialize('python',result)
            return render(request,"DataPage.html",{'heading':'Results','qset':result, 'colname': maincol})
    else:
        pf = Filter_Form1()
    return render(request,"Adder.html",{'form':pf, 'name':'Filter Apply','help':'*parametrs for filter'})


def reset_data(request):
    Phone.objects.all().delete()
    Filter.objects.all().delete()
    FilterPhone.objects.all().delete() 
    PROJECT_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__),'..','..'))
    os.chdir(os.path.join(PROJECT_DIR,'media','data'))
    data = pd.read_csv('ndtv_data_final.csv')
    for row in range(len(data)):
        i = list(data.iloc[row])
        reseter(i)
    os.chdir(PROJECT_DIR)
    return render(request,"AllPost.html",{})

def main_page(request):
    return render(request,"home_page.html",{})

def database(request):
    ob = serializers.serialize('python',Phone.objects.all())
    return render(request,"DataPage.html",{'heading':'DATABASE','qset':ob,'colname': maincol})

def queries_database(request):
    ob = serializers.serialize('python',Filter.objects.all())
    return render(request,"DataPage.html",{'heading':'QUERIES HISTORY','qset':ob,'colname':qcol})

def prediction_database(request):
    ob = serializers.serialize('python',FilterPhone.objects.all())
    return render(request,"DataPage.html",{'heading':'PREDICTION HISTORY','qset':ob,'colname':pcol})
    
def graph(request):
    if request.method=='POST':
        ff = Graph_Form(request.POST)
        if ff.is_valid():
            maker = ff.cleaned_data['choice']
            gm.make(maker)
            return render(request,"GraphPage.html")
    else:
        pf = Graph_Form()
    return render(request,"Adder.html",{'form':pf, 'name':'Graph Selector','help':'*select the graph to visualize'})
