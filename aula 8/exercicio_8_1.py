
from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)


alertas = []

pagina_html = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <title>Dashboard de Alertas</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            background-color: #f4f4f4;
        }
        h1 {
            color: #333;
        }
        form, table {
            background-color: white;
            padding: 20px;
            margin-bottom: 20px;
        }
        input, select, button {
            padding: 8px;
            margin: 5px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #ccc;
            padding: 10px;
            text-align: left;
        }
    </style>
</head>
<body>

    <h1>Dashboard de Alertas de Segurança</h1>

    <h2>Cadastrar alerta</h2>

    <form method="POST" action="/cadastrar">
        <input type="text" name="tipo"
               placeholder="Tipo do alerta" required>

        <select name="severidade" required>
            <option value="baixa">Baixa</option>
            <option value="media">Média</option>
            <option value="alta">Alta</option>
            <option value="critica">Crítica</option>
        </select>

        <input type="text" name="descricao"
               placeholder="Descrição" required>

        <button type="submit">Cadastrar</button>
    </form>

    <h2>Alertas cadastrados</h2>

    <table>
        <tr>
            <th>Tipo</th>
            <th>Severidade</th>
            <th>Descrição</th>
        </tr>

        {% for alerta in alertas %}
        <tr>
            <td>{{ alerta.tipo }}</td>
            <td>{{ alerta.severidade }}</td>
            <td>{{ alerta.descricao }}</td>
        </tr>
        {% endfor %}
    </table>

</body>
</html>
"""



@app.route("/", methods=["GET"])
def dashboard():
    return render_template_string(pagina_html, alertas=alertas)



@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    tipo = request.form.get("tipo", "").strip()
    severidade = request.form.get("severidade", "")
    descricao = request.form.get("descricao", "").strip()

    if not tipo or not descricao:
        return "Tipo e descricao sao obrigatorios", 400

    if severidade not in ("baixa", "media", "alta", "critica"):
        return "Severidade invalida", 400

    alertas.append({
        "tipo": tipo,
        "severidade": severidade,
        "descricao": descricao
    })

    return redirect(url_for("dashboard"))


if __name__ == "__main__":
    app.run(port=5001, debug=False)
