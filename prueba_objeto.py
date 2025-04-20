#!/usr/bin/env python3

#crear un calculador de promedios usando objetos

class Estudiente:
    def __init__(self, nombre, grado, nota=0):

        self.nombre = nombre
        self.grado = grado
        self.nota = nota
    
    def recuperacion(self, nota):
        self.nota += nota #para este ejercicio no es necesario usar +=

        if nota < 10:
            return f"\n[+] [{self.nombre}] no paso el examen final porque no cumple con la nota minia y su nota final fue: {nota}"
    
        return f"\n[+] [{self.nombre}] su nota final es: {nota} es mayor al promedio y pasa el examen"
ian = Estudiente("ian", "5to", 0)

print(ian.recuperacion(1))


