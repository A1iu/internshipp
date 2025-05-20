from flask import Flask, render_template, request, redirect, session, jsonify
import random

app = Flask(__name__)
app.secret_key = 'supersecurekey'

# Fake sensor data
def get_sensor_data():
    return {
        "temperature": round(random.uniform(22, 28), 1),
        "humidity": round(random.uniform(40, 60), 1)
    }

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/control')
def control():
    if not session.get('logged_in'):
        return redirect('/login')
    return render_template('control.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == '1234':
            session['logged_in'] = True
            return redirect('/control')
        return "Invalid credentials"
    return render_template('login.html')

@app.route('/api/data')
def api_data():
    return jsonify(get_sensor_data())

@app.route('/api/toggle')
def api_toggle():
    print("Simulated GPIO toggle")
    return "Simulated LED toggle"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
