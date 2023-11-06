import redis

r = redis.Redis(host='redis-2', port=6380, db=0)

def check_user_credentials(nombre, contrasena):
    stored_contrasena = r.hget("usuarios", nombre)
    return stored_contrasena and stored_contrasena.decode() == contrasena

def message_publisher(channel, message, nombre, contrasena):
    formatted_message = f"{nombre}: {message}"
    r.publish(channel, formatted_message)
    print("Mensaje enviado!")

if __name__ == '__main__':
    while True:
        nombre = input("Ingrese un nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")
        if check_user_credentials(nombre, contrasena):
            break
        else:
            print("Usuario no registrado. Introduce tus credenciales nuevamente.")

    while True:
        message = input("Mensaje: ")
        if message == "exit":
            break
        message_publisher("canal", message, nombre, contrasena)


