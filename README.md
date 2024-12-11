# RVC-TTS: Retrieval-based Voice Conversion and Text-to-Speech

## Overview
기존의 프로젝트에서 ~~ Mac 환경에서의 개발
~~ 수정예정
---

## Features
- **Retrieval-based Voice Conversion**: RVC 모델 생성부터 음성 변환까지  ~~ 수정예정

---

## Installation
1. assets 다운로드
2. ffmpeg 설치
3. RMVPE 인간 음성 피치 추출 알고리즘에 필요한 파일 다운로드
### 1. Clone the repository:
```bash
git clone https://github.com/hanseul37/RVC-TTS.git
cd RVC-TTS
```

### 2. Set up a Python virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## Usage
### 1. Prepare Your Dataset
Add your `.wav` files to the `dataset` directory. For example:
```bash
dataset/test.wav
```

### 2. Train the Model
Use the provided training script to train a voice conversion model:
```bash
python train.py
```

### 3. Run Inference
Perform inference using the trained model:
```bash
python main.py
```

---

## Reference Project
Retrieval-based-Voice-Conversion-WebUI
RVC-Studio
RVC_Inference_noGUI

