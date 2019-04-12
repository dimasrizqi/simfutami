from django.conf.urls import include,url
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView

urlpatterns = [
    #url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout,{'template_name': 'logout.html'}, name='logout'),

    url(r'^admin/', admin.site.urls),
    url(r'^inventory/', include('inventory.urls')),
    url(r'^produksi/', include('produksi.urls')),
    url(r'^kegiatan/', include('kegiatan.urls')),
]
