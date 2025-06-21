# 🚨 Insecure Python Flask Login System (for Security Review Practice)
# Note: This code is intentionally insecure for educational review purposes.

from flask import Flask, request, render_template_string

app = Flask(__name__)

# ❌ Hardcoded credentials (Bad Practice)
username = "admin"
password = "1234"

# ❌ Simple HTML with no CSRF protection
login_form = '''
    <h2>Login Page</h2>
    <form method="POST">
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
'''

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']

        # ❌ No input validation or sanitization
        # ❌ Password comparison in plaintext
        if user == username and pwd == password:
            return "<h3>Welcome, admin!</h3>"
        else:
            return "<h3>Invalid credentials</h3>"
    return render_template_string(login_form)

if __name__ == '__main__':
    # ❌ Debug mode in production is dangerous
    app.run(debug=True)
