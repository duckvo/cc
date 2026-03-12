#server
from wsgiref.simple_server import make_server
from spyne.application import Application
from spyne.decorator import rpc
from spyne.service import ServiceBase
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from spyne.model.primitive import Integer

class SquareService(ServiceBase):
    @rpc(Integer, _returns=Integer)
    def square_number(self, num):
        return num * num

soap_app = Application(
    [SquareService],
    tns="example.soap",
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

wsgi_app = WsgiApplication(soap_app)

host = "127.0.0.1"
port = 10000

server = make_server(host, port, wsgi_app)
print(f"Square SOAP Service listening on http://{host}:{port}")
server.serve_forever()

#client
from zeep import Client

client = Client("http://127.0.0.1:10000/?wsdl")

numbers = [3, 5, 7, 10, 12]

print("Square Number Results:")
print("-" * 30)
for num in numbers:
    result = client.service.square_number(num)
    print(f"Square of {num:>3} = {result}")