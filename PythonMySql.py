import tkinter as tk


#Modulos de tkinter
from tkinter import *

from tkinter import ttk
from tkinter import messagebox


class formularioHerramientas:
    
 def formulario():
  try:
      
   base = Tk()
   base.geometry("1600x1200")
   base.title("Crud en Python")
   
   
   groupBox = LabelFrame(base,text="Datos de las herramientas",padx=5,pady=5)
   groupBox.grid(row=0,column=0,padx=10,pady=10)
   
   labelidherramienta=Label(groupBox,text="Codigo herramienta:",width=13,font=("arial",12)).grid(row=0,column=0)
   textboxidtool = Entry(groupBox)
   textboxidtool.grid(row=0,column=1)
   
   labelnombre=Label(groupBox,text="Nombre:",width=13,font=("arial",12)).grid(row=1,column=0)
   textboxnombre = Entry(groupBox)
   textboxnombre.grid(row=1,column=1)
   
   labelmarca=Label(groupBox,text="Marca:",width=13,font=("arial",12)).grid(row=2,column=0)
   textboxmarca = Entry(groupBox)
   textboxmarca.grid(row=2,column=1)
   
   labelcondicion=Label(groupBox,text="Estado:",width=13,font=("arial",12)).grid(row=3,column=0)
   textboxcondicion = Entry(groupBox)
   textboxcondicion.grid(row=3,column=1)
   
   Button(groupBox,text="Guardar",width=10).grid(row=4,column=0)
   Button(groupBox,text="Modificar",width=10).grid(row=4,column=1)
   Button(groupBox,text="Eliminar",width=10).grid(row=4,column=2)
   
   tablainventario = LabelFrame(base,text="Inventario Herramientas",padx=5,pady=5,)
   tablainventario.grid(row=0,column=1,padx=5,pady=5)
   
   tree = ttk.Treeview(tablainventario,columns=("Codigo Herramienta","Nombre","Marca","Estado","Codigo Almacen"),show="headings",height=5,)
   tree.column("# 1",anchor=CENTER)
   tree.heading("# 1",text="Codigo Herramienta")
   tree.column("# 2",anchor=CENTER)
   tree.heading("# 2",text="Nombre")
   tree.column("# 3",anchor=CENTER)
   tree.heading("# 3",text="Marca")
   tree.column("# 4",anchor=CENTER)
   tree.heading("# 4",text="Estado")
   tree.column("# 5",anchor=CENTER)
   tree.heading("# 5",text="Codigo Almacen")
  
   
   tree.pack()
   
   
   groupBox1 = LabelFrame(base,text="Datos de los Responsables",padx=5,pady=5)
   groupBox1.grid(row=1,column=0,padx=10,pady=10)
   
   labelcedula1=Label(groupBox1,text="Cedula:",width=13,font=("arial",12)).grid(row=0,column=0)
   textboxcedula1 = Entry(groupBox1)
   textboxcedula1.grid(row=0,column=1)
   
   labelnombre1=Label(groupBox1,text="Nombre:",width=13,font=("arial",12)).grid(row=1,column=0)
   textboxnombre1 = Entry(groupBox1)
   textboxnombre1.grid(row=1,column=1)
   
   labelapellido1=Label(groupBox1,text="Telefono",width=13,font=("arial",12)).grid(row=2,column=0)
   textboxapellido1 = Entry(groupBox1)
   textboxapellido1.grid(row=2,column=1)
   
   labelcontacto1=Label(groupBox1,text="Correo:",width=13,font=("arial",12)).grid(row=3,column=0)
   textboxcontacto1 = Entry(groupBox1)
   textboxcontacto1.grid(row=3,column=1)
   
   labelentrega1=Label(groupBox1,text="Fecha Entrega:",width=13,font=("arial",12)).grid(row=4,column=0)
   textboxentrega1 = Entry(groupBox1)
   textboxentrega1.grid(row=4,column=1)
   
   labeldevolucion1=Label(groupBox1,text="Fecha Devolucion:",width=13,font=("arial",12)).grid(row=5,column=0)
   textboxdevolucion1 = Entry(groupBox1)
   textboxdevolucion1.grid(row=5,column=1)
   
   
   Button(groupBox1,text="Guardar",width=10).grid(row=6,column=0)
   Button(groupBox1,text="Modificar",width=10).grid(row=6,column=1)
   Button(groupBox1,text="Eliminar",width=10).grid(row=6,column=2)
  
   tablainventario1 = LabelFrame(base,text="Inventario Herramientas",padx=5,pady=5,)
   tablainventario1.grid(row=1,column=1,padx=5,pady=5)
   
   tree = ttk.Treeview(tablainventario1,columns=("Cedula","Nombre","Telefono","Correo","Fecha Entrega","Fecha Devolucion","Codigo Almacen"),show="headings",height=5,)
   tree.column("# 1",anchor=CENTER)
   tree.heading("# 1",text="Cedula")
   tree.column("# 2",anchor=CENTER)
   tree.heading("# 2",text="Nombre")
   tree.column("# 3",anchor=CENTER)
   tree.heading("# 3",text="Telefono")
   tree.column("# 4",anchor=CENTER)
   tree.heading("# 4",text="Correo")
   tree.column("# 5",anchor=CENTER)
   tree.heading("# 5",text="Fecha Entrega")
   tree.column("# 6",anchor=CENTER)
   tree.heading("# 6",text="Fecha Devolucion")
   tree.column("# 7",anchor=CENTER)
   tree.heading("# 7",text="Codigo Herramienta")
   
   tree.pack()
  
   groupBox2 = LabelFrame(base,text="Datos de la ubicacion",padx=5,pady=5)
   groupBox2.grid(row=2,column=0,padx=10,pady=10)
   
   labelidubicacion2=Label(groupBox2,text="Codigo Almacen",width=13,font=("arial",12)).grid(row=0,column=0)
   textboxdevolucion1 = Entry(groupBox2)
   textboxdevolucion1.grid(row=0,column=1)
   
   labeldeposito2=Label(groupBox2,text="Sector:",width=13,font=("arial",12)).grid(row=2,column=0)
   selecciondeposito2 = tk.StringVar()
   combo= ttk.Combobox(groupBox2,values=["Patio","Cuarto"],textvariable=selecciondeposito2)
   combo.grid(row=2,column=1)
   selecciondeposito2.set("Cuarto")
  
   labelcontenedor2=Label(groupBox2,text="Contenedor:",width=13,font=("arial",12)).grid(row=1,column=0)
   seleccioncontenedor2 = tk.StringVar()
   combo= ttk.Combobox(groupBox2,values=["Caja Azul","Caja Roja"],textvariable=seleccioncontenedor2)
   combo.grid(row=1,column=1)
   seleccioncontenedor2.set("Caja Azul")
   
   Button(groupBox2,text="Guardar",width=10).grid(row=3,column=0)
   Button(groupBox2,text="Modificar",width=10).grid(row=3,column=1)
   Button(groupBox2,text="Eliminar",width=10).grid(row=3,column=2)
   
   tablainventario2 = LabelFrame(base,text="Inventario Herramientas",padx=5,pady=5,)
   tablainventario2.grid(row=2,column=1,padx=5,pady=5)
   
   tree = ttk.Treeview(tablainventario2,columns=("Codigo Almacen","Sector","Contenedor"),show="headings",height=5,)
   tree.column("# 1",anchor=SE)
   tree.heading("# 1",text="Codigo Almacen")
   tree.column("# 2",anchor=SE)
   tree.heading("# 2",text="Sector")
   tree.column("# 3",anchor=SE)
   tree.heading("# 3",text="Contenedor")
   
   tree.pack()
  
   
   
   
   
   
   
   
    
   
  
   base.mainloop()
           
  except ValueError as error:
   print("Error al mostrar la interfaz,error; {}".format(error)) 

 formulario()   