from . import views
from django.urls import path 

urlpatterns = [
    path('', views.add_show,name='add'),
    path('<int:id>/', views.update_data,name='update'),
    path('delete/<int:id>', views.delete_data,name='delete'),
    
]
