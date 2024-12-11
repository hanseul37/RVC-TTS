import os
import shutil

def moving_directory(model_path: str, index_path: str):
    model_new_path = None
    if os.path.exists(model_path):
        model_new_path = shutil.move(model_path, 'models/RVC/')
        print(f'Deleted model file: {model_path}')
    else:
        print(f'Model file not found: {model_path}')

    index_new_path = None
    if os.path.exists(index_path):
        for filename in os.listdir(index_path):
            if filename.startswith('added') and filename.endswith('.index'):
                file_path = os.path.join(index_path, filename)
                index_new_path = shutil.move(file_path, 'models/RVC/.index/')
                break
        shutil.rmtree(index_path)
        print(f'Deleted index folder: {index_path}')
    else:
        print(f'Index folder not found: {index_path}')

    return model_new_path, index_new_path