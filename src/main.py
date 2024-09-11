from speech_recognition import kayit_dinle, ses_to_metn
from gpt_integration import gpt_ile_cevapla
from text_to_speech import metni_sese_cevir

def sesli_chatbot():
    # Ses kaydet
    kayit_dinle()

    # Sesi metne çevir
    kullanici_metin = ses_to_metn()
    print("Kullanıcı Metni:", kullanici_metin)

    # GPT-4 ile cevap üret
    chatbot_cevabi = gpt_ile_cevapla(kullanici_metin)
    print("Chatbot Cevabı:", chatbot_cevabi)

    # Cevabı sese çevir
    metni_sese_cevir(chatbot_cevabi)

if __name__ == "__main__":
    sesli_chatbot()
