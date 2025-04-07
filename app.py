from flask import Flask, request, jsonify
from sympy import symbols, sympify, diff, integrate, latex
from sympy.abc import x

app = Flask(__name__)

@app.route("/calcular", methods=["POST"])
def calcular():
    dados = request.get_json()
    expressao = dados.get("expressao", "")
    operacao = dados.get("operacao", "")

    try:
        expr = sympify(expressao)
        if operacao == "derivada":
            resultado = diff(expr, x)
        elif operacao == "integral":
            resultado = integrate(expr, x)
        else:
            return jsonify({"erro": "Operação inválida."})
        
        resultado_latex = latex(resultado)
        return jsonify({
            "resultado": resultado_latex,
            "grafico": ""
        })
    except Exception as e:
        return jsonify({"erro": str(e)})

if __name__ == "__main__":
    app.run()
