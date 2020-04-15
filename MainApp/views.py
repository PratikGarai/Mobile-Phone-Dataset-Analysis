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
            Name = i[1], 
            Brand = i[2],
            Model = i[3],
            Battery = i[4],
            Screen = i[5],
            Touchscreen = i[6],
            Resolution_x = i[7],
            Resolution_y = i[8],
            Processor_Cores = i[9],
            RAM = i[10],
            Storage = i[11],
            Rear_Camera = i[12],
            Front_Camera = i[13],
            OS = i[14],
            Wi_Fi = i[15],
            Bluetooth = i[16],
            GPS = i[17],
            SIMs = i[18],
            H_3G = i[19],
            LTE_4G = i[20],
            Price =i[21] )
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
    data = pd.read_csv('ndtv_data_final.csv')
    for row in range(len(data)):
        i = list(data.iloc[row])
        reseter(i)
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
            page = bs4.BeautifulSoup(open('graphplate.html'))
            return render(request,"GraphPage.html",{'page':str(page.select('div')[0])})
    else:
        pf = Graph_Form()
    return render(request,"Adder.html",{'form':pf, 'name':'Graph Selector','help':'*select the graph to visualize'})
