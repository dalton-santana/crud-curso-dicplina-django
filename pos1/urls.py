from django.contrib import admin
from django.urls import path, include
from .views import init

urlpatterns = [
    path('', init, name='init'),
    path('cursos/', include('cursos.urls')),
    path('disciplinas/', include('disciplinas.urls')),
    path('admin/', admin.site.urls),
]