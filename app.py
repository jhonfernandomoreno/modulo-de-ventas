from flask import Flask, render_template
app= Flask(__name__)

@app.route('/')
def sesion():
    return render_template('inicio.html')

@app.route('/dashboard')
def dash():
    return render_template('dashboard.html')

@app.route('/ventas')
def ventas():
    return 'Hola a todos'

@app.route('/acercade')
def acercade():
    return render_template('acercade.html')

if __name__ == "__main__":
    app.run(debug=True)
