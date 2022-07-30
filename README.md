# Documentación

Para utilizar el programa es necesario colocarse en el path de la carpeta y correr el comando:

> py .\buda.py \<color del tren\> \<estación inicio\> \<estación final\> \<nombre test.txt\>

Por ejemplo, puedes correrlo usando:

> py .\buda.py red D H test1.txt
(retorna **['D', 'C', 'G', 'H']**)

> py .\buda.py green C F test1.txt
(retorna **['C', 'D', 'E', 'F']** que es la misma distancia que tomando el camino **['C', 'G', 'H', 'I', 'F']**)

> py .\buda.py green C F test1.txt
(retorna **['C', 'G', 'H', 'I', 'F']**)


El test1.txt es el mismo ejemplo que se muestra en el enunciado de la Tarea 2, por lo que puedes probar distintas combinaciones de donde puede ir el tren.

Para realizar la tarea se crearon 2 clases, **Station** y **Map**, la primera contiene información sobre una estación, nos dice que color tiene, cual es su nombre y cuales son los terminales a los que puede alcanzar. Por otra parte la clase **Map** contiene a todas las estaciones, por lo que puede generar un mapa general de la red de metro. Para realizar la busqueda del camino mas corto se utilizó una especie de algoritmo de **<a href= https://en.wikipedia.org/wiki/Breadth-first_search>BFS</a>**, pero con modificaciones, se habría podido aplicar directamente si no fuese por los colores de las estaciones que cambian un poco el ejercicio, por lo que a pesar de usar **BFS** igualmente se buscan todas las posibilidades dentro del mapa. Otra posible solución pudo ser utilizar **Branch and Bound** para hacer mas fácil el problema de optimización.


Los casos bordes vistos son:
- El tren no puede iniciar o terminar en un color que no es su color (tren rojo no puede iniciar o terminar en una estación distinta de roja) (**py .\buda.py red D I test1.txt**)

- El tren "no quiere moverse", es decir, el punto inicial es igual al punto final (**py .\buda.py red A A test1.txt**)

- Los colores utilizados por los terminales y los trenes deben estar previamente definidos en la variable "valid_colors", usar un color que no aparece ahí hace que no funcione el programa. (**py .\buda.py rojo A A test1.txt**)

- La estación de inicio o termino no existen (**py .\buda.py red X Y test1.txt**)

- Si la estación final no es alcanzable (no hay un camino que conecté la estación inicial con la estación final) se retorna una lista vacía que se traduce a que no existe un camino que una esas 2 estaciones (**py .\buda.py red A E test3.txt**)

- Se evita la posibilidad de generar loops infinitos dentro de una ruta (cualquier ejemplo de los de arriba)