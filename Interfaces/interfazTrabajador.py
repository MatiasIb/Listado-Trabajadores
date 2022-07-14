from tkinter import *
import mysql.connector
from localStoragePy import localStoragePy
from tkinter import ttk
import os
import sys
localStorage = localStoragePy('PROYECTO, taller de desarrollo y software')

"""Funciones"""
def listarTrabajo():
    conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
    cursor1 = conexion1.cursor()
    sql = "SELECT * FROM trabajador WHERE usuario= %s and clave = %s"
    val = (localStorage.getItem("user"), localStorage.getItem("pass"))
    cursor1.execute(sql, val)   
    result = cursor1.fetchone()
    cursor1.close()
    conexion1.close()
    return result
    
trabajo = listarTrabajo() 

def datosLaborales():
    conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
    cursor1 = conexion1.cursor()
    sql = "select dl.cargo, ar.area ,dp.departamento, DATE_FORMAT(dl.fecha_ingreso, '%d-%m-%y') from ficha_trabajador ft INNER JOIN datos_laborales dl ON ft.datos_laborales_id_datos_laborales = dl.id_datos_laborales INNER JOIN departamentos dp ON ft.departamentos_id_departamentos = dp.id_departamentos INNER JOIN areas ar ON dl.areas_id_areas = ar.id_areas WHERE ft.trabajador_rut = %s"
    val = (localStorage.getItem("rut"))
    cursor1.execute(sql, (val,))   
    result = cursor1.fetchone()
    cursor1.close()
    conexion1.close()
    return result


"""Funciones"""

class modificarFicha():
    
    def __init__(self):
        datoslab = datosLaborales()
        interfaz = Toplevel()
        interfaz.title("consultar mis datos")
        w = interfaz.winfo_screenwidth()
        h = interfaz.winfo_screenheight()
        interfaz.geometry("%dx%d" % (w, h))
        destroy = interfaz.destroy

        """FUNCIONES"""

        user_nombres = StringVar()
        user_apellidos = StringVar()
        user_sexo = StringVar()
        user_direccion = StringVar()
        user_telefono = StringVar()

        def modificarFicha():
            conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
            cursor1 = conexion1.cursor()
            sql = "UPDATE trabajador SET nombres = %s, apellidos = %s, sexo = %s, direccion = %s, telefono = %s WHERE rut = %s"
            val = (user_nombres.get(), user_apellidos.get(), user_sexo.get(), user_direccion.get(), user_telefono.get(), localStorage.getItem("rut"))
            cursor1.execute(sql,val)
            conexion1.commit() 

            msg = Toplevel()
            msg.title("error")
            Label(msg, text="Se ha actualizado con exito, actualize para visualizar el cambio").grid(padx=5, row=0)
            Button(msg, text="aceptar", command=msg.destroy).grid(row=1)
            

        """FUNCIONES"""

        """TITULOS"""
        Label(interfaz, text="Modificar Ficha", font=("Roboto cn", 15)).place(relx=0.5, rely=0.05, anchor=N)

        Label(interfaz, text="RUT: ", font=("Roboto cn", 12)).place(relx=0.45, rely=0.15, anchor=CENTER)
        Label(interfaz, text="Nombres: ", font=("Roboto cn", 12)).place(relx=0.45, rely=0.20, anchor=CENTER)
        Label(interfaz, text="Apellidos: ", font=("Roboto cn", 12)).place(relx=0.45, rely=0.25, anchor=CENTER)
        Label(interfaz, text="Sexo: ", font=("Roboto cn", 12)).place(relx=0.45, rely=0.30, anchor=CENTER)
        Label(interfaz, text="Direccion: ", font=("Roboto cn", 12)).place(relx=0.45, rely=0.35, anchor=CENTER)
        Label(interfaz, text="Telefono: ", font=("Roboto cn", 12)).place(relx=0.45, rely=0.40, anchor=CENTER)
        Label(interfaz, text="Cargo: ", font=("Roboto cn", 12)).place(relx=0.45, rely=0.45, anchor=CENTER)
        Label(interfaz, text="Area: ", font=("Roboto cn", 12)).place(relx=0.45, rely=0.50, anchor=CENTER)
        Label(interfaz, text="Departamento: ", font=("Roboto cn", 12)).place(relx=0.45, rely=0.55, anchor=CENTER)
        Label(interfaz, text="Fecha de Ingreso: ", font=("Roboto cn", 12)).place(relx=0.45, rely=0.60, anchor=CENTER)
        """TITULOS"""
        """ENTRY"""
        rut = Label(interfaz, font=("Roboto cn", 12), text=trabajo[0]).place(relx=0.55, rely=0.15, anchor=CENTER)
        
        nombres = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_nombres)
        nombres.place(relx=0.57, rely=0.20, anchor=CENTER)
        nombres.insert(0, trabajo[1])

        apellidos = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_apellidos)
        apellidos.place(relx=0.57, rely=0.25, anchor=CENTER)
        apellidos.insert(0, trabajo[2])

        sexo = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_sexo)
        sexo.place(relx=0.57, rely=0.30, anchor=CENTER)
        sexo.insert(0,trabajo[3])

        direccion = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_direccion)
        direccion.place(relx=0.57, rely=0.35, anchor=CENTER)
        direccion.insert(0,trabajo[4])

        telefono = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_telefono)
        telefono.place(relx=0.57, rely=0.40, anchor=CENTER)
        telefono.insert(0,trabajo[5])

        Label(interfaz, font=("Roboto cn", 12), text=datoslab[0]).place(relx=0.55, rely=0.45, anchor=CENTER)

        Label(interfaz, font=("Roboto cn", 12), text=datoslab[1]).place(relx=0.55, rely=0.50, anchor=CENTER)

        Label(interfaz, font=("Roboto cn", 12), text=datoslab[2]).place(relx=0.55, rely=0.55, anchor=CENTER)

        Label(interfaz, font=("Roboto cn", 12), text=datoslab[3]).place(relx=0.55, rely=0.60, anchor=CENTER)

        Button(interfaz, text="Atras <--", font=("Roboto cn", 12), command=destroy).place(relx=0.30, rely=0.70, anchor=CENTER)
        Button(interfaz, text="Guardar", font=("Roboto cn", 12), command=modificarFicha).place(relx=0.70, rely=0.70, anchor=CENTER)
        interfaz.mainloop()

