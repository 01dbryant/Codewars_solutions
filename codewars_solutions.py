# solution code for Codewars problem: Even or Odd
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


# solution code for Codewars problem: convert a number to a string
def number_to_string(num):
    return str(num)

# solution code for Codewars problem:  Removes the spaces from the string.


def no_space(x):
    return x.replace(" ", "")

# solution code for Codewars problem: Or if you choose a vowel count


def get_count(sentence):
    vowels = "aeiou"
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count
