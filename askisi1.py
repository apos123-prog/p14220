# p14220
p14220 ergasia eisagwgi stin epistimi twn upologistwn



primes = []
for num in range(2, 1000):
    if all(num % i != 0 for i in range(2, num)):
        primes.append(num)
x = primes[-1] - primes[0]
print(x)
