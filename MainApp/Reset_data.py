from MainApp.models import Phone
import pandas as pd

data = pd.read_csv('ndtv_data_final.csv')
for i in range(1451):
    row = list(data.iloc[i])
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
