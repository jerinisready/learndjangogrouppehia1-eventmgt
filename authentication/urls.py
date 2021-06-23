from django.urls import path

from authentication.views import signup, signin, signout

urlpatterns = [
    # path('signup/', signup, name="signup"),
    # path('login/', LoginView.as_view(), name="login"),

    path('login/', signin, name="sign_in"),
    path('logout/', signout, name="sign_out"),

]
