from funciones import *
db=conectar_bd("localhost","proyectobd","proyectobd","provinciasbd")
print(menu())
opcion=int(input("Elige una opción: "))
while opcion!=7:
    if opcion==8:
        print(menu())
        opcion=int(input("Elige una opción: "))
    elif opcion==1:
        listar_comunidades(db)
        opcion=int(input("Elige una opción: "))
    elif opcion==2:
        habitantes=int(input("Introduce un número de habitantes: "))
        mayor_num_hab(db,habitantes)
        opcion=int(input("Elige una opción: "))
    elif opcion==3:
        nombre=input("Introduce el nombre de la provincia: ")
        loc_provincias(db,nombre)
        opcion=int(input("Elige una opción: "))
    elif opcion==4:
        localidad={}
        localidad["nombre"]=input("Nombre: ")
        localidad["ciudadanos"]=int(input("Número de ciudadanos: "))
        localidad["cp"]=int(input("Introduce un código postal de la localidad: "))
        nom_provincia=input("Provincia a la que pertenece: ")
        if not check_provincias(db,nom_provincia):
            print("La provincia no existe, introduce los datos de la misma: ")
            while not check_provincias(db,nom_provincia):
                n_provincia={}
                n_provincia["provname"]=nom_provincia
                n_provincia["ca"]=input("Introduce la comunidad autónoma a la que pertenece: ")
                crear_prov(db,n_provincia)
        localidad["provno"]=saber_provno(db,nom_provincia)
        crear_loc(db,localidad)
        opcion=int(input("Elige una opción: "))
    elif opcion==5:
        prov=input("Introduce el nombre de la provincia a borrar: ")
        borrar_provincia(db,prov)
        opcion=int(input("Elige una opción: "))
    elif opcion==6:
        locname=input("Introduce la localidad a actualizar sus habitantes :")
        act_hab=input("Introduce el nuevo número de habitantes")
        upd_habitantes(db,act_hab,locname)
        opcion=int(input("Elige una opción: "))
    else:
        print("Opción incorrecta, pulsa 8 para ver el menú")
        opcion=int(input("Elige una opción: "))
print("Adiós! ")