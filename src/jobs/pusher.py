from src.config.pusher_cliente import pusher_client

# EXPORTS
def send_push(event_id: str, message: str):
        pusher_client.trigger('chat', event_id, {
                'username': '@bot',
                'message': message,
                'serverOrigin': True
        })