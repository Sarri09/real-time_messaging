import redis

r = redis.Redis(host='172.17.0.2', port=6379, decode_responses=True)

channel = 'prueba' 

def message_publisher(channel, message, user):
    formatted_message = f"{user}: {message}"
    r.publish(channel, formatted_message)
    print("Mensaje enviado!")

if __name__ == '__main__':
    user = input("Ingrese un nombre de usuario: ")
    while True:
        message = input("Mensaje: ")
        if message == "exit":
            continue
        message_publisher(channel, message, user)

