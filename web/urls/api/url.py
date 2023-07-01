from django.urls import path

from web.views.web import view

app_name = "web_api"
urlpatterns = [
    path('', view.home, name='home'),
]
