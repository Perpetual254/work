from django.urls import path

from . import views

urlpatterns = [
    path ('dashboard/', views.dashboard, name='dashboard'),
    path('', views.register, name='register'),
    path('addworker', views.addworker, name='addworker'),
    path('editworker/<id>', views.editworker, name='editworker'),
    path('deleteworker/<id>', views.deleteworker ),
    path('updateworker/<id>', views.updateworker, name='updateworker'),
    path('editworker/<id>', views.editworker, name='editworker')





]




