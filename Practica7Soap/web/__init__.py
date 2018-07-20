#!/usr/bin/env python
import sys

from suds.client import Client

url = "http://localhost:7777/ws/AcademicoWebService?wsdl"
client = Client(url)
print "Lista de Estudiantes"
estudiantes=client.service.getAllEstudiante()
print estudiantes
"\n"

print"Asignatura especifica"
asignatura=client.service.getAsignatura("ISC-415").nombre
print asignatura +"\n"

print"Profesor especifico"
profesor=client.service.getProfesor("Mr Camacho").nombre
print profesor