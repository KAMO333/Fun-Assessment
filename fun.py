def dog_years():
    
#     """
#     Create a program that counts a dog's age in dog's years. The program should only calculate dog years until 20 human years.
#     Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.

#     Expected Output:
#     ```
#     Input a dog's age in human years: 15
#     The dog's age in dog's years is 73
#     ```
#     """

#     #enter your code here
    human_years = int(input("Input a dog's age in human years: "))

    # Check if the input is within the expected range
    if human_years > 20 or human_years < 1:
        raise ValueError('Enter a number between 1 and 20')

    # Calculate dog's age
    if human_years == 1:
        dogs_age = 10.5
    elif human_years == 2:
        dogs_age = 10.5 * 2
    else:
        dogs_age = 21 + (human_years - 2) * 4

    return f"The dog's age in dog's years is {dogs_age}"
    


def fizzbuzz(num):
    """
    Create a program that returns the numbers as a string from 1 to num. 
    But for multiples of three print “Fizz” instead of the number, 
    and for multiples of five print “Buzz”. For numbers which are 
    multiples of both three and five, print “FizzBuzz”.

    Expected Output:
    fizzbuzz(15) => "1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz"
    """

    #enter your code here

    result = ' '

    for i in range(1, num + 1):
        if i % 5 == 0 and i % 3 == 0:
            result += " " + "FizzBuzz"
        elif i %  5 == 0:
            result += " " + "Buzz"
        elif i % 3 == 0:
            result += " " + "Fizz"
        else:
            result += " " + str(i)
    
    return result.strip()


def word_lengths(sentence):
#     """
#     Create a program that takes a sentence and returns a dictionary with each unique word
#     as the key and the length of the word as the value.

#     Expected Output:
#     ```
#     Input a sentence: "Aunty Yankho is amazing"
#     Output: {'Aunty': 5, 'Yankho': 6, 'is': 2, 'amazing': 7}
#     ```
#     """
    
#     #enter your code here

    if type(sentence) != str:
        raise ValueError
    else:

        frequency = {}

        into_list = sentence.split()

        for item in into_list:
            frequency[item] = len(item)

        return frequency


def cube_sum(number):
#     """
#     Create a program that calculates the sum of the cubes of each digit in a number.
    
#     Expected Output:
#     ```
#     cube_sum(123) => 1^3 + 2^3 + 3^3 = 1 + 8 + 27 = 36
#     ```
#     """
    
#     #enter your code here
    digits = str(number)

    return sum([int(n) * int(n) * int(n) for n in digits])
