from django.db import models
from datetime import datetime
import pickle, urllib2
from django.contrib.auth.models import User
import os
#import erp.middleware.threadlocals

#sms notifcation variables
username = "onspot"
password = "digizu7iwyy99y"
senderid = "OnSpot"

# pickle file path
filepath = os.path.join( os.path.dirname( os.path.realpath( __file__ ) ) ,'dbfile' )

# Function for sms notification
def send_notification(modelname, timestamp, user):
	f = open(filepath,"rb")
	data = pickle.load(f)
	if data[modelname]:
		phone_number = data['phone_number']
		msg = "%s+added+a+new+entry+to+%s+on+%s" % (user.username,modelname,'+'.join(timestamp.ctime().split()))
		url = "http://sms.marketsolutions.co.in/pushsms.php?username=%s&password=%s&sender=%s&to=%s&message=%s" % (username,password,senderid,phone_number,msg)
		req = urllib2.Request(url)
		res = urllib2.urlopen(req)
	f.close()	

# Book 1 Direct Business

class DirectBusiness(models.Model):
	# Choices for the vehicle type
	PRIVATE_STATUS = "Private"
	COMMERCIAL_STATUS = "Commercial"
	CHOICES = ( (PRIVATE_STATUS, "Private"), (COMMERCIAL_STATUS, "Commercial"), )
	# Fields..
	covernote = models.CharField(max_length=250, verbose_name="Pos/Covernote",blank=True)
	committed_date = models.DateField(verbose_name="Committed Date",blank=True,null=True)
	details1 = models.TextField(verbose_name="Details",blank=True)
	covernote_number = models.BigIntegerField(verbose_name="Covernote Number",blank=True,null=True)
	policy_number = models.BigIntegerField(verbose_name="Policy Number",blank=True,null=True)
	delivery_date = models.DateField(verbose_name="Delivery Date",null=True,blank=True)
	delivery_method = models.CharField(verbose_name="Delivery Method",max_length=250,blank=True)
	rns_number = models.BigIntegerField(verbose_name="RNS Number",blank=True,null=True)
	vehicle_make_number = models.CharField(verbose_name="Vehicle make number",max_length=50,blank=True)
	manufactured_year = models.IntegerField(verbose_name="Manufactured Year",help_text="eg: 2003",blank=True,null=True)
	vehicle_type = models.CharField(verbose_name="Vehicle Type",max_length=15,choices=CHOICES,blank=True,null=True)
	customer_name = models.CharField(verbose_name="Name",max_length=50,blank=True)
	contact_number = models.BigIntegerField(verbose_name="Contact Number",blank=True,null=True)
	area = models.CharField(verbose_name="Area",max_length=250,blank=True)
	deal = models.CharField(verbose_name="Deal",max_length=250,blank=True)
	office_deal = models.CharField(verbose_name="Office Deal",max_length=250,blank=True)
	policy_premium = models.CharField(verbose_name="Policy Premium",max_length=250,blank=True)
	cash_discount = models.CharField(verbose_name="Cash Discount",max_length=50,blank=True)
	od_discount = models.CharField(verbose_name="OD Discount",max_length=50,blank=True)
	amount = models.DecimalField(verbose_name="Amount",max_digits=19,decimal_places=10,help_text="in numbers",blank=True,null=True)
	details2 = models.TextField(verbose_name="Details",blank=True)
	policy_details = models.TextField(verbose_name="Policy Details",blank=True) 
	# added after deployment
	careof = models.CharField(verbose_name="C/O",max_length=250,blank=True)
	od_premium = models.CharField(verbose_name="OD Premium",max_length=250,blank=True)
	# Cant be seen in the form
	timestamp = models.DateTimeField(default=datetime.now,editable=False)  # To save the time at which
	added_by = models.ForeignKey(User,editable=False)
		
	class Meta:
		ordering = ["-timestamp"]
		verbose_name_plural = "Direct Business"
	
	def __unicode__(self):
		return 	u'id %s created on %s' % (self.id, self.timestamp)
		
	def save(self, force_insert=False, force_update=False):
		send_notification('direct_business',self.timestamp,self.added_by)
		super(DirectBusiness,self).save(force_insert, force_update)	
		
			
		
	
