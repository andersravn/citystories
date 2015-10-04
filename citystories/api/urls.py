 #!/usr/bin/env python
 # -*- coding: utf-8 -*-

from django.conf.urls import include, url
from rest_framework import routers

from .views import NoteView, NoteMapView, UserEntryView, DfiFilmView, CreateUserEntryViewSet
import api.views

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^vote/up/(?P<info>.+)/', 'api.views.upvote', name='upvote'),
    url('^vote/down/(?P<info>.+)/', 'api.views.downvote', name='downvote'),
    url('^report/(?P<info>.+)/', 'api.views.report', name='report'),
    url('^notes/(?P<lat>.+)/(?P<lon>.+)/$', NoteView.as_view()),
    url('^notes/$', NoteMapView.as_view()),
    url('^userentries/(?P<location>.+)/$', UserEntryView.as_view()),
    url('^userentries/$', CreateUserEntryViewSet.as_view()),
    url('^dfifilm/$', DfiFilmView.as_view()),
]

urlpatterns += router.urls
