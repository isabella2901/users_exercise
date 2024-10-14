"""
This file contains the logic to:

1. Create an user
2. Update user information
3. Get all users
4. Get user information
"""
import user_repository
from users import users




def get_user(username):
    """
    """
    return user_repository.get_users(username)

def findAllUsers():
    
    print(user_repository.findAllUsers())
def create_user(username, **kwargs):
    global users
    users = user_repository.findAllUsers()
    """
    Crea un nuevo usuario y guarda la información en el archivo.
    """
    if username in users:
        raise Exception(f"El usuario {username} ya existe")
    
    if len(kwargs) != 3:
        raise Exception(f"La información del usuario no tiene la estructura esperada")

    cond = all([kwargs.get(key) for key in ["name", "degree", "password"]])
    
    if not cond:
        raise Exception(f"La información del usuario no tiene la estructura esperada")

    # Agregar el nuevo usuario al diccionario

    users[username] = kwargs

    # Guardar los usuarios actualizados en el archivo JSON
    user_repository.save_users(users)

    print(f"Usuario {username} creado correctamente.")

def update_user(username, **kwargs):
    global users
    users = user_repository.findAllUsers()
    """
    Actualiza la información de un usuario existente.
    """
    if username not in users:
        raise Exception(f"El usuario {username} no está registrado")

    # Aseguramos que la información contenga las claves necesarias
    cond = all([kwargs.get(key) for key in ["name", "degree", "password"]])
    
    if not cond:
        raise Exception(f"La información del usuario no tiene la estructura esperada")

    users[username] = kwargs  # Actualiza la información del usuario
    user_repository.save_users(users)  # Guarda los cambios en el archivo

    print(kwargs)