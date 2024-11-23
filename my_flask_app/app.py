from flask import Flask, request, render_template

app = Flask(__name__)

class HepatitisExpertSystem:
    def __init__(self):
        self.rules = [
            ("Hepatitis A", ["ictericia", "fiebre", "comida contaminada"]),
            ("Hepatitis B", ["ictericia", "fiebre", "dolor abdominal", "sangre","fluidos"]),
            ("Hepatitis C", ["ictericia", "fatiga", "inapetencia", "sangre"]),
            ("Hepatitis D", ["VHB positivo", "anti-VHD positivo"]),
            ("Hepatitis E", ["ictericia", "fiebre", "insalubridad"]),
            ("Otras Hepatitis", ["inapetencia", "náusea", "vómitos", "diarrea", "orina oscura", "heces pálidas", "dolor abdominal"])
        ]

    def infer(self, sintomas):
        posible_diagnostico = []
        for hepatitis, conditions in self.rules:
            if all(condition in sintomas for condition in conditions):
                posible_diagnostico.append(hepatitis)
        if not posible_diagnostico:
            return "No se encontró hepatitis"
        return f"Posible(s): {', '.join(posible_diagnostico)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    diagnosis = ""
    if request.method == 'POST':
        sintomas = request.form.getlist('sintomas')
        sistema_experto_hepatitis = HepatitisExpertSystem()
        diagnosis = sistema_experto_hepatitis.infer(sintomas)
    return render_template('index.html', diagnosis=diagnosis)

if __name__ == '__main__':
    app.run(debug=True)

