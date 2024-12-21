import mysql.connector
from tkinter.messagebox import *

ConnectBD= {"host": "localhost",
        "user":"root" ,
        "password":"Jd199923.",}

class ConnectBaseDatos:
    def __init__ (self, **kwargs):
        self.connectmysql= mysql.connector.connect(**kwargs)
        self.cursor = self.connectmysql.cursor()


    def Consult (self, sql):
        #Cualquier tipo de consulta general SHOW, Join, OrderBy, Select, USE, Etc..
        self.cursor.execute(sql)
        return self.cursor

    def ShowAnyItemsTableForID (self, bd, table, table2, columndata, conditional):
        Showtable = []

        self.cursor.execute (f"USE {bd}")
        self.cursor.execute (f"SELECT * FROM {table} INNER JOIN {table2}"
                             f" WHERE {table}.{columndata} = '{conditional}'"
                             f" AND {table2}.{columndata} = '{conditional}'")
        for i in self.cursor:
            Showtable.append(i)
        return Showtable

    def ShowDataTables (self, Bd, table):
        #Muestra los registros de las tablas.
        ShowTable = []
        self.cursor.execute(f"USE {Bd}")
        self.cursor.execute(f"SELECT * FROM {table}")
        for i in self.cursor:
            ShowTable.append(i)
        return ShowTable


    def SearchPassAndUser (self, Bd, user):
        userandpass = dict()
        self.cursor.execute(f"Use {Bd}")
        sql = self.cursor.execute(f"SELECT * FROM Users WHERE User_Name = '{user}'")
        self.cursor.execute(sql)
        info= self.cursor.fetchall()
        try:
            userpasslist= info[0]
            userandpass["User_name"] = userpasslist[1]
            userandpass["Password"] = userpasslist[3]
        except:
            showerror("Error", "El usuario que ingresó no existe en nuestra base de datos\n"
                      "Recuerde registrarse antes de intentar ingresar.")
        return userandpass


    def DeleteRowTable (self, Bd, Table, Condition):
        #Elimina los registros de las tablas.
        try:
            self.cursor.execute(f"USE {Bd}")
            sql = f"DELETE FROM {Table} WHERE {Condition}"
            self.cursor.execute (sql)
            self.connectmysql.commit()
            print("Información","¡Datos borrados con éxito!")
        except:
            print (f"La base de datos {Bd} o el registro {Condition} "
                   f"de la tabla {Table} no existe.")


    def AddRowTable (self, Bd, Table, Condition_1, Condition_2):
        #Agrega registros nuevos a las tablas.
        try:
            self.cursor.execute(f"USE {Bd}")
        except:
            print (f"La base de datos {Bd} no existe.")

        str1= str(Condition_1).replace("'","")
        str2= str(Condition_2).replace("'", '"')
        format1= f"INSERT INTO {Table} {str1} VALUES {str2}"
        format2= format1

        for i in format2:
            strparent = i
            if strparent ==  "[" or strparent == "]":
                format2= format1.replace("[","(").replace("]",")")
        try:
            self.cursor.execute(format2)
            self.connectmysql.commit()
            print(f"Se han registrado correctamente los datos {str2} en la tabla {Table}")
        except:
            print("Ocurrió un error inesperado.\n"
                   f"Los registros {str2} ya existen en la tabla {Table}"
                   "o no cumple con las condiciones de registro.")

    def UpdateRowTable (self, Bd, Table, Condition_1, Condition_2):
        #Actualiza los registros de las filas.
        self.cursor.execute (f"USE {Bd}")
        try:
            self.cursor.execute (f"UPDATE {Table} SET {Condition_1} WHERE {Condition_2}")
            self.connectmysql.commit()
        except:
            print (f"Ocurrió un error al momento de actualizar los datos {Condition_1}\n"
                   f"Importante: Los datos {Condition_2} no existen en la tabla. ")

