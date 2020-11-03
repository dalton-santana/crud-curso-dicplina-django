from django.urls import path
from .views import list_alunos, create_aluno, update_aluno, delete_aluno, create_matricula, update_matricula, delete_matricula

urlpatterns = [
    path('', list_alunos, name='list_alunos'),
    path('new', create_aluno, name='create_aluno'),
    path('update/<int:id>/', update_aluno, name='update_aluno'),
    path('delete/<int:id>/', delete_aluno, name='delete_aluno'),
    path('<int:id>/new_matricula/', create_matricula, name='create_matricula'),
    path('update_matricula/<int:id>/', update_matricula, name='update_matricula'),
    path('delete_matricula/<int:id>/', delete_matricula, name='delete_aluno'),
]
