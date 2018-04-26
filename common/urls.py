from django.conf.urls import url

from django.views.generic import RedirectView
app_name = 'common'


urlpatterns = [
    url(r'^$',  RedirectView.as_view(pattern_name='user:login'), name="home"),
]
