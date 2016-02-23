 #!/usr/bin/env python
 # -*- coding: utf-8 -*-

from django.conf.urls import url

from dashboard import views

urlpatterns = [
    url(r'^$', views.dash_view, name='dash'),
    url(r'^userentry-reports/', views.userentry_reports_view, name='userentry_reports'),
    url(r'^note-reports/', views.note_reports_view, name='note_reports'),
    url(r'^add-street/', views.add_street_view, name='add_street'),
    url(r'^filter/', views.filter_view, name='filter'),
    url(r'^scripts/', views.scripts_view, name='note_scripts'),
    url(r'^missing-coords/', views.missing_coords, name='missing_coords'),
    url(r'^load-csv/', views.load_csv, name='load_csv'),
    url(r'^load-notes/', views.load_notes, name='load_notes'),
    url(r'^delete-duplicates/', views.delete_duplicates, name='delete_duplicates'),
    url(r'^addpntfields/', views.add_pnt_fields, name='addpntfields'),
    url(r'^delete-notes/', views.delete_notes, name='delete_notes'),
    url(r'^stadsarkiv-api/', views.stadsarkiv_api, name='stadsarkiv_api'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^auth/', views.auth_view, name='auth_dash'),
    url(r'^logout/', views.logout_view, name='dash_logout'),
]
