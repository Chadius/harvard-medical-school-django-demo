from django.conf.urls import url

from . import views

app_name = 'participants'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index/$', views.index, name='index'),
    url(r'^new/$', views.new, name='new_participant'),
    url(r'^save/$', views.save, name='save_participant'),
    url(r'^update_review/(?P<participant_id>[0-9]+)/$', views.update_review, name='update_review'),
]