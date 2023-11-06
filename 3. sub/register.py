import redis

r = redis.Redis(host='172.18.0.2', port=6379, db=0)

def user_registered_handler(message):
    nombre = message["data"].decode()
    print(f"Nuevo usuario se ha unido: {nombre}")

if __name__ == '__main__':
    pubsub = r.pubsub()

    pubsub.subscribe("usuarios_registrados")

    for message in pubsub.listen():
        if message['type'] == 'message':
            user_registered_handler(message)

