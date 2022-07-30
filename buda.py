import sys

# Se define una lista de colores validos para las estaciones, None representa una estación sin color
valid_colors = ["red", "green", "blue", "black", None]

# Función utilizada para ordenar una lista a partir de su segundo elemento
def take_second(elem):
    return elem[1]

# Se define la clase estación que representa a una estación en especifico con nombre "station" y de color "color"
class Station:
    def __init__(self, station: str, color: str) -> None:
        assert color in valid_colors, f"La estación '{station}' no tiene un color valido {valid_colors}"
        self.station = station
        self.color = color
        self.next_station = list()

# Clase que contiene el mapa completo del metro
class Map:
    def __init__(self, map_path: str, train_color: str, start: str, end: str) -> None:
        # Lista que contiene el nombre de los nodos instanciados, permite un acceso mas rápido y limpio a la validación de datos
        self.valid_nodes = list()
        self.stations = dict()
        self.read_map(map_path)

        # Si el tren no tiene color entonces que su color sea None
        train_color = None if train_color == "None" else train_color
        self.train_color = train_color
        
        # Colocar assert que revise si start y end son nodos validos
        assert start in self.valid_nodes, "La estación de inicio no existe"
        assert end in self.valid_nodes, "La estación de fin no existe"

        if train_color != None and (self.stations[start].color != None or self.stations[end].color != None):
            assert self.stations[start].color == train_color or self.stations[end].color == train_color, "El tren no puede realizar este viaje, el inicio o el fin no corresponden a los colores que puede recorrer el tren"

        self.start = start
        self.end = end

    # Función que lee el archivo .txt e instancia las variables
    def read_map(self, path: str) -> None:  
        # Definimos las secciones validas e instanciamos la variable de section
        valid_sections = ["nodes", "paths", "color"]
        section = None
        with open(path) as file:
            for line in file:
                # Revisamos en que sección del archivo estamos (nodes, paths o color)
                if line.rstrip() in valid_sections:
                    section = line.rstrip()
                    continue
                
                # Leemos la sección nodes y generamos las estaciones del mapa
                if section == "nodes":
                    self.nodes_section(line.rstrip())
                
                # Leemos la sección paths y generamos los caminos del mapa
                elif section == "paths":
                    self.paths_section(line.rstrip())

    
    def nodes_section(self, line: str) -> None:
        node = line.split(",")
        # Transformamos el string "None" al valor None
        node[1] = None if node[1] == "None" else node[1]
        self.stations[node[0]] = Station(node[0], node[1])

        # Nos aseguramos de que no hayan estaciones duplicadas
        assert node[0] not in self.valid_nodes, f"La estación '{node[0]}' se ha instanciado mas de una vez en el archivo de lectura"
        self.valid_nodes.append(node[0])
                    
    def paths_section(self, line: str) -> None:
        path = line.split(",")

        # Revisamos que ambas estaciones del camino sean estaciones existentes
        assert path[0] in self.valid_nodes, f"La estación {path[0]} no existe, revisar la linea {line}"
        assert path[1] in self.valid_nodes, f"La estación {path[1]} no existe, revisar la linea {line}"

        # Agregamos la siguiente estacion al camino inicial (path[0] -> path[1])
        self.stations[path[0]].next_station.append(path[1])
        # Agregamos el camino en el otro sentido (path[1] -> path[0])
        self.stations[path[1]].next_station.append(path[0])

    # Usamos algoritmo de busqueda BFS porque este siempre encontrará el camino mas corto de un punto A a un punto B
    def calculate_best_route(self) -> list:
        """
        Lo que se hace en esta función es utilizar BFS para encontrar la ruta mas cercana, a bajo nivel lo que se hace es
        tener una lista de listas que se le agregan los distintos camino a examinar, por lo que siempre va a revisar los caminos de menor nivel
        """
        saved_paths = list()
        if self.start == self.end:
            return [self.start]
        paths = [[self.start]]
        paths_length = [0]
        for path in paths:
            actual_node = path[-1]
            if self.end in self.stations[actual_node].next_station:
                path_pos = paths.index(path)
                saved_paths.append((path + [self.end], paths_length[path_pos]))
            else:
                path_pos = paths.index(path)
                for station in self.stations[actual_node].next_station:
                    if station in path:
                        continue
                    paths.append(path + [station])
                    adding_value = 1 if self.stations[station].color == self.train_color or self.stations[station].color == None else 0
                    paths_length.append(paths_length[path_pos] + adding_value)
        
        # Ordenamos todos los caminos que encontramos segun la cantidad de paradas que se hacen 
        saved_paths.sort(key=take_second)
        if len(saved_paths) == 0:
            return []
        return saved_paths[0][0]

# Obtenemos los argumentos de la línea de comando
_, train_color, start, end, test = sys.argv

# Revisamos que el tren tenga un color valido
assert train_color in valid_colors, f"El tren no tiene un color valido, por favor elegir entre {valid_colors}"

# Cargamos el mapa del metro que está en el archivo "tests/test1.txt"
route = Map("tests/" + test, train_color, start, end)
print(route.calculate_best_route())