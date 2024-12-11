from schemas.model import Model
from core.train import train_model
from core.convert import mp3_to_wav
from core.inference import inference_voice

model = Model(
    model_name = 'test1',
    wav = 'dataset/test.wav',
    epoch = 10,
    batch_size = 7
)

model_path, index_path = train_model(model)
print(model_path, index_path)

mp3 = 'test_tts'
tts = mp3_to_wav(mp3)

inference_voice(tts, model_path)