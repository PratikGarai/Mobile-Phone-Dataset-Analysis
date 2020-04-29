import os, sys

PROJECT_DIR = os.path.abspath(os.path.join(os.path.abspath(__file__),'..','..'))
sys.path.append(PROJECT_DIR)
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Proj1.settings")
django.setup()
os.environ['DJANGO_SETTINGS_MODULE']='Proj1.settings'

from MainApp.models import FilterPhone
from MainApp.models import Phone
from MainApp.models import Filter
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np

def queryProcessor(i):
    p1 = Filter.objects.create(**i)
    p1.save()

    qset = Phone.objects.all()
    if i['Battery_1']!=None and i['Battery_1']!='':
        qset = qset.filter(Battery__gte = i['Battery_1'])
    if i['Battery_2']!=None and i['Battery_2']!='':
        qset = qset.filter(Battery__lte = i['Battery_2'])
    if i['Screen_1']!=None and i['Screen_1']!='':
        qset = qset.filter(Screen__gte = i['Screen_1'])
    if i['Screen_2']!=None and i['Screen_2']!='':
        qset = qset.filter(Screen__lte = i['Screen_2'])
    if i['Touchscreen']!='' :
        qset = qset.filter(Touchscreen = i['Touchscreen'])
    if i['Resolution_x_1']!=None and i['Resolution_x_1']!='':
        qset = qset.filter(Resolution_x__gte = i['Resolution_x_1'])
    if i['Resolution_x_2']!=None and i['Resolution_x_2']!='':
        qset = qset.filter(Resolution_x__lte = i['Resolution_x_2'])
    if i['Resolution_y_1']!=None and i['Resolution_y_1']!='':
        qset = qset.filter(Resolution_y__gte = i['Resolution_y_1'])
    if i['Resolution_y_2']!=None and i['Resolution_y_2']!='':
        qset = qset.filter(Resolution_y__lte = i['Resolution_y_2'])
    if i['Processor_Cores']!=None and i['Processor_Cores']!='':
        qset = qset.filter(Processor_Cores = i['Processor_Cores'])
    if i['RAM_1']!=None and i['RAM_1']!='':
        qset = qset.filter(RAM__gte = i['RAM_1'])
    if i['RAM_2']!=None and i['RAM_2']!='':
        qset = qset.filter(RAM__lte = i['RAM_2'])
    if i['Storage_1']!=None and i['Storage_1']!='':
        qset = qset.filter(Storage__gte = i['Storage_1'])
    if i['Storage_2']!=None and i['Storage_2']!='':
        qset = qset.filter(Storage__lte = i['Storage_2'])
    if i['Rear_Camera_1']!=None and i['Rear_Camera_1']!='':
        qset = qset.filter(Rear_Camera__gte = i['Rear_Camera_1'])
    if i['Rear_Camera_2']!=None and i['Rear_Camera_2']!='':
        qset = qset.filter(Rear_Camera__lte = i['Rear_Camera_2'])
    if i['Front_Camera_1']!=None and i['Front_Camera_1']!='':
        qset = qset.filter(Front_Camera__gte = i['Front_Camera_1'])
    if i['Front_Camera_2']!=None and i['Front_Camera_2']!='':
        qset = qset.filter(Front_Camera__lte = i['Front_Camera_2'])
    if i['OS']!='':
        qset = qset.filter(OS = i['OS'])
    if i['Wi_Fi']!='':
        qset = qset.filter(Wi_Fi = i['Wi_Fi'])
    if i['Bluetooth']!='':
        qset = qset.filter(Bluetooth = i['Bluetooth'])
    if i['GPS']!='':
        qset = qset.filter(GPS = i['GPS'])
    if i['SIMs_1']!=None and i['SIMs_1']!='':
        qset = qset.filter(SIMs__gte = i['SIMs_1'])
    if i['SIMs_2']!=None and i['SIMs_2']!='':
        qset = qset.filter(SIMs__lte = i['SIMs_2'])
    if i['H_3G']!='':
        qset = qset.filter(H_3G = i['H_3G'])
    if i['LTE_4G']!='':
        qset = qset.filter(LTE_4G = i['LTE_4G'])

    return qset

