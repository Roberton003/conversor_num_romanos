from flask import Flask, render_template, request

app = Flask(__name__)

def int_para_romano(num):
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    resultado = ""
    i = 0
    while num > 0:
        for _ in range(num // valores[i]):
            resultado += simbolos[i]
            num -= valores[i]
        i += 1
    return resultado

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/romano', methods=['POST'])
def romano():
    num = int(request.form['numero'])
    romano = int_para_romano(num)
    return render_template('romano.html', romano=romano)

if __name__ == '__main__':
    app.run(debug=True)
    