from django.contrib import admin
from .models import *

class transisiadmin(admin.ModelAdmin):
	readonly_fields = [
		'update_time',
	]

admin.site.register(Release);

admin.site.register(product);
admin.site.register(productperpalet);
admin.site.register(transisi);
admin.site.register(gudangracking);
admin.site.register(tujuan);
admin.site.register(productkeluar);
admin.site.register(pengguna);
admin.site.register(Instagram);
admin.site.register(departement);
admin.site.register(lokasipenyimpanan);
admin.site.register(jenis_status);
admin.site.register(status_product);