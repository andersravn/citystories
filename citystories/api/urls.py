 #!/usr/bin/env python
 # -*- coding: utf-8 -*-

from django.conf.urls import include, url
from rest_framework import routers

from .views import EntryViewSet, UserViewSet, TestEntryViewSet, CreateTestEntryViewSet, NoteView, NoteMapView
import api.views

router = routers.DefaultRouter()
router.register(r'entries', EntryViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^notes/up/(?P<note_id>.+)/', 'api.views.upvote_note', name='upvote_note'),
    url('^notes/down/(?P<note_id>.+)/', 'api.views.downvote_note', name='downvote_note'),
    url('^notes/report/(?P<note_id>.+)/', 'api.views.report_note', name='report_note'),
    url('^notes/(?P<lat>.+)/(?P<lon>.+)/$', NoteView.as_view()),
    url('^notes/$', NoteMapView.as_view()),
    url('^test-entries/(?P<location>.+)/$', TestEntryViewSet.as_view()),
    url('^test-entries/$', CreateTestEntryViewSet.as_view()),
]

urlpatterns += router.urls
