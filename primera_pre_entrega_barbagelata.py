

database = {"usuario_1": "1234" , "usuario_2": "4321", "usuario_3": "1324"}

#Menú

def menu():
    print("¡Bienvenido a la plataforma!")
    print("1. Registráte")
    print("2. Inicia sesión")
    print("3. Ver usuarios registrados")
    print("4. Salir")
    option = input("Elegí una opción: ")
    return option


#Registro y almacenamiento de usuarios

def user_login(database):
    user_name = input("Registra tu nombre de usuario: ")
    password = input("Registra tu clave: ")
    database[user_name] = password
    print("El usuario registrado exitosamente.")


#Comprobación de usuarios existentes en base de datos. 3 intentos para login.

def login(database):
    
    login_attempts = 0

    while login_attempts < 3:
        user_name = input("Ingresa tu nombre de usuario: ")
        password = input("Ingresa tu clave: ")
        if user_name in database and database[user_name] == password:
            print(f"Bienvenido/a: {user_name}")
            break
        else:
            print("Nombre de usuario o contraseña incorrecto")
            login_attempts = login_attempts + 1
    if login_attempts == 3:
        print("Agotaste tus intentos. Intentalo en 10 minutos")
        

#Mostrar a los usuarios existentes dentro de la base de datos

def show_users(database):
    print("Usuarios registrados: ")
    for user_name in database.keys():
        print(user_name)
        print()


#Opciones para el menú

while True:
    option = menu()

    if option == "1":
        user_login(database)
    elif option == "2":
        login(database)
    elif option == "3":
        show_users(database)
    elif option == "4":
        print("¡Volve pronto!")
        break
    else:
        print("La opción es incorrecta. Por favor, elegí una opción válida.")