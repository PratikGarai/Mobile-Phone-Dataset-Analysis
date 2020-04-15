from django.contrib import admin
from .models import Phone
from .models import FilterPhone
from .models import Filter
from .models import GraphModel

admin.site.register(Phone)
admin.site.register(FilterPhone)
admin.site.register(Filter)
admin.site.register(GraphModel)
# Register your models here.
