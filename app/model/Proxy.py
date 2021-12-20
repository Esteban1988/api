import requests
from app.model.ProxyRequest import ProxyRequest
from app.model.RequestConfigurations import RequestConfigurations


def meli_api_path():
    return 'https://api.mercadolibre.com/'


class Proxy:

    def __init__(self, request, requestCounter):
        self.request = request
        self.proxyRequest = ProxyRequest(request)
        self.configurations = RequestConfigurations()
        self.requestCounter = requestCounter

    def resend_request(self):
        self.increment_request_counter()
        if self.proxyRequest.is_valid():
            res = requests.get((meli_api_path() + '{}').format(self.request.path))
            self.log(res.status_code)
            self.store_proxy_request()
            return res.json()
        else:
            return self.proxyRequest.get_log()

    def increment_request_counter(self):
        self.requestCounter.increment(self.proxyRequest, self.configuration_for_proxy_request())

    def log(self, text_log):
        self.proxyRequest.set_log(text_log)

    def configuration_for_proxy_request(self):
        return self.configurations.at(self.proxyRequest.ip)

    # aca deberia loguear la request en una base nosql tipo mongoDb, en modo asincronico para que no interfiera con el tiempo de respuesta
    def store_proxy_request(self):
        return self

