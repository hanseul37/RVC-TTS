import os
import shutil

def cleaning_directory(dataset_path: str, model_path: str, index_path: str):
    if os.path.exists(dataset_path):
        os.remove(dataset_path)
        print(f'Deleted wav file: {dataset_path}')
    else:
        print(f'Wav file not found: {dataset_path}')

    if os.path.exists(model_path):
        os.remove(model_path)
        print(f'Deleted model file: {model_path}')
    else:
        print(f'Model file not found: {model_path}')

    if os.path.exists(index_path):
        shutil.rmtree(index_path)
        print(f'Deleted index folder: {index_path}')
    else:
        print(f'Index folder not found: {index_path}')
