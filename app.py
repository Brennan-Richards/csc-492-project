from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world(name=None):
    """
    The RISE ABOVE home page.
    """
    return render_template('home.html', name=name)


@app.route('/login', methods=['POST', 'GET'])
def login():
    """
    The page for the user to log in to the RISE ABOVE site.
    """
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)