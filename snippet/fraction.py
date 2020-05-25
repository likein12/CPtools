class Fraction:

    gcd_dict = {}

    def gcd(self, a ,b):
        if a<b:
            a,b = b,a

        if (a,b) in Fraction.gcd_dict:
            return Fraction.gcd_dict[(a,b)]

        a0,b0 = a,b
        while a%b!=0:
            a,b = b,a%b
        Fraction.gcd_dict[(a0,b0)] = b 
        return b
 
    def frac(self,a,b, gcd_flag = True):
        if a==0 and b==0:
            return (0,0)
        elif a==0:
            return (0,1)
        elif b==0:
            return (1,0)
        else:
            if gcd_flag:
                d = self.gcd(abs(a),abs(b))
            else:
                d = 1
            if b<0:
                a,b = -a,-b
            return (a//d,b//d)
    
    def __init__(self, a, b, gcd_flag = True):
        self.value = self.frac(a,b,gcd_flag)
 
    def v(self):
        return self.value
 
    def __lt__(self, other):
        assert self.value!=(0,0) and other.value!=(0,0), 'value (0,0) cannot be compared.'
        a,b = self.value
        c,d = other.value
        return a*d < b*c
    
    def __le__(self, other):
        assert self.value!=(0,0) and other.value!=(0,0), 'value (0,0) cannot be compared.'
        a,b = self.value
        c,d = other.value
        return a*d <= b*c
 
    def __eq__(self, other):
        a,b = self.value
        c,d = other.value
        return a==c and b==d
 
    def __ne__(self, other):
        a,b = self.value
        c,d = other.value
        return not (a==c and b==d)
 
    def __gt__(self, other):
        assert self.value!=(0,0) and other.value!=(0,0), 'value (0,0) cannot be compared.'
        a,b = self.value
        c,d = other.value
        return a*d > b*c
 
    def __ge__(self, other):
        assert self.value!=(0,0) and other.value!=(0,0), 'value (0,0) cannot be compared.'
        a,b = self.value
        c,d = other.value
        return a*d >= b*c
 
    def __add__(self, other):
        a,b = self.value
        c,d = other.value
        return Fraction(a*d + b*c, b*d)
        
    def __sub__(self, other):
        a,b = self.value
        c,d = other.value
        return Fraction(a*d - b*c, b*d)
 
    def __mul__(self, other):
        a,b = self.value
        c,d = other.value
        return Fraction(a*c, b*d)
 
    def __truediv__(self, other):
        a,b = self.value
        c,d = other.value
        return Fraction(a*d, b*c)
    
    def __neg__(self):
        a,b = self.value
        return Fraction(-a,b,True)
        
    def inv(self):
        a,b = self.value
        return Fraction(b,a,True)

    def show(self):
        a,b = self.value
        print('Fraction('+str(a)+'/'+str(b)+')')
