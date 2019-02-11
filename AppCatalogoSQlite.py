#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from io import open
import pickle
import sqlite3 as lite
import sys

# Crea una clase Python para definir el interfaz de usuario de
# la aplicación. Cuando se cree un objeto del tipo 'Aplicacion'
# se ejecutará automáticamente el método __init__() qué 
# construye y muestra la ventana con todos sus widgets: 


class Pelicula:
    # Constructor de clase
    def __init__(self,identificador, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        self.id = identificador
        #print('Se ha creado la película:',self.titulo)
        
    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)


class Catalogo:
    
    # Constructor de clase
    def __init__(self):
        pass

    def query(self,sql):
        con = lite.connect('catalogo.db')
        with con:
            cur = con.cursor()    
            cur.execute(sql)
            return cur

    def catalogoSet(self,titulo,duracion,anio):
        self.query('INSERT INTO peliculas(Titulo,Duracion,anio) VALUES ("'+titulo+'","'+duracion+'","'+anio+'")')
        
    def catalogoGet(self,sql):
        row=self.query(sql).fetchall()
        return row

class Aplicacion():
    def __init__(self):
        catalogo=Catalogo()

        raiz = Tk()
        raiz.config(bg = 'beige')
        raiz.title('- Catalogo -')
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
            messagebox.showinfo("Pelicula",catalogo.catalogoGet("SELECT * FROM peliculas"))

        Button (miFrame,text = "Cargar",command=lambda:catalogo.catalogoSet(eNombre.get(),eDuracion.get(),eLanzamiento.get())).grid(row=4,column=0)
        Button (miFrame,text = "Mostrar",command=lambda:mostrar()).grid(row=4,column=1)
        raiz.mainloop()

Aplicacion()