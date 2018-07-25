import math
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def main():
    if 'H' in request.args and 'S1' in request.args and 'S2' in request.args:
        h = int(request.args['H'])
        s1 = int(request.args['S1'])
        s2 = int(request.args['S2'])
        answer = 1/3 * h * (s1 + math.sqrt(s1 * s2) + s2)
    else:
        answer = ''
    return render_template('prisma_V.html', answer=str(answer))


'''@app.route('/prisma')
def main():
    return render_template('prisma_height.html')
'''

app.run(debug=True, port=8080)
