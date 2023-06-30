# print list of primenumber
def count_primes(num):
    for a in range(1,num+1):
        print(a)
        while a < num:
            print("A from second while")
            while a <= a:
                pass


prime = count_primes(101)
print(prime)