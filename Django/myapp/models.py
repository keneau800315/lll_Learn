from django.db import models
from django.db.models import CharField, DateField, IntegerField, ForeignKey, DecimalField
# Create your models here.
# 一個類別就是一個table，這邊要繼承models的.Model物件進行操作
#TUPLE KEY:VALUE
BALANCE_TYPE = ((u'買進',u'買進'),(u'賣出',u'賣出'))

#繼承models.Model進行操作

class Category(models.Model):
	category = CharField(max_length=25)
	#print物件時的顯示
	def __str__(self):
		return self.category



class Record(models.Model):
	date         = DateField()
	#Category的資料被刪除，Record資料也被刪除
	#以物件的方式來管理category
	category     = ForeignKey(Category,on_delete=models.SET_NULL,null=True)
	stockid      = IntegerField()
	balance_type = CharField(max_length=2, choices=BALANCE_TYPE)
	#帶有兩個小數位
	price        = DecimalField(max_digits=20, decimal_places=2)
	share        = IntegerField()
	amount       = IntegerField()
	def __str__(self):
		return str(self.stockid)