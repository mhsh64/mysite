from flask import Flask

app = Flask(__name__)

from itertools import permutations
from flask import render_template, request

@app.route('/', methods=['GET', 'POST'])
def output():
    result="hi"
    if request.args.get('perm', None):
        result = request.args['perm']
        perms = [''.join(p) for p in permutations(result)]
        return str(perms)
        return(len(perms))
    else:
        user = {'nickname': 'Dear User'}
        return render_template('index.html', title='Home', user=user)








