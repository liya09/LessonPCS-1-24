#Теранный оператор

age = 20
if age >=18:
    status = 'Взрослый'
else:
    status = 'Несовершеннолетний'
print(status)

#Теранный
status2 = "Взрослый" if age >=18 else "Несовершеннолетний"
print(status2)

###
n = 5 
if n >= 0:
    print("possitive")
else:
    print("negative")

###
print("positive" if n >=0 else "negative")

####
def ball_to_mark(ball):
    return 'отлично' if ball >=90 else 'хорошо' if ball >=75 else 'удов' if ball >=65 else 'неудов'

    print(ball_to_mark(76))

###
temperature = -5
print(f"На улице{'тепло' if temperature >0 else 'холодно'}")


####
nums =[]
for i in range(100):
    nums.append(i)
print(nums)

####
numbers = [i for i in range(100)]
print(numbers)

####
numbers = [i for i in range(100) if i %2 ==0]
print(numbers)

