from tkinter import *
import mysql.connector
from localStoragePy import localStoragePy
localStorage = localStoragePy('PROYECTO, taller de desarrollo y software')
from  tkinter import ttk

class crearDepartamento():
     def __init__(self):
        interfaz = Toplevel()
        interfaz.title("Crear Departamento")
        w = interfaz.winfo_screenwidth()
        h = interfaz.winfo_screenheight()
        interfaz.geometry("%dx%d" % (w, h))
        Label(interfaz, text="Crear Departamento", font=("Roboto cn", 15)).place(relx=0.5, rely=0.03, anchor=N)
        destroy = interfaz.destroy

        """VARIABLES"""
        dep_nombre = StringVar()

        """VARIABLES"""
        """FUNCIONES"""

        def agregarDep():
            conexion2 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores") 
            cursor2 = conexion2.cursor()
            sql = "INSERT INTO departamentos (departamento) VALUES (%s)"
            val = (dep_nombre.get())
            print(dep_nombre.get())
            cursor2.execute(sql, (val,))
            conexion2.commit()
            conexion2.close()
            advertencia = Toplevel()
            advertencia.title("Advertencia")
            Label(advertencia, text="se ha creado con exito").grid(padx=5, row=0)
            Button(advertencia, text="aceptar", command=advertencia.destroy).grid(row=1)

        """DATOS DEL Departamento"""
        Label(interfaz, text="Nombre: ", font=("Roboto cn", 12)).place(relx=0.2, rely=0.25, anchor=CENTER)

        """"ENTRY Derpartamento"""

        nombre = Entry(interfaz, font=("Roboto cn", 12), textvariable=dep_nombre)
        nombre.place(relx=0.34, rely=0.25, anchor=CENTER)

        """"ENTRY TRABAJADOR"""

        Button(interfaz, text="Atras <--", font=("Roboto cn", 12), command=destroy).place(relx=0.30, rely=0.75, anchor=CENTER)
        Button(interfaz, text="Guardar", font=("Roboto cn", 12), command=agregarDep).place(relx=0.70, rely=0.75, anchor=CENTER)
        """Datos"""
        interfaz.mainloop()

class crearArea():
     def __init__(self):
        interfaz = Toplevel()
        interfaz.title("Crear Area")
        w = interfaz.winfo_screenwidth()
        h = interfaz.winfo_screenheight()
        interfaz.geometry("%dx%d" % (w, h))
        Label(interfaz, text="Crear Area", font=("Roboto cn", 15)).place(relx=0.5, rely=0.03, anchor=N)
        destroy = interfaz.destroy

        """VARIABLES"""
        area_nombre = StringVar()

        """VARIABLES"""
        """FUNCIONES"""

        def agregarArea():
        
            conexion2 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores") 
            cursor2 = conexion2.cursor()
            sql = "INSERT INTO areas (area) VALUES (%s)"
            val = (area_nombre.get())
            print(area_nombre.get())
            cursor2.execute(sql, (val,))
            conexion2.commit()
            conexion2.close()
            advertencia = Toplevel()
            advertencia.title("Advertencia")
            Label(advertencia, text="se ha creado con exito").grid(padx=5, row=0)
            Button(advertencia, text="aceptar", command=advertencia.destroy).grid(row=1)

        """DATOS DEL Area"""
        Label(interfaz, text="Nombre: ", font=("Roboto cn", 12)).place(relx=0.2, rely=0.25, anchor=CENTER)

        """"ENTRY Area"""

        nombre = Entry(interfaz, font=("Roboto cn", 12), textvariable=area_nombre)
        nombre.place(relx=0.34, rely=0.25, anchor=CENTER)

        """"ENTRY TRABAJADOR"""

        Button(interfaz, text="Atras <--", font=("Roboto cn", 12), command=destroy).place(relx=0.30, rely=0.75, anchor=CENTER)
        Button(interfaz, text="Guardar", font=("Roboto cn", 12), command=agregarArea).place(relx=0.70, rely=0.75, anchor=CENTER)
        """Datos"""
        interfaz.mainloop()



