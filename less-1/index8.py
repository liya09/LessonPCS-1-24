def raz_park(park):
    while True:
        age = int(input("Введите возраст: "))
        Nameticket = input("введите название аттриакцион: ").capitalize()
        if Nameticket == 'Стоп':
            print("спасибо что посетили нас")
            break
        if Nameticket not in park:
            print ("Такого аттракционна нету")
            continue
        if park[Nameticket]['места'] == 0:
            print ("Мест больше нет")
            continue
        if  age < park[Nameticket]['возраст']:
            print("Вам пока нельзя на этот аттриакцион ")
            continue
        ticketUser = int(input("количество билетов"))
        if ticketUser > park[Nameticket]['места']:
            print("Недостаточно мест,у нас сейчас ",park[Nameticket]['места'], "мест" )
            continue
        
    price = park[Nameticket]['цена']*count
total += price
park[Nameticket]['места'] -= count
park[Nameticket] = park.get(Nameticket, 0) + count
print(f"Куплено {count} билет(ов) в {park} за {price} сом")
if total > 1500:
           print("Применена скидка 10%")
        
parkList = {
    "Американские горки": {"цена": 500, "места": 5, "возраст": 12},
    "Колесо обозрения": {"цена": 300, "места": 8, "возраст": 0},
    "Комната страха": {"цена": 400, "места":4, "возраст": 14},
    "Карусель": {"цена": 200, "места": 6, "возраст": 0}
}  
raz_park(parkList)