# Book 2, Direct Own Agent Business

class DirectOwnAgentBusiness(models.Model):
	# Choices for the vehicle type dropdown menu
	PRIVATE_STATUS = "Private"
	COMMERCIAL_STATUS = "Commercial"
	CHOICES = ( (PRIVATE_STATUS, "Private"), (COMMERCIAL_STATUS, "Commercial"), )
	# Fields..
	covernote = models.CharField(max_length=250, verbose_name="Pos/Covernote",blank=True)
	committed_date = models.DateField(verbose_name="Committed Date",blank=True,null=True)
	details1 = models.TextField(verbose_name="Details",blank=True)
	covernote_number = models.BigIntegerField(verbose_name="Covernote Number",blank=True,null=True)
	policy_number = models.BigIntegerField(verbose_name="Policy Number",blank=True,null=True)
	delivery_date = models.DateField(verbose_name="Delivery Date",blank=True,null=True)
	delivery_method = models.CharField(verbose_name="Delivery Method",max_length=250,blank=True)
	rns_number = models.BigIntegerField(verbose_name="RNS Number",blank=True,null=True)
	vehicle_make_number = models.CharField(verbose_name="Vehicle make number",max_length=50,blank=True)
	manufactured_year = models.IntegerField(verbose_name="Manufactured Year",help_text="eg: 2003",blank=True,null=True)
	vehicle_type = models.CharField(verbose_name="Vehicle Type",max_length=15,choices=CHOICES,blank=True,null=True)
	customer_name = models.CharField(verbose_name="Customer Name",max_length=50,blank=True)
	contact_number = models.BigIntegerField(verbose_name="Contact Number",blank=True,null=True)
	careof = models.CharField(verbose_name="C/O",max_length=250,blank=True)
	area = models.CharField(verbose_name="Area",max_length=250,blank=True)
	deal = models.CharField(verbose_name="Deal",max_length=250,blank=True)
	office_deal = models.CharField(verbose_name="Office Deal",max_length=250,blank=True)
	policy_premium = models.CharField(verbose_name="Policy Premium",max_length=250,blank=True)
	cash_premium_discount = models.CharField(verbose_name="Cash Premium Discount",max_length=50,blank=True)
	od_discount = models.CharField(verbose_name="OD Discount",max_length=50,blank=True)
	od_premium = models.CharField(verbose_name="OD Premium",max_length=250,blank=True)
	amount = models.DecimalField(verbose_name="Amount",max_digits=19,decimal_places=10,help_text="in numbers",blank=True,null=True)
	details2 = models.TextField(verbose_name="Details",blank=True)
	policy_details = models.TextField(verbose_name="Policy Details",blank=True)
	# Cant be seen in the form
	timestamp = models.DateTimeField(default=datetime.now,editable=False)  # To save the time at which the object is created
	added_by = models.ForeignKey(User,editable=False)
	
	class Meta:
		ordering = ["-timestamp"]
		verbose_name_plural = "Direct Own Agent Business"
		
	def __unicode__(self):
		return 	u'id %s created on %s' % (self.id, self.timestamp)
		
	def save(self, force_insert=False, force_update=False):
		send_notification('direct_own_agent_business',self.timestamp,self.added_by)
		super(DirectOwnAgentBusiness,self).save(force_insert, force_update)		

	
# Book 3

