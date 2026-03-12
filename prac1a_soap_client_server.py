#server
from wsgiref.simple_server import make_server
from spyne.application import Application
from spyne.decorator import rpc
from spyne.service import ServiceBase
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.model.primitive import Integer

class CalculatorService(ServiceBase):

    @rpc(Integer, Integer, _returns=Integer)
    def add_numbers(self, num1, num2):
        return num1 + num2

    @rpc(Integer, Integer, _returns=Integer)
    def sub_numbers(self, num1, num2):
        return num1 - num2

    @rpc(Integer, Integer, _returns=Integer)
    def mul_numbers(self, num1, num2):
        return num1 * num2

    @rpc(Integer, Integer, _returns=Integer)
    def div_numbers(self, num1, num2):
        if num2 == 0:
            return 0
        return num1 // num2   # integer division


soap_app = Application(
    [CalculatorService],
    tns="example.soap",
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(soap_app)

host = "127.0.0.1"
port = 10000

server = make_server(host, port, wsgi_app)
print(f"Listening on http://{host}:{port}")

server.serve_forever()

#client

from zeep import Client

client = Client("http://127.0.0.1:10000/?wsdl")

result_add = client.service.add_numbers(5,10)
result_sub = client.service.sub_numbers(32,21)
result_mul = client.service.mul_numbers(2,3)
result_div = client.service.div_numbers(20,4)

print(f"Addition: {result_add}")
print(f"Subtraction: {result_sub}")
print(f"Multiplication: {result_mul}")
print(f"Division: {result_div}")

