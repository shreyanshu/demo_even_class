from canteen_managemant_system import views
from django.urls import path

app_name = 'cms'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('list_food/', views.list_food, name='list_food'),
    path('add_food/', views.add_food, name='add_food'),
    path('edit_food/<int:id>/', views.edit_food, name='edit_food'),
    path('delete_food/<int:id>/', views.delete_food, name='delete_food'),
    path('list_cook/', views.CookListView.as_view(), name='list_cook'),
    path('', views.IndexView.as_view(), name='index'),
    path('cook_detail/<int:pk>/', views.CookDetailView.as_view(), name='detail_cook'),
    path('add_cook/', views.CreateCookView.as_view(), name='add_cook'),
    path('edit_cook/<int:pk>/', views.UpdateCookView.as_view(), name='edit_cook'),
    path('delete_cook/<int:pk>/', views.DeleteCookView.as_view(), name='delete_cook'),
    path('login/', views.login_view, name='login')
    # path('login/')
]