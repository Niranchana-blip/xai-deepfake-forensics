from backend.app.services.model_loader import load_model

model = load_model()

print("MODEL LOADED SUCCESSFULLY")
print(type(model))

print(model.classifier)