﻿""" Las listas en acción
Dejemos de lado las listas por un breve momento y veamos un tema intrigante.

Imagina que necesitas reorganizar los elementos de una lista, es decir, revertir el orden de los elementos: el primero y el quinto, así como el segundo y cuarto elementos serán intercambiados. El tercero permanecerá intacto.


Pregunta: ¿Cómo se pueden intercambiar los valores de dos variables?

Echa un vistazo al fragmento:"""

variable1 = 1
variable2 = 2

variable2 = variable1
variable1 = variable2 

# Si haces algo como esto, perderás el valor previamente almacenadoenvariable2. Cambiar el orden de las tareas no ayudará. Necesitas una tercera variable que sirva como almacenamiento auxiliar.

# Así es como puedes hacerlo:

variable1 = 1
variable2 = 2

auxiliar = variable1
variable1 = variable2
variable2 = auxiliar 

# Python ofrece una forma más conveniente de hacer el intercambio, echa un vistazo:

variable1 = 1
variable2 = 2

variable1, variable2 = variable2, variable1 