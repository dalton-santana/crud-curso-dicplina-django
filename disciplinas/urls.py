from django.urls import path
from .views import list_disciplinas, create_disciplina, update_disciplina, delete_disciplina

urlpatterns = [
    path('', list_disciplinas, name='list_disciplinas'),
    path('new', create_disciplina, name='create_disciplina'),
    path('update/<int:id>/', update_disciplina, name='update_disciplina'),
    path('delete/<int:id>/', delete_disciplina, name='delete_disciplina'),
]
