from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home' ),
    path('event_detail/<int:pk>/', views.EventDetail, name='event-detail')
]

