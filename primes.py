import os
import time
import math

red = "\033[0;31m"
green = "\033[0;32m"
reset = "\033[0;0m"
strike = "\033[9m"

#create the set of numbers 
def create_number_set():
    try:
        max_num = int(input("what number do you want to find primes up to - "))
        if max_num < 2:
            print("enter a number more than 2")
            return create_number_set()  
        else:
            number_set = set(range(2, max_num + 1))
            return number_set
    except ValueError:
        print("enter a number")
        return create_number_set()  

#checks if its prime  
def is_prime(n):
    if n <= 1: #if n is less than or equal to 1 if it is it rules it out as that cant be prime
        return False
    if n == 2: #automaticaly a prime number 
        return True
    if n % 2 == 0: #if n is even (divisible by 2) and greater than 2 it is ruled out
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2): #checks for factors of n starting from 3 up to the squr root of n and if any of the numbers evenly divide n it retunrs false 
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    numbers = create_number_set()
    print("number set - ", numbers)
    print("preparing...")
    time.sleep(1.2)
    print(green + "finding primes..." + reset)
    start_time = time.time()  

    primes = []  

    while numbers:
        current_num = numbers.pop()
        if is_prime(current_num):

            multiples = set(range(current_num * 2, max(numbers, default=current_num * 2) + 1, current_num)) #explain 
            numbers -= multiples
            primes.append(current_num)  
    end_time = time.time()  
    elapsed_time = end_time - start_time

    downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
    file_path = os.path.join(downloads_folder, 'prime-numbers.txt')

    with open(file_path, 'w') as file:
        for prime in primes:
            file.write(str(prime) + '\n')
    print("done =)")
    print("primes saved to", file_path)
    print("elapsed time", elapsed_time, "sec")
    print(green + "©2024 Ec#0")
