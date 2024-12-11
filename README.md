# RVC-TTS: Retrieval-based Voice Conversion Text-to-Speech

## Project Overview
**RVC-TTS** is an open-source software designed for high-quality voice conversion and text-to-speech (TTS) synthesis. Leveraging retrieval-based techniques and a modular design, this project provides an efficient and scalable way to process and convert audio data.

---

## Features
- **Retrieval-based Voice Conversion**: Transform audio with high fidelity using pre-trained models.
- **Text-to-Speech (TTS)**: Generate realistic speech from text inputs.
- **Custom Training**: Train and fine-tune models using your own datasets.
- **Web-based Interface**: Easy-to-use UI for inference and audio manipulation.

---

## Installation
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

## Directory Structure
RVC-TTS/
├── Retrieval_based_Voice_Conversion_WebUI/  # Main WebUI implementation
├── configs/                                # Configuration files
├── core/                                   # Core processing modules
├── logs/                                   # Logs and training outputs
├── models/                                 # Trained models
├── schemas/                                # Data schema definitions
├── songs/                                  # Generated audio samples
├── webui/                                  # Web UI assets
├── README.md                               # Project documentation
├── requirements.txt                        # Dependency list
└── main.py                                 # Main script for inference

---

## Dependencies
The following Python libraries are required to run the project:
- `librosa`: for audio processing
- `pydantic`: for data validation
- `faiss`: for efficient similarity search
- `parselmouth`: for pitch and audio feature extraction

Install them using:
```bash
pip install -r requirements.txt
```

---

## Acknowledgements
This project is inspired by state-of-the-art voice conversion techniques and leverages open-source tools such as Hugging Face Transformers and FAISS.
