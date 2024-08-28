'''
lista = ["juan", "maria", "carlos"] #string o cadena de texto

diccionario = { 
    "nombre":"Diego",
    "edad":25, "profesion":"profesor" }

productos = {
    "televisor":15000,
    "celular":30000,
    "portatil":160000
}

nombres = {
    "nombre":"carlos",
    "edad":20,
    "cursos":["Python","Javascript","Nodejs"]
}

print(nombres["nombre"])
print(nombres["edad"])
print(nombres["cursos"])
print(nombres["cursos"][1])

notas_estudiantes = {
    "Juan":[2.5,3,4.6],
    "Ana":[3.5,4.6,4.9],
    "Luis":[4,2.5,3.9]
}

'''
#print (notas_estudiantes["Juan"])


#-------------Agregar datos a un diccionario--------------
'''
miDiccionario = {
    "nombre":"Sara",
    "edad":30
}

miDiccionario["profesion"] = "instructora"

print(miDiccionario)

'''
#-------------Editar datos de un diccionario--------------
'''
miDiccionario["edad"] = 31

print(miDiccionario)

'''
#------------Eliminar datos de un diccionario-------------

'''
miDiccionario = {
    "nombre":"Sara",
    "edad":30,
    "profesion":"instructora"
}

print(miDiccionario)

del miDiccionario["profesion"]
print(miDiccionario)

prof = miDiccionario.pop("profesion")

print(prof)
print(miDiccionario)

'''
#-------------- Agregar multiples valores ----------------

miDiccionario = {
    "nombre":"Sara",
    "edad":30,
    "profesion":"instructora"
}

nuevosDatos = {
    "ciudades_de_colombia":"Cali",
    "documento":1234567,
    "telefono":22222
}

for clave, valor in nuevosDatos.items():
    print(clave)

print("nuevos datos: ",nuevosDatos["documento"]) #1234567
for clave, valor in nuevosDatos.items():
    miDiccionario[clave] = valor

print(miDiccionario)

