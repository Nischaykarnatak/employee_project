from . import views
from django.urls import path

urlpatterns = [
    path('', views.employee_register, name='employee_insert'),
    path('<int:id>/', views.employee_register, name='employee_update'),
    path('list', views.employee_list, name='employee_list'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete')
]