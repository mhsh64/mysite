from flask import Flask

app = Flask(__name__)

# render_template: takes a Jinja template as input and produces pure HTML
from flask import render_template, request
from myfunction import my_perm

# want my default page to be accessible by either GET or POST
@app.route('/', methods=['GET', 'POST'])
def output():
    input="hi"
    # Change request.args.get to request.form.get
    if  request.form.get('perm', None):
        input = request.form['perm']
        # check if user enters the alphabets only
        if  input.isalpha():
            result = my_perm(input)
            perms = [''.join(p) for p in result]
            dedups = len(perms)
            output = {'output_cell': str(perms)}
            return render_template('output.html',
                                    title='Output',
                                    input_word=input,
                                    ana_dups=dedups,
                                    output_html=output)
        # if user enters numbers or symbols, it runs alpha.html page
        else:
            return render_template('alpha.html')
    else:
        user = {'nickname': 'Dear User'}
        return render_template('index.html',
                                title='Home',
                                user_html=user)


# error page
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')





