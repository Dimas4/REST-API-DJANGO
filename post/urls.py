from django.conf.urls import url

from .views import PostApiView, PostDetaokAPIView, LangApiView, LangDetaokAPIView

urlpatterns = [
    url(r'^post/$', PostApiView.as_view(), name='list'),
    url(r'^post/(?P<pk>[0-9]+)/$', PostDetaokAPIView.as_view(), name='list'),

    url(r'^lang/$', LangApiView.as_view(), name='list'),
    url(r'^lang/(?P<pk>[0-9]+)/$', LangDetaokAPIView.as_view(), name='list'),

]