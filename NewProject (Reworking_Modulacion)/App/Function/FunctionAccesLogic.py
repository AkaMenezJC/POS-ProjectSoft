
import os
import tkinter as ttk
from tkinter import ttk
import customtkinter as Tk
from tkinter.messagebox import *
#from PIL import Image, ImageTk, ImageColor
import App.DataBase.DataBaseConnect as sqlbd
#

Iconfolder = os.path.dirname ("D:/ProjectTiendaRopas/NewProject"
                              " (Reworking_Modulacion)/App/Texture/Icon/IconApp.ico")

Database = sqlbd.ConnectBaseDatos(**sqlbd.ConnectBD)

class Roots_AppLogin:
#Esta clase representas las ventanas del programa.
    def __init__ (self, title, geometry):
        #Funcion de ventana inicial, login. con self doy entrada para las otras ventanas.
        self.savetitle = title
        self.savegeometry = geometry
        self.counttry = 0

        self.root = Tk.CTk()
        self.root.title(title)
        self.root.geometry(geometry)
        self.root.iconbitmap(os.path.join(Iconfolder, "IconApp.ico"))

        #Cuadro usuario & entry
        userlabel = Tk.CTkLabel (self.root,
                                 text= "Usuario")
        userlabel.pack()
        self.entryuser = Tk.CTkEntry(self.root,
                                     placeholder_text= "Usuario")
        self.entryuser.pack()

        #Cuadro password & entry
        passwordlabel = Tk.CTkLabel (self.root,
                                     text= "Contraseña")
        passwordlabel.pack()
        self.entrypassword = Tk.CTkEntry (self.root,
                                          placeholder_text= "Contraseña")
        self.entrypassword.pack()

        #Boton entrar
        entrybutton = Tk.CTkButton (self.root,
                                    text= "Entrar",
                                    command= self.AccesPrincipalMenu)
        entrybutton.pack(pady=20, padx= 20)
        self.root.mainloop()

    def AccesPrincipalMenu (self):
    #Esta función verifica el acceso hacia el menu principal.
        accesentryuser = self.entryuser.get()
        accesentrypass = self.entrypassword.get()
        access1 = Database.SearchPassAndUser("Tienda_Ropas", accesentryuser)
        verifypass = access1.get("Password")
        verifyuser = access1.get("User_name")

        if self.counttry < 3:
            if accesentrypass != "" and accesentrypass != verifypass:
                self.counttry += 1

            if accesentrypass != verifypass or accesentryuser != verifyuser:
                errorpass= Tk.CTkLabel (self.root, text="Contraseña o usuario incorrecto\n"
                            f"Intento {self.counttry} de 3", text_color= "Red")
                errorpass.pack()

            elif accesentrypass == verifypass and accesentryuser == verifyuser:
                showinfo("Información",
                        "¡Bienvenido!\nAhora puedes acceder a nuestro sistema.")
                self.root.destroy()
                Principal_Menu()
        if self.counttry >= 3:
            showerror ("Error",
                       "¡Acceso denegado por intentos fallidos!\nEl programa cerrará.")
            self.root.destroy()


