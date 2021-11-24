from django.conf.urls import url 
from tutorials import views 
 
urlpatterns = [ 
    url(r'^api/tutorials$', views.tutorial_list),
    url(r'^api/tutorials/(?P<name>\w{0,50})/$', views.tutorial_detail),
    url(r'^api/tutorials/(?P<name>\w{0,50})/$', views.tutorial_detail),

    
]