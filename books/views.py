from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse	
from django.contrib.admin.views.decorators import staff_member_required
from books.forms import AdminInfoForm, IncomeExpenseDateselectForm
from books.models import GEExpense, GEIncome
from django.core.urlresolvers import reverse
from django.core.exceptions import PermissionDenied
import calendar, datetime, pickle, os


# Permission checks are based on the delete permission on the model NameTransfer.
# Hence deleting or renaming that model may result in the failure of permission checks

#finding absolute path
filepath = os.path.join( os.path.dirname( os.path.realpath( __file__ ) ) ,'dbfile' )

@staff_member_required
def AdminInfo(request):
	if request.method == 'POST':
		form = AdminInfoForm(request.POST)
		if form.is_valid():
			admin_data = {}
			picklefile = open(filepath, "wrb")
			admin_data['direct_business'] = form.cleaned_data['direct_business']
			admin_data['direct_own_agent_business'] = form.cleaned_data['direct_own_agent_business']
			admin_data['other_agent_business'] = form.cleaned_data['other_agent_business']
			admin_data['name_transfer'] = form.cleaned_data['name_transfer']
			admin_data['files_follow_up'] = form.cleaned_data['files_follow_up']
			admin_data['ge_income'] = form.cleaned_data['ge_income']
			admin_data['ge_expense'] = form.cleaned_data['ge_expense']
			admin_data['third_party'] = form.cleaned_data['third_party']
			admin_data['phonecall_details'] = form.cleaned_data['phonecall_details']
			admin_data['cashbook'] = form.cleaned_data['cashbook']
			admin_data['claim_cheque_details'] = form.cleaned_data['claim_cheque_details']
			admin_data['covernote_book_details'] = form.cleaned_data['covernote_book_details']
			admin_data['phone_number'] =  form.cleaned_data['phone_number']
			admin_data['enquiry_book'] = form.cleaned_data['enquiry_book']
			admin_data['customer_care'] = form.cleaned_data['customer_care']
			pickle.dump(admin_data, picklefile)
			picklefile.close()
			return HttpResponseRedirect(reverse( 'admin:index'))
	else:
		picklefile = open(filepath, "rb")
		try:
			admin_data = pickle.load(picklefile)
		except:
			admin_data = {}	
		picklefile.close()
		form = AdminInfoForm(admin_data)
		if request.user.has_perm("books.delete_nametransfer"):
			return render_to_response('admin_info.html', { 'form' : form, }, context_instance=RequestContext(request, {}))	
		else:
			raise PermissionDenied


@staff_member_required
def income_expense_report(request, year, month=None):
	if not request.user.has_perm("books.delete_nametransfer"):
		raise PermissionDenied
	""" Function for calculating the current balance using GEIncome and GEExpense books """
	if month:
		ge_qs = GEExpense.objects.filter(date__year=year, date__month=month)
		gi_qs = GEIncome.objects.filter(date__year=year, date__month=month)
		month_name = calendar.month_name.__getitem__(int(month))
	else:
		ge_qs = GEExpense.objects.filter(date__year=year)
		gi_qs = GEIncome.objects.filter(date__year=year)
		month_name = None
		
	total_expense = 0
	for item in ge_qs:
		total_expense = total_expense + item.amount
	total_income = 0
	for item in gi_qs:
		total_income = total_income + item.amount
	current_balance = total_income - total_expense
	return render_to_response('income_expense_report.html', {'ge_qs':ge_qs, 'gi_qs':gi_qs, 'month_name':month_name, 'year':year, 'current_balance':current_balance,
																'total_income':total_income,'total_expense':total_expense})
@staff_member_required
def income_expense_dateselect(request):
	""" Function to get year and month from user and invoke income_expense_report """
	if not request.user.has_perm("books.delete_nametransfer"):
		raise PermissionDenied
	if request.method == 'POST':
		form = IncomeExpenseDateselectForm(request.POST)
		if form.is_valid():
			year = form.cleaned_data['year']
			month = form.cleaned_data['month']
			if int(month):
				return HttpResponseRedirect(reverse( 'income_expense_dateselect')+year+'/'+month+'/')
			else:
				return HttpResponseRedirect(reverse( 'income_expense_dateselect')+year+'/')
	else:
		form = IncomeExpenseDateselectForm(initial = {'year':datetime.datetime.now().year})
		return render_to_response('income_expense_dateselect.html',{'form':form,},context_instance=RequestContext(request, {}))
