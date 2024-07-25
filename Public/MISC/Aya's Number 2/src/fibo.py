def fibo(base0, base1, mod):
    def fibs(n):
        F = [[base0, base1],
            [1, 0]]
        if (n == 0):
            return 0
        power(F, n - 1)
        return ((F[0][0]*base1)%mod + (F[0][1]*base0)%mod)% mod

    def multiply(F, M):
        x = (F[0][0] * M[0][0] +
            F[0][1] * M[1][0])
        y = (F[0][0] * M[0][1] +
            F[0][1] * M[1][1])
        z = (F[1][0] * M[0][0] +
            F[1][1] * M[1][0])
        w = (F[1][0] * M[0][1] +
            F[1][1] * M[1][1])
        F[0][0] = x % mod
        F[0][1] = y % mod
        F[1][0] = z % mod
        F[1][1] = w % mod
    
    def power(F, n):
        if(n == 0 or n == 1):
            return
        M = [[base0, base1],
            [1, 0]]
        power(F, n // 2)
        multiply(F, F)
        if (n % 2 != 0):
            multiply(F, M)

    def fib(k):
        arr = [0]*100
        arr[0] = base0
        arr[1] = base1
        for i in range(2, k+1):
            arr[i] = ((base0 * arr[i - 1])%mod + (base1 * arr[i - 2])%mod)%mod
        return arr[k]
        
    # testCase
    for i in range(50, 100):
        assert fibs(i) == fib(i)

    return fibs(base0*base1)
