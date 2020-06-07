print('What do you call bears with no ears?')
input()
print('B\n\n')
print('On a turkey, which side would you find most feathers?')
input()
print('The outside\n\n')
print('What do you call a priest who becomes a lawyer?')
input()
print('A father-in-law!\n\n')
print('What do dentists call an astronaut\'s cavity?')
"""
There's a backslash right before the single quote: \'.
This backslash tells you that the letter right after it
is an escape character.
An escape character lets you print special characters that
are difficult or impossible to enter into the source code
In this case, if we didn’t include the backslash, the single quote in
astronaut\'s would be interpreted as the end of the string.

print('They flew away in a green\\teal helicopter.')

output: They flew away in a green\teal helicopter.

"""
input()
print('A black hole!\n\n')
print("What do you call an elephant that doesn't matter?")
input()
print('An irrelephant!\n\n')
print('What do you call it when a cat wins a dog show?')
input()
print('A cat-has-trophy!\n\n')
print('Knock knock.')
input()
print("Who's there?")
input()
print('Interrupting cow.')
input()
print('Interrupting cow wh', end='')
print('-MOO!')

"""
Normally, print() adds a newline character to the end of the string it
prints.
This is why a blank print() function will just print a newline. But
print() can optionally have a second parameter: end.
Remember that an argument is the value passed in a function call.
The blank string passed to print() is called a keyword argument.
The end in end='' is called a keyword parameter.
To pass a keyword argument to this keyword parameter, you must type
end= before it.

Because we passed a blank string to the end parameter, the print()
function will add a blank string instead of adding a newline.
This is why '-MOO!' appears next to the previous line, instead of on
its own line. There was no newline after the 'Interrupting cow wh'
string was printed. """
