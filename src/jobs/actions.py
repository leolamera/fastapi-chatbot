import requests

apikey = '66f4c24721202b548065511dd53f67c9'
password = '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'

urlApi = f'https://{apikey}:{password}@coozyybrand.myshopify.com/admin/api/2021-07/orders.json'

def format_response(order):
    current_total_price = order['current_total_price']
    custumer_name = order['billing_address']['name']
    financial_status = order['financial_status']
    line_items_list = order['line_items']
    city = order['shipping_address']['city']
    province_code = order['shipping_address']['province_code']
    order_status_url = order['order_status_url']

    text_response = ""

    text_response = f"Olá {custumer_name}, encontramos seu pedido!\nO status do seu pedido é {financial_status}\nSeu pedido foi:\n"

    items_str = ""
    for item in line_items_list:
        items_str = items_str + f"  *  {item['title']}\n"
        

    text_response = text_response + items_str + f"     no total de R$ {current_total_price}\n"
    text_response = text_response + f"Será entregue em {city}/{province_code}\nPara mais informações {order_status_url}"

    return text_response




def input_type(message_input: str):
    if '@' in message_input:
        return 'email'
    
    return 'order_number'

def get_order_by_id(orders_list: list, message_input: str):
    for order in orders_list:
        if message_input == str(order['order_number']):
            return format_response(order)

def get_order_by_email(orders_list: list, message_input: str):
    for order in orders_list:
        if message_input == str(order['email']):
            return format_response(order)

def get_order(message_input: str):
    input_message_type = input_type(message_input)

    response = requests.get(urlApi).json()
    orders_list = dict(response)['orders']
    if input_message_type == 'order_number':
        return get_order_by_id(orders_list, message_input)

    if input_message_type == 'email':
        return get_order_by_email(orders_list, message_input)
    


