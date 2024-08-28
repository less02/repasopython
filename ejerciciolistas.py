#______________________EJECICIO1________________________

#Escribe un programa en Python que permita al usuario crear una lista de compras. El programa debe solicitar al usuario que ingrese el nombre de los productos uno por uno y los agregue a la lista. Una vez que el usuario haya terminado de agregar productos, el programa debe imprimir la lista completa de compras en orden.


#Requisitos:


#El programa debe permitir al usuario ingresar productos hasta que decida detenerse.

#Después de ingresar cada producto, el usuario debe ser preguntado si desea agregar otro producto.

#Si el usuario decide que no quiere agregar más productos, el programa debe mostrar la lista completa de compras.



#Paso 1: Imiciar con la lista vacia

'''lista = []

while True:
    producto = input("Introduce un producto para la lista de compras: ")
    
    lista.append(producto)
    
    continuar = input("¿Desea agregar otro producto a la lista? (si/no): ").lower()
    
    if continuar == "no":
        break

print("\n Tu lista de compra es:")

for item in lista:
    print(f"-{item}") #recorre toda la lista, se almacena y imprime, la f es una forma de permitir la concatenacion'''
    

#______________________EJECICIO2________________________  

#Escribe un programa en Python que solicite al usuario ingresar una lista de números enteros. Luego, el programa debe calcular e imprimir la suma de todos los números ingresados. El programa debe continuar solicitando números hasta que el usuario decida dejar de ingresar más.

#Requisitos:

#El programa debe permitir al usuario ingresar números uno por uno.

#Después de ingresar cada número, el usuario debe ser preguntado si desea agregar otro número.

#Si el usuario decide que no quiere agregar más números, el programa debe calcular y mostrar la suma total de los números ingresados.

'''
listaEntero = []

while True:
    numeroEntero = int(input("Ingrese un numero entero: "))
    listaEntero.append(numeroEntero)
    
    otroEntero = (input("Desea ingresar otro numero entero? (si/no): ")).lower()
    
    if otroEntero == "no":
        break
    
suma = sum(listaEntero)

print("\n La suma de los número enteros almacenados es la siguiente: ", suma)
'''  
    
#______________________EJECICIO3________________________ 

#Escribe un programa en Python para gestionar una lista de contactos. 
#El programa debe permitir al usuario realizar las siguientes operaciones:

#Agregar un contacto a la lista, incluyendo un nombre y un número de teléfono.

#Eliminar un contacto de la lista especificando el nombre del contacto.

#Mostrar todos los contactos en la lista, con el formato "Nombre: Número de teléfono".

#El programa debe mostrar un menú con las opciones disponibles y seguir funcionando hasta que el usuario elija salir. Asegúrate de manejar situaciones en las que el usuario intente eliminar un contacto que no está en la lista y que el programa informe adecuadamente al usuario.

#Requisitos:

#El programa debe permitir al usuario ingresar contactos con un nombre y un número de teléfono.
#Debe ser posible eliminar un contacto buscando por el nombre.
#Debe mostrar todos los contactos en la lista en un formato claro.
#El programa debe seguir ejecutándose hasta que el usuario decida salir.

