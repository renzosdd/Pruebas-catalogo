#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as lite
import sys

class Catalogo:    
    def __init__(self):
        pass

    #Metodo para ejecutar sentencia SQL
    def query(self,sql):
        con = lite.connect('catalogo.db')
        with con:
            cur = con.cursor()    
            cur.execute(sql)
            return cur

    #Metodo para insertar un nuevo registro a la base.
    def catalogoSet(self,titulo,duracion,anio):
        self.query('INSERT INTO peliculas(Titulo,Duracion,anio) VALUES ("'+titulo+'","'+duracion+'","'+anio+'")')
        
    #Metodo para obtener datos de la base
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