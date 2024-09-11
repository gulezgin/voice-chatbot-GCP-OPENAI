from speech_recognition import kayit_dinle, ses_to_metn
from gpt_integration import gpt_ile_cevapla
from text_to_speech import metni_sese_cevir

def sesli_chatbot():
  
    kayit_dinle()

    kullanici_metin = ses_to_metn()
    print("Kullanıcı Metni:", kullanici_metin)

    chatbot_cevabi = gpt_ile_cevapla(kullanici_metin)
    print("Chatbot Cevabı:", chatbot_cevabi)
    
    metni_sese_cevir(chatbot_cevabi)

if __name__ == "__main__":
    sesli_chatbot()
