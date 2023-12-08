def collatz_conjecture():
    num = int(input("\nEnter an integer number: "))
    sequence = [num]
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = (num * 3) + 1
        sequence.append(num)
    return sequence
