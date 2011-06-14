from django import forms
import calendar, datetime


class AdminInfoForm(forms.Form):
	direct_business = forms.BooleanField(required=False)
	direct_own_agent_business = forms.BooleanField(required=False)
	other_agent_business = forms.BooleanField(required=False)
	name_transfer = forms.BooleanField(required=False)
	files_follow_up = forms.BooleanField(required=False)
	ge_income = forms.BooleanField(required=False)
	ge_expense = forms.BooleanField(required=False)
	third_party = forms.BooleanField(required=False)
	phonecall_details = forms.BooleanField(required=False)
	cashbook = forms.BooleanField(required=False)
	claim_cheque_details = forms.BooleanField(required=False)
	covernote_book_details = forms.BooleanField(required=False)
	enquiry_book = forms.BooleanField(required=False)
	customer_care = forms.BooleanField(required=False)
	phone_number = forms.IntegerField(required=False)
	
class IncomeExpenseDateselectForm(forms.Form):
	now = datetime.datetime.now()
	YEAR_CHOICES = [(i,int(i)) for i in range(2000,int(now.year)+1)]
	MONTH_CHOICES = [(0,None)] + [(i,calendar.month_name.__getitem__(i)) for i in range(1,13)]
	year = forms.ChoiceField(choices=YEAR_CHOICES,required=True)
	month = forms.ChoiceField(choices=MONTH_CHOICES,required=False)
