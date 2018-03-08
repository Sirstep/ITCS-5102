def permute(xs, low=0):
    if low + 1 >= len(xs):
        yield xs
    else:
        yield from permute(xs, low + 1)
    for i in range(low + 1, len(xs)):
        xs[low], xs[i] = xs[i], xs[low]
        yield from permute(xs, low + 1)
        xs[low], xs[i] = xs[i], xs[low]

l = []
s = list(input("Enter string to permute: "))
non = 0

for p in permute(s):
    if len(p) == len(s):
        non += 1
        if (''.join(p)) not in l:
            l.append(''.join(p))
            print(''.join(p))

print('\nUnique Permutations: ' + str(len(l)) + '\nTotal Permutations: ' + str(non))