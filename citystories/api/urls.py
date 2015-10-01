 #!/usr/bin/env python
 # -*- coding: utf-8 -*-

from django.conf.urls import include, url
from rest_framework import routers

from .views import UserViewSet, NoteView, NoteMapView, UserEntryViewSet, CreateUserEntryViewSet
import api.views

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^notes/up/(?P<note_id>.+)/', 'api.views.upvote_note', name='upvote_note'),
    url('^notes/down/(?P<note_id>.+)/', 'api.views.downvote_note', name='downvote_note'),
    url('^notes/report/(?P<note_id>.+)/', 'api.views.report_note', name='report_note'),
    url('^notes/(?P<lat>.+)/(?P<lon>.+)/$', NoteView.as_view()),
    url('^notes/$', NoteMapView.as_view()),
    url('^userentries/up/(?P<userentry_id>.+)/', 'api.views.upvote_userentry', name='upvote_userentry'),
    url('^userentries/down/(?P<userentry_id>.+)/', 'api.views.downvote_userentry', name='downvote_userentry'),
    url('^userentries/report/(?P<userentry_id>.+)/', 'api.views.report_userentry', name='report_userentry'),
    url('^userentries/(?P<location>.+)/$', UserEntryViewSet.as_view()),
    url('^userentries/$', CreateUserEntryViewSet.as_view()),
]

urlpatterns += router.urls
