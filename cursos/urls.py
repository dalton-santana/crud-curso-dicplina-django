from django.urls import path
from .views import list_cursos, create_curso, update_curso, delete_curso

urlpatterns = [
    path('', list_cursos, name='list_cursos'),
    path('new', create_curso, name='create_curso'),
    path('update/<int:id>/', update_curso, name='update_curso'),
    path('delete/<int:id>/', delete_curso, name='delete_curso'),
]
