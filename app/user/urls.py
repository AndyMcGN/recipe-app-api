""" URL mappings for user API """

from django.urls import path
from user import views

# define this and path names so it can be used in reverse() methods
# e.g. url = reverse('user:create')
app_name = 'user'

urlpatterns = [
    # .as_view() is used to convert the class based view into the
    # (django supported) functional view
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
]
