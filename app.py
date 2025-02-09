from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/donarnew')
def donarnew():
    return render_template('donar-details.html')

@app.route('/fund')
def fund():
    return render_template('fund.html')

@app.route('/userdetails')
def userdetails():
    return render_template('userdetails.html')

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/sucessful')
def sucessful():
    return render_template('sucess.html')










# Run the application
if __name__ == '__main__':
    app.run(debug=True)
    