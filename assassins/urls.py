from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings

from assassins import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^kill$', views.kill, name='kill'),
    url(r'^confirm_kill$', views.confirm_kill, name='confirm_kill'),
    url(r'^submit_registration$', views.submit_registration, name='submit_registration'),
    #url(r'^status$', views.status, name='status'),
    url(r'^admin/', views.admin, name='admin'),
    url(r'^update_dorm_info$', views.update_dorm_info, name='update_dorm_info'),
    url(r'^assign_targets$', views.assign_targets, name='assign_targets'),
    url(r'^shuffle_targets$', views.shuffle_targets, name='shuffle_targets'),
    url(r'^send_email$', views.send_email, name='send_email'),
    url(r'sudden_death_kill$', views.sudden_death_kill, name='sudden_death_kill'),
)
