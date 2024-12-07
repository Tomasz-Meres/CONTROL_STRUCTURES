###
# A program that prints the first twenty words of the Fibonacci sequence
#

fibonacci_sequence = [0, 1]  # first two numbers of Fibonacci sequence

for i in range(1, 19):
    next_number = fibonacci_sequence[i] + fibonacci_sequence[i - 1]
    fibonacci_sequence.append(next_number)

for x in fibonacci_sequence:
    print(f'{x}', end=' ')


"""
fibonacci_sequence = []
for i in range(0, 20):
    if i == 0 or i == 1:
        fibonacci_sequence.append(i)
    else:
        next_number = fibonacci_sequence[i-1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_number)

for x in fibonacci_sequence:
    print(f'{x}', end=' ')
"""