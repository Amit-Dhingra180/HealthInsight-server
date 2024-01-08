from models.diabetes_model import predict_diabetes

new_patient_attributes = [6, 160, 23, 14, 9, 29, 55]
x = predict_diabetes(new_patient_attributes)
print('This is in demo file', x)

