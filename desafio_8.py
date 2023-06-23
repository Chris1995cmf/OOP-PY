'''Integrantes Grupo 2:
- Santiago Francisco Risso
- Hector Gabriel Martinez
- Iara Abril Kauffman Cermak
- Christian Martín Fernández
- Bettiana Farias
- Brenda Uria
- Baez Dana
- Matías Nicolás Riquelme Tirado
- Eliana Gisel Gomez 
'''

from datetime import datetime, date

usuarios = []
publicaciones = []
comentarios = []

class Usuario:
    '''Clase Usuario
    
    Attributes:
        id (int, optional): id del usuario. Defaults to None.
        nombre (str, optional): Nombre del usuario. Defaults to None.
        apellido (str, optional): Apellido del usuario. Defaults to None.
        telefono (str, optional): Telefono del usuario. Defaults to None.
        username (str, optional): Username del usuario. Defaults to None.
        email (str, optional): Email del usuario. Defaults to None.
        fecha_registro (date, optional): Fecha de registro del usuario. Defaults to None.
        avatar (str, optional): avatar del usuario. Defaults to None.
        estado (bool, optional): Estado del usuario, si esta activo o no. Defaults to None.
        online (bool, optional): Si el usuario esta online o no. Defaults to None.    
    '''
    def __init__(self,id = None , nombre = None, apellido = None, telefono = None, username = None, email = None, contraseña = None, fecha_registro = None, avatar=None, estado=None, online=None) -> None:
        self.id=id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.username = username
        self.email = email
        self.contraseña = contraseña
        self.fecha_registro = fecha_registro
        self.avatar = avatar
        self.estado = True
        self.online = False
    
    def login(self):
        '''Verifica si las credenciales proporcionadas coinciden con las del 
        usuario y establece el estado de "online" en True si el inicio de 
        sesión es exitoso.

        Returns:
            Usuario: retorna el usuario si los credenciales son correctos.
            print(): imprime mensaje de error.
        '''
        username = input('Ingrese usuario: ')
        contraseña = input('Ingrese contraseña: ')
        for usuario in usuarios:
            if usuario.username == username and usuario.contraseña == contraseña:                
                print("\033[32m¡Inicio de sesión exitoso!\033[m")
                usuario.online = True
                return usuario
        return print("\033[31m¡Credenciales inválidas!\033[m")

    def registrar(self):
        '''Le pide al usuario que ingrese sus datos para ser registrado y asigna 
        esos valor a los atributos del objeto.
        '''
        self.id = len(usuarios) + 1
        self.nombre = input('Ingrese nombre:')
        self.apellido = input('Ingrese apellido:')
        self.telefono = input('Ingrese telefono:')
        self.username = input('Ingrese username:')
        self.email = input('Ingrese email:')
        self.contraseña = input('Ingrese contraseña:')
        self.fecha_registro = date.today()
        self.avatar = input('Ingrese avatar:')
        self.estado = True
        self.online = False
        
    

class Publico(Usuario):
    '''Clase Publico, hereda de la clase Usuario

    Attributes:
        es_publico (bool): True si es un usuario publico.
    '''
    def __init__(self, id=None, nombre =None, apellido=None, telefono=None, username=None, email=None, contraseña=None, fecha_registro=None, avatar=None, estado=None, online=None):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
        self.es_publico = True

    def registrar(self):
        '''Extiende el método registrar() de la clase Usuario, asigna el atributo 
        es_publico a True y agrega el objeto Publico a la lista de usuarios.
        '''
        super().registrar()
        self.es_publico = True
        usuarios.append(self)
        print("\033[32m¡El usuario público ha sido registrado correctamente!\033[m")
    
    def comentar(self):
        '''Imprime los artículos si existen, para que el usuario elija cual comentar.
        Luego crea un objecto de la clase Comentario y lo agregar a la lista de comentarios.

        Returns:
            print(): imprime mensaje de error o de éxito.
        '''
        if not publicaciones:
            return print("\033[31m!No hay artículos!\033[m")      
        
        contador = 0
        for i in publicaciones:
            contador += 1
            print(f"\033[35m{contador}-\033[m {vars(i)}")
            
        id_articulo = input("Elige el articulo para comentar: ")
        
        if not id_articulo.isdigit():
            return print("\033[31mError. Debe ingresar un numero entero positivo.\033[m")
        
        id_articulo = int(id_articulo)    
        
        if id_articulo > len(publicaciones): 
            return print( "\033[31mError. !Ingreso un numero de articulo que no existe!\033[m")
            
        texto = input("Ingresa tu comentario: ")
        comentario = Comentario(len(comentarios) + 1,id_articulo, self.id, texto,datetime.now(),True)
        comentarios.append(comentario)
        return print("\033[32m¡Comentario posteado exitosamente!\033[m")
        

