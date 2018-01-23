
from flask import Flask, render_template, redirect, request, session, flash

app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'

@app.route('/')
def form():
    return render_template('dojo_form.html')


@app.route('/result', methods=['POST'])
def create_user():
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
        return redirect('/')
    elif len(request.form['email_info']) < 1:
        flash("Email cannot be empty!")
        return redirect('/')
    elif len(request.form['description']) < 1:
        flash("Description cannot be empty!")
        return redirect('/')
    elif len(request.form['description']) > 120:
        flash("Description is too long!")
        return redirect('/')
    else:
        session['name'] = request.form['name']
        session['email'] = request.form['email_info']
        session['desc'] = request.form['description']
    return redirect('/new_page')


@app.route('/new_page')
def new_page():
    try:
        name = session['name']
        email = session['email']
        desc = session['desc']
    except:
        return redirect('/')

    return render_template('results.html', name=name, email_info=email, description=desc)


app.run(debug=True)








#
#
# from flask import Flask, render_template, redirect, request, flash
#
# app = Flask(__name__)
#
# @app.route('/')
# def form():
#     return render_template('dojo_form.html')
#
# @app.route('/result', methods=['POST'])
# def process():
#     if len(request.form['name']) < 1:
#         flash("Name cannot be empty!")
#     else:
#         flash("Success! Your name is {}".format(request.form['name']))
#     return redirect('/')
#
#
# @app.route('/result', methods=['POST'])
# def create_user():
#       print "Got Post Info"
#       first = request.form['name']
#       email = request.form['email_info']
#       desc = request.form['description']
#       print first, email
#       return render_template('results.html', name=first, email_info=email, description=desc)
#
# app.run(debug=True)
