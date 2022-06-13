# Estudiante: Keyber Yosnar Sequera Avendaño
# Carnet: 16-11120

# Problema 3: Simulador de manejador de memoria.

# Memoria como lista doblemente enlazada:

class Error(Exception):
    pass

class Nodo:
    def __init__(self, nombre = None, espacio = None, anterior = None, siguiente = None ):
        self.nombre = nombre
        self.espacio = espacio
        self.anterior = anterior
        self.siguiente = siguiente

class Memoria:
    # Creamos el constructor de la memoria:
    def __init__(self, tamanioMemoria = None):
        self.tamanioMemoria = tamanioMemoria
        self.primerBloque = Nodo(None, tamanioMemoria, None, None)
    
    # Calculamos la potencia de dos más cercana a un número:
    def encontrar_potencia_de_dos_mas_cercana(self, numero):
        '''
        Se encuentra el múltiplo de dos más cercano al número dado
        '''
        # Se verifica que el número no menor o igual a cero:
        if (numero <= 0):
            raise Error(f"Error, no se puede encontrar el multiplo mas cercado a {numero}")
        # Se halla el múltiplo de dos más cercano a numero:
        potencia = 0
        potencia_de_dos = 2**potencia
        if (numero != 1):
            while (potencia_de_dos < numero):
                potencia += 1
                potencia_de_dos = 2**potencia
        else:
            pass
        return (potencia_de_dos)
    
    # Creamos una manera de reservar memoria:
    def reservar(self, id, cantidad):
        # Definimos las variables que usaremos:
        nodo = self.primerBloque
        identificador_en_memoria = False
        bloque_asignado = False
        potencia_de_dos_mas_cercana = self.encontrar_potencia_de_dos_mas_cercana(cantidad)

        # Verificamos que "nombre" ya no tenga memoria reservada:
        while (nodo != None):
            if (nodo.nombre == id):
                identificador_en_memoria = True
                break
            else:
                nodo = nodo.siguiente

        # Hallamos la potencia de dos más cercana por arriba a la cantidad de
        # de memoria que se quiere reservar:
        nodo = self.primerBloque
        while (nodo != None and identificador_en_memoria == False and bloque_asignado == False):
            # Si el bloque actual no tiene elemento siguiente:
            if (nodo.siguiente == None):
                # Si el bloque actual es una potencia más grande de la
                # requerida, y el bloque está vacío lo partimos en dos:
                if (nodo.espacio > cantidad and nodo.nombre == None):
                    nodo.siguiente = Nodo(None, nodo.espacio // 2, nodo, None)
                    nodo.espacio = nodo.espacio // 2
                    nodo = self.primerBloque
                # Si el bloque cabe en el espacio actual y este está vacío
                # metemos la información aquí:
                elif (nodo.espacio == cantidad and nodo.nombre == None):
                    nodo.nombre = id
                    bloque_asignado = True
                # Si no cabe exploramos o los bloques estaban ocupados
                # exploramos el siguiente nodo:
                else:
                    nodo = nodo.siguiente
            # Si el bloque actual tiene elemento siguiente:
            else:
                # Si el bloque actual es una potencia más grande de la
                # requerida, y el bloque está vacío lo partimos en dos:
                if (nodo.espacio > cantidad and nodo.nombre == None):
                    nodo_auxiliar = nodo
                    nodo.siguiente.anterior = Nodo(None, nodo.espacio // 2, nodo, nodo.siguiente)
                    nodo.siguiente = Nodo(None, nodo.espacio // 2, nodo, nodo.siguiente)
                    nodo.espacio = nodo.espacio // 2
                    nodo = self.primerBloque
                # Si el bloque cabe en el espacio actual y este está vacío
                # metemos la información aquí:
                elif (nodo.espacio == cantidad and nodo.nombre == None):
                    nodo.nombre = id
                    nodo.siguiente.anterior = nodo
                    bloque_asignado = True
                # Si no cabe exploramos o los bloques estaban ocupados
                # exploramos el siguiente nodo:
                else:
                    nodo = nodo.siguiente
        
        # Imprimimos los mensajes de error en caso de que ocurrieran:
        if (identificador_en_memoria == True):
            print(f"Error, no se pudo reservar espacio para '{id}' puesto que ya se encuentra en la memoria.")
            bloque_asignado = True
        if (bloque_asignado == False):
            print(f"Error, no se pudo agregar a '{id}' en memoria puesto que no hay espacio suficiente.")

    # Creamos una función que pueda unir los bloques adyacentes
    # de la partición de un bloque que estén vacíos:
    def unir_bloques_libres_de_particion(self):
        nodo = self.primerBloque
        no_hay_mas_uniones = False

        while (no_hay_mas_uniones == False):
            # Si hay más de un bloque en la memoria:
            if (nodo.siguiente != None):
                # Si el nodo siguiente tiene el mismo tamanio que el actual:
                if (nodo.siguiente.espacio == nodo.espacio):
                    # Si ambos están vacíos entonces puede que los deba unir:
                    if (nodo.siguiente.nombre == None and nodo.nombre == None):
                        # Si no hay un bloque anterior, puedo unir los bloques:
                        if (nodo.anterior == None):
                            nodo.espacio = nodo.espacio * 2
                            nodo.siguiente.anterior = nodo
                            nodo.siguiente = nodo.siguiente.siguiente
                            nodo = self.primerBloque
                        # Si hay un bloque anterior me aseguro que los bloques
                        # tengan distinto tamaño:
                        else:
                            if (nodo.anterior.espacio != nodo.espacio):
                                nodo.espacio = nodo.espacio * 2
                                nodo.siguiente.anterior = nodo
                                nodo.siguiente = nodo.siguiente.siguiente
                                nodo = nodo.primerBloque
                    else:
                        nodo = nodo.siguiente
                else:
                    nodo = nodo.siguiente
            # Estamos en el único bloque de la memoria:
            else:
                no_hay_mas_uniones = True

    # Creamos una manera de liberar memoria:
    def liberar(self, id):
        # Definimos las variables que usaremos:
        nodo = self.primerBloque
        identificador_en_memoria = False
        
        # Comprobamos que el elemento esté en la memoria para poder
        # liberarlo:
        while (nodo != None):
            if (nodo.nombre == id):
                identificador_en_memoria = True
                break
            else:
                nodo = nodo.siguiente
        
        # Procedemos a liberar al elemento si está en el memoria:
        nodo = self.primerBloque
        while (nodo != None and identificador_en_memoria == True):
            if (nodo.nombre == id):
                # Caso en el que haya un objeto que ocupe toda la memoria:
                if (nodo.espacio == self.tamanioMemoria):
                    nodo.nombre = None
                else:
                    nodo.nombre = None
                    # Verifico que el bloque a la derecha no sea nulo:
                    if (nodo.siguiente != None):
                        # Si el nodo siguiente está vacío y tiene el mismo espacio
                        # del bloque que queremos liberar:
                        if (nodo.siguiente.espacio == nodo.espacio):
                            if (nodo.siguiente.nombre == None):
                                # Si estamos en el primer elemento unimos los bloques:
                                if (nodo.anterior == None):
                                    nodo.espacio = nodo.espacio * 2
                                    nodo.siguiente = nodo.siguiente.siguiente
                                    break
                                # Si hay un nodo anterior al actual
                                else:
                                    # Si el nodo anterior tiene un espacio distinto al actual
                                    # los uno:
                                    if (nodo.anterior.espacio != nodo.espacio):
                                        nodo.espacio = nodo.espacio * 2
                                        nodo.siguiente = nodo.siguiente.siguiente
                                        break
                                    # Si el nodo anterior está vacío y además tiene el mismo espacio que el
                                    # bloque actual:
                                    else:
                                        if (nodo.anterior.nombre == None):
                                            nodo.anterior.espacio = nodo.espacio * 2
                                            nodo.anterior.siguiente = nodo.siguiente
                                            break
                    else:
                        # Si estamos en el último bloque:
                        if (nodo.anterior != None):
                            # Si el bloque anterior tiene el mismo tamaño que el actual
                            # y está vacío unimos los bloques:
                            if(nodo.anterior.nombre == None and nodo.anterior.espacio == nodo.espacio):
                                nodo.anterior.espacio = nodo.espacio * 2
                                nodo.anterior.siguiente = nodo.siguiente
                                break
                    break
            else:
                nodo = nodo.siguiente
        # Verificamos que al liberar los bloques no queden más
        # bloques por unir:
        self.unir_bloques_libres_de_particion()

        # Si el identificador que se desea liberar no está en memoria
        # se muestra un mensaje acorde a la situación:
        if (identificador_en_memoria == False):
            print(f"Error, no se pudo liberar a '{id} de memoria, pues no esta en la memoria.'")

    # Creamos una función que imprima la lista enlazada:
    def mostrar(self):
        cadena = ""
        # Imprimimos todos los bloques que están libres:
        nodo = self.primerBloque
        while (nodo != None):
            if (nodo.nombre == None):
                print(f"Bloque libre de tamanio {nodo.espacio}.")
            nodo = nodo.siguiente
        # Imprimimos todos los bloques que están ocupados:
        nodo = self.primerBloque
        while (nodo != None):
            if (nodo.nombre != None):
                print(f"Bloque de tamanio {nodo.espacio} ocupado por {nodo.nombre}.")
            nodo = nodo.siguiente

memoria = Memoria(int(input("Escriba la cantidad de memoria que quiere reservar: ")))
decision = input('''> Que desea hacer sus opciones son:
RESERVAR <nombre> <cantidad>
LIBERAR <nombre>
MOSTRAR
SALIR
> ''')
decision = decision.split(" ")
while (decision[0].upper() != "SALIR"):
    if (decision[0].upper() == "RESERVAR"):
        memoria.reservar(decision[1], int(decision[2]))
    elif (decision[0].upper() == "LIBERAR"):
        memoria.liberar(decision[1])
    elif (decision[0].upper() == "MOSTRAR"):
        memoria.mostrar()
    else:
        pass
    decision = input("> ")
    decision = decision.split(" ")