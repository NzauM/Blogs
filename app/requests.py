import urllib.request,json
from .models import Quote



get_quotes_url = 'http://quotes.stormconsultancy.co.uk/random.json'

def getquotes():
    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_resp = json.loads(get_quotes_data)

        quote_results = None


        if get_quotes_resp:
            quotes_result_list = get_quotes_resp
            quote_results = process_results(quotes_result_list)


        

    return quote_results


def process_results(quotes_result_list):

    quote_result = []

    id = quotes_result_list.get('id')
    quote = quotes_result_list.get('quote')
    author = quotes_result_list.get('author')

    if quote:
        my_quote = Quote(id,author,quote)
        quote_result.append(my_quote)

    return quote_result


    
        

       

    

   


