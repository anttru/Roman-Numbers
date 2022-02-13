romanPriority = {
    "M"  : 1,
    "CM" : 2,
    "CD" : 2,
    "D"  : 2,
    "C"  : 3,
    "XC" : 4,
    "XL" : 4,   
    "L"  : 4,
    "X"  : 5,
    "IX" : 6,
    "V"  : 6,
    "IV" : 6,
    "I"  : 7
}

romanValues = {
    "M" : 1000,
    "CM": 900,
    "D" : 500,
    "CD": 400,
    "C" : 100,
    "XC": 90,
    "L" : 50,
    "XL": 40,
    "X" : 10,
    "IX": 9,
    "V" : 5,
    "IV": 4,
    "I" : 1
}

arabValues = {
    1000 : "M",
    900  : "CM",
    500  : "D",
    400  : "CD",
    100  : "C",
    90   : "XC",
    50   : "L",
    40   : "XL",
    10   : "X",
    9    : "IX",
    5    : "V",
    4    : "IV",
    1    : "I"
}
class RomanError(Exception):
    pass

def symbolExists(roman):
    if isinstance(roman, str) == False:
        raise RomanError("{} no es una cadena de texto".format(roman))
    for i in range (len(roman)):
        if roman[i] not in romanPriority:
            raise RomanError("{} no es un símbolo romano".format(roman[i]))

def currentAndNextSymbol(roman,i):
    if i == len(roman)-1:
        return (roman[-1], None)
    elif i == (len(roman)-2):
        if (roman[i] + roman[i+1]) in romanPriority:
            return (roman[i:i+2], None)
        else:
            return (roman[i], roman[i+1])
    elif i <= (len(roman) -3):
        if (roman[i] + roman[i+1]) in romanPriority:
            if i == (len(roman)-3):
                return (roman[i:i+2], roman[i+2])
            elif (roman[i+2] + roman[i+3]) in romanPriority:
                return (roman[i:i+2], roman[i+2:i+4])
            else: 
                return (roman[i:i+2], roman[i+2])
        elif (roman[i+1] + roman[i+2]) in romanPriority:
            return (roman[i], roman[i+1:i+3])
        else:
            return (roman[i], roman[i+1])

def checkOrder(roman):
    i =0
    repetitions = 0
    while i< len(roman):
        currentNext = currentAndNextSymbol(roman,i)
        currentSymbol = currentNext[0]
        nextSymbol = currentNext[1]
        if nextSymbol == None:
            return "ok"
        elif romanPriority[currentSymbol] > romanPriority[nextSymbol]:
            raise RomanError("{} no puede ir antes de {}".format(currentSymbol, nextSymbol))
        elif (currentSymbol in ("CM", "CD", "D", "XL", "XC", "L", "IX", "V", "IV")) and romanPriority[currentSymbol] == romanPriority[nextSymbol]:
            raise RomanError("{} no puede estar en un número romano que contenga además {}".format(currentSymbol, nextSymbol))
        elif (currentSymbol in ("CM", "CD", "XL", "XC", "IX", "IV")) and romanPriority[currentSymbol] == (romanPriority[nextSymbol]-1):
            raise RomanError("{} no puede ir seguido de {}".format(currentSymbol, nextSymbol))
        elif currentSymbol in ("M", "C", "X", "I"):
            if currentSymbol == nextSymbol:
                repetitions +=1
                if repetitions > 2:
                    raise RomanError("{} no puede repetirse más de tres veces".format(currentSymbol))
            else:
                repetitions = 0
        if currentSymbol in ("CM", "CD", "XC", "XL", "IX", "IV"):
            i +=1
        i +=1
            
def validateRoman(roman):
    symbolExists(roman)
    checkOrder(roman)

def validateArab(arab):
    if isinstance(arab, int) == False:
        raise TypeError("{} no es un número entero".format(arab))
    if arab < 1:
        raise ValueError("{} no es un número mayor que cero".format(arab))


def romanToArab(roman):
    validateRoman(roman)
    i = 0
    value = 0
    nextSymbol = 0 
    while nextSymbol != None:
        currentSymbol = currentAndNextSymbol(roman,i)[0]
        nextSymbol = currentAndNextSymbol(roman,i)[1]
        value += romanValues[currentSymbol]
        if currentSymbol in ("CM", "CD", "XC", "XL", "IX", "IV"):
            i += 1
        i += 1
    return value


def arabToRoman(arab):
    validateArab(arab)
    roman = ""
    if arab> 3999:
        roman += "("
        roman += arabToRoman(arab//1000)
        arab = arab%1000
        roman += ")"
    for i in (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1):
        times =  arab // i
        arab = arab % i
        roman += arabValues[i]*times
    return roman

#test

if __name__ == '__main__':

    for i in range(1,4000):
        if romanToArab(arabToRoman(i)) != i:
            print("fallo en {}".format(i))
            print(romanToArab(arabToRoman(i)))
            print(arabToRoman(i))
        