def main():
    start = int(input('Enter the starting range: '))
    end = int(input('Enter the ending range: '))

    print(prime_num_finder(start, end))


def prime_num_finder(start_range, end_range):
    prime_numbers = []
    for num in range(start_range, end_range+1):
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if num > 1 and is_prime:
            prime_numbers.append(num)
    return prime_numbers


main()
