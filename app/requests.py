import urllib.request,json
from .models import Quote

base_url = None

def configure_request(app):
    global base_url
    base_url = app.config['QUOTE_API_BASE_URL']

def get_quote():
    get_quote_details_url = base_url.format()

    with urllib.request.urlopen(get_quote_details_url) as url:
        quote_details_data = url.read()
        quote_details_response = json.loads(quote_details_data)

        quote_object = None
        if quote_details_response:
            id = quote_details_response.get('id')
            author = quote_details_response.get('author')
            quote = quote_details_response.get('quote')

            quote_object = Quote(id, author, quote)

    return quote_object
