from django.contrib import admin

# Register your models here.
from .models import Record, Category
#放進來後台管理介面才能使用這兩個表格
admin.site.register(Record)
admin.site.register(Category)