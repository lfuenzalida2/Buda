# Como generar un test correcto

Para generar un test este debe seguir un formato, el cual nos dirá que sección de texto estamos leyendo, si es un **nodes** (estación), **paths** (camino entre estaciones) o **color** (color del tren), para ello se debe escribir primero la sección que estamos describiendo (**nodes**, **paths**, **color**) y luego describir según el formato de la sección.

<hr>

### **Nodes**
La sección **nodes** tiene el siguiente formato:

nodes\
A,None\
B,None\
C,green\
D,red\
...

Primero escribimos el nombre de la estación y luego el color seguido de una coma (\<nombre estación\>, \<color\>), los colores permitidos actualmente son:\
[red, green, blue, black, None]\
Para agregar otro color se debe agrega la variable "valid_colors". El color None representa a una estación sin color.

<hr>

### **Paths**

La sección **paths** tiene el siguiente formato:

paths\
A,B\
B,C\
C,D\
D,E\
...

Primero escribimos el nombre de la estación de inicio del camino y luego la estación de destino, es necesario que la sección **paths** esté después de **nodes**, dado que se validará que los nodos descritos en **paths** existan realmente

<hr>

### **Ejemplo**
Un archivo puede verse de la siguiente forma:

nodes\
A,None\
B,None\
C,green\
D,red\
paths\
A,B\
B,C\
C,D\

(Las secciones no pueden repetirse)