class modificarContactosEmergencia(): 
    def __init__(self):
        interfaz = Toplevel()
        interfaz.title("consultar mis datos")
        w = interfaz.winfo_screenwidth()
        h = interfaz.winfo_screenheight()
        interfaz.geometry("%dx%d" % (w, h))
        """Funciones"""
        def traerContactosEmergencia():
                conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
                cursor1 = conexion1.cursor()
                sql = "SELECT nombre, relacion_trabajador, telefono FROM contactos_emergencia WHERE trabajador_rut = %s"
                val = (localStorage.getItem("rut"))
                cursor1.execute(sql, (val,))   
                result = cursor1.fetchall()
                conexion1.close()
                return result

        cargas = traerContactosEmergencia()
        destroy = interfaz.destroy
        cargasFamiliares_frame = Frame(interfaz, width=700, height=700)
        cargasFamiliares_frame.place(relx=0.5, rely=0.3, anchor=CENTER)
        Label(interfaz, text="Contacto de Emergencia", font=("Roboto cn", 15)).place(relx=0.5, rely=0.03, anchor=N)
        Button(interfaz, text="Atras <--", font=("Roboto cn", 12), command=destroy).place(relx=0.30, rely=0.70, anchor=CENTER)
            
        """scroll"""
        cargasFamiliares_scroll = Scrollbar(cargasFamiliares_frame)
        cargasFamiliares_scroll.pack(side=RIGHT, fill=Y)

        cargasFamiliares_scroll = Scrollbar(cargasFamiliares_frame,orient='horizontal')
        cargasFamiliares_scroll.pack(side= BOTTOM,fill=X)

        cargasFamiliares = ttk.Treeview(cargasFamiliares_frame,yscrollcommand=cargasFamiliares_scroll.set, xscrollcommand =cargasFamiliares_scroll.set)

        cargasFamiliares.pack()

        cargasFamiliares_scroll.config(command=cargasFamiliares.yview)
        cargasFamiliares_scroll.config(command=cargasFamiliares.xview)

        """scroll"""
        cargasFamiliares['columns'] = ('nombre', 'relacion_trabajador', 'telefono')

        cargasFamiliares.column("#0", width=0,  stretch=NO)
        cargasFamiliares.column("nombre",anchor=CENTER, width=140)
        cargasFamiliares.column("relacion_trabajador", anchor=CENTER, width=140)
        cargasFamiliares.column("telefono",anchor=CENTER,width=140)



        cargasFamiliares.heading("#0",text="",anchor=CENTER)
        cargasFamiliares.heading("nombre",text="Nombre",anchor=CENTER)
        cargasFamiliares.heading("relacion_trabajador",text="Relacion",anchor=CENTER)
        cargasFamiliares.heading("telefono",text="Telefono",anchor=CENTER)


        id = 0
        for i in cargas:
            cargasFamiliares.insert(parent='',index='end',iid=id,text='',
            values=(i[0],i[1],i[2]))
            id +=1
        cargasFamiliares.pack()

        
        interfaz.mainloop()



