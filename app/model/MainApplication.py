import redis
from flask import Flask
from flask import request

from app.model.Proxy import Proxy
from app.model.RequestValidator import RequestValidator


app = Flask(__name__)
redisConection = redis.Redis(host="127.0.0.1", port=6379)
request_counter = RequestValidator(redisConection)
print("inicializacion")


@app.route("/")
def index():
    return "Meli proxi challenger"


# /categories/MLA97994
# /categories/MLA5725
@app.route("/<categories>")
@app.route("/<categories>/<itemCode>")
def item(categories='', itemCode=''):
    proxy = Proxy(request, request_counter)
    return proxy.resend_request()


if __name__ == "__main__":
    app.run(debug=True, port=8000)
