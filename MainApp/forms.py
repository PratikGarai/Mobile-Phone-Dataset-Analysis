from .models import Phone
from django import forms
from .models import FilterPhone
from .models import Filter
from .models import GraphModel

class Phone_Form(forms.ModelForm):
    class Meta:
        model = Phone
        fields = "__all__"

class Filter_Form(forms.ModelForm):
    class Meta:
        model = FilterPhone
        fields = "__all__"

class Filter_Form1(forms.ModelForm):
    class Meta:
        model  = Filter
        fields = "__all__"

class Graph_Form(forms.ModelForm):
    class Meta:
        model  = GraphModel
        fields = "__all__"
