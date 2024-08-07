from flask import Flask, request, render_template_string, render_template
from jinja2 import Template

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.args.get('data'):

        filters = ["config", "self", "request", "[", "]", "-", '"', "+", " ", "join", "%", "%25"]

        for x in filters:
            if x in request.args.get('data'):
                return "BAD HACKER!!", 400
        input = request.args.get('data')
        name  = render_template_string(input)
        
        return render_template('index.html', nama=name)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
