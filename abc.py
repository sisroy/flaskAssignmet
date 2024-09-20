# 5.Implement user sessions in a Flask app to store and display user-specific data.
from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)

# Secret key for session management (important to keep this safe!)
app.secret_key = 'your_secret_key_here'


@app.route('/')
def index():
    # If the user is logged in (i.e., username exists in session), display a personalized greeting.
    if 'username' in session:
        username = session['username']
        return f'Logged in as {username} <br><a href="/logout">Logout</a>'
    return 'You are not logged in <br><a href="/login">Login</a>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Store username in session
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            <input type="submit" value="Login">
        </form>
    '''


@app.route('/logout')
def logout():
    # Remove username from session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
