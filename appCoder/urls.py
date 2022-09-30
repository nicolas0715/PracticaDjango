from django.urls import path
from appCoder.view import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("inicio/", inicio),
    path("", home2 ), 
    path("cursos/", cursos),
    path("entregables/", entregables ),
    path("estudiantes/", estudiantes),
    path("profesores/", profesores),
    path("api_estudiante/", api_estudiante),
    path("buscar_estudiante/", buscar_estudiante),

    path("create_estudiantes/", create_estudiantes),
    path("read_estudiantes/", read_estudiantes),
    path("update_estudiantes/<estudiante_id>", update_estudiantes),
    path("delete_estudiantes/<estudiante_id>", delete_estudiantes),
    path("login/", login_request),
    path("registro/", registro),
    path('logout/', LogoutView.as_view(template_name = 'home2.html'), name="Logout" ),
    path("perfil/", perfilView),
    path("perfil/editarPerfil/", editarPerfil),
    path("perfil/changepass/", changepass),
    path("perfil/changeavatar/", agregarAvatar),

]