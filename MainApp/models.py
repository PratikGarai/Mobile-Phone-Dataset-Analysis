from django.db import models

class Phone(models.Model):
    simc = [
            (1,'1'),
            (2,'2'),
            (3,'3')
            ]
    corec = [
            (1,'single core'),
            (2,'dual core'),
            (4,'quad core'),
            (6,'hexa core'),
            (8,'octa core'),
            (10,'deca core')
            ]
    ync = [
            ('Yes','Yes'),
            ('No','No')
        ]
    osc = [
            ('iOS','iOS'),
            ('Android','Android'),
            ('BlackBerry','BlackBerry'),
            ('Windows','Windows'),
            ('Cyanogen','Cyanogen'),
            ('Tizen','Tizen'),
            ('Sailfish','Sailfish')
            ]
    Name = models.CharField(max_length=100)
    Brand = models.CharField(max_length=100)
    Model = models.CharField(max_length=100 )
    Battery = models.IntegerField(help_text='in mAh')
    Screen = models.DecimalField(max_digits=5,decimal_places=2,help_text='in Inches')
    Touchscreen =  models.CharField(max_length=10,choices=ync)
    Resolution_x = models.IntegerField(help_text = 'width in Pixels' )
    Resolution_y = models.IntegerField(help_text = 'height in Pixels' )
    Processor_Cores = models.IntegerField(choices=corec)
    RAM = models.IntegerField(help_text='in MB')
    Storage = models.DecimalField(max_digits = 10, decimal_places = 3, help_text='in GB')
    Rear_Camera = models.DecimalField(max_digits = 6, decimal_places = 2, help_text='in MP if present or 0')
    Front_Camera = models.DecimalField(max_digits = 6, decimal_places= 2, help_text='in MP if present or 0')
    OS = models.CharField(max_length = 25, choices = osc)
    Wi_Fi =  models.CharField(max_length=10,choices=ync)
    Bluetooth =  models.CharField(max_length=10,choices=ync)
    GPS =  models.CharField(max_length=10,choices=ync)
    SIMs =  models.IntegerField(choices = simc)
    H_3G =  models.CharField(max_length=10,choices=ync)
    LTE_4G =  models.CharField(max_length=10,choices=ync)
    Price = models.IntegerField(help_text='in Rupees, no commas or spaces')
    
class FilterPhone(models.Model):
    simc = [
            (1,'1'),
            (2,'2'),
            (3,'3')
            ]
    corec = [
            (1,'single core'),
            (2,'dual core'),
            (4,'quad core'),
            (6,'hexa core'),
            (8,'octa core'),
            (10,'deca  core')
            ]
    ync = [
            ('Yes','Yes'),
            ('No','No')
        ]
    osc = [
            ('iOS','iOS'),
            ('Android','Android'),
            ('BlackBerry','BlackBerry'),
            ('Windows','Windows'),
            ('Cyanogen','Cyanogen'),
            ('Tizen','Tizen'),
            ('Sailfish','Sailfish')
            ]
    Battery = models.IntegerField(help_text='in mAh')
    Screen = models.DecimalField(max_digits=5,decimal_places=2,help_text='in Inches')
    Touchscreen =  models.CharField(max_length=10,choices=ync)
    Resolution_x = models.IntegerField(help_text='width in Pixels')
    Resolution_y = models.IntegerField(help_text='height in Pixels')
    Processor_Cores = models.IntegerField(choices = corec)
    RAM = models.IntegerField(help_text='in MB')
    Storage = models.DecimalField(max_digits = 10, decimal_places = 3,help_text='in GB')
    Rear_Camera = models.DecimalField(max_digits = 6, decimal_places = 2, help_text='in MP if present else 0')
    Front_Camera = models.DecimalField(max_digits = 6, decimal_places= 2, help_text='in MP if present else 0')
    OS = models.CharField(max_length = 25, choices = osc)
    Wi_Fi =  models.CharField(max_length=10,choices=ync)
    Bluetooth =  models.CharField(max_length=10,choices=ync)
    GPS =  models.CharField(max_length=10,choices=ync)
    SIMs =  models.IntegerField(choices = simc)
    H_3G =  models.CharField(max_length=10,choices=ync)
    LTE_4G =  models.CharField(max_length=10,choices=ync)
    Predicted = models.IntegerField(blank = True)

