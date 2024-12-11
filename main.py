from schemas.model import Model
from core.train import train_model
from core.convert import mp3_to_wav
from core.inference import inference_voice
from core.moving import moving_directory

model = Model(
    model_name = 'test1',
    wav = 'dataset/test.wav'
)

#model_path, index_path = train_model(model)

#print(model_path, index_path)

#mp3 = 'test_tts'
#tts = mp3_to_wav(mp3)
#model_path = 'models/RVC/test1.pth'

#inference_voice(tts, model_path)