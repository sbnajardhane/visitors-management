from django.conf.urls import url, patterns, include

from . import views

urlpatterns = [
    url(r'^insert/$', 'visitor.views.insert'),
    url(r'^male/$','visitor.views.male'), 
    url(r'^dashboard/$','visitor.views.dashboard'),
    url(r'^count/$','visitor.views.count'),
    url(r'^countdate/$','visitor.views.countdate'),
    #url(r'^chart/$','visitor.views.chart_view'),
    url(r'^table/$','visitor.views.table'),
    url(r'^table1/$','visitor.views.table1'),
    url(r'^profile/$','visitor.views.profile'),
    url(r'^staff/$','visitor.views.staff'),
    url(r'^profile/comment/$','visitor.views.comment'),
    url(r'^event/$','visitor.views.event'),
    url(r'^uploadfile/$','visitor.views.uploadFile'),
    url(r'^event/eventProfile/$', 'visitor.views.eventProfile'),
   	# url(r'^staff/profile/$','visitor.views.staffProfile'),
	url(r'^staff/(?P<person_id>[0-9]*\.?[0-9]+)/$','visitor.views.staffProfile', name="staffProfile"),

   #url(r'^get/(?P<person_id>\d+)/$','visitor.views.exp'),	

    #url(r'^$', views.gender)
]
