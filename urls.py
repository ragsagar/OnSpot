from django.conf.urls.defaults import *
#from django.contrib import admin
#from books.exporter import export



# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^erp/', include('erp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #(r'^login/', 'django.contrib.auth.views.login'),
    url(r'^sms_notification/$', 'books.views.AdminInfo', name='admininfo'),
    url(r'^income_expense_report/$', 'books.views.income_expense_dateselect', name='income_expense_dateselect'),
    url(r'^income_expense_report/(?P<year>\d{4})/(?P<month>\d{1,2})/$', 'books.views.income_expense_report', name='income_expense_month' ),
    url(r'^income_expense_report/(?P<year>\d{4})/$', 'books.views.income_expense_report', name='income_expense_year'),
	#(r'^export/(?P<admin_site>.)/(?P<model_name>.)/(?P<app_label>.*)/$', admin.site.admin_view(export), {'admin_site': admin.site}),
    (r'^(?P<app_label>[\d\w]+)/(?P<model_name>[\d\w]+)/csv/', 'books.csv_view.admin_list_export'),
    # Uncomment the next line to enable the admin:
    url(r'^', include(admin.site.urls)),
)
