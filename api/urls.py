from django.urls import path
from . import views

urlpatterns = [
    path('project/', views.get_projects),
    path('project/add/', views.add_project),
    path('project/<int:pk>', views.project),
]