class modificarCargasFamiliares():
    def __init__(self):
        interfaz = Toplevel()
        interfaz.title("consultar mis datos")
        w = interfaz.winfo_screenwidth()
        h = interfaz.winfo_screenheight()
        interfaz.geometry("%dx%d" % (w, h))

        """FUNCIONES"""
        def traerCargas():
            conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
            cursor1 = conexion1.cursor()
            sql = "SELECT rut_fam ,nombre_carga_familiar, parentesco, sexo FROM cargas_familiares WHERE trabajador_rut = %s"
            val = (localStorage.getItem("rut"))
            cursor1.execute(sql, (val,))   
            result = cursor1.fetchall()
            return result
        cargas = traerCargas()
        cargasFamiliares_frame = Frame(interfaz, width=700, height=700)
        cargasFamiliares_frame.place(relx=0.5, rely=0.3, anchor=CENTER)
        Label(interfaz, text="Cargas Familiares", font=("Roboto cn", 15)).place(relx=0.5, rely=0.03, anchor=N)

            
        """scroll"""
        cargasFamiliares_scroll = Scrollbar(cargasFamiliares_frame)
        cargasFamiliares_scroll.pack(side=RIGHT, fill=Y)

        cargasFamiliares_scroll = Scrollbar(cargasFamiliares_frame,orient='horizontal')
        cargasFamiliares_scroll.pack(side= BOTTOM,fill=X)

        cargasFamiliares = ttk.Treeview(cargasFamiliares_frame,yscrollcommand=cargasFamiliares_scroll.set, xscrollcommand =cargasFamiliares_scroll.set)

        cargasFamiliares.pack()

        cargasFamiliares_scroll.config(command=cargasFamiliares.yview)
        cargasFamiliares_scroll.config(command=cargasFamiliares.xview)

        """scroll"""
        cargasFamiliares['columns'] = ('rut_fam', 'nombre_cargas_familiar', 'parentesco', 'sexo')

        cargasFamiliares.column("#0", width=0,  stretch=NO)
        cargasFamiliares.column("rut_fam",anchor=CENTER, width=140)
        cargasFamiliares.column("nombre_cargas_familiar", anchor=CENTER, width=140)
        cargasFamiliares.column("parentesco",anchor=CENTER,width=140)
        cargasFamiliares.column("sexo",anchor=CENTER,width=140)


        cargasFamiliares.heading("#0",text="",anchor=CENTER)
        cargasFamiliares.heading("rut_fam",text="Rut",anchor=CENTER)
        cargasFamiliares.heading("nombre_cargas_familiar",text="Nombre",anchor=CENTER)
        cargasFamiliares.heading("parentesco",text="Parentesco",anchor=CENTER)
        cargasFamiliares.heading("sexo",text="Sexo",anchor=CENTER)


        id = 0
        for i in cargas:
            cargasFamiliares.insert(parent='',index='end',iid=id,text='',
            values=(i[0],i[1],i[2], i[3]))
            id +=1
        cargasFamiliares.pack()
        destroy = interfaz.destroy  
        Button(interfaz, text="Atras <--", font=("Roboto cn", 12), command=destroy).place(relx=0.30, rely=0.70, anchor=CENTER)
                 
        interfaz.mainloop()

 
        """FUNCIONES"""



