import redis

r = redis.Redis(host='172.18.0.3', port=6379, decode_responses=True)

channel = 'prueba'

def message_handler(message):
    print(f"{message['data']}")

pubsub = r.pubsub()
pubsub.subscribe(channel)

for message in pubsub.listen():
    if message['type'] == 'message':
        message_handler(message)

