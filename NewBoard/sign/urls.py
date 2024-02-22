from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from sign import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='sign/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='sign/logout.html'), name='logout'),
    path('signup/', views.sign_up, name='signup'),
    path('activation/', views.activation, name='activation')
]