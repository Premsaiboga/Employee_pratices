from django.urls import path
from .views import Employeecreateview,Employeecrudview

urlpatterns =[
    path('create/', Employeecreateview.as_view()),
    path('<int:pk>/',Employeecrudview.as_view())
]