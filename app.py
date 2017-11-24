from flask import Flask, render_template
from flask import send_from_directory, request
import tree
from flask import g

app = Flask(__name__, static_folder="static", template_folder="templates")
app.config['DEBUG'] = True


AVAILABLE_COMMANDS = {
    'random': 'random',
    'onebyone': 'onebyone',
    'off': 'off',
}

def serve_static(filename):
    url = os.path.dirname(str(request.url_rule))[1:]
    #root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(url, filename)


def get_thread(cmd):
    thread = getattr(g, '_thread', None)
    if thread == None:
        g._thread = tree.Random()
        g._thread.start()

    return g._thread

@app.route('/')
def index():
    return render_template('index.html', commands = AVAILABLE_COMMANDS, status = "off")

@app.route('/<cmd>')
def command(cmd=None):
    t = get_thread(cmd)
    if cmd == "random":
        t.mode = "random"
    elif cmd == 'onebyone':
        t.mode = "onebyone"
    else:
        t_mode = "off"
    # ser.write(camera_command)
    return render_template('index.html', commands = AVAILABLE_COMMANDS, status = cmd)

# Run
if __name__ == '__main__':
    app.run(
       # debug=True,
        host = "0.0.0.0",
        port = 5000,
        threaded=True,
    )
# socket.run(app)
