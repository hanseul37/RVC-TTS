import os
from schemas.voice import Voice

def inference_voice(voice: Voice):
    exec_arg = "python inference_cli.py " + '"' + voice.model_path + '" "' + voice.tts + '" ' + str(
        voice.f0_up_key) + ' "[\\"' + voice.f0_method + '\\"]" ' + str(voice.f0_autotune) + " " + voice.merge_type + " " + str(
        voice.index_rate) + " " + str(voice.filter_radius) + " " + voice.resample_sr + " " + str(voice.rms_mix_rate) + " " + str(
        voice.protect) + " " + "output/"

    print(exec_arg)
    os.system(exec_arg)