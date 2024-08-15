from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<gform_id>[0-9]+)/export_csv/$', views.export_csv, name="export_csv"),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^edit_profile/$', views.edit_profile, name='edit_profile'),
    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^register/$', views.register, name='register'),
    url(r'^(?P<gform_id>[0-9]+)/user/(?P<user_id>[0-9]+)/$', views.filler, name='filler'),
    url(r'^(?P<gform_id>[0-9]+)/user/(?P<user_id>[0-9]+)/link$', views.link, name='link'),
    url(r'^(?P<gform_id>[0-9]+)/user/(?P<user_id>[0-9]+)/link$', views.responses, name='responses'),

    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<gform_id>[0-9]+)/$', views.detail, name='detail'),
#     url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
#     url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),
    url(r'^create_form/$', views.create_form, name='create_form'),
    url(r'^(?P<gform_id>[0-9]+)/create_question/$', views.create_question, name='create_question'),
    url(r'^(?P<gform_id>[0-9]+)/delete_question/(?P<question_id>[0-9]+)/$', views.delete_question, name='delete_question'),
#     url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    url(r'^(?P<gform_id>[0-9]+)/delete_form/$', views.delete_form, name='delete_form'),
]
