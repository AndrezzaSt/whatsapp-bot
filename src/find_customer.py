import json

json_str = '''
{
    "List": [
        {
            "NAME": "MARCIA",
            "CARD": "11105",
            "TYPE": "P"
        },
        {
            "NAME": "ANDREZZA",
            "CARD": "11106",
            "TYPE": "C"
        },
        {
            "NAME": "ALEXANDRE",
            "CARD": "11107",
            "TYPE": "C"
        },
        {
            "NAME": "JONAS",
            "CARD": "11108",
            "TYPE": "P"
        },
        {
            "NAME": "CARLOS",
            "CARD": "11109",
            "TYPE": "C"
        }
    ]
}
'''


data = json.loads(json_str)

def check_if_customer_exists(card_number):
        for customer in data['List']:
            if customer['CARD'] == card_number:
                    result_str = (customer['NAME'] + ' ' + ' Número do cartão: ' + customer['CARD'] + ' ' + 'Tipo: ' +  customer['TYPE'])
                    return(result_str)
    
def get_customer(card_number):   
    if(check_if_customer_exists(card_number) == None):
        return('Cartao não encontrado!')
    else:
        return(check_if_customer_exists(card_number))