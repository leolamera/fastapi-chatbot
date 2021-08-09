from src.config.watson_assistant import assistant

# EXPORTS
def send_text(text_message: str, session_id: str):
    response = assistant.message(
        assistant_id='39f2c9c5-2d83-4a2d-b703-468ab79504b8',
        session_id=session_id,
        input={
            'message_type': 'text',
            'text': text_message
        }
    ).get_result()

    return response

def create_session():
    response = assistant.create_session(
        assistant_id='39f2c9c5-2d83-4a2d-b703-468ab79504b8'
    ).get_result()

    return response['session_id']

def get_text_response(watson_response):
    text_list = watson_response['output']['generic']
    return [text_response['text'] for text_response in text_list]

def get_action_response(watson_response):
    try:
        action = watson_response['output']['user_defined']['action']
        return action
    except:
        return True

def get_body_response(watson_response):
    try:
        body = watson_response['output']['user_defined']['body']
        return body
    except:
        return True
