from flask import Flask, render_template, request

def fibonacci(p_num):
    secuencia = [0, 1]  # primeros dos términos
    for i in range(2, p_num):
        siguiente = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente)
    return secuencia[:p_num]  # por si pnum < 2

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def procesar():
    x = None
    if request.method == 'POST':
        numero = int(request.form['numero'])
        x=fibonacci(numero)
    return render_template("index.html",x=x)#Tiene que ser así porque si igualara directamente como hago en la linea pasada daría error al estar trabajando con un None como si fuera un número 

if __name__ == "__main__":  
    app.run()