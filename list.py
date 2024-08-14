# Task 1
name = ["Rakib", "Rafay", "Khadija", "Ameena", "Ayesha"]
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])

# Task 2
print(f"\nHello, {name[0]}! Hope you are fine.")
print(f"Hello, {name[1]}! Hope you are fine.")
print(f"Hello, {name[2]}! Hope you are fine.")
print(f"Hello, {name[3]}! Hope you are fine.")
print(f"Hello, {name[4]}! Hope you are fine.")

# Task 3
tranportation_mode=["Car","Bus","Bike","Train"]
print(f"\nI would Like to own a {tranportation_mode[1]} mode")

# Task 4
dinner_guest=["Rafay","Ameena","Khadija"]
print(f"\n{dinner_guest[0]}, I would be honored to have you join me for dinner.")
print(f"\n{dinner_guest[1]}, I would be honored to have you join me for dinner.")
print(f"\n{dinner_guest[2]}, I would be honored to have you join me for dinner.")

# Task 5
unable_to_attend=dinner_guest[0]
print(f"\nSorry {unable_to_attend} can't make it to dinner.")
dinner_guest[0]="Ayesha"
print(f"\n{dinner_guest[0]}, I would be honored to have you join me for dinner.")

# Task 6

dinner_guest = ["Ayesha", "Ameena", "Khadija"]

print("\nGood news! I found a bigger table, so now I can invite more guests!")
dinner_guest.insert(0, "Rafay")
middle_index = len(dinner_guest) // 2
dinner_guest.insert(middle_index, "Rakib")
dinner_guest.append("Ayesha")
print(f"\n{dinner_guest[0]}, I would be honored to have you join me for dinner.")
print(f"\n{dinner_guest[1]}, I would be honored to have you join me for dinner.")
print(f"\n{dinner_guest[2]}, I would be honored to have you join me for dinner.")
print(f"\n{dinner_guest[3]}, I would be honored to have you join me for dinner.")
print(f"\n{dinner_guest[4]}, I would be honored to have you join me for dinner.")
print(f"\n{dinner_guest[5]}, I would be honored to have you join me for dinner.")

# Task 7
dinner_guest = ["Rafay", "Ayesha", "Ameena", "Rakib", "Khadija", "Ayesha"]

print("\nUnfortunately, I can only invite two people for dinner.")

removed_guest = dinner_guest.pop()
print(f"\nSorry {removed_guest}, I can't invite you to dinner.")

removed_guest = dinner_guest.pop()
print(f"\nSorry {removed_guest}, I can't invite you to dinner.")

removed_guest = dinner_guest.pop()
print(f"\nSorry {removed_guest}, I can't invite you to dinner.")

removed_guest = dinner_guest.pop()
print(f"\nSorry {removed_guest}, I can't invite you to dinner.")

print(f"\n{dinner_guest[0]}, you are still invited to dinner.")
print(f"\n{dinner_guest[1]}, you are still invited to dinner.")

del dinner_guest[0]
del dinner_guest[0]

print("\nFinal guest list:", dinner_guest)

# Task 8
places = ["Paris", "Tokyo", "New York", "Cape Town", "Sydney"]

print("Original list:", places)
print("Alphabetical order:", sorted(places))
print("Original list (unchanged):", places)
print("Reverse-alphabetical order:", sorted(places, reverse=True))
print("Original list (unchanged):", places)

places.reverse()
print("List after reverse():", places)

places.reverse()
print("List after reversing again:", places)

places.sort()
print("List after sort():", places)

places.sort(reverse=True)
print("List after sort(reverse=True):", places)

# Task 9
cities = ["Paris", "Tokyo", "New York", "Cape Town", "Sydney"]

print("Original list:", cities)
print("Alphabetical order:", sorted(cities))
print("Original list (unchanged):", cities)
print("Reverse-alphabetical order:", sorted(cities, reverse=True))
print("Original list (unchanged):", cities)

cities.reverse()
print("List after reverse():", cities)

cities.reverse()
print("List after reversing again:", cities)

cities.sort()
print("List after sort():", cities)

cities.sort(reverse=True)
print("List after sort(reverse=True):", cities)

cities.append("Los Angeles")
print("List after append():", cities)

cities.insert(0, "Berlin")
print("List after insert():", cities)

removed_city = cities.pop()
print("Removed city:", removed_city)
print("List after pop():", cities)

cities.remove("Tokyo")
print("List after remove():", cities)

del cities[0]
print("List after del:", cities)

cities.clear()
print("List after clear():", cities)

#Task 10
# List of cities
cities = ["Paris", "Tokyo", "New York", "Cape Town", "Sydney"]

# Attempt to access an index that does not exist
try:
    print(cities[10])  # This will cause an IndexError
except IndexError as e:
    print("IndexError:", e)

# Correct the error by accessing a valid index
print("Accessing a valid index:", cities[2])  # This should work
