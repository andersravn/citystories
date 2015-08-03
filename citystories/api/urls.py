from django.conf.urls import include, url
from rest_framework import routers

from .views import EntryViewSet, UserViewSet, TestEntryViewSet, NoteView

router = routers.DefaultRouter()
router.register(r'entries', EntryViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^notes/(?P<location>.+)/$', NoteView.as_view()),
    url('^test-entries/', TestEntryViewSet.as_view()),
]

urlpatterns += router.urls
