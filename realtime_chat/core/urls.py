from django.urls import path
from  core.views import frontpage, signup, login
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/',signup  ,name='singup'),
    path('login/',auth_views.LoginView.as_view(template_name = 'core/login.html')  ,name='login'),
    path('logout/', auth_views.LogoutView.as_view()  ,name='logout'),
    ]