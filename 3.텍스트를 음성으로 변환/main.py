from gtts import gTTS # 문자를 음성으로 변환해주는 라이브러리
from playsound import playsound # 음성 파일을 실행해주는 라이브러리

def create_voice_from_file(file_path, output_file):
    input_lang = "ko"
    encoding = 'utf-8'
    
    with open(file_path, 'r', encoding=encoding) as file:
        text = file.read()
    
    tts = gTTS(text= text, lang = input_lang)
    tts.save(output_file)

file_path = "3.텍스트를 음성으로 변환/text.txt"
output_file = "3.텍스트를 음성으로 변환/output.mp3"

create_voice_from_file(file_path, output_file)
playsound(output_file)
