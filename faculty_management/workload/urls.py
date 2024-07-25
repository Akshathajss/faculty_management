from django.urls import path
from . import views
from workload.views import index,display_table,BV_TC,home
urlpatterns = [
    path('', views.index, name='index'),
    path('BV_TC/',BV_TC ),
    path('display_table/',display_table ),
    path('index/',index ),
    path('home/',home ),
]
