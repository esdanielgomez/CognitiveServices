import os, requests, time 
from xml.etree import ElementTree
import uuid, json

suscripcionTexto = "a7d29f3b1c7544629f6c13eec462a148"

def traducirTexto(texto, idiomaInicial, idiomaFinal):
    base_url = 'https://api.cognitive.microsofttranslator.com'
    path = '/translate?api-version=3.0'
    params = '&to=en'
    constructed_url = base_url + path + params

    headers = {
        'Ocp-Apim-Subscription-Key': suscripcionTexto,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text' : texto
    }]

    request = requests.post(constructed_url, headers=headers, json=body)
    response = json.loads(str(request.text))
    return response[0]['translations'][0]['text']