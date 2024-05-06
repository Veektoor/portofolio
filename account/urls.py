from django.contrib import admin
from django.urls import path
from aacount import views



# django admin changes
admin.site.site_header = "Login to site"
admin.site.site_title = "Welcome to DashBord"
admin.site.index_title = "Welcome to Portal"



urlpatterns = [
    path('', views.home, name='home'),
    path('project', views.project, name='project'),
    path('contact', views.contact, name='contact'),
    # path('skills', views.skills, name='skills'),
    # path('contact', views.contact, name='contact'),
]