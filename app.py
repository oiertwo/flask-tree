from flask import Flask, render_template
from flask import send_from_directory, request
import tree

app = Flask(__name__, template_folder="templates")
app.config['DEBUG'] = True


AVAILABLE_COMMANDS = {
    'random': 'random',
    'onebyone': 'onebyone',
}

global thread

thread = None

def serve_static(filename):
    url = os.path.dirname(str(request.url_rule))[1:]
    #root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(url, filename)


@app.route('/')
def index():
    return render_template('index.html', commands = AVAILABLE_COMMANDS, status = "off")

@app.route('/<cmd>')
def command(cmd=None):
    if thread:
        thread.stop(10)
    if cmd == 'random':
        st = "random"
        thread = tree.Random()
    else:
        st = "one by one"
        thread = tree.Onebyone()

    thread.start()
    # ser.write(camera_command)
    return render_template('index.html', commands = AVAILABLE_COMMANDS, status = st)

# Run
if __name__ == '__main__':
    app.run(
       # debug=True,
        host = "0.0.0.0",
        port = 5000,
        threaded=True,
    )
# socket.run(app)
