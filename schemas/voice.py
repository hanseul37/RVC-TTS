from pydantic import BaseModel

class Voice(BaseModel):
    tts: str
    model_path: str
    f0_up_key = int
    f0_method = str
    merge_type = str
    f0_autotune = bool
    resample_sr = int
    index_rate = float
    filter_radius = int
    rms_mix_rate = float
    protect = float