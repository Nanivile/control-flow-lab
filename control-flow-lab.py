# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

letter = input('Please enter a letter from the alphabet (a-z or A-Z): ').lower()
if letter == 'a' or letter =='e' or letter == 'i' or letter == 'o' or letter == 'u':
    print(f'The letter {letter} is a vowel')
else:
    print(f'The letter {letter} is a consonant.')



# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

quit = ''
while True:
    if quit == 'quit':
        break
    word = input('Please enter a word or phrase: ')
    print(f'What you enterd is {len(word)} characters long')
    quit = input('If you want to quit, enter "quit"').lower()



# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age like this:
#      Input a dog's age: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hints:
# Use the int() function to convert the string returned from input() into an integer
# Start with an if that checks if the age is less than 3

dog_age = input("Input a dog's age: ")
dog_age = int(dog_age)
if dog_age < 3:
    print(f"The dog's age in dog years is {dog_age*10}")
else:
    print(f"The dog's age in dog years is {20+((dog_age-2)*7)}")

# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - exactly two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

print('Enter the lengths of three side of a triangle')
a = input('a: ')
b = input('b: ')
c = input('c: ')
a = int(a)
b = int(b)
c = int(c)

if a == b and a == c and b == c:
    print('This is an equilateral triangle')
elif a == b and a != c or b == c and b != a or c == a and c != b:
    print('This is an isosceles triangle')
else:
    print('This triangle is scalene')

# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hints:
# The next number is found by adding the two numbers before it
# Use a while loop with a looping variable, or look into Python ranges, e.g.:
#   for n in range(50):

fib1 = 0
fib2 = 1
fib_holder = 1
for fib in range(50):
    print(f'term: {fib+1} / number: {fib1}')
    fib1 = fib1 + fib_holder
    fib_holder = fib2
    fib2 = fib1

# exercise-06 What's the Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
#   if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.

month = input('Enter the month of the year (Jan - Dec): ').lower()
day = input('Enter the day of the month: ')
day = int(day)

if month in ['dec', 'jan', 'feb', 'mar']:
    if month == 'dec' and day < 21:
        print(f'{month} {day} is in Fall')
    elif month == 'mar' and day > 19:
        print(f'{month} {day} is in Spring')
    else:
        print(f'{month} {day} is in Winter')
if month in ['april', 'may', 'jun']:
    if month == 'jun' and day > 20:
        print(f'{month} {day} is in Summer')
    else:
        print(f'{month} {day} is in Spring')
if month in ['july', 'aug', 'sep']:
    if month == 'sep' and day > 21:
        print(f'{month} {day} is in Fall')
    else:
        print(f'{month} {day} is in Summer')
if month in ['oct', 'nov']:
    print(f'{month} {day} is in Fall')