from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        # Add logic to validate and store user data here
        return render_template('success.html', name=name)
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
