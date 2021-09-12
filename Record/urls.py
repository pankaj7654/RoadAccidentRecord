
from django.urls import path
from Record.views import index
from Record.views import signup, login , formdata
from Record.middlewares.login_required_middleware import login_required
from Record.middlewares.can_not_access_after_login import cantAccessAfterLogin


urlpatterns = [
    path('', login_required(index), name='index'),
    path('signup/', cantAccessAfterLogin(signup.SignupView.as_view()) , name='signupView'),
    path('login/', cantAccessAfterLogin(login.LoginView.as_view()) , name='loginView'),
    path('logout/', index.logout , name='logout'),
    path('formdata/', formdata.FormdataView.as_view()),
]
