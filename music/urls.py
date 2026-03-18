from django.conf.urls import url
from . import views 
from django.views.generic.base import TemplateView
from music import views
from django.contrib.auth import views as auth_views




app_name = "music"
urlpatterns = [

    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.search, name='search'),
    url(r'^$', views.home, name='home'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
	url(r'^signup/$', views.signup, name='signup' ),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^song/(?P<pk>[0-9]+)/$', views.PlayView.as_view(), name='play'),
    url(r'^song/$', views.SongView.as_view(), name='song'),
    url(r'^album/add/$', views.AlbumCreate.as_view(), name="addalbum"),
    url(r'^album/edit/$', views.AlbumUpdate.as_view(), name="Updatealbum"),
    url(r'^song/add/$', views.SongAdd.as_view(), name="addsong"),
]
