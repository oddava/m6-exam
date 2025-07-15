from django.urls import path

from expense_tracker import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile', views.profile, name='profile'),
    path('add_expense', views.add_expense, name='add_expense'),
    path('<int:eid>/delete', views.delete, name='delete'),
    path('register', views.register, name='register')
]