'''
ListaUsuarios = []
ListaNumeros = []


while True:
    
    usuario = input("Ingresa tu nombre: ")
    numero = int(input("Ingresa tu número de teléfono: "))
    
    ListaUsuarios.append(usuario)
    ListaNumeros.append(numero)
    
    otroUsuario = input("¿Desea ingresar otro usuario? (si/no): ").lower()
    
    if otroUsuario == "no":
        break
    
print("\nLa lista de contacto es la siguiente:")

for usuario, numero in zip(ListaUsuarios, ListaNumeros):
    print(f"- {usuario}: {numero}") #Esto permite iterar sobre ambas listas al mismo tiempo, emparejando cada usuario con su respectivo número.

#Eliminar contacto 

EliminarContacto = input("Desea eliminar un contacto de su lista de contactos? (si/no): ")

for usuario, numero in zip(ListaUsuarios, ListaNumeros):
    print(f"- {usuario}: {numero}") #Esto permite iterar sobre ambas listas al mismo tiempo, emparejando cada usuario con su respectivo número.
    
    if EliminarContacto == "si":
        
        contactoAeliminar = int(input(f"Cual de tus contactos deseas eliminar?, siendo 0 el primero contacto, 1 el segundo, 2 el tercero y así sucesivamente: "))
    
        # Verifica si el índice está en el rango correcto
        if 0 <= contactoAeliminar < len(ListaUsuarios):
            
            # Elimina el contacto seleccionado
            usuarioEliminado = ListaUsuarios.pop(contactoAeliminar)
            numeroEliminado = ListaNumeros.pop(contactoAeliminar)
            print(f"\n El contacto {usuarioEliminado}: {numeroEliminado} ha sido eliminado.")
        else:
            print("El número ingresado no es válido.")
    else:
        print("No se ha eliminado ningún contacto.")

    # Muestra la lista actualizada
    print("\nLista de contactos actualizada:")
    for usuario, numero in zip(ListaUsuarios, ListaNumeros):
        print(f"- {usuario}: {numero}")
'''       

#______________________EJECICIO4________________________

#Escribe un programa en Python que permita al usuario crear una lista de sus películas favoritas.

#El programa debe permitir al usuario realizar las siguientes acciones:

#Agregar una película a la lista.

#Eliminar una película especificando su nombre.

#Mostrar todas las películas en la lista.

#Buscar si una película específica está en la lista.

#El programa debe ofrecer estas opciones en un menú y continuar funcionando hasta que el usuario decida salir.
'''
listaDePeliculasFavoritas = []

#primera parte
while True: 
    pelicula = int(input("Ingrese una pelicula: "))
    listaDePeliculasFavoritas.append(pelicula)
    
    otraPelicula = (input("Desea ingresar otra pelicula? (si/no): ")).lower()
    
    if otraPelicula == "no":
        break
    
print("\n Tu lista de peliculas es la siguiente:")

for pelicula in listaDePeliculasFavoritas:
    print(f"-{pelicula}") #recorre toda la lista, se almacena y imprime, la f es una forma de permitir la concatenacion
''' 

def CrearListaDePeliculasFavoritas():
    listaDePeliculasFavoritas = []
    while True:
        peliculaFavorita = input("Ingresa tu pelicula favorita: ").lower()
        listaDePeliculasFavoritas.append(peliculaFavorita)
    
        otraPeliculaFavorita = input("Desea ingresar otra pelicula favorita? (s/n): ").lower()
    
        if otraPeliculaFavorita == "n":
            break
    
    return listaDePeliculasFavoritas   

def AgregarPelicula(lista): #lista, la funcion va a utilizar la informacion que hay en lista
    nuevaPelicula = input("Que pelicula deseas agregar ?").lower()
    
    if nuevaPelicula in lista:
        print("La pelicula ya se encuentra almacenada")
        
    else:
        lista.append(nuevaPelicula)
        print("La pelicula a sido agregada con éxito")
 
#para nombrar funciones siempre tu funcion debe comenzar con mayuscula
#si la funcion es una palabra compuesta debe escribirse con ambas mayusculas
#ejemplo AgregarProducto, EliminarUsuario, etc...
#-->para nombrar variables existen dos formas, camelCase y snake_case, ambas son aceptadas
#tener en cuenta que si se usa una u otra en todo el codigo se debe usar la misma regla para nombrar tus variables
#ejemplo si vas a nombrar una variable en camelCase esta se ve de esta manera diccionarioDeVestidos, peliculasDeTerror
#humanos, nacionalidadesSudamericanas......si por el contrario decides usar snake_case seria diccionario_de_vestidos,
#peliculas_de_terror, humanos, nacionalidades_sudameticanas, etc...
#si usas tus variables en snake_case, las claves que sean en camelCase y si usas tus variables en camelCase las claves deben ser
#en snake_case....personalmente yo uso mis variablen en camelCase y las claves en snake_case.

