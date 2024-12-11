from pydub import AudioSegment

def mp3_to_wav(src_file: str):
    dest_file = f'tts/wav/{src_file}.wav'
    sound = AudioSegment.from_mp3(f'tts/mp3/{src_file}.mp3')
    sound.export(dest_file, format="wav")
    return dest_file