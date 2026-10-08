
def string_length(text):
    return len(text)



def first_two_and_last_two_characters(text):
    if len(text) < 2:
        return ""

    return text[:2] + text[-2:]


def add_ing(text):
    if len(text) < 3:
        return text

    if text.endswith("ing"):
        return text + "ly"

    return text + "ing"


def longest_word(words):
    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest, len(longest)



def remove_even_index(text):
    result = ""

    for i in range(len(text)):
        if i % 2 != 0:
            result += text[i]

    return result



def find_minimum(numbers):
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest



def find_maximum(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest



def repeat_string(text, number):
    if type(number) == float:
        return text

    return text * number


# 9. Square every element in a list
def square_elements(numbers):
    result = []

    for number in numbers:
        result.append(number ** 2)

    return result



def sum_of_squares(numbers):
    total = 0

    for number in numbers:
        total += number ** 2

    return total


print(string_length("semicolon"))

print(first_two_and_last_two_characters("semicolon"))
print(first_two_and_last_two_characters("on"))
print(first_two_and_last_two_characters("o"))

print(add_ing("jollof"))
print(add_ing("unfalling"))
print(add_ing("so"))

words = ["university", "marriage", "baby", "cry", "mother", "food"]
word, length = longest_word(words)
print(word, length)

print(remove_even_index("parallelogram"))

numbers = [7884, 7488, 7848, 78844]
print(find_minimum(numbers))
print(find_maximum(numbers))

print(repeat_string("hey", 10))
print(repeat_string("dude", 3.0))

numbers = [5, 7, 9, 11, 13]
print(square_elements(numbers))
print(sum_of_squares(numbers))


