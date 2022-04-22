'''1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this'''
expenses = [2200,2350,2600,2130,2190]
'''Q1'''
print(expenses[1]-expenses[0])

'''Q2'''
total = 0
for i in range(3):
    total += expenses[i]
print(total)

'''Q3'''
exactly = False
for e in expenses:
    if e == 2000:
        exactly = True
        break
print(exactly)

'''Q4'''
expenses.append(1980)
print(expenses)

'''Q5'''
expenses[3] -= 200
print(expenses)