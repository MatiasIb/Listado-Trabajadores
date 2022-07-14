from tkinter import *
from tkinter import ttk
import mysql.connector
from localStoragePy import localStoragePy
from Interfaces.interfazJefeRRHH import interfazJefe
localStorage = localStoragePy('PROYECTO, taller de desarrollo y software')
from Interfaces.interfazTrabajador import interfazTrabajador
from Interfaces.interfazPersonalRRHH import interfazPersonalRRHH
from Interfaces.interfazAdministrador import interfazAdministrador

class Login():
    
    def __init__(self):
        login = Tk()
        login.title('LOGIN')
        usuario = StringVar()
        clave = StringVar()     
        width=350
        height=500
        screenwidth = login.winfo_screenwidth()
        screenheight = login.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        login.geometry(alignstr)
            #Imagen Logo
        image=PhotoImage(file="imagenes/logo.gif")
        image=image.subsample(2,2)
        Label(image=image).place(relx=0.5, rely=0.2, anchor=CENTER)

       
        Label(login, text = "Usuario:").place(relx=0.5, rely=0.45, anchor=CENTER)
        Label(login, text = "Clave:").place(relx=0.5, rely=0.55, anchor=CENTER)

        Entry(login, width=40, textvariable=usuario).place(relx=0.5, rely=0.5, anchor=CENTER)
        Entry(login, width=40, textvariable=clave, show="*").place(relx=0.5, rely=0.6, anchor=CENTER)
        
        """FUNCIONES"""
        def validarUsuario():
            conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
            cursor1 = conexion1.cursor()
            sql = "select tr.usuario, tr.clave, tr.rut, dl.cargo from trabajador tr INNER JOIN ficha_trabajador ft ON tr.rut = ft.trabajador_rut INNER JOIN datos_laborales dl ON ft.datos_laborales_id_datos_laborales = dl.id_datos_laborales WHERE usuario= %s and clave = %s;"
            val = (usuario.get(), clave.get())
            
            cursor1.execute(sql, val)   
            result = cursor1.fetchone()
            def destroy():
                login.destroy()
            if result:
                if result[3] == "Jefe RRHH":
                    localStorage.setItem("user", result[0])
                    localStorage.setItem("pass", result[1])
                    localStorage.setItem("rut", result[2])
                    localStorage.setItem("result", result[3])
                    login.destroy()
                    interfazJefe()
                if result[3] == "Personal RRHH":
                    localStorage.setItem("user", result[0])
                    localStorage.setItem("pass", result[1])
                    localStorage.setItem("rut", result[2])
                    localStorage.setItem("result", result[3])
                    destroy()
                    interfazPersonalRRHH()
                if result[3] == "Administrador":
                    localStorage.setItem("user", result[0])
                    localStorage.setItem("pass", result[1])
                    localStorage.setItem("rut", result[2])
                    localStorage.setItem("result", result[3])
                    destroy()
                    interfazAdministrador()
                else:
                    localStorage.setItem("user", result[0])
                    localStorage.setItem("pass", result[1])
                    localStorage.setItem("rut", result[2])
                    localStorage.setItem("result", result[3])
                    destroy()
                    interfazTrabajador()
            else:
                def pantalla(): 
                    error = Tk()
                    error.title("error")
                    Label(error, text="La clave o el usuario estan mal escritos, reintente nuevamente").grid(padx=5, row=0)
                    Button(error, text="aceptar", command=error.destroy).grid(row=1)
                pantalla()

        """FUNCIONES"""

        Button(login, text="Iniciar Sesion", width=40, command=validarUsuario).place(relx=0.5, rely=0.8, anchor=CENTER)
        
        login.mainloop()

Login()

