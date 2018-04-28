#from .profile import views
from django.conf.urls import url
from django.contrib.auth import views as auth_views
# from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import RedirectView

from . import views
from .views import UserView, UserDelete, UserEdit, UserCreate, UserUpdatePass, UserList

app_name = 'user'

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='user:login', permanent=False)),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^create/$', UserCreate.as_view(), name='create'),
    #
    # url(r'^change-password/', auth_views.password_change, {'template_name': 'registration/password_change_form.html'}, name='password_change'),
    # url(r'^accounts/password/change/done/', auth_views.password_change_done, {'template_name': 'registration/password_change_done.html'}, name='password_change_done'),
    url(r'^change-password/', UserUpdatePass.as_view(), name="change_pass"),
    url(r'^list/$', UserList.as_view(), name="list"),
    url(r'^me/$', UserView.as_view(), name="me"),
    # TODO these are not really implemented yet
    url(r'^(?P<user_id>\d*)/view/$', UserView.as_view(), name="view"),
    url(r'^(?P<user_id>\d*)/update/$', UserEdit.as_view(), name="update"),
    url(r'^(?P<user_id>\d*)/delete/$', UserDelete.as_view(), name="delete"),
]