class Colaborador(Usuario):
    '''Clase Colaborador, hereda de la clase Usuario

    Attributes:
        es_colaborador (bool): True si es un usuario colaborador.
    '''
    def __init__(self, id=None, nombre =None, apellido=None, telefono=None, username=None, email=None, contraseña=None, fecha_registro=None, avatar=None, estado=None, online=None):
        super().__init__(id, nombre, apellido, telefono, username, email, contraseña, fecha_registro, avatar, estado, online)
        self.es_colaborador = True
    
    def registrar(self):
        '''Extiende el método registrar() de la clase Usuario, asigna el atributo 
        es_publico a True y agrega el objeto Colaborador a la lista de usuarios.
        '''
        super().registrar()
        self.es_colaborador = True
        usuarios.append(self)
        print("\033[32m¡El usuario Colaborador ha sido registrado correctamente!\033[m")

    def comentar(self):
        '''Imprime los artículos si existen, para que el usuario elija cual comentar.
        Luego crea un objecto de la clase Comentario y lo agregar a la lista de comentarios.

        Returns:
            print(): imprime mensaje de error o de éxito.
        '''
        if not publicaciones:
            return print("\033[31m¡No hay artículos!\033[m")      
        
        contador = 0
        for i in publicaciones:
            contador += 1
            print(f"\033[35m{contador}-\033[m {vars(i)}")
            
        id_articulo = input("Elige el articulo para comentar: ")
        
        if not id_articulo.isdigit():
            return print("\033[31mError. Debe ingresar un numero entero positivo.\033[m")
        
        id_articulo = int(id_articulo)    
        
        if id_articulo > len(publicaciones): 
            return print("\033[31mError. !Ingreso un numero de articulo que no existe!\033[m")
            
        texto = input("Ingresa tu comentario: ")
        comentario = Comentario(len(comentarios) + 1,id_articulo, self.id, texto,datetime.now(),True)
        comentarios.append(comentario)
        return print("\033[32m!Comentario posteado exitosamente!\033[m")

    def publicar(self):
        '''Le pide los datos del articulo a publicar al usuario, 
        luego crea un objeto Articulo con esos datos y lo agrega a la lista de publicaciones.
        '''
        id = len(publicaciones) + 1
        id_usuario = self.id
        titulo = input("Ingrese titulo del articulo: ")
        resumen = input("Ingrese resumen del articulo: ")
        contenido = input("Ingrese contenido del articulo: ")
        fecha_publicacion = date.today()
        imagen = input("Ingrese imagen del articulo: ")
        estado = True
        publicaciones.append(Articulo(id,id_usuario,titulo,resumen,contenido,fecha_publicacion,imagen,estado))
        
        print("\033[32m!Articulo publicado!\033[m")
        
class Articulo:
    '''Clase Articulo
    
    Attributes:
        id (int): id del articulo
        id_usuario (int): id del usuario que realiza el comentario.
        titulo (str): titulo del articulo
        resumen (str): resumen del articulo
        contenido (str): contenido del articulo
        fecha_publicacion (date): fecha de publicación del articulo
        imagen (str): dirección de la imagen del articulo
        estado (bool): estado del articulo, True o False.
    
    '''
    def __init__(self, id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado):
        self.id = id
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.resumen = resumen
        self.contenido = contenido
        self.fecha_publicacion = fecha_publicacion
        self.imagen = imagen
        self.estado = estado


