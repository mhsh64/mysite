from flask import Flask

app = Flask(__name__)

# request function: provides a global context which is used to
# access information about the latest request made to our application
# tion. GET arguments that user passes along as part of a
# request are automatically available in request.args, from which we can access
# key-value pairs as we would with a Python dictionary

# render_template: takes a Jinja template as input and produces pure HTML

from itertools import permutations
from flask import render_template, request

# want our default page to be accessible by either GET or POST
@app.route('/', methods=['GET', 'POST'])
def output():
    result="hi"
    # Change request.args.get to request.form.get
    if request.form.get('perm', None):
        result = request.form['perm']
        perms = [''.join(p) for p in permutations(result)]
        return str(perms)
    else:
        user = {'nickname': 'Dear User'}
        return render_template('index.html',
                                title='Home',
                                user=user)








