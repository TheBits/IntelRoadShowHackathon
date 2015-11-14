import subprocess
import uuid

UUID = uuid.uuid1()

MIC_TIMEOUT = 5
OUT_FILE = 'speech-mmpc.mp3'
API_KEY = 'a4842bb7-929b-4d4d-9982-4a1eff599563'

def save_mic(mic_timeout=MIC_TIMEOUT, out_file=OUT_FILE):
    subprocess.call(["timeout", str(mic_timeout), 'ffmpeg',  '-y', '-f',  'alsa', '-i', 'pulse', '-acodec', 'libmp3lame', out_file])

def recognize(audio_file):
    url =   'https://asr.yandex.net/asr_xml?'+\
    'uuid=' + str(UUID.hex) + \
    '&key=' + API_KEY + \
    '&topic=queries' + \
    '&lang=ru-RU'
    command = ['curl', '-v', '-s', '-X', 'POST', '--data-binary', '@'+OUT_FILE, url, '-H', "Content-Type: audio/x-mpeg-3"]
    print('command: ' + ' '.join(command))
    out_text = subprocess.check_output(command)
    out_text = str(out_text)
    print(out_text)

if __name__ == '__main__':
    print('start record')
    save_mic()
    print('stop record')
    print('start speech to text')
    recognize(OUT_FILE)
    print('ok')
