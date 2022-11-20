# x = [ [5,2,3], [10,8,9] ] 
# estudiantes = [
#     {'first_name':  'Michael', 'last_name' : 'Jordan'},
#     {'first_name' : 'John', 'last_name' : 'Rosales'}
# ]
# directorio_deportes = {
#     'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
#     'futbol' : ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [ {'x': 10, 'y': 20} ]

# x[1][0]= 15

# print(x)

# estudiantes[0]["last_name"]="Bryant"
# print(estudiantes)

# directorio_deportes["futbol"][0]="Andres"
# print(directorio_deportes)

# z[0]["y"]=30
# print(z)

#-----------------------------------------------------------------------------------

# estudiantes2 = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]

# def iterate_dictionary(list):
#     for i in range(0, len(list)):
#         for valores in list[i].items():
#             print(valores)

# iterate_dictionary(estudiantes2)

#------------------------------------------------------------------------------------

estudiantes2 = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterate_dictionary2(nombre_llave,lista):
    for i in range(0, len(lista)):
        for llave,valor in lista[i].items():
            if llave == nombre_llave:
                print(valor)
iterate_dictionary2('first_name',estudiantes2)
iterate_dictionary2('last_name',estudiantes2)

#-----------------------------------------------------------------------------------

# dojo = {
#    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }

# def print_info(diccionario):
#     for llave,valor in diccionario.items():
#         print(f"{len(valor)}"  f"{llave}" + "\n")
#         for i in range(0, len(valor)):
#             print(valor[i])

# print_info(dojo)



