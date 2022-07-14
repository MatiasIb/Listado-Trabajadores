from tkinter import *
import mysql.connector
from localStoragePy import localStoragePy
localStorage = localStoragePy('PROYECTO, taller de desarrollo y software')
from  tkinter import ttk

class modificarTrabajadores():
     
     def __init__(self):    
        """Funciones"""

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

        def listarTrabajadores():
            conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
            cursor1 = conexion1.cursor()
            sql = "select * from trabajador"
            cursor1.execute(sql)   
            result = cursor1.fetchall()
            cursor1.close()
            conexion1.close()
            return result

        def listarTrabajador():
            conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
            cursor1 = conexion1.cursor()
            sql = "select * from trabajador where rut = %s"
            val = (rutn.get())
            cursor1.execute(sql, (val,))   
            result = cursor1.fetchone()
            cursor1.close()
            conexion1.close()
            return result

        def datosLaborales():
            conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
            cursor1 = conexion1.cursor()
            sql = "select dl.cargo, ar.area ,dp.departamento, DATE_FORMAT(dl.fecha_ingreso, '%d-%m-%y') from ficha_trabajador ft INNER JOIN datos_laborales dl ON ft.datos_laborales_id_datos_laborales = dl.id_datos_laborales INNER JOIN departamentos dp ON ft.departamentos_id_departamentos = dp.id_departamentos INNER JOIN areas ar ON dl.areas_id_areas = ar.id_areas WHERE ft.trabajador_rut = %s"
            val = (rutn.get())
            cursor1.execute(sql, (val,))   
            result = cursor1.fetchone()
            cursor1.close()
            conexion1.close()
            return result
        """Funciones"""
        def ventanaModificarPorRut():
            if  rutn.get() == "admin":
                advertencia = Toplevel()
                advertencia.title("Advertencia")
                Label(advertencia, text="No tiene los privilegios para modificar un administrador").grid(padx=5, row=0)
                Button(advertencia, text="aceptar", command=advertencia.destroy).grid(row=1)
            else:
                trabajo = listarTrabajador()
                datoslab = datosLaborales()
                interfaz = Toplevel()
                interfaz.title("consultar mis datos")
                w = interfaz.winfo_screenwidth()
                h = interfaz.winfo_screenheight()
                interfaz.geometry("%dx%d" % (w, h))
                destroy = interfaz.destroy

                """FUNCIONES"""

                user_rut = StringVar()
                user_nombres = StringVar()
                user_apellidos = StringVar()
                user_sexo = StringVar()
                user_direccion = StringVar()
                user_telefono = StringVar()
                user_cargo = StringVar()
                user_fechaIngreso = StringVar()

                def modificarFicha():
                    if  rutn.get() == "admin":
                        advertencia = Toplevel()
                        advertencia.title("Advertencia")
                        Label(advertencia, text="No tiene los privilegios para modificar un administrador").grid(padx=5, row=0)
                        Button(advertencia, text="aceptar", command=advertencia.destroy).grid(row=1)
                    else:
                        conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
                        cursor1 = conexion1.cursor()
                        sql = "UPDATE trabajador SET nombres = %s, apellidos = %s, sexo = %s, direccion = %s, telefono = %s WHERE rut = %s"
                        val = (user_nombres.get(), user_apellidos.get(), user_sexo.get(), user_direccion.get(), user_telefono.get(), rutn.get())
                        cursor1.execute(sql,val)
                        conexion1.commit()

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

                        conexion2 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
                        cursor2 = conexion2.cursor()
                        sql = "UPDATE ficha_trabajador SET departamentos_id_departamentos = %s WHERE trabajador_rut = %s"
                        val = (id_departamento, rutn.get())
                        cursor2.execute(sql,val)
                        conexion2.commit()

                        conexion3 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
                        cursor3 = conexion3.cursor()
                        sql = "SELECT datos_laborales_id_datos_laborales FROM ficha_trabajador WHERE trabajador_rut = %s"
                        val = (rutn.get())
                        cursor3.execute(sql,(val,))
                        id_datos_laborales = cursor3.fetchone()
                        conexion3.commit()

                        conexion4 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
                        cursor4 = conexion4.cursor()
                        sql = "UPDATE datos_laborales SET cargo = %s, fecha_ingreso = %s, areas_id_areas = %s WHERE id_datos_laborales = %s"
                        val = (user_cargo.get(), user_fechaIngreso.get(), id_Area, id_datos_laborales[0] )
                        cursor4.execute(sql,val)
                        conexion4.commit()

                        

                        msg = Toplevel()
                        msg.title("Informacion")
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
                rut = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_rut)
                rut.place(relx=0.62, rely=0.15, anchor=CENTER)
                rut.insert(0, trabajo[0])

                nombres = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_nombres)
                nombres.place(relx=0.62, rely=0.20, anchor=CENTER)
                nombres.insert(0, trabajo[1])

                apellidos = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_apellidos)
                apellidos.place(relx=0.62, rely=0.25, anchor=CENTER)
                apellidos.insert(0, trabajo[2])

                sexo = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_sexo)
                sexo.place(relx=0.62, rely=0.30, anchor=CENTER)
                sexo.insert(0,trabajo[3])

                direccion = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_direccion)
                direccion.place(relx=0.62, rely=0.35, anchor=CENTER)
                direccion.insert(0,trabajo[4])

                telefono = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_telefono)
                telefono.place(relx=0.62, rely=0.40, anchor=CENTER)
                telefono.insert(0,trabajo[5])

                cargo = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_cargo)
                cargo.place(relx=0.62, rely=0.45, anchor=CENTER)
                cargo.insert(0, datoslab[0])

                #Menu Desplegable Area
                options = StringVar(interfaz)
                options.set(datoArea[1]) # default value
                area = OptionMenu(interfaz, options, *datoArea)
                area.config(width=16, font=('Helvetica', 12))
                area.place(relx=0.62, rely=0.50, anchor=CENTER)

                #Menu Desplegable Departamento
                options1 = StringVar(interfaz)
                options1.set(datoDepartamento[1]) # default value
                departamento = OptionMenu(interfaz, options1, *datoDepartamento)
                departamento.config(width=16, font=('Helvetica', 12))
                departamento.place(relx=0.62, rely=0.55, anchor=CENTER)

                fechaIngreso = Entry(interfaz, font=("Roboto cn", 12), textvariable=user_fechaIngreso)
                fechaIngreso.place(relx=0.62, rely=0.60, anchor=CENTER)
                fechaIngreso.insert(0, datoslab[3])

                Button(interfaz, text="Atras <--", font=("Roboto cn", 12), command=destroy).place(relx=0.30, rely=0.70, anchor=CENTER)
                Button(interfaz, text="Guardar", font=("Roboto cn", 12), command=modificarFicha).place(relx=0.70, rely=0.70, anchor=CENTER)
                interfaz.mainloop()

        trabajadores = listarTrabajadores()
        interfaz  = Tk()
        interfaz.title('Consultar Trabajadores')
        w = interfaz.winfo_screenwidth()
        h = interfaz.winfo_screenheight()
        interfaz.geometry("%dx%d" % (w, h))
        
        
        Label(interfaz, text="Trabajadores", font=("Roboto cn", 15)).place(relx=0.5, rely=0.05, anchor=N)

        """Apartado de trabajadores"""
        table_frame = Frame(interfaz, width=700, height=700)
        table_frame.place(relx=0.27, rely=0.4, anchor=CENTER)


        """scroll"""
        tabla_scroll = Scrollbar(table_frame)
        tabla_scroll.pack(side=RIGHT, fill=Y)

        tabla_scroll = Scrollbar(table_frame,orient='horizontal')
        tabla_scroll.pack(side= BOTTOM,fill=X)

        tabla = ttk.Treeview(table_frame,yscrollcommand=tabla_scroll.set, xscrollcommand =tabla_scroll.set)

        tabla.pack()

        tabla_scroll.config(command=tabla.yview)
        tabla_scroll.config(command=tabla.xview)

        """scroll"""
        tabla['columns'] = ('rut', 'nombres', 'apellidos', 'sexo', 'direccion', 'telefono')

        tabla.column("#0", width=0,  stretch=NO)
        tabla.column("rut",anchor=CENTER, width=120)
        tabla.column("nombres", anchor=CENTER, width=120)
        tabla.column("apellidos",anchor=CENTER,width=120)
        tabla.column("sexo",anchor=CENTER,width=120)
        tabla.column("direccion",anchor=CENTER,width=120)
        tabla.column("telefono",anchor=CENTER,width=120)

        tabla.heading("#0",text="",anchor=CENTER)
        tabla.heading("rut",text="RUT",anchor=CENTER)
        tabla.heading("nombres",text="Nombres",anchor=CENTER)
        tabla.heading("apellidos",text="Apellidos",anchor=CENTER)
        tabla.heading("sexo",text="Sexo",anchor=CENTER)
        tabla.heading("direccion",text="Direccion",anchor=CENTER)
        tabla.heading("telefono",text="Telefono",anchor=CENTER)

        id = 0
        for i in trabajadores:
            tabla.insert(parent='',index='end',iid=id,text='',
            values=(i[0],i[1],i[2],i[3],i[4], i[5]))
            id +=1
        tabla.pack()
        """Apartado de trabajadores"""
        Label(interfaz, text="Ingrese el rut aqui: ").place(relx=0.66, rely=0.26)
        rutn = Entry(interfaz, width=40)
        rutn.pack()
        rutn.place(relx=0.70, rely=0.30, anchor=CENTER)

        Button(interfaz, text="Atras <--", font=("Roboto cn", 12), command=interfaz.destroy).place(relx=0.30, rely=0.70, anchor=CENTER)
        Button(interfaz, text="Modificar Trabajador", font=("Roboto cn", 12), command=ventanaModificarPorRut).place(relx=0.7, rely=0.35, anchor=CENTER)

        interfaz.mainloop()


