
from django.urls import path, include

from address import views

app_name = 'address'

urlpatterns = [

    path('',views.home,name='home'),    # Program moves to the Home function in views from which the homepage will be loaded in frontend
    path('delete/<int:addr_id>/',views.delete,name="delete"),    # Program moves to the delete function in views from which the delete page will be loaded in frontend
    path('update/<int:addr_id>/',views.update,name="update"),    # Program moves to the Home function in views from which the edit page will be loaded in frontend
]