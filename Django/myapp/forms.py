from django.forms import ModelForm,TextInput
from .models import Record
from datetime import date
class RecordForm(ModelForm):
	class Meta:
		#使用哪個models的物件作連動
		model = Record
		#使用Record當中的哪幾個欄位
		fields = ['date','category','stockid','balance_type','price','share','amount']
		widgets = {
			'date':TextInput(attrs={
				'id':'datepicker1',
				'value':date.today().strftime('%Y-%m-%d')
				})
		}

