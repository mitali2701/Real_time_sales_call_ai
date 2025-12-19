import os

def save_uploaded_audio(uploaded_file):
    path = os.path.join("audio", uploaded_file.name)
    with open(path, "wb") as f:
        f.write(uploaded_file.read())
    return path