class OtherAgentBusiness(models.Model):
	# Choices for the vehicle type dropdown menu
	PRIVATE_STATUS = "Private"
	COMMERCIAL_STATUS = "Commercial"
	CHOICES = ( (PRIVATE_STATUS, "Private"), (COMMERCIAL_STATUS, "Commercial"), )
	# Fields..
	covernote = models.CharField(max_length=250, verbose_name="Pos/Covernote",blank=True)
	committed_date = models.DateField(verbose_name="Committed Date",blank=True,null=True)
	details1 = models.TextField(verbose_name="Details",blank=True)
	covernote_number = models.BigIntegerField(verbose_name="Covernote Number",blank=True,null=True)
	delivery_date = models.DateField(verbose_name="Delivery Date",blank=True,null=True)
	delivery_method = models.CharField(verbose_name="Delivery Method",max_length=250,blank=True)
	rns_number = models.BigIntegerField(verbose_name="RNS Number",blank=True,null=True)
	vehicle_make_number = models.CharField(verbose_name="Vehicle make number",max_length=50,blank=True)
	manufactured_year = models.IntegerField(verbose_name="Manufactured Year",help_text="eg: 2003",blank=True,null=True)
	vehicle_type = models.CharField(verbose_name="Vehicle Type",max_length=15,choices=CHOICES,blank=True,null=True)
	customer_name = models.CharField(verbose_name="Customer Name",max_length=50,blank=True)
	contact_number = models.BigIntegerField(verbose_name="Contact Number",blank=True,null=True)
	careof = models.CharField(verbose_name="C/O",max_length=250,blank=True)
	area = models.CharField(verbose_name="Area",max_length=250,blank=True)
	deal = models.CharField(verbose_name="Deal",max_length=250,blank=True)
	office_deal = models.CharField(verbose_name="Office Deal",max_length=250,blank=True)
	policy_premium = models.CharField(verbose_name="Policy Premium",max_length=250,blank=True)
	cash_discount = models.DecimalField(verbose_name="Cash Premium Discount",max_digits=19,decimal_places=10,help_text="in numbers",blank=True,null=True)
	od_discount = models.CharField(verbose_name="OD Discount",max_length=50,blank=True)
	od_premium = models.CharField(verbose_name="OD Premium",max_length=250,blank=True)
	amount = models.DecimalField(verbose_name="Amount",max_digits=19,decimal_places=10,help_text="in numbers",blank=True,null=True)
	details2 = models.TextField(verbose_name="Details",blank=True)
	policy_details = models.TextField(verbose_name="Policy Details",blank=True)
	# Cant be seen in the form
	timestamp = models.DateTimeField(default=datetime.now,editable=False)  # To save the time at which the object is created
	added_by = models.ForeignKey(User,editable=False)
	
	class Meta:
		ordering = ["-timestamp"]
		verbose_name_plural = "Other Agent Business"
		
	def __unicode__(self):
		return 	u'id %s created on %s' % (self.id, self.timestamp)
		
	def save(self, force_insert=False, force_update=False):
		send_notification('other_agent_business',self.timestamp,self.added_by)
		super(OtherAgentBusiness,self).save(force_insert, force_update)	

				
	
# Book 4

class NameTransfer(models.Model):
	# Choices for the vehicle type dropdown menu
	PRIVATE_STATUS = "Private"
	COMMERCIAL_STATUS = "Commercial"
	CHOICES = ( (PRIVATE_STATUS, "Private"), (COMMERCIAL_STATUS, "Commercial"), )
	# Fields..
	recieved_date = models.DateField(verbose_name="Recieved Date",blank=True,null=True)
	committed_date = models.DateField(verbose_name="Committed Date",blank=True,null=True)
	details = models.TextField(verbose_name="Details",blank=True)
	endorsement = models.CharField(verbose_name="Endorsement",max_length=250,blank=True)
	delivery_date = models.DateField(verbose_name="Delivery Date",blank=True,null=True)
	delivery_method = models.CharField(verbose_name="Delivery Method",max_length=250,blank=True)
	vehicle_number = models.CharField(verbose_name="Vehicle Number",max_length=50,blank=True)
	vehicle_type = models.CharField(verbose_name="Vehicle Type",max_length=15,choices=CHOICES,blank=True,null=True)
	customer_name = models.CharField(verbose_name="Customer Name",max_length=50,blank=True)
	name_transfer = models.CharField(verbose_name="Name Transfer to",max_length=50,blank=True)
	contact_number = models.BigIntegerField(verbose_name="Contact Number",blank=True,null=True)
	careof = models.CharField(verbose_name="C/O",max_length=250,blank=True)
	deal = models.CharField(verbose_name="Deal",max_length=250,blank=True)
	office_deal = models.CharField(verbose_name="Office Deal",max_length=250,blank=True)
	endorsement_fee = models.CharField(verbose_name="Endorsement Fees",max_length=50,blank=True)
	amount = models.DecimalField(verbose_name="Amount",max_digits=19,decimal_places=10,help_text="in numbers",blank=True,null=True)
	#added after deployment
	policy_number = models.BigIntegerField(verbose_name="Policy Number",blank=True,null=True)
	#cannot be seen
	timestamp = models.DateTimeField(default=datetime.now,editable=False)  # To save the time at which the object is created
	added_by = models.ForeignKey(User,editable=False)

	
	class Meta:
		ordering = ["-timestamp"]
		verbose_name_plural = "Name Transfer"
		
	def __unicode__(self):
		return 	u'id %s created on %s' % (self.id, self.timestamp)
	
	def save(self, force_insert=False, force_update=False):
		send_notification('name_transfer',self.timestamp,self.added_by)
		super(NameTransfer,self).save(force_insert, force_update)
	
