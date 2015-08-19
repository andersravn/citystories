 #!/usr/bin/env python
 # -*- coding: utf-8 -*-

from django.conf.urls import include, url

from dashboard import views

urlpatterns = [
    url(r'^$', views.dash_view, name='dash'),
    url(r'^add-street/', views.add_street_view, name='add_street'),
    url(r'^scripts/', views.scripts_view, name='note_scripts'),
    url(r'^load-csv/', views.load_csv, name='load_csv'),
    url(r'^stadsarkiv-api/', views.stadsarkiv_api, name='stadsarkiv_api'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^auth/', views.auth_view, name='auth_dash'),
    url(r'^logout/', views.logout_view, name='dash_logout'),
]
