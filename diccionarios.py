# Diccionario: 
# Es una colección de datos que se alamacena en pares de clave-valor.
# 1. Un diccionario comienza y termina con llaves (curly braces {}).
# 2. Cada par de clave-valor se separa por dos puntos (:).
# 3. Cada elemento (propiedad) del diciconario se separan por comas (,).
# 4. Cada clave es un String (cadena de texto).
# 5. Cada valor puede ser de cualquier tipo de dato.

#Ejemplo:
# Que almacene los datos de un pais.

pais1 = {
            'nombre': 'Colombia',
            'capital': 'Bogotá',
            'moneda': 'Peso Colombiano',
            'ciudades_principales' : [
                                          'Barranquilla',
                                          'Medellín',
                                          'Cali',
                                    ],
            'poblacion' : {
                             'Censo' : 50.3,
                             'Densidad' : 45,
                        }
      }

pais2 = {
            'nombre': 'Ecuador',
            'capital': 'Quito',
            'moneda': 'Dolar',
            'ciudades_principales' : [
                                          'Guayaquil',
                                          'Cuenca',
                                          'Ambato',
                                    ],
            'poblacion' : {
                             'Censo' : 17.2,
                             'Densidad' : 30,
                        }
      }

pais3 = {
            'nombre': 'Paraguay',
            'capital': 'Asunción',
            'moneda': 'Guaraní',
            'ciudades_principales' : [
                                          'Encarnación',
                                          'San Lorenzo',
                                          'Villa Rica',
                                    ],
            'poblacion' : {
                             'Censo' : 6.8,
                             'Densidad' : 10,
                        }
      }

#Acceder a la información del diccionario (pais)
# print(pais1['nombre'])
print(pais1['capital'])
print(pais1['moneda'])

# Acceder a una ciudad del pais1
print(pais1['ciudades_principales'][1])
print("---------------")
# Iterar las ciudades del pais1
for ciudad in pais1['ciudades_principales']:
    print(ciudad)
    
print("---------------")
# Iterar el diccionario pais2
for ciudad in pais2['ciudades_principales']:
    print(ciudad)

print("---------------")
# Iterar el diccionario pais3
for ciudad in pais3['ciudades_principales']:
    print(ciudad)

#Acceder a datos poblacionales pais1
print("---------------")
print("Censo: ", pais1['poblacion']['Censo'], "millones de habitantes")
print("Densidad: ", pais1['poblacion']['Densidad'], "personas por km2")