# Book 5
	
class FilesFollowUp(models.Model):
	customer_name = models.CharField(verbose_name="Customer Name",max_length=50,blank=True)
	vehicle_number = models.CharField(verbose_name="Vehicle Number",max_length=50,blank=True)
	premium = models.CharField(verbose_name="Premium",max_length=250,blank=True)
	recieved_amount = models.DecimalField(verbose_name="Recieved Amount",max_digits=19,decimal_places=10,help_text="in numbers",blank=True,null=True)
	balance_amount = models.DecimalField(verbose_name="Balance Amount",max_digits=19,decimal_places=10,help_text="in numbers",blank=True,null=True)
	cheque = models.CharField(verbose_name="Cheque",max_length=50,blank=True)
	insurance_type = models.CharField(verbose_name="Insurance Type",max_length=100,blank=True)
	previous_policy_copy = models.CharField(verbose_name="Previous Policy Copy",max_length=250,blank=True)
	rc_copy = models.CharField(verbose_name="RC copy",max_length=250,blank=True)
	new_policy_copy = models.CharField(verbose_name="New Policy Copy",max_length=250,blank=True)
	hand_oversheet = models.CharField(verbose_name="Hand Oversheet",max_length=250,blank=True)
	yellow_covernote_copy = models.CharField(verbose_name="Yellow Covernote Copy",max_length=250,blank=True)
	Photo = models.CharField(verbose_name="Photo",max_length=250,blank=True)
	chaseprint = models.CharField(verbose_name="Chase Print", max_length=250,blank=True)
	calculation_table = models.CharField(verbose_name="Calculation Table", max_length=250,blank=True)
	endorsement = models.CharField(verbose_name="Endorsement", max_length=250,blank=True)
	quotation = models.CharField(verbose_name="Quotation", max_length=250,blank=True)
	verify_details = models.CharField(verbose_name="Verify Details", max_length=250,blank=True)
	date = models.CharField(verbose_name="Date", max_length=250,blank=True)
	hand_over_to = models.CharField(verbose_name="Hand over to", max_length=250,blank=True)
	courier_details = models.CharField(verbose_name="Courier Details", max_length=250,blank=True)
	recieved_person = models.CharField(verbose_name="Recieved Person", max_length=250,blank=True)
	details = models.TextField(verbose_name="Details",blank=True)
	committed_policy_date = models.CharField(verbose_name="Committed Policy Date", max_length=250,blank=True)
	policy_recieved_date = models.CharField(verbose_name="Policy Committed Date", max_length=250,blank=True)
	policy_number = models.BigIntegerField(verbose_name="Policy Number",blank=True,null=True)
	delivered_by = models.CharField(verbose_name="Delivered by", max_length=250,blank=True)
	#added after deployment
	inspection_report = models.TextField(verbose_name="Inspection Report",blank=True)
	renewal_notice = models.TextField(verbose_name="Renewal Notice",blank=True)
	#Cannot be seen
	timestamp = models.DateTimeField(default=datetime.now,editable=False)  # To save the time at which the object is created
	added_by = models.ForeignKey(User,editable=False)
		
	class Meta:
		ordering = ["-timestamp"]
		verbose_name_plural = "Files Follow Ups"
		
	def __unicode__(self):
		return 	u'id %s created on %s' % (self.id, self.timestamp)

	def save(self, force_insert=False, force_update=False):
		send_notification('files_follow_up',self.timestamp,self.added_by)
		super(FilesFollowUp,self).save(force_insert, force_update)
	
