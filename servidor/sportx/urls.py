from django.urls import path
from sportx import views

urlpatterns = [
    path('', views.BackendInfo),
    path('pqrs/', views.PqrsList),
    path('pqrs/create/', views.PqrsCreate),
    path('pqrs/<int:pk>', views.PqrsDetail),
    path('pqrs/deleteseveral/<pks>', views.DeleteSeveralPqrs),
]