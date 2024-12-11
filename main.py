from schemas.model import Model
from schemas.voice import Voice
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

voice = Voice(
    tts = tts,
    model_path = model_path,
    f0_up_key = 0,
    f0_method = "rmvpe",
    merge_type = "median",
    f0_autotune = False,
    resample_sr = "0",
    index_rate = 0.75,
    filter_radius = 3,
    rms_mix_rate = 0.2,
    protect = 0.2
)

inference_voice(voice)