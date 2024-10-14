"""
This file contains logic interact with the user
"""
import user_service
from users import users

def get_user():
    """
    """
    username = input("Ingrese el username: ")
    response = user_service.get_user(username)
    if response:
        print(response)
    else:
        print(f"El usuario {username} no esta registrado")
        

def create_user_info():
    """
    Solicita la información del usuario y lo crea.
    """
    username = input("Ingrese el nuevo username: ")
    name = input("Ingrese el nombre: ")
    degree = input("Ingrese el grado: ")
    password = input("Ingrese la contraseña: ")

    try:
        user_service.create_user(username, name=name, degree=degree, password=password)
    except Exception as e:
        print(e) 

        
def update_user_info():
    """
    Solicita la información del usuario y la actualiza.
    """
    username = input("Ingrese el username: ")
    name = input("Ingrese el nuevo nombre: ")
    degree = input("Ingrese el nuevo grado: ")
    password = input("Ingrese la nueva contraseña: ")

    try:
        user_service.update_user(username, name=name, degree=degree, password=password)
        print(f"Información del usuario {username} actualizada correctamente.")
    except Exception as e:
        print(e)


def menu():
    message = """\
    Seleccione una opcion

    1. Obtener informacion de un usuario
    2. Obtener usuarios
    3. Crear usuario
    4. Actualizar informacion del usuario
    5. Salir
    """
    print(message)

def main():
    """
    """
    flag = True
    usersloaded = user_service.user_repository.load_users()
    
    while flag:
        menu()
        option = input("Opción: ")

        if option == "1":
            get_user()
        
        elif option == "2":
            user_service.findAllUsers()

        
        elif option == "3":
            create_user_info() 
            
        elif option == "4":
            update_user_info()
        
        elif option == "5":
            flag = False
        else:
            print("Opción no válida")

main()