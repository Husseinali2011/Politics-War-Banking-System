from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Basic route
@app.route('/')
def home():
    return "<h1>Welcome to Politics, War & Banking System</h1><p>This is the home page.</p>"

# Route with variable
@app.route('/nation/<int:nation_id>')
def nation_page(nation_id):
    # In a real app, you'd fetch data from PnW API
    return f"<h1>Nation {nation_id}</h1><p>Details about nation {nation_id}.</p>"

# Route with GET/POST
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Validate login (dummy)
        if username == 'admin' and password == 'password':
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials"
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/dashboard')
def dashboard():
    return "<h1>Dashboard</h1><p>Welcome to your banking dashboard!</p>"

if __name__ == '__main__':
    app.run(debug=True)