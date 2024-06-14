import speech_recognition

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.5

commands_dict = {
    'commands':{
        'greeting': ['привет','приветствую','здарова','приветик'],
        'create_task': ['сделай задачу','сделаю задачу','заадчу','запиши',]
    }
}
def listen_command():
    '''Слушает наши команды'''
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
            return query
    except speech_recognition.UnknownValueError:
        return f'Я тебя ваще не понял'


def greeting():
    '''Приветствие пользователя'''
    return('Привет нищеброд!')

def create_task():
    '''Записывает список дел'''

    print('Что делаем сегодня?')
    query = listen_command()
    with open('todo-list.txt', 'a') as file:
        file.write(f'*{query}\n')
        return(f'Задача {query} была записана')

def main():
    query = listen_command()
    for k,v in commands_dict['commands'].items():
        if query in v:
            print(k)


if __name__ == '__main__':
    main()