from google.cloud import texttospeech

def metni_sese_cevir(metin, cikis_dosyasi="audio/cevap.mp3"):
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=metin)
    ses = texttospeech.VoiceSelectionParams(language_code="tr-TR", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL)
    audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

    response = client.synthesize_speech(input=input_text, voice=ses, audio_config=audio_config)

    with open(cikis_dosyasi, "wb") as cikis:
        cikis.write(response.audio_content)
    print(f"Cevap kaydedildi: {cikis_dosyasi}")
