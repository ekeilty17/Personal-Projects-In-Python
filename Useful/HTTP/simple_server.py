#PYTHONPATH=/Users/Standard/Documents/gitsrc/Python/Useful/HTTP twistd -n web --class=simple_server.resource
# or
#./exc.sh simepl_server            (or whatever you decide to name this file)
#
# I don't know why it's so complicated to run...
# I think it has to do with the fact that I'm running a twisted server and klein is an extension of twisted

from klein import Klein

app=Klein()

@app.route('/')
def home(request):
    return "Welcome!"

@app.route('/<Id>')
def print_id(request, Id):
    return Id

app.run("localhost", 8081)
