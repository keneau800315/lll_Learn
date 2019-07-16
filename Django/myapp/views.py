from django.shortcuts import render,redirect
from .models import Record, Category
from .forms import RecordForm
from django.contrib.auth.decorators import login_required
# Create your views here.
#要先在settings.py註冊myapp資料夾才能使用

#request代表史用者輸入網址後的發送的請求，請求會被包裝成request物件
#加上login_required在試用者有登錄的狀況下才能執行
@login_required
def frontpage(request):
	#initial給定預設值
	record_form = RecordForm(initial= {'balance_type':'買進'})
	#利用Record物件操作ORM語法
	records = Record.objects.filter()
	income_list  = [record.amount for record in records if record.balance_type == '賣出']
	outcome_list  = [record.amount for record in records if record.balance_type == '買進']
	income = sum(income_list) if len(income_list) !=0 else 0
	outcome = sum(outcome_list) if len(outcome_list) !=0 else 0
	net = income - outcome
	return render(request,"app/index.html",locals())

@login_required
def settings(request):
	categories = Category.objects.filter()
	return render(request,"app/settings.html",locals())
@login_required
def addcategory(request):
	if request.method=='POST':
		category=request.POST['add_category_name']
		Category.objects.get_or_create(category=category)
		return redirect('/settings')
@login_required
def delcategory(request,category):
	if request.method=='POST':
		Category.objects.filter(category = category).delete()
		return redirect('/settings')
@login_required
def addrecord(request):
	if request.method=='POST':
		#把request.POST物件的dictionary塞給表格將form全部填好
		form =RecordForm(request.POST)
		#檢查格式
		if form.is_valid():
			form.save()
	return redirect('/')
@login_required
def delrecord(request):
	if request.method == 'POST':
		id = request.POST['delete_val']
		Record.objects.filter(id = id).delete()
	return redirect('/')