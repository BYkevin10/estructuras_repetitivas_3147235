paises = [
            {
               'nombre' : 'Venezuela', 
               'capital' : 'Caracas',
               'moneda' : 'Bolivar',
               'poblacion' : 
                  {
                        'Censo' : 28.3,
                        'Densidad' : 30,
                  },
               'ciudades' : 
                  [
                        'Maracaibo',
                        'Valencia',
                        'Barquisimeto',
                        'Maracay',
                        'Carabobo',
                  ],
               'superficie' : 916445,
            },
            {
               'nombre' : 'Brasil', 
               'capital' : 'Brasilia',
               'moneda' : 'Real',
               'poblacion' :
                  {
                        'Censo' : 212.6,
                        'Densidad' : 25,
                  },
               'ciudades' :
                  [
                        'Sao Paulo',
                        'Rio de Janeiro',
                        'Salvador',
                        'Fortaleza',
                        'Belo Horizonte',
                  ],
               'superficie' : 8515767,
               
            },
            {
               'nombre' : 'Paraguay',
               'capital' : 'Asunción',
               'moneda' : 'Guarani',
               'poblacion' :
                  {
                        'Censo' : 6.8,
                        'Densidad' : 10,
                  },
               'ciudades' :
                  [
                        'Encarnación',
                        'San Lorenzo',
                        'Villa Rica',
                        'Ciudad del Este',
                        'Luque',
                  ],
               'superficie' : 406752,
            },
      ]

for pais in paises:
    print("Nombre:",pais['nombre'])
    print("Capital:",pais['capital'])
    print("Poblacion:")
    print("🔥Censo:",pais['poblacion']['Censo'])
    print("🔥Densidad:", pais['poblacion']['Densidad'])
    print("🔥Ciudades principales:")
    for ciudad in pais['ciudades']:
        print("😊",ciudad)
    print("🔥Superficie en Km²:",pais['superficie'])
    print("---------------")
    