class ExcepcionDatosAlumnos(Exception):
	pass

class LineaErronea(ExcepcionDatosAlumnos):
	def __init__(self):
	 	super().__init__("¡Error en alguna linea del archivo!")

class ArchivoVacio(ExcepcionDatosAlumnos):
	def __init__(self):
	 	super().__init__("¡El archivo está vacío!")

##############################################
			# P R O G R A M A #
##############################################

archivo = input("introduce el nombre del archivo: ")		# Solicito el archivo al usuario

lista = ""
lista_nombres = []
dicc_alumnos = {}

try:
	with open(archivo + ".txt","r") as a:
		leer = a.readlines()	# Añadimos todas las lineas del archivo a una variable como una lista.
		
		
	if len(leer)==0:	# Indico que si la variable que guarda las lineas de archivo es de largo 0, lance error de que el archivo está vacío.
		raise ArchivoVacio

	lista = "".join(leer).split() # Limpio los caracteres de formato y lo meto en una lista todo limpio ya.

	for i in lista:

		if i.isalpha():
			lista_nombres.append(i)
			# Guardo los nombres en una lista

		elif not i.isalpha():		# Cuando ya he recorrido el nombre y apellido, los añado como Key de diccionario y la nota la introduzco como valor.

			if len(lista_nombres) != 2:
				raise LineaErronea	# En caso de no tener el nombre y apellido almacenado lanzo el error de linea ya que me indica que la estructura de la linea está mal.
				
			if " ".join(lista_nombres) in dicc_alumnos.keys():
				dicc_alumnos[" ".join(lista_nombres)] += float(i)

			else:
				dicc_alumnos[" ".join(lista_nombres)] = float(i)
			lista_nombres = []
				# Si los nombres figuran como Key ya en el diccionario sumo el valor al ya existente y sino lo añado por primera vez.
				# Por ultimo limpio la lista de nombres.

	for keys,values in sorted(dicc_alumnos.items()):	# Recorro las keys y values del diccionario y las imprimo ya ordenadas.
		print(keys,values)	

except ArchivoVacio as e:
	print(e)

except LineaErronea as a:
	print(a)


