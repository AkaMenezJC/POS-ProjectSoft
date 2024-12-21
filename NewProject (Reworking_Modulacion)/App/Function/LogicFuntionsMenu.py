import App.Function.FunctionAccesLogic as Logic




class FunctionLogicMenu:
        #self.Inventary =[Logic.Principal_Menu.InventaryMenu(self)["ID"],
                         #Logic.Principal_Menu.InventaryMenu(self)["Nombre"]]

    def DeleteItemInventary(self):
        self.Inventary = Logic.Principal_Menu()
        #Esta función elimina un item del inventario por ID o Nombre.
        productid= self.Inventary.delforid.get()
        productname= self.Inventary.delforname.get()
        conditional= f"Id_Product = '{productid}'"
        conditional1= f"Product_Name = '{productname}'"
        Logic.Database.DeleteRowTable("Tienda_Ropas","Inventary", conditional)
        Logic.Database.DeleteRowTable("Tienda_Ropas","Products", conditional1)



"""
    def DeleteItemForHeight(self):
        productheight= self.delforheight.get()
        productid= self.delforid.get()

        conditional= f"Id_Product = '{productid}' AND Height = '{productheight}'"
        DB.DeleteRowTable("Tienda_Ropas", "Inventary", conditional)

    def AddItemInventary(self):
        #Esta función agrega un nuevo item al inventario en la base de datos.
        conditional= ("Id_Product", "Stock", "Height", "Product_Price", "Id_Provider")
        itemlistadd= (self.registerid.get(),
                       self.registercount.get(),
                       self.registerheight.get(),
                       self.registerprice.get(),
                       self.registerprovider.get(),)

        conditional1= ("Id_Product", "Product_Name", "Pro_Description")
        itemlistadd1= (itemlistadd[0], self.registername.get(), "N/A")
        Database.AddRowTable("Tienda_Ropas", "Products", conditional1, itemlistadd1)
        Database.AddRowTable("Tienda_Ropas","Inventary", conditional, itemlistadd)

    def SearchInventaryItem (self):
        consult= self.consultprodid.get()
        #consult1= self.consultprodname.get()
        listforid= Database.ShowAnyItemsTableForID("Tienda_Ropas",
                                                   "Inventary",
                                                   "Products",
                                                   "Id_product", consult)
        for i in range(len(listforid)):
            listformat= listforid[i]
            listformat2= (listformat[1], # ID producto
                          listformat[8], # Nombre_product
                          listformat[3], # Talla
                          listformat[2], # Cantidad
                          listformat[5], # ID Proveedor
                          listformat[6]) # Tiempo Timestamtp
            self.listreeview.insert ("","end", text= "", values= listformat2)
        #for i in range(len(listforheight)):
            #listformat= listforheight[i]
            #listformat2= (listformat[1], # ID producto
                          #listformat[8], # Nombre_product
                          #listformat[3], # Talla
                          #listformat[2], # Cantidad
                          #listformat[5], # ID Proveedor
                          #listformat[6]) # Tiempo Timestamtp
            #self.listreeview.insert ("","end", text= "", values= listformat2)
"""
        
