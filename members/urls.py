from django.urls import path
from .views import UserResgiterView , UserEditView
from django.contrib.auth import views as auth_views
from .import views
urlpatterns = [
    path('register/',UserResgiterView.as_view(),name='register'),
    path('edit_profile/',UserEditView.as_view(),name='edit_profile'),
    #path('passwor', auth_views.PasswordChangeView.as_view()),
    #path('<int:id>/password/',auth_views.PasswordChangeView.as_view()),
    path('password_success',views.Password_Success,name='password_success'),


    
]