from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name="home"),
    path('update.html/<str:pk>/',views.update,name="update"),
    path('delete.html/<str:pk>/',views.delete,name="delete"),
]