class borrarTrabajadores():

        def __init__(self):
            """Funciones"""

            def listarTrabajo():
                conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
                cursor1 = conexion1.cursor()
                sql = "select * from trabajador"
                cursor1.execute(sql)   
                result = cursor1.fetchall()
                cursor1.close()
                conexion1.close()
                return result

            def borrarTrabajadores():
                """Esta funcion: borrarTrabajadores, tiene 6 conexiones, la cual la conexion2, pide el id de datos_laborales que estan en ficha_trabajador
                   Que luego pasa hacia la conexion 3, que ahi elimina la columna de datos_laborales por el id, la conexion 1, borra la ficha del trabajador,
                   la 4 conexion elimina los contactos de emergencia y la quinta las cargas familiares, la 6 conexion elimina la tabla trabajador."""

                if rutn.get() == "admin":
                    advertencia = Toplevel()
                    advertencia.title("Advertencia")
                    Label(advertencia, text="No tiene los privilegios para Eliminar un administrador").grid(padx=5, row=0)
                    Button(advertencia, text="aceptar", command=advertencia.destroy).grid(row=1)
                else:
                    conexion2 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
                    cursor2 = conexion2.cursor()
                    sql = "SELECT datos_laborales_id_datos_laborales FROM ficha_trabajador WHERE trabajador_rut = %s"
                    val = (rutn.get())
                    cursor2.execute(sql, (val,))
                    datos = cursor2.fetchone()
                    conexion2.commit()   
                    cursor2.close()
                    conexion2.close()

                    conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
                    cursor1 = conexion1.cursor()
                    sql = "DELETE FROM ficha_trabajador WHERE trabajador_rut = %s"
                    val = (rutn.get())
                    cursor1.execute(sql, (val,))
                    conexion1.commit()   
                    cursor1.close()
                    conexion1.close()

                    conexion3 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
                    cursor3 = conexion3.cursor()
                    sql = "DELETE FROM datos_laborales WHERE id_datos_laborales = %s "
                    val = (datos[0])
                    cursor3.execute(sql, (val,))
                    conexion3.commit()   
                    cursor3.close()
                    conexion3.close()

                    conexion4 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
                    cursor4 = conexion4.cursor()
                    sql = "DELETE FROM contactos_emergencia WHERE trabajador_rut = %s "
                    val = (rutn.get())
                    cursor4.execute(sql, (val,))
                    conexion4.commit()   
                    cursor4.close()
                    conexion4.close()


                    conexion5 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
                    cursor5 = conexion5.cursor()
                    sql = "DELETE FROM cargas_familiares WHERE trabajador_rut = %s "
                    val = (rutn.get())
                    cursor5.execute(sql, (val,))
                    conexion5.commit()   
                    cursor5.close()
                    conexion5.close()

                    conexion6 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
                    cursor6 = conexion6.cursor()
                    sql = "DELETE FROM trabajador WHERE rut = %s "
                    val = (rutn.get())
                    cursor6.execute(sql, (val,))
                    conexion6.commit()   
                    cursor6.close()
                    conexion6.close()
                    advertencia = Toplevel()
                    advertencia.title("Informacion")
                    Label(advertencia, text="Se ha eliminado con exito").grid(padx=5, row=0)
                    Button(advertencia, text="aceptar", command=advertencia.destroy).grid(row=1)





            """Funciones"""
            trabajo = listarTrabajo()
            interfaz  = Tk()
            interfaz.title('Consultar Trabajadores')
            w = interfaz.winfo_screenwidth()
            h = interfaz.winfo_screenheight()
            interfaz.geometry("%dx%d" % (w, h))
        
        
            Label(interfaz, text="Trabajadores", font=("Roboto cn", 15)).place(relx=0.5, rely=0.05, anchor=N)

            """Apartado de trabajadores"""
            table_frame = Frame(interfaz, width=700, height=700)
            table_frame.place(relx=0.27, rely=0.4, anchor=CENTER)


            """scroll"""
            tabla_scroll = Scrollbar(table_frame)
            tabla_scroll.pack(side=RIGHT, fill=Y)

            tabla_scroll = Scrollbar(table_frame,orient='horizontal')
            tabla_scroll.pack(side= BOTTOM,fill=X)

            tabla = ttk.Treeview(table_frame,yscrollcommand=tabla_scroll.set, xscrollcommand =tabla_scroll.set)

            tabla.pack()

            tabla_scroll.config(command=tabla.yview)
            tabla_scroll.config(command=tabla.xview)

            """scroll"""
            tabla['columns'] = ('rut', 'nombres', 'apellidos', 'sexo', 'direccion', 'telefono')

            tabla.column("#0", width=0,  stretch=NO)
            tabla.column("rut",anchor=CENTER, width=120)
            tabla.column("nombres", anchor=CENTER, width=120)
            tabla.column("apellidos",anchor=CENTER,width=120)
            tabla.column("sexo",anchor=CENTER,width=120)
            tabla.column("direccion",anchor=CENTER,width=120)
            tabla.column("telefono",anchor=CENTER,width=120)


            tabla.heading("#0",text="",anchor=CENTER)
            tabla.heading("rut",text="RUT",anchor=CENTER)
            tabla.heading("nombres",text="Nombres",anchor=CENTER)
            tabla.heading("apellidos",text="Apellidos",anchor=CENTER)
            tabla.heading("sexo",text="Sexo",anchor=CENTER)
            tabla.heading("direccion",text="Direccion",anchor=CENTER)
            tabla.heading("telefono",text="Telefono",anchor=CENTER)

            id = 0
            for i in trabajo:
                tabla.insert(parent='',index='end',iid=id,text='',
                values=(i[0],i[1],i[2],i[3],i[4], i[5]))
                id +=1
            tabla.pack()
            """Apartado de trabajadores"""
            """Apartado cargas familiares"""
            Label(interfaz, text="Ingrese el rut aqui: ").place(relx=0.66, rely=0.26)
            rutn = Entry(interfaz, width=40)
            rutn.pack()
            rutn.place(relx=0.70, rely=0.30, anchor=CENTER)

            Button(interfaz, text="Atras <--", font=("Roboto cn", 12), command=interfaz.destroy).place(relx=0.30, rely=0.70, anchor=CENTER)
            Button(interfaz, text="Eliminar Trabajador", font=("Roboto cn", 12), command=borrarTrabajadores).place(relx=0.7, rely=0.35, anchor=CENTER)

            interfaz.mainloop()




