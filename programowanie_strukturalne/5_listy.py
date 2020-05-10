progr=['Python', 'PHP', 'C#', 'JS', 'Java']
print(progr)
print(type(progr))

first=progr[0]
print(first)

threeElements = progr[0:3]
print(threeElements)

last=progr[-1]
print(last)

#Dodanie nowego elementu na koniec listy
progr.append('R')
progr.append('Python')
print(progr)

#zliczanie
countElement=progr.count('Python')
print(countElement)

#ilość elementów w liście
countElementsOflist=len(progr)
print(countElementsOflist)

#połączenie list
anotherList=['C', 'C++']
progr.extend(anotherList)
print('progr: ' +str(progr))
print('anotherList: ' +str(anotherList))

#Usuwanie elementów z listy
new=progr
print('New list: '+ str(new))
new.clear()
print('New list: '+ str(new))
print('Rozmiar New List: '+ str(len(new)))
print('progr: '+ str(progr))
print('Rozmiar New List: '+ str(len(progr)))

x=8
print(x)



country=[1, 2, 3, 4, 5]

print("Podaj dwa nowe elementy")
x = input("Podaj pierwszy element: ")
x= str(x)
country.append(x)
y = input("Podaj drugi element: ")
y = str(y)
country.append(y)



print("1. Wyświetl pierwsze 3 elementy listy")
print("2. Wyświetl elementy listy, które dodał*m (dane pobierz z listy)")
print("3. Wyświetl zawartość listy")
print("4. Wyczyść zawartość listy")
print("5. Znajdź element w liście, który poda użytkownik (wyświetl czy jest dodany do listy")

wprowadz=input("Wybierz opcje 1, 2, 3, 4 lub 5 ")
wprowadz = int(wprowadz)
if wprowadz==1: 
    threeElements = country[0:3]
    print(threeElements)
elif wprowadz==2:
    newElements = country[-1, -2]
elif wprowadz==3:
    print(country)
elif wprowadz==4:
    country.clear()
elif wprowadz==5:
    z = input("Podaj element: ")
    sprawdzenie=country.count(z)
    if sprawdzenie:
        print("Jest taki element")
    else: 
        print("Nie ma takiego na liście")













