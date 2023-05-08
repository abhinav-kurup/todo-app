from django.urls import path
from . import views
urlpatterns=[
    path('task-list/',views.tasklist ),
    path('taskl/<str:pk>/',views.taskl ),
    path('task-update/<str:pk>/',views.update ),
    path('task-delete/<str:pk>/',views.delete ),
    path('task-create/',views.create ),
]