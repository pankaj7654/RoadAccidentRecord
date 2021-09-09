
from django.urls import path
from Record.views import index
from Record.views import signup, login

urlpatterns = [
    path('', index.index , name='index'),
    path('signup/', signup.SignupView.as_view() , name='signupView'),
    path('login/', login.LoginView.as_view() , name='loginView'),
    path('logout/', index.logout , name='logout'),
]
