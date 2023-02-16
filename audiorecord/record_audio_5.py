from audio_settings import *

outputFile = "audio_5.wav"
audio_output_file = "output_5.wav"
device_index = 2
audio = pyaudio.PyAudio()


def audioExists(audioFile):
    if os.path.isfile(audioFile):
        os.remove(audioFile)

def outputExists(audio_output_file):
    if os.path.isfile(audio_output_file):
        os.remove(audio_output_file)

def audioDevice():
    with open("vardata.txt", "r") as file:
        text = file.readlines()
        audio_device_index = text[0]
        return int(audio_device_index)

def record(outputFile, index):
    stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,input_device_index = index, frames_per_buffer=CHUNK)
    Recordframes = []
 
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        Recordframes.append(data)
    
    stream.stop_stream()
    stream.close()
    audio.terminate()
    
    waveFile = wave.open(outputFile, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(Recordframes))
    waveFile.close()
    
def amplifyAudio():
    factor = 10
    with wave.open(outputFile, 'rb') as wav:
        p = wav.getparams()
        with wave.open(audio_output_file, 'wb') as audio:
            audio.setparams(p)
            frames = wav.readframes(p.nframes)
            audio.writeframesraw(audioop.mul(frames, p.sampwidth, factor))

audioExists(outputFile)
outputExists(audio_output_file)
record(outputFile, audioDevice())
amplifyAudio()