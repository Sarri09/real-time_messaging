import redis
import json

r = redis.StrictRedis(host='redis-1', port=6379, db=0)

def registrar_usuario():
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    contraseña = input("Contraseña: ")

    clave_usuario = f"usuario:{correo}"

    if r.exists(clave_usuario):
        print("El usuario ya está registrado.")
    else:
        usuario_info = {
            'nombre': nombre,
            'correo': correo,
            'contraseña': contraseña
        }
        # Convertir el diccionario a una cadena JSON
        usuario_info_str = json.dumps(usuario_info)
        r.hset(clave_usuario, 'info', usuario_info_str)
        print("Usuario registrado con éxito.")

        r.publish("usuarios_registrados", nombre)
        print(f"Nuevo usuario se ha unido: {nombre}")

if __name__ == '__main__':
    registrar_usuario()


