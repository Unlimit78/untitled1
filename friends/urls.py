from django.urls import path
from .views import find_friend , other_profiles,friends,add_friend,delete_friend

urlpatterns = [
    path('find_friend/',find_friend,name='find_friend'),
    path('<int:other_id>/',other_profiles,name='other_profiles'),
    path('accounts/profile/friends/',friends,name='friends'),
    path('add/<int:friend_id>/',add_friend,name='add_friend'),
    path('accounts/profile/friends/<int:friend_id>/',delete_friend,name='delete_friend'),

]
