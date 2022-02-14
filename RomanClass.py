from RomanNumerals import arabToRoman, romanToArab

class RomanNumber:
    def __init__(self, value):
        if isinstance(value, int):
            self.roman = arabToRoman(value)
            self.arab = value
        elif isinstance(value, str):
            self.arab = romanToArab(value)
            self.roman = value
        else: 
            raise TypeError("La entrada ha de ser entero o un número romano")

    def __str__(self):
        return self.roman
    
    def __repr__(self):
        return "{}.....{}".format(self.roman, self.arab)

    def __lt__(self, other):
        if not isinstance(other, RomanNumber):
            raise TypeError("Entrada ha de ser de clase romano")
        return self.arab < other.arab
    def __eq__(self, other):
        if not isinstance(other, RomanNumber):
            raise TypeError("Entrada ha de ser de clase romano")
        return self.arab == other.arab
    def __ne__(self, other):
        if not isinstance(other, RomanNumber):
            raise TypeError("Entrada ha de ser de clase romano")
        return self.arab != other.arab
    def __gt__(self, other):
        if not isinstance(other, RomanNumber):
            raise TypeError("Entrada ha de ser de clase romano")
        return self.arab > other.arab
    def __ge__(self, other):
        if not isinstance(other, RomanNumber):
            raise TypeError("Entrada ha de ser de clase romano")
        return self.arab >= other.arab
    def __le__(self, other):
        if not isinstance(other, RomanNumber):
            raise TypeError("Entrada ha de ser de clase romano")
        return self.arab <= other.arab
    def __add__(self, other):
        if not isinstance(other, RomanNumber):
            raise TypeError("Entrada ha de ser de clase romano")
        total = self.arab + other.arab
        return RomanNumber(total)
        

    




    