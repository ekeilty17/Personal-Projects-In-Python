#PYTHONPATH=/Users/Standard/Documents/gitsrc/Python/Useful/HTTP twistd -n web --class=simple_server.resource
# or
#./exc.sh server            (or whatever you decide to name this file)

from twisted.internet.defer import succeed
from klein import Klein
import json

class Item():
    
    #internal variables
    def __init__(self, Id, name, description):
        self.Id = Id
        self.name = name
        self.description = description

    #getters
    def getId(self):
        return self.Id
    def getName(self):
        return self.name
    def getDescription(self):
        return self.description

    #setters
    def setId(self, Id):
        self.Id = Id
    def setName(self, name):
        self.name = name
    def setDescription(self, description):
        self.description = description

class ItemStore(object):
    app = Klein()

    def __init__(self):
        self.items = [{
                'Id' : 'python',
                'name' : 'Pyhton',
                'description' : 'I love Python... 2.7 none of that 3.6 crap'
            }]
    
    #GET Requests
    @app.route('/')
    def home(self, request):
        #simply returns 
        return "Welcome!"

    @app.route('/post', methods=['GET'])
    def items(self, request):
        request.setHeader('Content-Type', 'application/json')
        return json.dumps(self.items)

    @app.route('/<string:Id>', methods=['GET'])
    def print_id(self, request, Id):
        return Id
    
    @app.route('/post/<string:Id>', methods=['GET'])
    def get_item(self, request, Id):
        #request.setHeader('Content-Type', 'application/json')
        #return json.dumps(self.items.get(Id))
        return Id

    #POST Request
    @app.route('/post', methods=['POST'])
    def items(self, request):
        request.setHeader('Content-Type', 'application/json')
        #self.items += [json.load(request.content)]
        #return json.dumps(request.content)
        return "Hello there"

    """
    #PUT Request
    @app.route('/post/<string:name>', methods=['PUT'])
    def save_item(self, request, name):
        request.setHeader('Content-Type', 'application/json')
        body = json.loads(request.content.read())
        self._items[name] = body
         return json.dumps({'success': True})
    """

store = ItemStore()
store.app.run('localhost', 8082)
