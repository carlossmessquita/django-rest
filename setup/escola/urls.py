from django.urls import path, include
from .views import AlunosViewSet, CursosViewSet, MatriculasViewSet, \
    ListaMatriculaAluno, ListaAlunosMatriculados
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='alunos')
router.register('cursos', CursosViewSet, basename='cursos')
router.register('matriculas', MatriculasViewSet, basename='matriculas')


urlpatterns = [
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', ListaMatriculaAluno.as_view()),
    path('curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view()),
    path('api-auth/', include('rest_framework.urls'))
]