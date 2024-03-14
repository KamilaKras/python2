numbers = [1,2,3,4,5]
numbers_in_range = list(range(1,6))

print(numbers)
print(numbers_in_range)

for value in numbers:
    print(value)

squares = []

for value in range(1,11):
    square = value **2
    squares.append(square)
print(squares)

even_numbers = list(range(2,11,2))
print(even_numbers)

for square in squares:
    print(square)

for value in range(0, len(squares)):
    print(squares[value])

#pobieranie czesci elementow
students = ['adam', 'bartosz', 'filip', 'grzegorz', 'jan']
print(students[0:2]) #wycinek dwóch pierwszych wartosci
print(students[:2]) #wyconek dwóch pierwszych wartosci
print(students[1:3])
print(students[2:4])
print(students[2:])
print(students[-2:]) #wyconek dwóch ostatnich wartosci

#kopiowanie list
another_students = students

print(id(students))
print(id(another_students))


#Instrukcje warunkowe

cars = ['audi', 'bmw', 'renault', 'skoda']

for car in cars:
    print(car)

for car in cars:
    #warunki wrzucone w oddzielnych zmiennych
    is_bmw = car.lower() == 'bmw'
    is_skoda = car.lower() == 'skoda'
    print(f"is_bmw: {is_bmw}")
    print(f"is_skoda: {is_skoda}")

    if car == 'bmw':
        print(car.upper())
    elif car == 'skoda':
        print(car)
    else:
        print(car.title())