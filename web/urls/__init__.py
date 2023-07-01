from django.urls import path, include

urlpatterns = [
    path('', include('web.urls.web')),
    path('web/api/', include('web.urls.api')),
]
