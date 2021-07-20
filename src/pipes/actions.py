from src.jobs.shopify_orders import get_order
from src.jobs.save_leads import save_lead, store_attendance

def feature_disabled(input: str, action_response):
    return 'A integração está momentaneamente fora do ar.'


actions_pipeline = {
    'statusOrder': get_order,
    'saveLead': save_lead,
    'registerHelp': store_attendance,
    'trackOrder': feature_disabled
}

