#Exercise #1:

monthly_expenses=[2200, 2350, 2600, 2130, 2190]

# Find out if any month is exactly 2000
print(2000 in monthly_expenses)
# When insert is used, we specify the index of where to insert
monthly_expenses.insert(5, 1980)
# When append is used, we add the element to the end of the list
monthly_expenses.append(23)
# Changing value of a known index
monthly_expenses[3] = monthly_expenses[3] - 200


#Exercise #2:
heros=['spider man','thor','hulk','iron man','captain america']
# Finding Length
print(len(heros))
# Adding to the end of the list
heros.append('black panther')
print(heros)
# Removing it then adding after hulk
heros.remove('black panther')
print(heros)
heros.insert(3, 'black panther')
print(heros)
# remove thor and huld and add doctor stange
heros[1:3] = ['doctor stange']
print(heros)
# Sorting by alphabetic order
heros.sort()
print(heros)


# Exercise #3
max = int(input("Enter a number as the max"))
odd_numbers = []
for i in range(1, max):
    if i % 2 == 1:
        odd_numbers.append(i)
print(odd_numbers)

        