# Book 6	General Expense

# Income Page
class GEIncome(models.Model):
	date = models.DateField(verbose_name="Date",blank=True,null=True)
	given_by = models.CharField(verbose_name="Given by", max_length=250,blank=True)
	usage = models.CharField(verbose_name="Usage", max_length=250,blank=True)
	amount = models.DecimalField(verbose_name="Amount",max_digits=19,decimal_places=10,help_text="in numbers",blank=True,null=True)
	timestamp = models.DateTimeField(default=datetime.now,editable=False)  # To save the time at which the object is created
	added_by = models.ForeignKey(User,editable=False)
	
	class Meta:
		ordering = ["-timestamp"]
		verbose_name_plural = "General Expense (Income)"
		
	def __unicode__(self):
		return 	u'id %s created on %s' % (self.id, self.timestamp)
	
	def save(self, force_insert=False, force_update=False):
		send_notification('ge_income',self.timestamp,self.added_by)
		super(GEIncome,self).save(force_insert, force_update)
		
# Expense Page
class GEExpense(models.Model):
	date = models.DateField(verbose_name="Date",blank=True,null=True)
	deal = models.CharField(verbose_name="Deal", max_length=250,blank=True)
	particulars = models.CharField(verbose_name="Particulars", max_length=250,blank=True)
	billno = models.CharField(verbose_name="Bill no", max_length=50,blank=True)
	amount = models.DecimalField(verbose_name="Amount",max_digits=19,decimal_places=10,help_text="in numbers",blank=True,null=True)
	timestamp = models.DateTimeField(default=datetime.now,editable=False)  # To save the time at which the object is created
	added_by = models.ForeignKey(User,editable=False)
	
	class Meta:
		ordering = ["-timestamp"]
		verbose_name_plural = "General Expense (Expense)"
		
	def __unicode__(self):
		return 	u'id %s created on %s' % (self.id, self.timestamp)

	def save(self, force_insert=False, force_update=False):
		send_notification('ge_expense',self.timestamp,self.added_by)
		super(GEExpense,self).save(force_insert, force_update)
			
	
# Balance Sheet
#  Balance = Income-Expense

# Book 7

class ThirdParty(models.Model):
	# Choices for the vehicle type dropdown menu
	PRIVATE_STATUS = "Private"
	COMMERCIAL_STATUS = "Commercial"
	CHOICES = ( (PRIVATE_STATUS, "Private"), (COMMERCIAL_STATUS, "Commercial"), )
	# Fields..
	recieved_date = models.DateField(verbose_name="Recieved Date",blank=True,null=True)
	policy_number = models.BigIntegerField(verbose_name="Policy Number",blank=True,null=True)
	del_method = models.CharField(verbose_name="Del Field", max_length=250,blank=True)
	vehicle_number = models.CharField(verbose_name="Vehicle Number",max_length=50,blank=True)
	manufacturing_year = models.IntegerField(verbose_name="Manufactured Year",help_text="eg: 2003",blank=True,null=True)
	vehicle_type = models.CharField(verbose_name="Vehicle Type",max_length=15,choices=CHOICES,blank=True,null=True)
	customer_name = models.CharField(verbose_name="Name",max_length=50,blank=True)
	contact_number = models.BigIntegerField(verbose_name="Contact Number",blank=True,null=True)
	premium = models.CharField(verbose_name="Premium",max_length=250,blank=True)
	amount = models.DecimalField(verbose_name="Amount",max_digits=19,decimal_places=10,help_text="in numbers",blank=True,null=True)
	timestamp = models.DateTimeField(default=datetime.now,editable=False)  # To save the time at which the object is created
	added_by = models.ForeignKey(User,editable=False)
	
	class Meta:
		ordering = ["-timestamp"]
		verbose_name_plural = "Third Parties"
		
	def __unicode__(self):
		return 	u'id %s created on %s' % (self.id, self.timestamp)
		
	def save(self, force_insert=False, force_update=False):
		send_notification('third_party',self.timestamp,self.added_by)
		super(ThirdParty,self).save(force_insert, force_update)		

	