class consultarTrabajadores():
    
    def __init__(self):
        
        """FUNCIONES"""
        def listarTrabajo():
            conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
            cursor1 = conexion1.cursor()
            sql = "select * from trabajador"
            cursor1.execute(sql)   
            result = cursor1.fetchall()
            cursor1.close()
            conexion1.close()
            return result
        trabajo = listarTrabajo()

        def traerCargasFamiliares():
            conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
            cursor1 = conexion1.cursor()
            sql = "select nombre_carga_familiar, parentesco, sexo from cargas_familiares WHERE trabajador_rut = %s"
            val = (rutn.get())
            cursor1.execute(sql, (val,))   
            result = cursor1.fetchall()
            cursor1.close()
            conexion1.close()
            return result

        def traerContactosEmergencia():
            conexion1 = mysql.connector.connect(host="localhost", user="root", passwd="", database="listadotrabajadores")
            cursor1 = conexion1.cursor()
            sql = "select nombre,  relacion_trabajador, telefono from contactos_emergencia WHERE trabajador_rut = %s"
            val = (rutn.get())
            cursor1.execute(sql, (val,))   
            result = cursor1.fetchall()
            cursor1.close()
            conexion1.close()
            return result

        """FUNCIONES"""
        def contactosEmergencia():
            datos = rutn.get()
            cargas = traerContactosEmergencia()
            interfaz = Toplevel()
            interfaz.title("Contactos Emergencia")
            interfaz.geometry("600x350")
            destroy = interfaz.destroy
            cargasFamiliares_frame = Frame(interfaz, width=700, height=700)
            cargasFamiliares_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
            Label(interfaz, text="Contactos Emergencia", font=("Roboto cn", 15)).place(relx=0.5, rely=0.03, anchor=N)
            Button(interfaz, text="Atras <--", font=("Roboto cn", 12), command=destroy).place(relx=0.5, rely=0.90, anchor=CENTER)
            
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
            cargasFamiliares['columns'] = ('nombre', 'relacion', 'telefono')

            cargasFamiliares.column("#0", width=0,  stretch=NO)
            cargasFamiliares.column("nombre",anchor=CENTER, width=140)
            cargasFamiliares.column("relacion", anchor=CENTER, width=140)
            cargasFamiliares.column("telefono",anchor=CENTER,width=140)



            cargasFamiliares.heading("#0",text="",anchor=CENTER)
            cargasFamiliares.heading("nombre",text="Nombre",anchor=CENTER)
            cargasFamiliares.heading("relacion",text="Relacion",anchor=CENTER)
            cargasFamiliares.heading("telefono",text="Telefono",anchor=CENTER)


            id = 0
            for i in cargas:
                cargasFamiliares.insert(parent='',index='end',iid=id,text='',
                values=(i[0],i[1],i[2]))
                id +=1
            cargasFamiliares.pack()

        
            interfaz.mainloop()
        

        def cargasFamiliares():
            datos = rutn.get()
            cargas = traerCargasFamiliares()
            interfaz = Toplevel()
            interfaz.geometry("600x350")
            destroy = interfaz.destroy
            cargasFamiliares_frame = Frame(interfaz, width=700, height=700)
            cargasFamiliares_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
            Label(interfaz, text="Cargas Familiares", font=("Roboto cn", 15)).place(relx=0.5, rely=0.03, anchor=N)
            Button(interfaz, text="Atras <--", font=("Roboto cn", 12), command=destroy).place(relx=0.5, rely=0.90, anchor=CENTER)
            
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
            cargasFamiliares['columns'] = ('nombre_cargas_familiar', 'parentesco', 'sexo')

            cargasFamiliares.column("#0", width=0,  stretch=NO)
            cargasFamiliares.column("nombre_cargas_familiar",anchor=CENTER, width=140)
            cargasFamiliares.column("parentesco", anchor=CENTER, width=140)
            cargasFamiliares.column("sexo",anchor=CENTER,width=140)



            cargasFamiliares.heading("#0",text="",anchor=CENTER)
            cargasFamiliares.heading("nombre_cargas_familiar",text="Nombre",anchor=CENTER)
            cargasFamiliares.heading("parentesco",text="Parentesco",anchor=CENTER)
            cargasFamiliares.heading("sexo",text="Sexo",anchor=CENTER)


            id = 0
            for i in cargas:
                cargasFamiliares.insert(parent='',index='end',iid=id,text='',
                values=(i[0],i[1],i[2]))
                id +=1
            cargasFamiliares.pack()

        
            interfaz.mainloop()
        """FUNCIONES"""

        interfaz  = Tk()
        interfaz.title('Consultar Trabajadores')
        w = interfaz.winfo_screenwidth()
        h = interfaz.winfo_screenheight()
        interfaz.geometry("%dx%d" % (w, h))
        
        
        Label(interfaz, text="Trabajadores", font=("Roboto cn", 15)).place(relx=0.5, rely=0.05, anchor=N)

        """Apartado de trabajadores"""
        table_frame = Frame(interfaz, width=700, height=700)
        table_frame.place(relx=0.27, rely=0.4, anchor=CENTER)


        """scroll"""
        tabla_scroll = Scrollbar(table_frame)
        tabla_scroll.pack(side=RIGHT, fill=Y)

        tabla_scroll = Scrollbar(table_frame,orient='horizontal')
        tabla_scroll.pack(side= BOTTOM,fill=X)

        tabla = ttk.Treeview(table_frame,yscrollcommand=tabla_scroll.set, xscrollcommand =tabla_scroll.set)

        tabla.pack()

        tabla_scroll.config(command=tabla.yview)
        tabla_scroll.config(command=tabla.xview)

        """scroll"""
        tabla['columns'] = ('rut', 'nombres', 'apellidos', 'sexo', 'direccion', 'telefono')

        tabla.column("#0", width=0,  stretch=NO)
        tabla.column("rut",anchor=CENTER, width=120)
        tabla.column("nombres", anchor=CENTER, width=120)
        tabla.column("apellidos",anchor=CENTER,width=120)
        tabla.column("sexo",anchor=CENTER,width=120)
        tabla.column("direccion",anchor=CENTER,width=120)
        tabla.column("telefono",anchor=CENTER,width=120)


        tabla.heading("#0",text="",anchor=CENTER)
        tabla.heading("rut",text="RUT",anchor=CENTER)
        tabla.heading("nombres",text="Nombres",anchor=CENTER)
        tabla.heading("apellidos",text="Apellidos",anchor=CENTER)
        tabla.heading("sexo",text="Sexo",anchor=CENTER)
        tabla.heading("direccion",text="Direccion",anchor=CENTER)
        tabla.heading("telefono",text="Telefono",anchor=CENTER)

        id = 0
        for i in trabajo:
            tabla.insert(parent='',index='end',iid=id,text='',
            values=(i[0],i[1],i[2],i[3],i[4], i[5]))
            id +=1
        tabla.pack()
        """Apartado de trabajadores"""
        """Apartado cargas familiares"""
        Label(interfaz, text="Ingrese el rut aqui: ").place(relx=0.66, rely=0.26)
        rutn = Entry(interfaz, width=40)
        rutn.pack()
        rutn.place(relx=0.70, rely=0.30, anchor=CENTER)
        """padx=500, pady=170"""
       
        """Botones"""
        Button(interfaz, text="Atras <--", font=("Roboto cn", 12), command=interfaz.destroy).place(relx=0.30, rely=0.70, anchor=CENTER)
        Button(interfaz, text="Cargas Familiares", width=25, height=2, command=cargasFamiliares).place(relx=0.60, rely=0.37, anchor=CENTER)
        Button(interfaz, text="Contactos de Emergencias", width=25, height=2, command=contactosEmergencia).place(relx=0.80, rely=0.37, anchor=CENTER)
        """Botones"""

        

