import subprocess
import uuid

UUID = uuid.uuid1()

MIC_TIMEOUT = 5
OUT_FILE = 'out.wav'
API_KEY = 'a4842bb7-929b-4d4d-9982-4a1eff599563'

def save_mic(mic_timeout=MIC_TIMEOUT, out_file=OUT_FILE):
    subprocess.call(["timeout", str(mic_timeout), 'ffmpeg',  '-y', '-ar', '16000', '-acodec', 'pcm_s16be', '-f',  'alsa', '-i', 'pulse', out_file])

def recognize(audio_file):
    url =   'https://asr.yandex.net/asr_xml?'+\
    'uuid=' + str(UUID.hex) + \
    '&key=' + API_KEY + \
    '&topic=numbers' + \
    '&lang=ru-RU'
    command = ['curl', '-X', 'POST', '--data-binary', '@'+OUT_FILE, url, '-H', "Content-Type: audio/x-wav"]
    command = ['curl', '-v', '-X', 'POST', '--data-binary', '@'+OUT_FILE, url, '-H', "Content-Type: audio/x-pcm;bit=16;rate=16000"]
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
