from schemas.model import Model
from train import train_model

model = Model(
    model_name = 'test',
    wav = 'dataset/test.wav'
)

model_path, index_path = train_model(model)

print(model_path, index_path)