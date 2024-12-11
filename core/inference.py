import os

def inference_voice(
        tts: str,
        model_path: str
        ):

    f0_up_key = 0
    f0_method = "rmvpe"
    merge_type = "median"
    f0_autotune = False
    resample_sr = "0"
    index_rate = 0.75
    filter_radius = 3
    rms_mix_rate = 0.2
    protect = 0.2

    exec_arg = "python inference_cli.py " + '"' + model_path + '" "' + tts + '" ' + str(
        f0_up_key) + ' "[\\"' + f0_method + '\\"]" ' + str(f0_autotune) + " " + merge_type + " " + str(
        index_rate) + " " + str(filter_radius) + " " + resample_sr + " " + str(rms_mix_rate) + " " + str(
        protect) + " " + "output/"

    print(exec_arg)
    os.system(exec_arg)