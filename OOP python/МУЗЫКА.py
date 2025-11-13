import time

def type_lyric(line, char_delay=0.06):
    # Проходим по каждому символу строки
    for char in line:
        print(char, end="", flush=True)
        time.sleep(char_delay)  # задержка между символами
    print()  # перенос строки после каждой строки текста


def play_reel():
    lyrics = [
"Secrets I have held in my heart",
"Are harder to hide than I thought",
"Maybe I just wanna be yours",
"I wanna be yours",
"I wanna be yours",
"Wanna be yours",
"Wanna be yours",
"Wanna be yours",
"Let me be your 'leccy meter",
"An' I’ll never run out",
"Let me be the portable heater",
"That you’ll get cold without",
"I wanna be your setting lotion (Wanna be)",
"Hold your hair in deep devotion (How it deep?)",
"At least as deep as the Pacific Ocean",
"I wanna be yours",
"Secrets I have held in my heart",
"Are harder to hide than I thought",
"Maybe I just wanna be yours",
"I wanna be yours",
"I wanna be yours",
"Wanna be yours",
"Wanna be yours",
"Wanna be yours",
"Wanna be yours",
"Wanna be yours",
"Wanna be yours",
"Wanna be yours",
"Wanna be yours",
"I wanna be your vacuum cleaner (Wanna be yours)",
"Breathin' in your dust (Wanna be yours)",
"I wanna be your Ford Cortina (Wanna be yours)",
"I will never rust (Wanna be yours)",
"I just wanna be yours (Wanna be yours)",
"I just wanna be yours (Wanna be yours)",
"I just wanna be yours (Wanna be yours)",
"I just wanna be yours (Wanna be yours)"
        
]

    delays = [1.8, 1.8, 2.2, 2.5, 1.8, 1.8, 2.0, 2.2, 2.5, 1.5, 1.8, 1.8, 2.2, 2.5, 1.8, 1.8, 2.0, 2.2, 2.5, 1.5, 1.8, 1.8, 2.2, 2.5, 1.8, 1.8, 2.0, 2.2, 2.5, 1.5, 1.8, 1.8, 2.2, 2.5, 1.8, 1.8, 2.0, 2.2, 2.5, 1.5, 1.8, 1.8, 2.2, 2.5, 1.8, 1.8, 2.0, 2.2, 2.5, 1.5]

    print("\nNow Playing: 'I Wanna Be Yours' - Arctic Monkeys (Python Reel)\n")
    time.sleep(1.5)

    for i, line in enumerate(lyrics):
        type_lyric(line)
        time.sleep(delays[i])  # задержка между строкамb

# Запуск
play_reel()