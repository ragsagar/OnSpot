from django.contrib import admin
from books.csv_view import export
from django.core.exceptions import PermissionDenied
from books.models import DirectBusiness, DirectOwnAgentBusiness, OtherAgentBusiness
from books.models import NameTransfer, FilesFollowUp, GEIncome, GEExpense, ThirdParty
from books.models import PhonecallDetails, CashBook, ClaimChequeDetails, CovernoteBookDetails
from books.models import EnquiryBook, CustomerCare

# Action function 
def export_as_csv(modeladmin, request, queryset):
	if not request.user.is_staff:
		raise PermissionDenied
	return export(queryset)
export_as_csv.short_description = "Export selected rows into csv"	

# Class for giving readonly permissions to employees

class ReadPermissionModelAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        if getattr(request, 'readonly', False):
            return True
        return super(ReadPermissionModelAdmin, self).has_change_permission(request, obj)

    def changelist_view(self, request, extra_context=None):
        try:
            return super(ReadPermissionModelAdmin, self).changelist_view(
                request, extra_context=extra_context)
        except PermissionDenied:
            pass
        #if request.method == 'POST':
        #   raise PermissionDenied
        request.readonly = True
        return super(ReadPermissionModelAdmin, self).changelist_view(
            request, extra_context=extra_context)

    

# Model Admin Classes

class DirectBusinessAdmin(ReadPermissionModelAdmin):
	list_display = [field.name for field in DirectBusiness._meta.fields]
	actions = [export_as_csv]
	#search_fields = ('delivery_date',)
	
	def save_model(self, request, obj, form, change):
		obj.added_by = request.user
		obj.save()


class DirectOwnAgentBusinessAdmin(ReadPermissionModelAdmin):
	list_display = [field.name for field in DirectOwnAgentBusiness._meta.fields]
	actions = [export_as_csv]
	#search_fields = ('timestamp',)
	
	def save_model(self, request, obj, form, change):
		obj.added_by = request.user
		obj.save()

	
class OtherAgentBusinessAdmin(ReadPermissionModelAdmin):
	list_display = [field.name for field in OtherAgentBusiness._meta.fields]	
	actions = [export_as_csv]
	#search_fields = ('timestamp',)
	
	def save_model(self, request, obj, form, change):
		obj.added_by = request.user
		obj.save()
		
	
class NameTransferAdmin(ReadPermissionModelAdmin):
	list_display = [field.name for field in NameTransfer._meta.fields]	
	actions = [export_as_csv]
	search_fields = ('vehicle_number',)
	
	def save_model(self, request, obj, form, change):
		obj.added_by = request.user
		obj.save()

	
class FilesFollowUpAdmin(ReadPermissionModelAdmin):
	list_display = [field.name for field in FilesFollowUp._meta.fields]
	actions = [export_as_csv]
	search_fields = ('vehicle_number',)
	
	def save_model(self, request, obj, form, change):
		obj.added_by = request.user
		obj.save()

	
class GEIncomeAdmin(ReadPermissionModelAdmin):
	list_display = [field.name for field in GEIncome._meta.fields]
	actions = [export_as_csv]
	#search_fields = ('timestamp',)
	
	def save_model(self, request, obj, form, change):
		obj.added_by = request.user
		obj.save()

	
class GEExpenseAdmin(ReadPermissionModelAdmin):
	list_display = [field.name for field in GEExpense._meta.fields]
	actions = [export_as_csv]
	#search_fields = ('timestamp',)
	
	def save_model(self, request, obj, form, change):
		obj.added_by = request.user
		obj.save()

	
class ThirdPartyAdmin(ReadPermissionModelAdmin):
	list_display = [field.name for field in ThirdParty._meta.fields]	
	actions = [export_as_csv]
	search_fields = ('vehicle_number',)
	
	def save_model(self, request, obj, form, change):
		obj.added_by = request.user
		obj.save()

	

class PhonecallDetailsAdmin(ReadPermissionModelAdmin):
	list_display = [field.name for field in PhonecallDetails._meta.fields]	
	actions = [export_as_csv]
	search_fields = ('vehicle_number',)
	
	def save_model(self, request, obj, form, change):
		obj.added_by = request.user
		obj.save()


class CashBookAdmin(ReadPermissionModelAdmin):
	list_display = [field.name for field in CashBook._meta.fields]
	actions = [export_as_csv]
	search_fields = ('vehicle_number',)
	
	def save_model(self, request, obj, form, change):
		obj.added_by = request.user
		obj.save()

	
class ClaimChequeDetailsAdmin(ReadPermissionModelAdmin):
	list_display = [field.name for field in ClaimChequeDetails._meta.fields]		
	actions = [export_as_csv]
	#search_fields = ('timestamp',)
	
	def save_model(self, request, obj, form, change):
		obj.added_by = request.user
		obj.save()

	
class CovernoteBookDetailsAdmin(ReadPermissionModelAdmin):
	list_display = [field.name for field in CovernoteBookDetails._meta.fields]
	actions = [export_as_csv]
	#search_fields = ('timestamp',)
	
	def save_model(self, request, obj, form, change):
		obj.added_by = request.user
		obj.save()

	
class CustomerCareAdmin(ReadPermissionModelAdmin):
	list_display = [field.name for field in CustomerCare._meta.fields]	
	actions = [export_as_csv]
	#search_fields = ('timestamp',)
	
	def save_model(self, request, obj, form, change):
		obj.added_by = request.user
		obj.save()


class EnquiryBookAdmin(ReadPermissionModelAdmin):
	list_display = [field.name for field in EnquiryBook._meta.fields]	
	actions = [export_as_csv]
	#search_fields = ('timestamp',)
	
	def save_model(self, request, obj, form, change):
		obj.added_by = request.user
		obj.save()

	
admin.site.register(DirectBusiness, DirectBusinessAdmin)
admin.site.register(DirectOwnAgentBusiness, DirectOwnAgentBusinessAdmin)
admin.site.register(OtherAgentBusiness, OtherAgentBusinessAdmin)
admin.site.register(NameTransfer, NameTransferAdmin)
admin.site.register(FilesFollowUp, FilesFollowUpAdmin)
admin.site.register(GEIncome, GEIncomeAdmin)
admin.site.register(GEExpense, GEExpenseAdmin)
admin.site.register(ThirdParty, ThirdPartyAdmin)
admin.site.register(PhonecallDetails, PhonecallDetailsAdmin)
admin.site.register(CashBook, CashBookAdmin)
admin.site.register(ClaimChequeDetails, ClaimChequeDetailsAdmin)
admin.site.register(CovernoteBookDetails, CovernoteBookDetailsAdmin)
admin.site.register(EnquiryBook, EnquiryBookAdmin)
admin.site.register(CustomerCare, CustomerCareAdmin)
