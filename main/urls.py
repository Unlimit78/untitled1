from django.urls import path
from .views import index,UserLogin,UserLogout,profile,ChangeInfo,\
ChangePassword,RegisterUserView,RegisterDoneView,DeleteUser,page


urlpatterns = [
    path('',index,name='index'),
    path('accounts/login/',UserLogin.as_view(),name='login'),
    path('accounts/logout/',UserLogout.as_view(),name='logout'),
    path('accounts/profile/',profile,name='profile'),
    path('accounts/profile/change/',ChangeInfo.as_view(),name='profile_change'),
    path('accounts/profile/password/change/',ChangePassword.as_view(),name='password_change'),
    path('accounts/register/',RegisterUserView.as_view(),name='register'),
    path('accounts/register/done/',RegisterDoneView.as_view(),name='register_done'),
    path('accounts/profile/delete/',DeleteUser.as_view(),name='profile_delete'),
    path('page/',page,name="page"),


]