class consultarDatos():
    def __init__(self):
        datoslab = datosLaborales()
        interfaz = Toplevel()
        interfaz.title("consultar mis datos")
        w = interfaz.winfo_screenwidth()
        h = interfaz.winfo_screenheight()
        interfaz.geometry("%dx%d" % (w, h))
        """FUNCIONES"""

        def destroy():
            interfaz.destroy()
        """FUNCIONES"""
        """TITULOS"""
        Label(interfaz, text="FICHA CONSULTADA", font=("Roboto cn", 15)).place(relx=0.5, rely=0.05, anchor=N)

        Label(interfaz, text="RUT: ", font=("Roboto cn", 12)).place(relx=0.45, rely=0.15, anchor=CENTER)
        Label(interfaz, text="Nombres: ", font=("Roboto cn", 12)).place(relx=0.45, rely=0.20, anchor=CENTER)
        Label(interfaz, text="Apellidos: ", font=("Roboto cn", 12)).place(relx=0.45, rely=0.25, anchor=CENTER)
        Label(interfaz, text="Sexo: ", font=("Roboto cn", 12)).place(relx=0.45, rely=0.30, anchor=CENTER)
        Label(interfaz, text="Direccion: ", font=("Roboto cn", 12)).place(relx=0.45, rely=0.35, anchor=CENTER)
        Label(interfaz, text="Telefono: ", font=("Roboto cn", 12)).place(relx=0.45, rely=0.40, anchor=CENTER)
        Label(interfaz, text="Cargo: ", font=("Roboto cn", 12)).place(relx=0.45, rely=0.45, anchor=CENTER)
        Label(interfaz, text="Area: ", font=("Roboto cn", 12)).place(relx=0.45, rely=0.50, anchor=CENTER)
        Label(interfaz, text="Departamento: ", font=("Roboto cn", 12)).place(relx=0.45, rely=0.55, anchor=CENTER)
        Label(interfaz, text="Fecha de Ingreso: ", font=("Roboto cn", 12)).place(relx=0.45, rely=0.60, anchor=CENTER)
        """TITULOS"""

        """DATOS"""
        Label(interfaz, text=trabajo[0], font=("Roboto cn", 12)).place(relx=0.55, rely=0.15, anchor=CENTER)
        Label(interfaz, text=trabajo[1], font=("Roboto cn", 12)).place(relx=0.55, rely=0.20, anchor=CENTER)
        Label(interfaz, text=trabajo[2], font=("Roboto cn", 12)).place(relx=0.55, rely=0.25, anchor=CENTER)
        Label(interfaz, text=trabajo[3], font=("Roboto cn", 12)).place(relx=0.55, rely=0.30, anchor=CENTER)
        Label(interfaz, text=trabajo[4], font=("Roboto cn", 12)).place(relx=0.55, rely=0.35, anchor=CENTER)
        Label(interfaz, text=trabajo[5], font=("Roboto cn", 12)).place(relx=0.55, rely=0.40, anchor=CENTER)
        Label(interfaz, text=datoslab[0], font=("Roboto cn", 12)).place(relx=0.55, rely=0.45, anchor=CENTER)
        Label(interfaz, text=datoslab[1], font=("Roboto cn", 12)).place(relx=0.55, rely=0.50, anchor=CENTER)
        Label(interfaz, text=datoslab[2], font=("Roboto cn", 12)).place(relx=0.55, rely=0.55, anchor=CENTER)
        Label(interfaz, text=datoslab[3], font=("Roboto cn", 12)).place(relx=0.55, rely=0.60, anchor=CENTER)

        Button(interfaz, text="Atras <--", font=("Roboto cn", 12), command=destroy).place(relx=0.30, rely=0.70, anchor=CENTER)
        Button(interfaz, text="Cargas Familiares", font=("Roboto cn", 12), command=modificarCargasFamiliares).place(relx=0.40, rely=0.70, anchor=CENTER)
        Button(interfaz, text="Contactos de Emergencia", font=("Roboto cn", 12), command=modificarContactosEmergencia).place(relx=0.55, rely=0.70, anchor=CENTER)

        """DATOS"""
        interfaz.mainloop()





class interfazTrabajador():

    def __init__(self):
        interfaz = Tk()
        interfaz.title('TRABAJADOR')
        w = interfaz.winfo_screenwidth()
        h = interfaz.winfo_screenheight()
        destroy = interfaz.destroy
        interfaz.geometry("%dx%d" % (w, h))
        img = PhotoImage(file="imagenes/logo.gif")
        img=img.subsample(2,2)
        Label(interfaz, text="Bienvenido usuario apellido", font=("Roboto cn", 15)).place(relx=0.1, rely=0.0, anchor=NW)
        Label(interfaz, image=img).place(relx=0.9, rely=0.05, anchor=NE)

        Button(interfaz, text="consultar mis datos", font=("Roboto cn", 20), command=consultarDatos).place(relx=0.5, rely=0.4, anchor=CENTER)
        Button(interfaz, text="modificar mis datos", font=("Roboto cn", 18), command=modificarFicha).place(relx=0.5, rely=0.5, anchor=CENTER)
        Button(interfaz, text="salir", font=("Roboto cn", 16), bg="red", command=destroy).place(relx=0.5, rely=0.6, anchor=CENTER)
        
        
        interfaz.mainloop()