def predictorFunc(i):
    l = []
    inp = []
    prediction = 0
    if i['Battery']!=None and i['Battery']!='':
        l.append('Battery')
        inp.append(i['Battery'])
    if i['Screen']!=None and i['Screen']!='':
        l.append('Screen')
        inp.append(i['Screen'])
    if i['Touchscreen']!='' :
        l.append('Touchscreen')
        inp.append(YesNo(i['Touchscreen']))
    if i['Resolution_x']!=None and i['Resolution_x']!='':
        l.append('Resolution_x')
        inp.append(i['Resolution_x'])
    if i['Resolution_y']!=None and i['Resolution_y']!='':
        l.append('Resolution_y')
        inp.append(i['Resolution_y'])
    if i['Processor_Cores']!=None and i['Processor_Cores']!='':
        l.append('Processor_Cores')
        inp.append(i['Processor_Cores'])
    if i['RAM']!=None and i['RAM']!='':
        l.append('RAM')
        inp.append(i['RAM'])
    if i['Storage']!=None and i['Storage']!='':
        l.append('Storage')
        inp.append(i['Storage'])
    if i['Rear_Camera']!=None and i['Rear_Camera']!='':
        l.append('Rear_Camera')
        inp.append(i['Rear_Camera'])
    if i['Front_Camera']!=None and i['Front_Camera']!='':
        l.append('Front_Camera')
        inp.append(i['Front_Camera'])
    if i['OS']!='':
        l.append('OS')
        inp.append(OS_convertor(i['OS']))
    if i['Wi_Fi']!='':
        l.append('Wi_Fi')
        inp.append(YesNo(i['Wi_Fi']))
    if i['Bluetooth']!='':
        l.append('Bluetooth')
        inp.append(YesNo(i['Bluetooth']))
    if i['GPS']!='':
        l.append('GPS')
        inp.append(YesNo(i['GPS']))
    if i['SIMs']!=None and i['SIMs']!='':
        l.append('SIMs')
        inp.append(i['SIMs'])
    if i['H_3G']!='':
        l.append('H_3G')
        inp.append(YesNo(i['H_3G']))
    if i['LTE_4G']!='':
        l.append('LTE_4G')
        inp.append(YesNo(i['LTE_4G']))
    if(l==[]):
        return 'Error!'
    l.append('Price')
    k = list(Phone.objects.all().values(*l))
    d = pd.DataFrame(k)
    for i1 in d.columns:
        if i1 in ['Touchscreen','LTE_4G','H_3G','Wi_Fi','GPS','Bluetooth']:
            d[i1] = d[i1].apply(lambda x : 1 if x=='Yes' else 0)
    if 'OS' in d.columns:
        d['OS'] = d['OS'].apply(OS_convertor)
    s = StandardScaler()
    t = StandardScaler()
    # model = SVR()
    model = RandomForestRegressor(n_jobs = 4, n_estimators = 100)
    model.fit(s.fit_transform(d.drop(['Price'],axis=1)),t.fit_transform(np.array([d['Price']]).transpose()))
    inp = np.array(inp).reshape(1,-1)
    prediction  = t.inverse_transform(model.predict(s.transform(inp)))
    prediction = int(prediction[0]-prediction[0]%100)
    i['Predicted'] = prediction
    p1 = FilterPhone.objects.create(**i)
    p1.save()
    return prediction

def OS_convertor(x):
    if x == 'iOS':
        return 6
    if x == 'Android':
        return 5
    if x == 'BlackBerry':
        return 3
    if x == 'Windows':
        return 4
    if x == 'Cyanogen':
        return 2
    if x == 'Tizen':
        return 0
    if x == 'Sailfish':
        return 1

def YesNo(x):
    if x=='Yes':
        return 1
    else:
        return 0
