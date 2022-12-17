from django.urls import path
from empmanage import views

urlpatterns=[
    path('',views.home,name='emphome'),
    path('AddEmployee/',views.addEmployee,name='addemp'),
  #  path('home/',views.home),
    path('delete_emp/<int:emp_id>',views.delete_emp,name='deleteemp'),
    path('update_emp/<int:emp_id>',views.update_emp,name='updateemp')
] 