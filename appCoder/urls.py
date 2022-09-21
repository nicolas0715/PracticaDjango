from django.urls import path
from appCoder.view import *

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
]