from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([
    ('Disease', 'Fever'),
    ('Disease', 'Cough'),
    ('Disease', 'Fatigue'),
    ('Disease', 'Chills')
])

cpd_D = TabularCPD('Disease', 2, [[0.3], [0.7]]) 

cpd_F = TabularCPD('Fever', 2,
    [[0.1, 0.5],
     [0.9, 0.5]],
    evidence=['Disease'], evidence_card=[2])

cpd_C = TabularCPD('Cough', 2,
    [[0.2, 0.4],
     [0.8, 0.6]],
    evidence=['Disease'], evidence_card=[2])

cpd_Fat = TabularCPD('Fatigue', 2,
    [[0.3, 0.7],
     [0.7, 0.3]],
    evidence=['Disease'], evidence_card=[2])

cpd_Ch = TabularCPD('Chills', 2,
    [[0.4, 0.6],
     [0.6, 0.4]],
    evidence=['Disease'], evidence_card=[2])

model.add_cpds(cpd_D, cpd_F, cpd_C, cpd_Fat, cpd_Ch)
model.check_model()

inference = VariableElimination(model)

q1 = inference.query(
    variables=['Disease'],
    evidence={'Fever': 1, 'Cough': 1}
)

print("Flu =", round(q1.values[0], 3))
print("Cold =", round(q1.values[1], 3))

q2 = inference.query(
    variables=['Disease'],
    evidence={'Fever': 1, 'Cough': 1, 'Chills': 1}
)

print("Flu =", round(q2.values[0], 3))
print("Cold =", round(q2.values[1], 3))

q3 = inference.query(
    variables=['Fatigue'],
    evidence={'Disease': 0}
)

print("P(Fatigue = Yes | Flu) =", round(q3.values[1], 3))
