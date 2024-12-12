# RVC-TTS: Retrieval-based Voice Conversion and Text-to-Speech

---

## Overview
- **RVC-TTS**는 음성 기반의 RVC 모델 생성 및 음성 변환을 지원하는 프로젝트입니다.
- 이 프로젝트는 [RVC-Project/Retrieval-based-Voice-Conversion-WebUI](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI), [SayanoAI/RVC-Studio](https://github.com/SayanoAI/RVC-Studio) 프로젝트의 코드를 사용합니다.
- RVC Web UI 환경의 제약 없이 RVC 기능을 활용할 수 있도록 독립형 Python 기반 프로젝트로 구현되었습니다.
- 특히, 기존의 RVC는 Mac OS 환경에서 커스텀 사용에 제한이 있었습니다. 이 프로젝트는 Mac OS에서 개발되어 Mac OS 사용자가 개발에 활용할 수 있습니다.

## Features
- **RVC 모델 생성**: 사용자의 음성을 기반으로 RVC 모델을 생성합니다. 
- **RVC 모델 추론**: RVC 모델을 기반으로 음성을 변환합니다.
- **OS Free**: 이 프로젝트는 Mac OS에서 개발되었으며, Window OS 사용자도 사용 가능합니다. 다만, Apple M1, M2 프로세서의 경우, 추론 과정에서 오류가 발생할 가능성이 있습니다.  
- **Python 버전**: 이 프로젝트는 Python 3.10 버전에서 개발되었으며, 최소 Python 3.8 이상의 버전을 사용해야 합니다. Python 3.9 또는 Python 3.10 버전의 사용을 권장합니다.

## Installation
### 1. Clone the repository:
```bash
git clone https://github.com/hanseul37/RVC-TTS.git
cd RVC-TTS
```

### 2. Set up a Python virtual environment and install dependencies:
pip 최신 버전(24.1)에서는 설치에 문제가 있을 수 있습니다. 
`pip install --upgrade pip==23.0.1`로 다운그레이드하여 설치를 진행해주세요.
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Install ffmpeg:
시스템에 ffmpeg를 설치합니다.
- Mac: `brew install ffmpeg`
- Windows: [ffmpeg 공식 웹사이트](https://ffmpeg.org/)에서 다운로드 후 환경 변수를 설정합니다.

### 4. Download assets:
- RVC는 추론과 훈련을 위해 다른 일부 사전 훈련된 모델이 필요합니다. [Hugging Face space](https://huggingface.co/lj1995/VoiceConversionWebUI/tree/main)에서 다운로드할 수 있습니다.
- `hubert`, `pretrained_v2`, `rmvpe` 모델 파일들을 다운로드 한 후, `Retrieval_based_Voice_Conversion_WebUI/assets` 폴더의 각 모델 폴더에 모델을 위치시킵니다.
<img width="324" alt="스크린샷 2024-12-12 오후 5 15 29" src="https://github.com/user-attachments/assets/2638eee5-daa7-4a26-be5b-7e60dcca0260" />

- `models` 폴더에도 `hubert`, `rmvpe` 모델을 저장합니다.
<img width="351" alt="스크린샷 2024-12-12 오후 5 25 01" src="https://github.com/user-attachments/assets/86f63e6d-319e-4dde-abb7-1e02eadc3fbf" />

## Train
### 1. Prepare Your Dataset
모델로 생성하고자 하는 음성을 `.wav` 파일 형식으로 `dataset` 폴더에 준비합니다.

### 2. Train the Model
다음처럼 Model 파라미터를 조정하여 모델을 학습합니다.
생성된 모델은 `models/RVC` 폴더에, 인덱스 파일은 `models/RVC/.index` 폴더에 저장됩니다.
```python
from schemas.model import Model
from core.train import train_model

model = Model(
    model_name = 'test1',
    wav = 'dataset/test.wav',
    epoch = 10,
    batch_size = 7
)

model_path, index_path = train_model(model)
```

## Inference
### 1. Prepare the Voice
변환하고자 하는 음성을 준비합니다.
변환하고자 하는 음성이 `mp3` 형식일 경우, `tts/mp3` 폴더에 음성 파일을 위치시키고, 다음 코드를 사용하여 `wav` 형식으로 변환할 수 있습니다.
```python
from core.convert import mp3_to_wav

mp3 = 'test_tts'
tts = mp3_to_wav(mp3)
```
변환하고자 하는 음성이 `wav` 형식일 경우, `tts/wav` 폴더에 음성 파일을 위치시킵니다.

### 2. Model
RVC 모델을 `models/RVC` 폴더에, 인덱스 파일을 `models/RVC/.index` 폴더에 저장합니다.
이 프로젝트의 Train 과정을 진행하였다면, 모델은 자동적으로 이 위치에 이동되므로 이 작업은 생략할 수 있습니다.

### 3. Inference
다음처럼 원하는 Voice 파라미터를 입력하여 추론을 진행합니다.
추론이 완료된 음성은 `output` 폴더에 저장됩니다.
```python
from schemas.voice import Voice
from core.inference import inference_voice

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
```
**Train, Inference 전체 예시는 `main.py`에서 확인할 수 있습니다.**

## Demo
아래 링크는 침착맨 유튜브의 5분 음성으로 epoch=5, batch_size=7로 학습한 RVC 모델로 뉴스 TTS 음성을 추론한 예시입니다.

[RVC-TTS 데모 영상](https://drive.google.com/file/d/1dQxbXpND-s_njj7MYu2MXGbjd_V8UCNY/view?usp=drive_link)

다음 링크에서는 위 영상에서 변환한 음성을 확인할 수 있습니다.

[RVC-TTS 예시 음성](https://drive.google.com/file/d/1iaNIcvUgJVfFyw8lnowztDxobZgJaUDR/view?usp=sharing)

## Future Work
현재 `Amazon Polly` 서비스를 이용하여 RVC 모델의 학습부터 추론까지 이어지는 파이프라인 구현을 완료하였습니다.
이 경우, Polly의 한국어 음성은 여성 음성인 '서연'만 사용가능하여 남성 음성 변환 시, 정확도가 떨어지는 문제가 발생할 가능성이 있습니다.
이에, 다른 TTS 서비스와 연계하여 정확도 높은 음성을 학습, 추론하는 과정을 계획중입니다.

## Reference Project
- [RVC-Project/Retrieval-based-Voice-Conversion-WebUI](https://github.com/RVC-Project/Retrieval-based-Voice-Conversion-WebUI)
- [SayanoAI/RVC-Studio](https://github.com/SayanoAI/RVC-Studio)
- [mamang74/RVC_Inference_noGUI](https://github.com/mamang74/RVC_Inference_noGUI)

