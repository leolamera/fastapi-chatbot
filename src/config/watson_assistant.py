from ibm_watson import AssistantV2
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('PA62T9yoETuSiEvNLSiyOK9trfM2ooJrImhvk8WwgV1b')
assistant = AssistantV2(
    version='2020-04-01',
    authenticator=authenticator
)

assistant.set_service_url('https://api.us-south.assistant.watson.cloud.ibm.com/instances/391549c1-9c84-4fe4-a2b9-8a62480525a6')
