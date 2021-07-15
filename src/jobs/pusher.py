from src.config.pusher_cliente import pusher_client
import time

# EXPORTS
def send_push(event_id: str, message: str):
        time.sleep(1)
        pusher_client.trigger('chat', event_id, {
                'username': '@bot',
                'message': message,
                'serverOrigin': True
        })