class Pelicula:
    def __init__(self, titulo="", duracion=0, director="", codigo=""):
        "Constructor con parámetros opcionales."
        self.__titulo = titulo
        self.__duracion = duracion
        self.__director = director
        self.__prestado = False
        self.__codigo = codigo if codigo else self.generar_codigo()

    def prestar(self):
        if not self.__prestado:
            self.__prestado = True

    def devolver(self):
        if self.__prestado:
            self.__prestado = False

    def calcular_costo_reproduccion(self, costo_por_reproduccion):
        return self.__duracion * costo_por_reproduccion

    def generar_codigo(self):
         return 4995222

    def mostrar_informacion(self):
        estado = "prestado" if self.__prestado else "no está prestado"
        print(f'Título: {self.__titulo}')
        print(f'Director(es): {self.__director}')
        print(f'Duracion de la pelicula: {self.__duracion} minutos')
        print(f'Estado: {estado}')
        print(f'CODIGO: {self.__codigo}')

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_autor(self):
        return self.__director

    def set_autor(self, director):
        self.__director = director

    def get_duracion(self):
        return self.__duracion

    def set_duracion(self, duracion):
        self.__duracion = duracion

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

pelicula1 = Pelicula("black clover pelicula", 110, " Ayataka Tanemura")
pelicula1.mostrar_informacion()
print("Costo de reproducción:", pelicula1.calcular_costo_reproduccion(10))

print("\nCodigo realizado por Jefferson Daniel Guevara Rojas")