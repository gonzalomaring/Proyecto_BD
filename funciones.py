import sys
import MySQLdb

def conectar_bd(host,usuario,clave,nombrebd):
    try:
        db=MySQLdb.connect(host,usuario,clave,nombrebd)
        return db
    except MySQLdb.Error as e:
        print("No puedo conectarme a la base de datos:",e)
        sys.exit(1)

def desconectar_bd(db):
    db.close()

def menu():
    menu=("Menu:\n1.Listar provincias y su comunidad viendo al final el nº total de provincias\n2.Ver localidades con un nº mayor de habitantes mayor que el introducido\n3.Introducir una provincia y ver las localidades que están en ellas\n4.Insertar una localidad,creando una nueva provincia si fuera necesario\n5.Borrar una provincia\n6.Actualizar el número de habitantes que tiene una localidad.\n7.Salir")
    return menu

def listar_comunidades(db):
    sql="select provname,comunidad_autonoma from provincias;"
    cursor=db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        registros=cursor.fetchall()
        for registro in registros:
            print("La provincia",registro.get("provname"),"se encuentra en la comunidad ",registro.get("comunidad_autonoma"))
        print("\nNúmero de provincias de las que disponemos información:",cursor.rowcount)
    except:
        print("Error en la consulta")

def mayor_num_hab(db,numhab):
    sql="select nombre from localidades where ciudadanos>%i;"%numhab
    cursor=db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        registros=cursor.fetchall()
        print("Las localidades con más de",numhab,"habitantes son:")
        for registro in registros:
            print(registro.get("nombre"))
    except:
        print("Error en la consulta")

def loc_provincias(db,nombreprov):
    sql="select nombre from localidades where provno in(select provno from provincias where provname='%s');"%nombreprov
    cursor=db.cursor(MySQLdb.cursors.DictCursor)
    try:
        cursor.execute(sql)
        registros=cursor.fetchall()
        print("La provincia",nombreprov,"tiene las siguientes localidades:")
        for registro in registros:
            print(registro.get("nombre"))
    except:
        print("Error en la consulta")

def check_provincias(db,nombreprov):
    sql="select provname from provincias where provname='%s'"%nombreprov
    cursor=db.cursor(MySQLdb.cursors.DictCursor)
    check=False
    cursor.execute(sql)
    registros=cursor.fetchall()
    for registro in registros:
        if registro.get("provname")==nombreprov:
                check=True
    return check
def crear_prov(db,prov):
    cursor=db.cursor()
    nombre=prov.get("provname")
    com=prov.get("ca")
    sql="insert into provincias(provname,comunidad_autonoma) values('%s','%s');"%(nombre,com)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("Error al insertar la provincia")
        db.rollback()

def crear_loc(db,loc):
    cursor=db.cursor()
    sql="insert into localidades(nombre,ciudadanos,cp,provno) values('%s',%i,%i,'%s');"%(loc.get("nombre"),loc.get("ciudadanos"),loc.get("cp"),loc.get("provno"))
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("Error al crear la localidad")
        db.rollback
def saber_provno(db,provincia):
    sql="select provno from provincias where provname='%s'"%provincia
    cursor=db.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(sql)
    registros=cursor.fetchall()
    for registro in registros:
        return registro.get("provno")

def borrar_provincia(db,provincia):
    sql="delete from provincias where provname='%s'"%provincia
    cursor=db.cursor()
    resp=input("Estás seguro de querer borrar la provincia?")
    if resp=="s" or resp=="S":
        try:
            cursor.execute(sql)
            db.commit()
            if cursor.rowcount==0:
                print("No existen provincias con ese nombre")
        except:
            print("Error al borrar")
            db.rollback()
def upd_habitantes(db,numero,nombre):
    cursor=db.cursor()
    sql="update localidades set ciudadanos=%s where nombre='%s'"%(numero,nombre)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        print("Error al actualizar")
        db.rollback()


