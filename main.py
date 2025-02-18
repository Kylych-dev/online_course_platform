
def hello():
    numbers = [1, 2, 3, 4, 5]
    for i in numbers:
        pass





def replace_letter(letter):
    letter = letter.lower()
    frequency = {}
    for let in letter:
        frequency[let] = frequency.get(let, 0) + 1
    # print(frequency, '-=-=')
    for let in letter:
        print(let)
    return letter
# result = replace_letter('hello world')

# print(result)


def replace_letter_2(letter):
    letter1 = letter.lower()
    res = letter1
    frequency = {}

    for let in letter1:
        print(let, '<>')
        if let in frequency:
            frequency[let] += 1
    print(frequency, 'it is frequency')

    for val in letter:
        res = res.replace(val, ')')
    return res


result = replace_letter_2('HELLO')

print(result, 'it is result')