class crearTrabajador():
     def __init__(self):
        interfaz = Toplevel()
        interfaz.title("Crear Trabajador")
        w = interfaz.winfo_screenwidth()
        h = interfaz.winfo_screenheight()
        interfaz.geometry("%dx%d" % (w, h))
        Label(interfaz, text="Crear Trabajador", font=("Roboto cn", 15)).place(relx=0.5, rely=0.03, anchor=N)
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
            if user_cargo.get() == "Administrador":
                advertencia = Toplevel()
                advertencia.title("Advertencia")
                Label(advertencia, text="No tiene los privilegios para agregar un administrador").grid(padx=5, row=0)
                Button(advertencia, text="aceptar", command=advertencia.destroy).grid(row=1)
            else:
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

                #Validar Datos Laborales


                
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
        Label(interfaz, text="Recuerde guardar antes de ingresar cargas familiares o contactos de emergencia", font=("Roboto cn", 12)).place(relx=0.5, rely=0.70, anchor=CENTER)


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
        Button(interfaz, text="Ingresar Cargas Familiar", font=("Roboto cn", 12), command=agregacargafamiliar).place(relx=0.60, rely=0.75, anchor=CENTER)
        Button(interfaz, text="Ingresar Contacto Emergencia", font=("Roboto cn", 12), command=agregarcontactoemergencia).place(relx=0.45, rely=0.75, anchor=CENTER)

        """Datos Nomina Sueldo"""
        interfaz.mainloop()


class interfazJefe():
    def __init__(self):
        interfaz = Tk()
        interfaz.title('INTERFAZ JEFE RRHH')
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
        
        Button(interfaz, text="Consulta de Trabajadores ", font=("Roboto cn", 20), command=consultarTrabajadores).place(relx=0.5, rely=0.3, anchor=CENTER)
        Button(interfaz, text="Creacion Ficha Trabajador", font=("Roboto cn", 20),command=crearTrabajador).place(relx=0.5, rely=0.4, anchor=CENTER)
        Button(interfaz, text="Modificar Ficha Trabajador", font=("Roboto cn", 20),command=modificarTrabajadores).place(relx=0.5, rely=0.5, anchor=CENTER)
        Button(interfaz, text="Eliminacion de Ficha Trabajador", font=("Roboto cn", 20),command=borrarTrabajadores).place(relx=0.5, rely=0.6, anchor=CENTER)
        
        Button(interfaz, text="Salir", font=("Roboto cn", 20), command=destroy).place(relx=0.5, rely=0.8, anchor=CENTER)

        interfaz.mainloop()
