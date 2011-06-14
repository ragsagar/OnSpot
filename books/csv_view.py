import csv
from django.http import HttpResponse, HttpResponseForbidden
from django.template.defaultfilters import slugify
from django.db.models.loading import get_model
from django.core.exceptions import PermissionDenied

def export(qs, fields=None):
    model = qs.model
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % slugify(model.__name__)
    writer = csv.writer(response)
    
	# Write headers to CSV file
    if fields:
        headers = fields
    else:
        headers = []
        for field in model._meta.fields:
            headers.append(field.name)
    if headers[0] == 'action_checkbox':
		del headers[0]        
    writer.writerow(headers)
    
	# Write data to CSV file
    for obj in qs:
        row = []
        for field in headers:
            if field in headers:
                val = getattr(obj, field)
                if callable(val):
                    val = val()
                row.append(val)
        writer.writerow(row)
    # Return CSV file to browser as download
    return response

def admin_list_export(request, model_name, app_label, queryset=None, fields=None, list_display=True):
    
    if not request.user.is_staff:
        #return HttpResponseForbidden()
        raise PermissionDenied
           
    if not queryset:
        model = get_model(app_label, model_name)
        queryset = model.objects.all()
        filters = dict()
        for key, value in request.GET.items():
            if key not in ('ot', 'o', 'p'):
                filters[str(key)] = str(value)
        if len(filters):
            queryset = queryset.filter(**filters)
    
    if not fields and list_display:
		from django.contrib import admin
		ld = admin.site._registry[queryset.model].list_display
		if ld and len(ld) > 0 : fields = ld
    return export(queryset, fields)
    
