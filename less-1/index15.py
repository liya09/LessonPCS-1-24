def TourAgent(tours, services):
    total = 0 
    orders = []
    name = input("Ваше имя")
    age = int (input("Введите возраст:"))
    while True:
        print("доступные туры")
        for key, val in tours.items():
            print(key,val['цена'],val['min_age'],val['длительность'],val['Количество'])
        choice = input ("Выберите тур(стоп):")
        if choice == 'стоп':
            break
        if choice not in tours:
            print("Такого тура нет")
            continue

        total += tours[choice]['цена']
        orders.append((choice,tours[choice]['цена']))
        print(f"Клиент:{name} взял(а) тур на {choice} за {total}$")
        print(orders)

        
    


tours = {
    'Тайланд': {'цена':500, 'min_age':16, 'длительность':5, "Количество":6 },
     'Италия': {'цена':1100, 'min_age':18, 'длительность':3, "Количество":10 },
      'Турция': {'цена':400, 'min_age':16, 'длительность':7, "Количество":9 },
}
services = {
  'страховка': 300,
  'эккурсии': 100,
  'трансфер': 200,
}
 
TourAgent(tours, services)