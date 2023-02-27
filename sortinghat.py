Griffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print('Q1) Do you like Dawn or Dusk?')
print('   1) Dawn')
print('   2) Dusk')

Q1 = int(input('Do you like Dawn or Dusk?'))
if Q1 == 1:
    Griffindor += 1
    Ravenclaw += 1
elif Q1 == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print('Wrong input.')

print("Q2) When I'm dead I want people to remember me as:")
print('   1) The Good')
print('   2) The Great')
print('   3) The Wise')
print('   4) The Bold')

Q2 = int(input('When I am dead I want people to remember me as:'))
if Q2 == 1:
    Hufflepuff += 2
elif Q2 == 2:
    Slytherin += 2
elif Q2 == 3:
    Ravenclaw += 2
elif Q2 == 4:
    Griffindor += 2
else:
    print('Wrong input.')

print('Q3) Whcih kind of instrument most pleases your ear?')
print('  1) The violin')
print('  2) The trumpet')
print('  3) The piano')
print('  4) The drum')

Q3 = int(input('Which kind of instrument most pleases your ear?'))
if Q3 == 1:
    Slytherin += 3
elif Q3 == 2:
    Hufflepuff += 3
elif Q3 == 3:
    Ravenclaw += 3
elif Q3 == 4:
    Griffindor += 3
else:
    print('Wrong input.')

if Griffindor >= 3:
    print('Congrats! You are from: Griffindor')
elif Ravenclaw >= 3:
    print('Congrats! You are from: Ravenclaw')
elif Hufflepuff >= 3:
    print('Congrats! You are from: Hufflepuff')
elif Slytherin >= 3:
    print('Congrats! You are from: Slytherin')
