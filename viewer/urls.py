from django.urls import path
from . import views

app_name = 'viewer'

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.contents, name='contents'),
    # path('', views.resource, name='resource'),
]