def EliminarPelicula(lista): #eliminar pelicula de una lista
    peliculaEliminada = input("Ingrese el nombre de la película que desea eliminar: ").lower()
    
    if peliculaEliminada in lista:
        lista.remove(peliculaEliminada)
        print(f"La película '{peliculaEliminada}' ha sido eliminada de la lista.")
            
    else:
        print("La película no se encuentra en la lista.")
        
def MostrarPeliculas(lista):
    print(lista)

def BuscarPelicula(lista):
    peliculaBuscada = input("Ingresa la pelicula que deseas buscar: ").lower()
    
    if peliculaBuscada in lista:
        print(f"La pelicula {peliculaBuscada} si se encuentra disponible en tu lista")
  
    else:
        print("Tu pelicula no se encuentra almacenada")
        
def Menu():
    print("-------------------------------MENU---------------------------------")
    print("Buscar pelicula (1) - Agregar Pelicula(2) - Eliminar Pelicula(3) - Mostrar Peliculas(4)")
    peticion = int(input("Que deseas hacer?, si deseas buscar una pelicula ingresa (1), si deseas agregar una pelicula ingresa (2), si deseas eliminar una pelicula ingresa (3), si deseas mostras tus peliculas ingresa (4)"))
    
    return peticion

while True:
    print("---------------BIENVENIDO A TU ALMACÉN DE PELÍCULAS-----------------")     
    print("Crea tu lista de películas favoritas")
    
    listaDePeliculasFavoritas = CrearListaDePeliculasFavoritas()
    
    while True:
        peticion = Menu()
        
        if peticion == 1:
            BuscarPelicula(listaDePeliculasFavoritas)
        
        elif peticion == 2:
            AgregarPelicula(listaDePeliculasFavoritas)
        
        elif peticion == 3:
            EliminarPelicula(listaDePeliculasFavoritas)
        
        elif peticion == 4:
            MostrarPeliculas(listaDePeliculasFavoritas)
        
        else:
            print("Su marcación es inválida.")
        
        volverMenu = input("¿Deseas volver al menú? (s/n): ").lower()
        
        if volverMenu == "n":
            salirAplicacion = input("¿Deseas salir de la aplicación? (s/n): ").lower()
            if salirAplicacion == "s":
                print("Gracias por usar el almacén de películas. ¡Hasta luego!")
                exit()  # Termina la ejecución del programa
            else:
                break  # Sale del bucle del menú y vuelve al menú principal


#______________________EJECICIO5________________________

#Escribe un programa en Python para gestionar una lista de tareas pendientes. El programa debe implementar un CRUD (Crear, Leer, Actualizar, Eliminar) para las tareas y permitir al usuario realizar las siguientes acciones:

#Crear una nueva tarea: Añadir una tarea a la lista con una descripción y una fecha de vencimiento.

#Leer todas las tareas: Mostrar todas las tareas actuales, incluyendo su descripción y fecha de vencimiento.

#Actualizar una tarea: Modificar la descripción y/o la fecha de vencimiento de una tarea existente especificando su número de identificación.

#Eliminar una tarea: Eliminar una tarea de la lista especificando su número de identificación.

#El programa debe ofrecer un menú de opciones y seguir funcionando hasta que el usuario decida salir. Asegúrate de manejar situaciones en las que el usuario intente realizar acciones sobre tareas que no existen y proporciona mensajes adecuados.

#Requisitos:

#El programa debe permitir al usuario ingresar una descripción y una fecha de vencimiento para cada nueva tarea.

#Cada tarea debe tener un identificador único que se utiliza para actualizar o eliminar la tarea.

#El programa debe mostrar todas las tareas en un formato claro.

#El usuario debe poder actualizar la descripción y/o la fecha de vencimiento de una tarea.

#El usuario debe poder eliminar una tarea especificando su identificador.