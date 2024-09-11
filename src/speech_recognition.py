from google.cloud import speech
import pyaudio
import wave

def kayit_dinle(sure=5, dosya_adi="audio/kayit.wav"):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)

    print("Kayıt başlıyor...")
    frames = []
    for _ in range(0, int(RATE / CHUNK * sure)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("Kayıt tamamlandı.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    with wave.open(dosya_adi, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

def ses_to_metn(dosya_adi="audio/kayit.wav"):
    client = speech.SpeechClient()

    with open(dosya_adi, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="tr-TR",
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        return result.alternatives[0].transcript
