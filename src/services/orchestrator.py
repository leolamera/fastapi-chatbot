from src.pipes.orchestrator import status_pipeline, verify_status

from src.jobs.watson_manager import get_text_response, get_action_response
from src.jobs.pusher_output import send_push

from src.models.interfaces import WebEvent

from src.pipes.actions import actions_pipeline


async def webhook_page(request: WebEvent):
    event_id = request.eventId
    message = request.message    


    status = verify_status(event_id)
    foward_function = status_pipeline[status]
    feedback_response = foward_function(request)
    text_response_list = get_text_response(feedback_response)
    action_response = get_action_response(feedback_response)
    if action_response == True:
        for text_response in text_response_list:
            send_push(event_id, text_response)

        return []
    
    print("RODAR ACTION")
    action_function = actions_pipeline[action_response]

    response = await action_function(message, feedback_response)
    send_push(event_id, response)

    for text_response in text_response_list:
        send_push(event_id, text_response)

    return []
