
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index,name='index'),
    path('<id>/<str:slug>/',views.detail_view,name='details'),
    path('search/', views.search,name='search'),
]