class crearJefeRRHH():
     def __init__(self):
        interfaz = Toplevel()
        interfaz.title("Crear Jefe RRHH")
        w = interfaz.winfo_screenwidth()
        h = interfaz.winfo_screenheight()
        interfaz.geometry("%dx%d" % (w, h))
        Label(interfaz, text="Crear Jefe RRHH", font=("Roboto cn", 15)).place(relx=0.5, rely=0.03, anchor=N)
        destroy = interfaz.destroy
        """VARIABLES"""
        user_rut = StringVar()
        user_nombres = StringVar()
        user_apellidos = StringVar()
        user_sexo = StringVar()
        user_direccion = StringVar()
        user_telefono = StringVar()
        user_cargo = StringVar()
        user_area = IntVar()
        user_departamento = IntVar()
        user_fechaIngreso = StringVar()
        user_usuario = StringVar()
        user_clave = StringVar()
        """FUNCIONES"""
        """"TEST"""

        def agregacargafamiliar():
            interfaz = Toplevel()
            interfaz.title("Asignar Carga Familiar")
            w = interfaz.winfo_screenwidth()
            h = interfaz.winfo_screenheight()
            interfaz.geometry("%dx%d" % (w, h))
            destroy = interfaz.destroy
            """VARIABLES CARGA EMERGENCIA"""

            user_rutfam = StringVar()
            user_nombrefam = StringVar()
            user_parentezco = StringVar()
            user_sexo = StringVar()
            
            """"ENTRY TRABAJADOR"""
            Label(interfaz, text="Agregar Carga Familiar", font=("Roboto cn", 15)).place(relx=0.5, rely=0.05, anchor=N)

            
            rutfam = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_rutfam)
            rutfam.place(relx=0.34, rely=0.20, anchor=CENTER)
            
            nombrefam = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_nombrefam)
            nombrefam.place(relx=0.34, rely=0.25, anchor=CENTER)
            
            parentezco = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_parentezco)
            parentezco.place(relx=0.34, rely=0.30, anchor=CENTER)

            sexo = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_sexo)
            sexo.place(relx=0.34, rely=0.35, anchor=CENTER)

            """DATOS DEL TRABAJADOR"""
            Label(interfaz, text="Rut: ", font=("Roboto cn", 12)).place(relx=0.2, rely=0.20, anchor=CENTER)
            Label(interfaz, text="Nombres: ", font=("Roboto cn", 12)).place(relx=0.2, rely=0.25, anchor=CENTER)
            Label(interfaz, text="Parentezco: ", font=("Roboto cn", 12)).place(relx=0.2, rely=0.30, anchor=CENTER)
            Label(interfaz, text="Sexo: ", font=("Roboto cn", 12)).place(relx=0.2, rely=0.35, anchor=CENTER)

            def agregarcargafam():
                #Carga Familiar
                conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
                cursor1 = conexion1.cursor()
                sql = "INSERT INTO cargas_familiares(rut_fam, nombre_carga_familiar, parentesco, sexo, trabajador_rut) VALUES ( %s, %s, %s, %s,  %s)"
                val = (user_rutfam.get(), user_nombrefam.get(), user_parentezco.get(), user_sexo.get(), user_rut.get())
                print(user_rut.get())
                cursor1.execute(sql,val)
                conexion1.commit()
                conexion1.close()
                advertencia = Toplevel()
                advertencia.title("Informacion")
                Label(advertencia, text="Se ha ingresado con exito").grid(padx=5, row=0)
                Button(advertencia, text="aceptar", command=advertencia.destroy).grid(row=1)


            """BOTONES ATRAS Y GUARDAR"""
            Button(interfaz, text="Atras <--", font=("Roboto cn", 12), command=destroy).place(relx=0.25, rely=0.75, anchor=CENTER)
            Button(interfaz, text="Guardar", font=("Roboto cn", 12), command=agregarcargafam).place(relx=0.70, rely=0.75, anchor=CENTER)
        
        def agregarcontactoemergencia():
            interfaz = Toplevel()
            interfaz.title("Asignar Carga Familiar")
            w = interfaz.winfo_screenwidth()
            h = interfaz.winfo_screenheight()
            interfaz.geometry("%dx%d" % (w, h))
            destroy = interfaz.destroy

            """VARIABLES Contacto EMERGENCIA"""
            user_nombreem = StringVar()
            user_relacion = StringVar()
            user_tel = StringVar()

            """"ENTRY TRABAJADOR"""
            Label(interfaz, text="Agregar Contacto Emergencia", font=("Roboto cn", 15)).place(relx=0.5, rely=0.05, anchor=N)

            nombreem = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_nombreem)
            nombreem.place(relx=0.34, rely=0.25, anchor=CENTER)
            
            relacionem = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_relacion)
            relacionem.place(relx=0.34, rely=0.30, anchor=CENTER)

            telefonoem = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_tel)
            telefonoem .place(relx=0.34, rely=0.35, anchor=CENTER)

            """DATOS DEL TRABAJADOR"""
            Label(interfaz, text="Nombres: ", font=("Roboto cn", 12)).place(relx=0.2, rely=0.25, anchor=CENTER)
            Label(interfaz, text="Relacion Trabajador: ", font=("Roboto cn", 12)).place(relx=0.2, rely=0.30, anchor=CENTER)
            Label(interfaz, text="Telefono: ", font=("Roboto cn", 12)).place(relx=0.2, rely=0.35, anchor=CENTER)


            def agregarcontactoem():
                #Contacto Emergencia
                conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
                cursor1 = conexion1.cursor()
                sql = "INSERT INTO contactos_emergencia(nombre, relacion_trabajador, telefono, trabajador_rut) VALUES ( %s, %s, %s, %s)"
                val = (user_nombreem.get(), user_relacion.get(), user_tel.get(), user_rut.get())
                cursor1.execute(sql,val)
                conexion1.commit()
                conexion1.close()
                advertencia = Toplevel()
                advertencia.title("Informacion")
                Label(advertencia, text="Se ha ingresado con exito").grid(padx=5, row=0)
                Button(advertencia, text="aceptar", command=advertencia.destroy).grid(row=1)


            """BOTONES ATRAS Y GUARDAR"""
            Button(interfaz, text="Atras <--", font=("Roboto cn", 12), command=destroy).place(relx=0.25, rely=0.75, anchor=CENTER)
            Button(interfaz, text="Guardar", font=("Roboto cn", 12), command=agregarcontactoem).place(relx=0.70, rely=0.75, anchor=CENTER)


        def traerArea():
            conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores") 
            cursor1 = conexion1.cursor()
            sql = "SELECT area from areas"
            cursor1.execute(sql)
            area = cursor1.fetchall()
            my_list = [r for r, in area] 
            conexion1.close()
            return my_list

        datoArea = traerArea()

        def traerDepartamento():
            conexion5 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
            cursor5 = conexion5.cursor()
            sql = "SELECT departamento from departamentos"
            cursor5.execute(sql)
            departamento = cursor5.fetchall()
            my_list2 = [r for r, in departamento]
            conexion5.close()
            return my_list2
        
        datoDepartamento = traerDepartamento()

        #Agregar datos de trabajador
        
        def agregarTrabajador():
            #Trabajador
            conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
            cursor1 = conexion1.cursor()
            sql = "INSERT INTO trabajador(rut, nombres, apellidos, sexo, direccion, telefono, usuario, clave) VALUES ( %s, %s, %s, %s,  %s,  %s,  %s, %s)"
            val = (user_rut.get(),user_nombres.get(), user_apellidos.get(), user_sexo.get(), user_direccion.get(), user_telefono.get(), user_usuario.get(), user_clave.get())
            cursor1.execute(sql,val)
            conexion1.commit()
            conexion1.close()
            #Datos Laborales

            #Traer id area
            conexion7 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
            cursor7 = conexion7.cursor()
            sql = "SELECT id_areas, area FROM areas WHERE area = %s;"
            val = (options.get())
            cursor7.execute(sql,(val,))
            traerId = cursor7.fetchone()
            id_Area = traerId[0]
            conexion7.close()

            conexion8 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
            cursor8 = conexion8.cursor()
            sql = "SELECT id_departamentos FROM departamentos WHERE departamento = %s;"
            val = (options1.get())
            cursor8.execute(sql,(val,))
            traer_id_departamento = cursor8.fetchone()
            id_departamento = traer_id_departamento[0]
            conexion8.close()

            #Validar Datos Laborales
            conexion4 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
            cursor4 = conexion4.cursor()
            sql = "SELECT `AUTO_INCREMENT` FROM  INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'listadotrabajadores' AND   TABLE_NAME   = 'datos_laborales';"
            cursor4.execute(sql)   
            result = cursor4.fetchone()
            id_datos_laborales = result[0]
            cursor4.close()



            conexion3 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores") 
            cursor3 = conexion3.cursor()
            sql = "INSERT INTO datos_laborales (cargo, fecha_ingreso, areas_id_areas) VALUES (%s, %s , %s)"
            val = (user_cargo.get(), user_fechaIngreso.get(), id_Area)
            cursor3.execute(sql, val)
            conexion3.commit()
            conexion3.close()

            
            #Ficha Trabajador
            conexion6 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores") 
            cursor6 = conexion6.cursor()
            sql = "INSERT INTO ficha_trabajador (departamentos_id_departamentos, datos_laborales_id_datos_laborales, trabajador_rut) VALUES (%s, %s , %s)"
            val = (id_departamento, id_datos_laborales, user_rut.get() )
            cursor6.execute(sql, val)
            conexion6.commit()
            conexion6.close()

            advertencia = Toplevel()
            advertencia.title("Informacion")
            Label(advertencia, text="Se ha ingresado con exito").grid(padx=5, row=0)
            Button(advertencia, text="aceptar", command=advertencia.destroy).grid(row=1)

        """DATOS DEL TRABAJADOR"""
        Label(interfaz, text="RUT: ", font=("Roboto cn", 12)).place(relx=0.2, rely=0.20, anchor=CENTER)
        Label(interfaz, text="Nombres: ", font=("Roboto cn", 12)).place(relx=0.2, rely=0.25, anchor=CENTER)
        Label(interfaz, text="Apellidos: ", font=("Roboto cn", 12)).place(relx=0.2, rely=0.30, anchor=CENTER)
        Label(interfaz, text="Sexo: ", font=("Roboto cn", 12)).place(relx=0.2, rely=0.35, anchor=CENTER)
        Label(interfaz, text="Direccion: ", font=("Roboto cn", 12)).place(relx=0.2, rely=0.40, anchor=CENTER)
        Label(interfaz, text="Telefono: ", font=("Roboto cn", 12)).place(relx=0.2, rely=0.45, anchor=CENTER)
        Label(interfaz, text="Cargo: ", font=("Roboto cn", 12)).place(relx=0.2, rely=0.50, anchor=CENTER)
        Label(interfaz, text="Area: ", font=("Roboto cn", 12)).place(relx=0.2, rely=0.55, anchor=CENTER)
        Label(interfaz, text="Departamento: ", font=("Roboto cn", 12)).place(relx=0.2, rely=0.60, anchor=CENTER)
        Label(interfaz, text="Fecha Ingreso: ", font=("Roboto cn", 12)).place(relx=0.5, rely=0.20, anchor=CENTER)
        Label(interfaz, text="Usuario: ", font=("Roboto cn", 12)).place(relx=0.5, rely=0.25, anchor=CENTER)
        Label(interfaz, text="Clave: ", font=("Roboto cn", 12)).place(relx=0.5, rely=0.30, anchor=CENTER)
        Label(interfaz, text="Recuerde guardar antes de salir", font=("Roboto cn", 12)).place(relx=0.5, rely=0.70, anchor=CENTER)


        """DATOS DEL TRABAJADOR"""

        """"ENTRY TRABAJADOR"""
        rut = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_rut)
        rut.place(relx=0.34, rely=0.20, anchor=CENTER)

        
        nombres = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_nombres)
        nombres.place(relx=0.34, rely=0.25, anchor=CENTER)
   

        apellidos = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_apellidos)
        apellidos.place(relx=0.34, rely=0.30, anchor=CENTER)


        sexo = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_sexo)
        sexo.place(relx=0.34, rely=0.35, anchor=CENTER)


        direccion = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_direccion)
        direccion.place(relx=0.34, rely=0.40, anchor=CENTER)


        telefono = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_telefono)
        telefono.place(relx=0.34, rely=0.45, anchor=CENTER)


        cargo = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_cargo)
        cargo.place(relx=0.34, rely=0.50, anchor=CENTER)

     

        #Menu Desplegable Area
        options = StringVar(interfaz)
        options.set(datoArea[0]) # default value
        area = OptionMenu(interfaz, options, *datoArea)
        area.config(width=16, font=('Helvetica', 12))
        area.place(relx=0.34, rely=0.55, anchor=CENTER)

        #Menu Desplegable Departamento
        options1 = StringVar(interfaz)
        options1.set(datoDepartamento[0]) # default value
        departamento = OptionMenu(interfaz, options1, *datoDepartamento)
        departamento.config(width=16, font=('Helvetica', 12))
        departamento.place(relx=0.34, rely=0.60, anchor=CENTER)


        fecha_ingreso = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_fechaIngreso)
        fecha_ingreso.place(relx=0.65, rely=0.20, anchor=CENTER)


        usuario = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_usuario)
        usuario.place(relx=0.65, rely=0.25, anchor=CENTER)


        clave = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_clave)
        clave.place(relx=0.65, rely=0.30, anchor=CENTER)

        """"ENTRY TRABAJADOR"""

        Button(interfaz, text="Atras <--", font=("Roboto cn", 12), command=destroy).place(relx=0.25, rely=0.75, anchor=CENTER)
        Button(interfaz, text="Guardar", font=("Roboto cn", 12), command=agregarTrabajador).place(relx=0.70, rely=0.75, anchor=CENTER)
        """
        Button(interfaz, text="Ingresar Cargas Familiar", font=("Roboto cn", 12), command=agregacargafamiliar).place(relx=0.60, rely=0.75, anchor=CENTER)
        Button(interfaz, text="Ingresar Contacto Emergencia", font=("Roboto cn", 12), command=agregarcontactoemergencia).place(relx=0.45, rely=0.75, anchor=CENTER)
        """
        """Datos Nomina Sueldo"""
        interfaz.mainloop()

