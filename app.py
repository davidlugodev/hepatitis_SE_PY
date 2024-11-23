from flask import Flask, request, render_template_string

app = Flask(__name__)

class HepatitisExpertSystem:
    def __init__(self):
        self.rules = [
            ("Hepatitis A", ["ictericia", "fiebre"]),
            ("Hepatitis B", ["ictericia", "fiebre", "dolor abdominal"]),
            ("Hepatitis C", ["ictericia", "fatiga", "pérdida de apetito"]),
            ("Hepatitis D", ["infectado con VHB"]),
            ("Hepatitis E", ["ictericia", "fiebre", "agua/alimentos contaminados"]),
            ("Otras Hepatitis", ["pérdida del apetito", "náusea", "vómitos", "diarrea", "orina oscura", "evacuaciones pálidas", "dolor abdominal"])
        ]

    def infer(self, symptoms):
        possible_diagnoses = []
        for hepatitis, conditions in self.rules:
            if all(condition in symptoms for condition in conditions):
                possible_diagnoses.append(hepatitis)
        if not possible_diagnoses:
            return "No se encontró hepatitis"
        return f"Posible(s): {', '.join(possible_diagnoses)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    diagnosis = ""
    if request.method == 'POST':
        symptoms = request.form.getlist('symptoms')
        hepatitis_expert_system = HepatitisExpertSystem()
        diagnosis = hepatitis_expert_system.infer(symptoms)
    return render_template_string(open("index.html").read(), diagnosis=diagnosis)

if __name__ == '__main__':
    app.run(debug=True)

