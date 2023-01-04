from ratio import Rationnel

f1 = Rationnel(2, 7)
f2 = Rationnel(5, 3)
print(f1)
print(f2)
print(f1/f2)

def nombre_euler(n, d):
        n = 0
        d = 0
        for i in range(0,n):
            n += 1 * i
            d += i * d*(i - 1)
        return Rationnel(n, d)

print(nombre_euler(5, 7))