class Filter(models.Model):
    simc = [
            (1,'1'),
            (2,'2'),
            (3,'3')
            ]
    corec = [
            (1,'single core'),
            (2,'dual core'),
            (4,'quad core'),
            (6,'hexa core'),
            (8,'octa core'),
            (10,'deca core')
            ]
    ync = [
            ('Yes','Yes'),
            ('No','No')
        ]
    osc = [
            ('iOS','iOS'),
            ('Android','Android'),
            ('BlackBerry','BlackBerry'),
            ('Windows','Windows'),
            ('Cyanogen','Cyanogen'),
            ('Tizen','Tizen'),
            ('Sailfish','Sailfish')
            ]
    Battery_1 = models.IntegerField(help_text='in mAh',blank = True,null=True)
    Battery_2 = models.IntegerField(help_text='in mAh',blank = True,null=True)
    Screen_1 = models.DecimalField(max_digits=5,blank = True ,decimal_places=2,help_text='in Inches',null=True)
    Screen_2 = models.DecimalField(max_digits=5,blank = True ,decimal_places=2,help_text='in Inches',null=True)
    Touchscreen =  models.CharField(max_length=10,choices=ync, blank=True)
    Resolution_x_1 = models.IntegerField(help_text='width in Pixels',blank = True,null=True )
    Resolution_x_2 = models.IntegerField(help_text='width in Pixels',blank = True,null=True )
    Resolution_y_1 = models.IntegerField(help_text='height in Pixels', null=True, blank = True)
    Resolution_y_2 = models.IntegerField(help_text='height in Pixels', null=True, blank = True)
    Processor_Cores = models.IntegerField(choices = corec , null=True, blank = True)
    RAM_1 = models.IntegerField(help_text='in MB', null=True, blank = True)
    RAM_2 = models.IntegerField(help_text='in MB', null=True, blank = True)
    Storage_1 = models.DecimalField(max_digits = 10, decimal_places = 3,blank = True,help_text='in GB',null=True)
    Storage_2 = models.DecimalField(max_digits = 10, decimal_places = 3,blank = True,help_text='in GB',null=True)
    Rear_Camera_1 = models.DecimalField(max_digits = 6, decimal_places = 2, blank = True, help_text='in MP if present',null=True)
    Rear_Camera_2 = models.DecimalField(max_digits = 6, decimal_places = 2, blank = True, help_text='in MP if present',null=True)
    Front_Camera_1 = models.DecimalField(max_digits = 6, decimal_places= 2, help_text='in MP if present',null=True,blank=True)
    Front_Camera_2 = models.DecimalField(max_digits = 6, decimal_places= 2, help_text='in MP if present',null=True,blank=True)
    OS = models.CharField(max_length = 25, choices = osc,blank=True)
    Wi_Fi =  models.CharField(max_length=10,choices=ync,blank=True)
    Bluetooth =  models.CharField(max_length=10,choices=ync,blank = True)
    GPS =  models.CharField(max_length=10,choices=ync,blank=True)
    SIMs_1 =  models.IntegerField(choices = simc , null = True, blank = True)
    SIMs_2 =  models.IntegerField(choices = simc , null = True, blank = True)
    H_3G =  models.CharField(max_length=10,choices=ync,blank=True)
    LTE_4G =  models.CharField(max_length=10,choices=ync,blank=True)

class GraphModel(models.Model):
    ch = [
            (1,'Sample Graph 1'),
            (2,'Sample Graph 2')
            ]
    choice  = models.IntegerField(choices = ch)
