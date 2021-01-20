
# -------------- Proyecto CRUD. Programacion 3. ING Informatica -------------------- 
# ------ Alumnos: Gabriel Boada. C.I:27904987 y Fairuth Zamora. C.I:27904628 -------

from tkinter import *
from tkinter import messagebox
import sqlite3

# ---------------------- Funciones -------------------------------

def conexionBBDD():

	miConexion=sqlite3.connect("Estudiantes")

	miCursor=miConexion.cursor()

	miCursor.execute('''
		CREATE TABLE DATOSESTUDIANTES (
		CEDULA INTEGER PRIMARY KEY ,
		NOMBRE_ESTUDIANTE VARCHAR(50) ,
		APELLIDO VARCHAR(50) ,
		CARRERA VARCHAR(50) ,
		TELEFONO VARCHAR(30) ,
		CORREO VARCHAR(50))		
		''')

	messagebox.showinfo("BBDD" , "Base de datos creada exitosamente")

def salirAplicacion():

	valor=messagebox.askquestion("Salir" , "¿Desea salir de la aplicacion?")

	if valor=="yes":
		root.destroy()

def crear():
	miConexion=sqlite3.connect("Estudiantes")

	miCursor=miConexion.cursor()

	miCursor.execute("INSERT INTO DATOSESTUDIANTES VALUES('" + miId.get() +
		"','" + miNombre.get() +
		"','" + miApellido.get() +
		"','" + miCarrera.get() +
		"','" + miTelefono.get() +
		"','" + miCorreo.get() + "')")

	miConexion.commit()

	messagebox.showinfo("BBDD" , "Registro insertado exitosamente")

def leer():

	miConexion=sqlite3.connect("Estudiantes")

	miCursor=miConexion.cursor()

	miCursor.execute("SELECT * FROM DATOSESTUDIANTES WHERE Cedula=" + miId.get())

	elEstudiante=miCursor.fetchall()

	for Estudiante in elEstudiante:

		miId.set(Estudiante[0])
		miNombre.set(Estudiante[1])
		miApellido.set(Estudiante[2])
		miCarrera.set(Estudiante[3])
		miTelefono.set(Estudiante[4])
		miCorreo.set(Estudiante[5])

	miConexion.commit()

def actualizar():

	miConexion=sqlite3.connect("Estudiantes")

	miCursor=miConexion.cursor()

	miCursor.execute("UPDATE DATOSESTUDIANTES SET NOMBRE_ESTUDIANTE='" + miNombre.get() +
	"', Apellido='" + miApellido.get() +
	"', Carrera='" + miCarrera.get() +
	"', Telefono='" + miTelefono.get() +
	"', Correo='" + miCorreo.get() +
	"' WHERE Cedula=" + miId.get())
	
	miConexion.commit()

	messagebox.showinfo("BBDD" , "Registro actualizado exitosamente")

def eliminar():

	miConexion=sqlite3.connect("Estudiantes")

	miCursor=miConexion.cursor()

	miCursor.execute("DELETE FROM DATOSESTUDIANTES WHERE CEDULA=" + miId.get())

	miConexion.commit()

	messagebox.showinfo("BBDD" , "Registro borrado exitosamente")


root=Tk()

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="conectar", command=conexionBBDD)
bbddMenu.add_command(label="salir", command=salirAplicacion)

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)

# ----------------------- Campos ---------------------------------

miFrame=Frame(root)
miFrame.pack()

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miCarrera=StringVar()
miTelefono=StringVar()
miCorreo=StringVar()


cuadroID=Entry(miFrame, textvariable=miId)
cuadroID.grid(row=0 , column=1 , padx=10 , pady=10)

cuadroNombre=Entry(miFrame, textvariable=miNombre)
cuadroNombre.grid(row=1 , column=1 , padx=10 , pady=10)

cuadroApellido=Entry(miFrame, textvariable=miApellido)
cuadroApellido.grid(row=2 , column=1 , padx=10 , pady=10)

cuadroCarrera=Entry(miFrame, textvariable=miCarrera)
cuadroCarrera.grid(row=3 , column=1 , padx=10 , pady=10)

cuadroTelefono=Entry(miFrame, textvariable=miTelefono)
cuadroTelefono.grid(row=4 , column=1 , padx=10 , pady=10)

cuadroCorreo=Entry(miFrame, textvariable=miCorreo)
cuadroCorreo.grid(row=5 , column=1 , padx=10 , pady=10)

# ----------------------- Etiquetas ---------------------------------

idLabel=Label(miFrame, text="Cedula:")
idLabel.grid(row=0 , column=0 , sticky="e" , padx=10 , pady=10)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1 , column=0 , sticky="e" , padx=10 , pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2 , column=0 , sticky="e" , padx=10 , pady=10)

carreraLabel=Label(miFrame, text="Carrera:")
carreraLabel.grid(row=3 , column=0 , sticky="e" , padx=10 , pady=10)

telefonoLabel=Label(miFrame, text="Telefono:")
telefonoLabel.grid(row=4 , column=0 , sticky="e" , padx=10 , pady=10)

correoLabel=Label(miFrame, text="Correo:")
correoLabel.grid(row=5 , column=0 , sticky="e" , padx=10 , pady=10)

# ------------------------- Botones ---------------------------------

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="Crear", command=crear)
botonCrear.grid(row=1 , column=0 , sticky="e" , padx=10 , pady=10)

botonLeer=Button(miFrame2, text="Leer", command=leer)
botonLeer.grid(row=1 , column=1 , sticky="e" , padx=10 , pady=10)

botonActualizar=Button(miFrame2, text="Actualizar", command=actualizar)
botonActualizar.grid(row=1 , column=2 , sticky="e" , padx=10 , pady=10)

botonBorrar=Button(miFrame2, text="Borrar", command=eliminar)
botonBorrar.grid(row=1 , column=3 , sticky="e" , padx=10 , pady=10)


root.mainloop()
