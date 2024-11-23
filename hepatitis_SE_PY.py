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
        self.symptoms_list = [
            "dolor abdominal", "orina turbia", "deposiciones pálidas", "fatiga", "febrícula", 
            "picazón", "ictericia", "inapetencia", "náuseas", "vómitos", "pérdida de peso"
        ]

    def infer(self, symptoms):
        possible_diagnoses = []
        for hepatitis, conditions in self.rules:
            if all(condition in symptoms for condition in conditions):
                possible_diagnoses.append(hepatitis)
        if not possible_diagnoses:
            return "No se encontró hepatitis"
        return f"Posible(s): {', '.join(possible_diagnoses)}"

# Datos de entrada del paciente
patient_symptoms = [
    "ictericia", "fiebre", "dolor abdominal", "orina turbia", "deposiciones pálidas",
    "fatiga", "febrícula", "picazón", "inapetencia", "náuseas", "pérdida de peso"
]

# Crear una instancia del sistema experto
hepatitis_expert_system = HepatitisExpertSystem()

# Inferir el diagnóstico
diagnosis = hepatitis_expert_system.infer(patient_symptoms)

# Mostrar el diagnóstico
print(f"Diagnóstico: {diagnosis}")