# Book 8

class PhonecallDetails(models.Model):
	date = models.DateField(verbose_name="Date",blank=True,null=True)
	name = models.CharField(verbose_name="Name",max_length=50,blank=True)
	place = models.CharField(verbose_name="Place", max_length=50,blank=True)
	vehicle_number = models.CharField(verbose_name="Vehicle Number",max_length=50,blank=True)
	vehicle_model = models.CharField(verbose_name="Vehicle Model", max_length=30,blank=True)
	pre_idv = models.CharField(verbose_name="Pre idv",max_length=50,blank=True)
	pre_nib = models.CharField(verbose_name="Pre nib",max_length=50,blank=True)
	pre_premium = models.CharField(verbose_name="Vehicle Number",max_length=50,blank=True)
	contact_number = models.BigIntegerField(verbose_name="Contact Number",blank=True,null=True)
	timestamp = models.DateTimeField(default=datetime.now,editable=False)  # To save the time at which the object is created
	added_by = models.ForeignKey(User,editable=False)
	
	class Meta:
		ordering = ["-timestamp"]
		verbose_name_plural = "Phone Calls Details"
		
	def __unicode__(self):
		return 	u'id %s created on %s' % (self.id, self.timestamp)
		
	def save(self, force_insert=False, force_update=False):
		send_notification('phonecall_details',self.timestamp,self.added_by)
		super(PhonecallDetails,self).save(force_insert, force_update)	

	
	
# Book 9

class CashBook(models.Model):
	date = models.DateField(verbose_name="Date",blank=True,null=True)
	vehicle_number = models.CharField(verbose_name="Vehicle Number",max_length=50,blank=True)
	customer_name = models.CharField(verbose_name="Customer Name Given Person",max_length=50,blank=True)
	actual_amount  = models.DecimalField(verbose_name="Actual Amount",max_digits=19,decimal_places=10,help_text="in numbers",blank=True,null=True)
	recieved_amount = models.DecimalField(verbose_name="Recieved Amount",max_digits=19,decimal_places=10,help_text="in numbers",blank=True,null=True)
	balance_amount = models.DecimalField(verbose_name="Balance Amount",max_digits=19,decimal_places=10,help_text="in numbers",blank=True,null=True)
	cash_cheque = models.CharField(verbose_name="Cash Cheque", max_length=20,blank=True)
	recieved_person = models.CharField(verbose_name="Recieved Person", max_length=50,blank=True)
	hand_over_to = models.CharField(verbose_name="Hand over to", max_length=250,blank=True)
	delivered_to = models.CharField(verbose_name="Delivered to", max_length=250,blank=True)
	type_of_cheque = models.CharField(verbose_name="Type of cheque", max_length=50,blank=True)
	contact_number = models.BigIntegerField(verbose_name="Contact Number",blank=True,null=True)
	careof = models.CharField(verbose_name="C/O",max_length=250,blank=True)
	timestamp = models.DateTimeField(default=datetime.now,editable=False)  # To save the time at which the object is created
	added_by = models.ForeignKey(User,editable=False)
	
	class Meta:
		ordering = ["-timestamp"]
		verbose_name_plural = "Cashbook"
		
	def __unicode__(self):
		return 	u'id %s created on %s' % (self.id, self.timestamp)
		
	def save(self, force_insert=False, force_update=False):
		send_notification('cashbook',self.timestamp,self.added_by)
		super(CashBook,self).save(force_insert, force_update)

	
# Book 10

