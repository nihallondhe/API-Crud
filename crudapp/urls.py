from django.urls import path
from crudapp.views import EmployeTable,EmployeeUpdate

urlpatterns = [
    path('',EmployeTable.as_view(),name='home'),
    path('Emp/<int:pk>',EmployeeUpdate.as_view()),
    
]