#Interfaz Administrador
class interfazAdministrador():
    def __init__(self):
        interfaz = Tk()
        interfaz.title('INTERFAZ Administrador')
        w = interfaz.winfo_screenwidth()
        h = interfaz.winfo_screenheight()
        interfaz.geometry("%dx%d" % (w, h))
        Label(interfaz, text="Bienvenido [Nombre] [Apellido]")
        img = PhotoImage(file="imagenes/logo.gif")
        img=img.subsample(2,2)
        Label(interfaz, text="Bienvenido usuario apellido", font=("Roboto cn", 15)).place(relx=0.1, rely=0.05, anchor=NW)
        Label(interfaz, image=img).place(relx=0.9, rely=0.0, anchor=NE)
        def destroy():
            interfaz.destroy()
        
        Button(interfaz, text="Crear Departamento", font=("Roboto cn", 20), command=crearDepartamento).place(relx=0.5, rely=0.3, anchor=CENTER)
        Button(interfaz, text="Crear Area", font=("Roboto cn", 20), command=crearArea).place(relx=0.5, rely=0.4, anchor=CENTER)
        Button(interfaz, text="Crear Cuentas Jefes RRHH", font=("Roboto cn", 20), command=crearJefeRRHH).place(relx=0.5, rely=0.2, anchor=CENTER)

        
        Button(interfaz, text="Salir", font=("Roboto cn", 20), command=destroy).place(relx=0.5, rely=0.8, anchor=CENTER)

        interfaz.mainloop()
