def add_note(filename):
    note = input("Введите заметку: ")
    with open(filename, "a", encoding="utf-8") as file:
        file.write(note + "\n")
    print("Заметка добавлена.")

def show_notes(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            notes = file.readlines()
            if not notes:
                print("Заметок пока нет.")
            else:
                print("Все заметки:")
                for i, note in enumerate(notes, 1):
                    print(f"{i}. {note.strip()}")
    except FileNotFoundError:
        print("Файл заметок не найден, заметок пока нет.")

def search_notes(filename):
    word = input("Введите слово для поиска: ")
    try:
        with open(filename, "r", encoding="utf-8") as file:
            notes = file.readlines()
            found = False
            for note in notes:
                if word.lower() in note.lower():
                    print(note.strip())
                    found = True
            if not found:
                print("Совпадений не найдено.")
    except FileNotFoundError:
        print("Файл заметок не найден, заметок пока нет.")

def main():
    filename = "notes.txt"
    while True:
        print("""
1. Добавляет заметку в файл
2. Показывает все заметки
3. Ищет заметку по слову
4. Заканчивает работу по выбору пользователя
""")
        choice = input("Выберите действие (1-4): ")
        if choice == "1":
            add_note(filename)
        elif choice == "2":
            show_notes(filename)
        elif choice == "3":
            search_notes(filename)
        elif choice == "4":
            print("Выход из программы.")
            break
        else:
            print("Некорректный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()
