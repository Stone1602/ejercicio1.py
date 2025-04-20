#!/usr/bin/env python3

class Persona:
    def __init__(self, nombre, edad):

        self.nombre = nombre
        self.edad = edad

    def saludo(self):

        return f"hola, soy {self.nombre} y tengo {self.edad} años"

ian = Persona("ian", 24)
danna = Persona("danna", 22)
print(ian.saludo())
print(danna.saludo())
