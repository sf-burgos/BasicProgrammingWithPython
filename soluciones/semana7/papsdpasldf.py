def primes_sieve(limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)

    return primes

primes = set(primes_sieve(1000000));
exclude = ['2','4','5','6','8','0']
def circularPrime(n):
    ss = str(n);
    for i in range(n):
        if ss[-1] in exclude:
            return 0;
        if int(ss) not in primes:
            return 0;
        ss = ss[-1] + ss[:-1];
    return 1;

gg = 0;
for num in primes:
    gg += circularPrime(num);
print (gg);
