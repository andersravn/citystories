 #!/usr/bin/env python
 # -*- coding: utf-8 -*-

from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.authtoken import views

from .views import NoteView, NoteMapView, UserEntryView, DfiFilmView, CreateUserEntryViewSet, AllDataLessThanView, \
    AllDataGreaterThanView

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views.obtain_auth_token),
    url('^vote/up/(?P<info>.+)/', 'api.views.upvote', name='upvote'),
    url('^vote/down/(?P<info>.+)/', 'api.views.downvote', name='downvote'),
    url('^report/(?P<info>.+)/', 'api.views.report', name='report'),
    url('^notes/(?P<lat>.+)/(?P<lon>.+)/(?P<distance>.+)/$', NoteView.as_view()),
    url('^notes/$', NoteMapView.as_view()),
    url('^userentries/(?P<lat>.+)/(?P<lon>.+)/(?P<distance>.+)/$', UserEntryView.as_view()),
    url('^userentries/$', CreateUserEntryViewSet.as_view()),
    url('^alldatalessthan/(?P<lat>.+)/(?P<lon>.+)/(?P<distance>.+)/$', AllDataLessThanView.as_view()),
    url('^alldatagreaterthan/(?P<lat>.+)/(?P<lon>.+)/(?P<distance>.+)/$', AllDataGreaterThanView.as_view()),
    url('^dfifilm/$', DfiFilmView.as_view()),
]

urlpatterns += router.urls
