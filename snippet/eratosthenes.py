def sieve_of_eratosthenes(n):
	pl = [i for i in range(2, n + 1)]
	i=0
	p = pl[0]
	while p**2<=n:
		pl = [pl[j] for j in range(len(pl)) if pl[j]%p!=0 or j<=i]
		i+=1
		p=pl[i]
	return pl
