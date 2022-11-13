from django.urls import path, include

urlpatterns = [
    path('fluxos/', include('apps.mapa.urls')),
    path('forum/', include('apps.forum.urls')),
]
