from flask import Flask

app = Flask(__name__)

# render_template: takes a Jinja template as input and produces pure HTML
from flask import render_template, request

# added my own function, this function will remove duplicate words, if we have duplicate characters in input
def my_perm(y):
    if len(y) == 1:
        return [y]
    p = []
    temp = my_perm(y[1:])
    for i in temp:
        for x in range(len(i) + 1):
            p.append(i[:x] + y[0] + i[x:])
    return list(set(p))


# want my default page to be accessible by either GET or POST
@app.route('/', methods=['GET', 'POST'])
def output():
    input="hi"
    # Change request.args.get to request.form.get
    if request.form.get('perm', None):
        input = request.form['perm']
        result = my_perm(input)
        perms = [''.join(p) for p in result]
        dedups = len(perms)
        output = {'output_cell': str(perms)}
        return render_template('output.html',
                                title='Output',
                                input_word=input,
                                ana_dups=dedups,
                                output_html=output)
    else:
        user = {'nickname': 'Dear User'}
        return render_template('index.html',
                                title='Home',
                                user_html=user)








