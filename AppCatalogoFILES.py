#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from io import open
import pickle

# Crea una clase Python para definir el interfaz de usuario de
# la aplicación. Cuando se cree un objeto del tipo 'Aplicacion'
# se ejecutará automáticamente el método __init__() qué 
# construye y muestra la ventana con todos sus widgets: 


class Pelicula:
    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        #print('Se ha creado la película:',self.titulo)
        
    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)


class Catalogo:
    
    peliculas = []
    
    # Constructor de clase
    def __init__(self):
        self.cargar()
        
    def agregar(self,p):
        self.peliculas.append(p)
        self.guardar() #Guardado automatico
        
    def mostrar(self):
        #print("Se muestran entraste")
        return self.peliculas
        
    def cargar(self):
        fichero = open('catalogo.pckl','ab+')
        fichero.seek(0)
        try:
            self.peliculas = pickle.load(fichero)
        except:
            #print("El fichero esta vacio")
            pass
        finally:
            fichero.close()
            del(fichero)
            #print("Se han cargado {} peliculas".format(len(self.peliculas)))
    
    def guardar(self):
        fichero = open('catalogo.pckl','wb')
        pickle.dump(self.peliculas,fichero)
        fichero.close()
        del(fichero)

    #Destructor de clase
    def __del__(self):
        self.guardar() #Guardado automatico

class Aplicacion():
    def __init__(self):
        catalogo=Catalogo()

        raiz = Tk()
        raiz.config(bg = 'beige')
        raiz.title('------- Catalogo -------')
        miFrame=Frame(raiz)
        miFrame.pack()
    
        Label(miFrame, text = "Nombre Pelicula:").grid(row=1,column=0)
        eNombre = Entry(miFrame)
        eNombre.grid(row=1,column=1)

        Label(miFrame, text = "Duracion:").grid(row=2,column=0)
        eDuracion = Entry(miFrame)
        eDuracion.grid(row=2,column=1)

        Label(miFrame, text = "Lanzamiento:").grid(row=3,column=0)
        eLanzamiento = Entry(miFrame)
        eLanzamiento.grid(row=3,column=1)
        def mostrar():
            messagebox.showinfo("Pelicula",catalogo.mostrar()[0])
            
        Button (miFrame,text = "Cargar",command=lambda:catalogo.agregar( Pelicula(eNombre.get(),eDuracion.get(),eLanzamiento.get()) )).grid(row=4,column=0)
        Button (miFrame,text = "Mostrar",command=lambda:mostrar()).grid(row=4,column=1)
        raiz.mainloop()

Aplicacion()