class Principal_Menu:
    def __init__(self):
        #Esta función crea la ventana menu principal,
        #Se utiliza en el login llamandola si pasa la verificacion
        #Y solo puede accederse a esta ventana a traves del login.
        self.root = Tk.CTk()
        self.root.title("Fruto Bendito - Menú principal")
        self.root.geometry("500x180")
        self.root.iconbitmap(os.path.join(Iconfolder, "IconApp.ico"))

        #Cuadros que necesitaré en los menus/ventanas
        self.frame1= Tk.CTkFrame(self.root)
        self.frame2= Tk.CTkFrame(self.root)

        salesbutton = Tk.CTkButton(self.root,
                                   text= "Ventas",
                                   width=85, height=30,)
                                   #command=self.SalesMenu)
        salesbutton.grid(row= 5, column= 0,
                         pady= 15, padx= 20)

        inventarybutton = Tk.CTkButton(self.root,
                                       text = "Inventario",
                                       width=85, height=30,
                                       command= self.InventaryMenu)
        inventarybutton.grid(row= 1, column= 0,
                             pady= 15, padx= 20)

        clientsbutton = Tk.CTkButton(self.root,
                                     text = "Clientes",
                                     width=85, height=30,)
                                     #command= self.ClientsMenu)
        clientsbutton.grid(row= 3, column= 0,
                           pady= 15, padx= 20)

        providersbutton = Tk.CTkButton(self.root,
                                       text = "Proveedores",
                                       width=85, height=30,)
                                       #command= self.ProvidersMenu)
        providersbutton.grid(row= 1, column= 1,
                             pady= 15, padx= 20)

        ordersbutton = Tk.CTkButton(self.root,
                                    text = "Pedidos",
                                    width=85, height=30,)
                                    #command= self.OrdersMenu)
        ordersbutton.grid(row= 3, column= 1,
                          pady= 15, padx= 20)

        exitbutton = Tk.CTkButton (self.root,
                                   text="Salir",
                                   width= 30, height=20,)
        exitbutton.grid(row= 5, column= 4,
                          pady= 15, padx= 20)
        self.root.mainloop()

    def InventaryMenu(self):
        #Debe permitir registrar y eliminar productos de la tabla inventarios
        #Además debe mostrar en tiempo real el coste total de la materia prima.
        #Debe mostrar la tabla de inventarios y poder acceder a cada prodictos
        #El acceso a cada producto debe ser por ID o nombre e imprimirlo en la ventana
        self.root.destroy()
        self.root = Tk.CTk()
        self.root.title("Fruto Bendito: Inventario")
        self.root.geometry("843x635")
        self.root.iconbitmap(os.path.join(Iconfolder, "IconApp.ico"))
        self.root.resizable(width=False, height=False)
        #Fun = FunctionLogicMenu

        #Llamando los frames (Frame1, Frame2)
        self.frame1= Tk.CTkFrame(self.root)
        self.frame1.grid(row= 1, column= 0)

        self.frame2= Tk.CTkFrame(self.root)
        self.frame2.grid(row= 1, column= 1)

        #--------->>> FRAME 1  <<<--------
        #Subcuadro, de consulta por nombre o ID
        consultlabel= Tk.CTkLabel(self.frame1,
                                  text="Consultar producto") #Label
        consultlabel.grid(row= 0, column= 0)
        self.consultprodname= Tk.CTkEntry(self.frame1,
                                     placeholder_text="Nombre_Producto") #Entry
        self.consultprodname.grid(row=1, column= 0,
                             padx= 10, pady= 10)
        self.consultprodid= Tk.CTkEntry(self.frame1,
                                   placeholder_text="ID_Producto") #Entry
        self.consultprodid.grid(row=1, column= 1,
                           padx= 10, pady= 10)
        self.consultforheigth= Tk.CTkEntry(self.frame1,
                                           placeholder_text= "Talla")
        self.consultforheigth.grid(row=3, column= 0,
                                   padx= 10, pady= 10)

        searchallbutton = Tk.CTkButton(self.frame1,
                                       text="Todos los productos")
        searchallbutton.grid(row=4, column= 0)

        searchbutton= Tk.CTkButton(self.frame1,
                                   text="Buscar producto",)
                                   #command= Proj.Function_Menu.SearchInventaryItem)#Button
        searchbutton.grid(row= 4, column= 1,
                          padx= 10, pady= 15)

        #Subcuadro registro de producto al inventario. (Frame 1)
        registerlabel= Tk.CTkLabel (self.frame1,
                                    text="Registrar producto:") #Label
        registerlabel.grid(row= 5, column= 0)

        self.registerid= Tk.CTkEntry(self.frame1,
                                   placeholder_text="ID_Producto") #Entry
        self.registerid.grid(row=6, column= 0,
                        padx= 10, pady= 10)

        self.registername= Tk.CTkEntry(self.frame1,
                                   placeholder_text="Nombre_Producto") #Entry
        self.registername.grid(row=7, column= 0,
                          padx= 10, pady= 10)

        self.registercount= Tk.CTkEntry(self.frame1,
                                   placeholder_text="Cantidad")  #Entry
        self.registercount.grid(row=6, column= 1,
                           padx= 10, pady= 5)

        self.registerprovider= Tk.CTkEntry(self.frame1,
                                   placeholder_text="ID_Proveedor") #Entry
        self.registerprovider.grid(row=7, column= 1,
                              padx= 10, pady= 5)

        self.registerheight= Tk.CTkEntry(self.frame1,
                                          placeholder_text="Talla")
        self.registerheight.grid(row= 8, column= 0,
                                 padx= 10, pady= 10)
        self.registerprice= Tk.CTkEntry(self.frame1,
                                        placeholder_text="Precio")
        self.registerprice.grid(row= 8, column= 1,
                                 padx= 10, pady= 10)

        regproductbutton= Tk.CTkButton(self.frame1,
                                       text= "Registrar producto",)
                                       #command= Proj.Function_Menu.AddItemInventary) #Button
        regproductbutton.grid(row= 9, column = 1,
                              padx= 10, pady= 15)

        #Subcuadro eliminar producto de la base de datos por ID. (Frame 1)
        deletelabel= Tk.CTkLabel (self.frame1,
                                  text="Eliminar producto:") #Label
        deletelabel.grid(row= 10, column= 0,)
        deleteheightlabel= Tk.CTkLabel(self.frame1, text= "Eliminar Talla:")
        deleteheightlabel.grid(row= 10, column= 1)
        self.delforid= Tk.CTkEntry(self.frame1,
                              placeholder_text="ID_Producto") #Entry
        self.delforid.grid(row=11, column= 1,
                      padx= 10, pady= 10)

        self.delforname= Tk.CTkEntry(self.frame1,
                                placeholder_text="Nombre_Producto") #Entry
        self.delforname.grid(row= 11 , column=0,
                        padx= 10, pady= 10)

        self.delforheight= Tk.CTkEntry(self.frame1,
                                       placeholder_text= "Talla")
        self.delforheight.grid(row= 12, column= 1,
                               padx= 10, pady= 10)

        delproductbutton= Tk.CTkButton(self.frame1,
                                       text="Eliminar producto\n(Full)",)
                                       #command= Fun) #Button
        delproductbutton.grid(row= 13, column= 0,      #Antes de actualizar la tabla en la BD
                              padx= 10, pady= 15)      #Realizar una verificacion de acceso.

        delforheighbutton= Tk.CTkButton(self.frame1,
                                        text= "Eliminar por talla",)
                                        #command= Proj.Function_Menu.DeleteItemForHeight)
        delforheighbutton.grid(row= 13, column= 1,
                               padx= 10, pady= 15,)

        #-------->>> FRAME 2 <<<-----------
        #Cuadro de resultados, debe entregar busquedas por ID o nombre.
        resultlist= Tk.CTkLabel(self.frame2, text= "Resultados")        #Label
        resultlist.grid(row=0, column=0)
        productslist = Tk.CTkScrollableFrame(self.frame2,
                                                  width=500, height=505,)
        productslist.grid(row= 1, column= 0)

        #TreeView TK
        column= ("Id_product","Product_name","Height", "Stock", "Id_Provider", "Create_at")
        self.listreeview= ttk.Treeview(productslist, height= 450, show= "headings", columns= column)
        self.listreeview.heading("Id_product", text="ID",anchor="c")
        self.listreeview.heading("Product_name", text="Nombre producto", anchor="c")
        self.listreeview.heading("Height", text= "Talla", anchor= "c")
        self.listreeview.heading("Stock", text="Cantidad",anchor="c")
        self.listreeview.heading("Id_Provider", text="ID proveedor",anchor="c")
        self.listreeview.heading("Create_at", text="Fecha de registro",anchor="c")

        self.listreeview.column ("Id_product", width=40, minwidth= 30)
        self.listreeview.column ("Product_name", width=130, minwidth= 90)
        self.listreeview.column ("Height", width= 40, minwidth= 30)
        self.listreeview.column ("Stock", width=80, minwidth= 60)
        self.listreeview.column ("Id_Provider", width=90, minwidth= 80)
        self.listreeview.column ("Create_at", width=130, minwidth= 90)

        self.listreeview.pack()

        #-------->>> fuera de frame <<<-------
        #vuelve al menu principal
        returnprimenu= Tk.CTkButton(self.root,
                                    text="Menú principal", #Button
                                    command= Principal_Menu)
        returnprimenu.grid(row= 2, column= 0,
                           pady= 2, padx= 1)

        treecleanbutton = Tk.CTkButton (self.root,
                                  text= "Limpiar tabla")
        treecleanbutton.grid(row= 2, column= 1)

        self.root.mainloop()

        #return {"ID": self.delforid.get(),
                #"Nombre": self.delforname.get(), 
                #"Talla": self.delforheight.get()}

