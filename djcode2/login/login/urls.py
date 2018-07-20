from django.conf.urls import  include, url
from django.contrib import admin
from logReg import views,middleware

urlpatterns = [
    # Examples:
    # url(r'^$', 'login.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/',  include(admin.site.urls)),
    url(r'^login/$', views.login),
    url(r'^regist/$',views.regist),
    url(r'^index/$', views.index),
    url(r'^logout/$',views.logout),
    url('^url/$', middleware.my_middleware),
]