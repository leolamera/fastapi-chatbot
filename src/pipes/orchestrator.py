from src.jobs.mongo_sessions import store_event, store_status, store_context, find_store_context_by_id, find_status_by_id
from src.jobs.watson_manager import create_session, send_text

from src.models.interfaces import WebEvent, WatsonResponse

def new_event(event_id: str):
    founded_status = find_status_by_id(event_id)
    if founded_status == None:
        return True
    
    return False

def store_new_event(web_event: WebEvent) -> WatsonResponse:
    event_id = web_event.eventId
    watson_session = create_session()
    store_event(web_event)
    store_status({
        'eventId': event_id,
        'status': 'watson'
    })
    store_context({
        'eventId': event_id,
        'watsonSession': watson_session
    })

    return {
        'event_id': event_id,
        'session_id': watson_session,
        'message': web_event.message,
    }

def get_session_id(web_event: WebEvent):
    event_id = web_event.eventId
    response = find_store_context_by_id(event_id)
    watson_session = response['watsonSession']
    return watson_session

def pipeline_watson(web_event: WebEvent):
    session_id = get_session_id(web_event)
    watson_response = send_text(web_event.message, session_id)
    return watson_response

def pipeline_start(web_event: WebEvent):
    # registro
    tidy_data = store_new_event(web_event)
    watson_response = send_text(tidy_data['message'], tidy_data['session_id'])
    return watson_response

# EXPORTS

status_pipeline = {
    'watson': pipeline_watson,
    'start': pipeline_start
}

def verify_status(event_id: str):
    is_new_event = new_event(event_id)
    if is_new_event == False:
        return 'watson'

    return 'start'