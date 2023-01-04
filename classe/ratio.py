def pgcd(x, y):
    if(x == 0):
        return y
    
    while(x % y != 0):
        r = x % y
        x = y
        y = r
    return y

class Rationnel:
    def __init__(self, num, den = 1):
        if den == 0:
            raise ZeroDivisionError('denominateur nul')
        else:
            self.num = num
            self.den = den
            self.normalise()
        
    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        n = self.num * other.den + other.num * self.den
        d = self.den * other.den
        return Rationnel (n,d)

    def __sub__(self, other):
        n = self.num * other.den - other.num * self.den
        d = self.den * other.den
        return Rationnel (n,d) 

    def __mul__(self, other):
        n = self.num * other.num
        d = self.den * other.den
        return Rationnel (n,d)

    def __truediv__(self, other):
        if (other == 0):
            return
        else:
            n = self.num * other.den
            d = self.den * other.num
        return Rationnel (n,d)

    def normalise(self):
        g = pgcd(abs(self.num), abs(self.den))
        self.num = self.num // g
        self.den = self.den // g

        if (self.num * self.den < 0):
            if self.den < 0:
                self.den = -self.den
                self.num = -self.num
            else:
                if self.den < 0:
                    self.den = -self.den
                    self.num = -self.num