class ClaimChequeDetails(models.Model):
	cheque_date = models.DateField(verbose_name="Date",blank=True,null=True)
	customer_name = models.CharField(verbose_name="Customer Name Given Person",max_length=50,blank=True)
	cheque_number = models.CharField(verbose_name="Cheque Number", max_length=20,blank=True)
	address_of_recieved_person = models.CharField(verbose_name="Address of Recieved Person", max_length=250,blank=True)
	mobile_number = models.CharField(verbose_name="Mobile Number", max_length=20,blank=True)
	signature = models.CharField(verbose_name="Signature", max_length=50,blank=True)
	delivery_date = models.DateField(verbose_name="Delivery Date",blank=True,null=True)
	relationship_with_customer = models.CharField(verbose_name="Relationship with customer", max_length=25,blank=True)
	#added after deployment
	cheque_amount = models.DecimalField(verbose_name="Cheque Amount",max_digits=19,decimal_places=10,help_text="in numbers",blank=True,null=True)
	#Cannot be seen
	timestamp = models.DateTimeField(default=datetime.now,editable=False)  # To save the time at which the object is created
	added_by = models.ForeignKey(User,editable=False)
	
	class Meta:
		ordering = ["-timestamp"]
		verbose_name_plural = "Claim Cheque Details"
		
	def __unicode__(self):
		return 	u'id %s created on %s' % (self.id, self.timestamp)

	def save(self, force_insert=False, force_update=False):
		send_notification('claim_cheque_details',self.timestamp,self.added_by)
		super(ClaimChequeDetails,self).save(force_insert, force_update)
		
# Book 11

class CovernoteBookDetails(models.Model):
	book_number = models.CharField(verbose_name="Book Number", max_length=20,blank=True)
	recieved_date = models.DateField(verbose_name="Recieved Date",blank=True,null=True)
	covernote_leaf_number = models.CharField(verbose_name="Covernote Leaf Number", max_length=20,blank=True)
	usage_of_leaf = models.CharField(verbose_name="Usage of the Leaf", max_length=50,blank=True)
	#added after deployment
	return_to_pkd_on = models.DateField(verbose_name="Return to Palakkad on",blank=True,null=True)
	by = models.CharField(verbose_name="By",max_length=50,blank=True)
	#Cannot be seen
	timestamp = models.DateTimeField(default=datetime.now,editable=False)  # To save the time at which the object is created
	added_by = models.ForeignKey(User,editable=False)
		
	class Meta:
		ordering = ["-timestamp"]
		verbose_name_plural = "Covernote Book Details"
		
	def __unicode__(self):
		return 	u'id %s created on %s' % (self.id, self.timestamp)
	
	def save(self, force_insert=False, force_update=False):
		send_notification('covernote_book_details',self.timestamp,self.added_by)
		super(CovernoteBookDetails,self).save(force_insert, force_update)
	
# Books added after deployment
# Book 12

class EnquiryBook(models.Model):
	details = models.TextField(verbose_name="Details",blank=True)
	name = models.CharField(verbose_name="Name",max_length=50,blank=True)
	place = models.CharField(verbose_name="Place",max_length=50,blank=True)
	timestamp = models.DateTimeField(default=datetime.now,editable=False)  # To save the time at which the object is created
	added_by = models.ForeignKey(User,editable=False)
	
	class Meta:
		ordering = ["-timestamp"]
		verbose_name_plural = "Enquiry Books"
		
	def __unicode__(self):
		return 	u'id %s created on %s' % (self.id, self.timestamp)
	
	def save(self, force_insert=False, force_update=False):
		send_notification('enquiry_book',self.timestamp,self.added_by)
		super(EnquiryBook,self).save(force_insert, force_update)
	
#Book 13

class CustomerCare(models.Model):
	name = models.CharField(verbose_name="Name",max_length=50,blank=True)
	policy_number = models.BigIntegerField(verbose_name="Policy Number",blank=True,null=True)
	details = models.TextField(verbose_name="Details",blank=True)
	followup_details = models.TextField(verbose_name="Follow Up Details",blank=True)
	timestamp = models.DateTimeField(default=datetime.now,editable=False)  # To save the time at which the object is created
	added_by = models.ForeignKey(User,editable=False)
	
	class Meta:
		ordering = ["-timestamp"]
		verbose_name_plural = "Customer Care"
		
	def __unicode__(self):
		return 	u'id %s created on %s' % (self.id, self.timestamp)
	
	def save(self, force_insert=False, force_update=False):
		send_notification('customer_care',self.timestamp,self.added_by)
		super(CustomerCare,self).save(force_insert, force_update)	
		
	
	
		
	
	
	
	
	
	
	
	
	
	
		
	
	
	
		
	
	