class Comentario:
    '''Clase comentario

        Attributes:
            id (int): id del comentario.
            id_articulo (int): id del articulo donde se realizo el comentario.
            id_usuario (int): id del usuario que realizo el comentario.
            contenido (str): contenido del comentario
            fecha_hora (datetime): fecha y hora de publicacion del comentario.
            estado (bool): estado del comentario, True o False.
        '''
    def __init__(self, id, id_articulo, id_usuario, contenido, fecha_hora, estado):
        self.id = id
        self.id_articulo = id_articulo
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.fecha_hora = fecha_hora
        self.estado = estado
            
def menu ():
    '''Menu de acciones.''' 
    salida = False 
    while salida == False:   
        print("------------------------------------")
        print("1. Registrar usuario publico.")
        print("2. Registrar usuario colaborador. ")
        print("3. Mostrar usuarios registrados. ")
        print("4. Login. ")   
        print("5. Salir.")
        print("------------------------------------")
        opción = input("Ingrese un numero correspondiente a la opción que desea realizar: ")
        if opción == "1":
            usuario = Publico()
            usuario.registrar()
        elif opción == "2":
            usuario = Colaborador()
            usuario.registrar()
        elif opción == "3":
                if not usuarios:
                    print("\033[31m¡No hay usuarios registrados!\033[m")
                contador = 0
                for i in usuarios:
                    contador += 1
                    print(f"\033[35m{contador}-\033[m {vars(i)}")
        elif opción == "4":
           usuario = Usuario().login()
           if hasattr(usuario,'es_colaborador'):
               #usuario colaborador
                print("------------------------------------")
                print(f"\033[34m!Bienvenido {usuario.username}! Usted es un usuario Colaborador.\033[m")
                salida2 = False 
                while salida2 == False:   
                    print("------------------------------------")
                    print("1. Publicar Articulo. ")
                    print("2. Realizar un comentario. ")
                    print("3. Mostrar Artículos. ")
                    print("4. Mostrar Comentarios. ")
                    print("5. Logout. ")
                    print("------------------------------------")
                    opción = input("Ingrese un numero correspondiente a la opción que desea realizar: ")
                    if opción == "1":
                       usuario.publicar()
                    elif opción == "2":
                        usuario.comentar()
                    elif opción == "3":
                        if not publicaciones:
                            print("\033[31m¡No hay artículos!\033[m")
                            continue
                        contador = 0
                        for i in publicaciones:
                            contador += 1
                            print(f"\033[35m{contador}-\033[m {vars(i)}")
                    elif opción == "4":
                        if not comentarios:
                            print("\033[31m¡No hay comentarios!\033[m")
                            continue
                        contador = 0
                        for i in comentarios:
                            contador += 1
                            print(f"\033[35m{contador}-\033[m {vars(i)}")
                    else:
                        print("\033[33mLogout...\033[m")
                        usuario.online = False
                        salida2 = True
           elif hasattr(usuario,'es_publico'):
                #usuario publico
                print("------------------------------------")
                print(f"\033[34m!Bienvenido {usuario.username}! Usted es un usuario Publico.\033[m")
                salida2 = False 
                while salida2 == False:   
                    print("------------------------------------")
                    print("1. Realizar un comentario. ")
                    print("2. Mostrar Artículos. ")
                    print("3. Mostrar Comentarios. ")
                    print("4. Logout. ")
                    print("------------------------------------")
                    opción = input("Ingrese un numero correspondiente a la opción que desea realizar: ")
                    if opción == "1":
                        usuario.comentar()
                    elif opción == "2":
                        if not publicaciones:
                            print("\033[31m¡No hay artículos!\033[m")
                            continue
                        contador = 0
                        for i in publicaciones:
                            contador += 1
                            print(f"\033[35m{contador}-\033[m {vars(i)}")
                    elif opción == "3":
                        if not comentarios:
                            print("\033[31m¡No hay comentarios!\033[m")
                            continue
                        contador = 0
                        for i in comentarios:
                            contador += 1
                            print(f"\033[35m{contador}-\033[m {vars(i)}")
                    else:
                        print("\033[33mLogout...\033[m")
                        usuario.online = False
                        salida2 = True                            
        else:
            salida = True  

menu()



