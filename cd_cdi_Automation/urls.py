from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.EmployeeViewSet.as_view({'get': 'list'}), name='employee-list'),
    path('employees/create/', views.EmployeeCreateViewSet.as_view({'post': 'create'}), name='employee-create'),
    path('employees/<int:pk>/update/', views.EmployeeUpdateViewSet.as_view({'put': 'update'}), name='employee-update'),
    path('employees/<int:pk>/delete/', views.EmployeeDeleteViewSet.as_view({'delete': 'destroy'}), name='employee-delete'),
    path('employees/list/', views.employee_list, name='employee-list-view'),
    path('employees/create/form/', views.employee_create, name='employee-create-form'),
]
