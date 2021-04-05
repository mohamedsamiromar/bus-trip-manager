from django.urls import path
from apps.swvlauthentication import views

urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('signup/', views.signup, name='signup'),
    path('edit_profile', views.edit_profile, name='edit_profile')

]