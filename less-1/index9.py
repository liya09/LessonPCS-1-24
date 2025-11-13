def hotel_booking(hotel):
    booking = []
    total = 0
    while True:
        name = input("имя:").lower()
        if name == "Стоп":
            print("Спасибо что зашли")
            break
        guests = int(input("Количество гостей:"))
        room = input("Стандарт, Комфорт или Люкс\n какое хотите?").title()
        if room not in hotel:
            print ("Такого номера нет")
            continue
        if hotel[room]["места"]== 0:
            print("Слишком много гостей для этого номера")
            continue
        nights = int(input("На сколько ночей ?"))
        if nights <= 0:
            print("Должно быть от 1го или больше дней")
            continue
        sums = hotel[room]["цена"] * nights
        total = total + sums
        hotel[room]['места'] -= 1
        booking.append(f"{room} {nights} = {sums}  сом")
        print(total, "total")
        print(f"Вы {name} забронили {room} на {nights} ночи , за {total} сом")
        
    if total >2000:
        dis = total*0.15 
        total = total - dis 
        print(f"Итоговая сумма : {total} сом со скидкой 15%")
    else:
        (f"Итоговая сумма : {total} сом")

hotelList = {
    "Стандарт": {"цена": 3000, "места": 5, "макс_гостей": 2},
    "Комфорт": {"цена":5000, "места":3, "макс_гостей":3},
    "Люкс": {"цена": 10000, "места":2, "макс_гостей":4}
}

hotel_booking(hotelList)
