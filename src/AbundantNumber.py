x = 0

numberInput = int(input('Please enter a number: '))

propdivisers = []
propdivisersum = 0

while (x < numberInput):
    x = x + 1
    if ( (numberInput % x == 0) & ( x != numberInput) ):
        propdivisers.append(x)

propdivisersum = sum(propdivisers)

if (propdivisersum > numberInput):
    print("Number: " + str(numberInput) + " is a abundant number.")
else:
    print("Number" + str(numberInput) + "is not an abundant.")

print("The sum of the divisers: " + str(propdivisersum))
print("The number: " + str(numberInput) + " has a abundance of " + str(propdivisersum - numberInput) )
print("Proper divisers are: ")
print(propdivisers)
