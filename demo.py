from models.heart_model import predict_heart
another_patient = [58, 0, 3, 100, 248, 0, 0, 122, 0, 1, 1, 0, 2]
x = predict_heart(another_patient)
print('another', x)

