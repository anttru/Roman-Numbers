romanValues = {
    "M" : 1000,
    "CM": 900,
    "L" : 500,
    "CL": 400,
    "C" : 100,
    "XC": 90,
    "D" : 50,
    "XD": 40,
    "X" : 10,
    "IX": 9,
    "V" : 5,
    "IV": 4,
    "I" : 1
}

arabValues = {
    1000 : "M",
    900  : "CM",
    500  : "L",
    400  : "CL",
    100  : "C",
    90   : "XC",
    50   : "D",
    40   : "XD",
    10   : "X",
    9    : "IX",
    5    : "V",
    4    : "IV",
    1    : "I"
}
romanPriority = {
    "M"  : 1,
    "CM" : 2,
    "CL" : 3,
    "L"  : 4,
    "C"  : 5,
    "XC" : 6,
    "XD" : 7,   
    "D"  : 8,
    "X"  : 9,
    "IX" : 10,
    "V"  : 11,
    "IV" : 12,
    "I"  : 13
}

class RomanError(Exception):
    pass

def symbolExists(roman):
    if isinstance(roman, str) == False:
        raise RomanError("{} no es una cadena de texto".format(roman))
    for i in range (len(roman)):
        if roman[i] not in romanPriority:
            raise RomanError("{} no es un símbolo romano".format(roman[i]))

def countSymbols(roman):
    symbolCounter= {
    "M" : 0,
    "CM": 0,
    "L" : 0,
    "CL": 0,
    "C" : 0,
    "XC": 0,
    "XD": 0,
    "D" : 0,
    "X" : 0,
    "IX": 0,
    "V" : 0,
    "IV": 0,
    "I" : 0
    }
    i=0
    if len(roman) == 1:
            pass
    while i<= (len(roman)-2):
        if (roman[i] + roman[i+1]) in romanPriority:
            symbolCounter[roman[i] + roman[i+1]] +=1
            i+=1
            if i == (len(roman)-2):
                symbolCounter[roman[-1]] += 1
        elif roman[i] in romanPriority:
            symbolCounter[roman[i]] +=1
            if i == (len(roman)-2):
                symbolCounter[roman[-1]] += 1
        i+=1 
    for symbol in symbolCounter:
        if symbolCounter[symbol] > 1 and symbol in ("CM", "XC", "L", "V", "IV", "D", "IX", "CL", "XL"):
            raise RomanError("{} no puede repetirse".format(symbol))
        elif symbolCounter[symbol] > 3 and symbol in ("M", "C", "X", "I"):
            raise RomanError("{} no puede repetirse más de 3 veces".format(symbol))
    if  (symbolCounter["CM"] + symbolCounter["L"] + symbolCounter["CL"]) > 1 or \
        (symbolCounter["XD"] + symbolCounter["D"] + symbolCounter["XC"]) > 1 or \
        (symbolCounter["IX"] + symbolCounter["V"] + symbolCounter["IV"]) > 1 :
            raise RomanError("Combinación no válida de 9/5/4")
    if  ((symbolCounter["CM"] == 1 or symbolCounter["CL"] ==1) and symbolCounter["C"]) > 0 or \
        ((symbolCounter["XC"] == 1 or symbolCounter["XD"] ==1) and symbolCounter["X"]) > 0 or \
        ((symbolCounter["IX"] == 1 or symbolCounter["IV"] ==1) and symbolCounter["I"]) > 0 :
            raise RomanError("Combinación no válida de 9/4/1")
    
def checkOrder(roman):
    i=0
    while i<= (len(roman)-2):
        if len(roman) == 1:
            pass
        elif len(roman) == 2 and ((roman[i] + roman[i+1]) in romanPriority):
            pass
        elif  ((roman[i] + roman[i+1]) in romanPriority) and i == (len(roman)-2):
            pass 
        elif ((roman[i] + roman[i+1]) in romanPriority):
            if romanPriority[roman[i] + roman[i+1]] >= romanPriority[roman[i+2]]:
                raise RomanError("{} no puede ir antes de {}".format((roman[i] + roman[i+1]),roman[i+2]))
            i+=1
        elif (roman[i]) in romanPriority:
            if romanPriority[roman[i]] > romanPriority[roman[i+1]]:
                raise RomanError("{} no puede ir antes de {}".format(roman[i],roman[i+1]))
        i+= 1        

def validateRoman(roman):
    symbolExists(roman)
    countSymbols(roman)
    checkOrder(roman)

def validateArab(arab):
    if isinstance(arab, int) == False:
        raise TypeError("{} no es un número entero".format(arab))
    if arab < 1:
        raise ValueError("{} no es un número mayor que cero".format(arab))
    if arab >= 4000:
        raise ValueError("{} es mayor de 3999".format(arab))

def romanToArab(roman):
    validateRoman(roman)
    i = 0
    value = 0
    if len(roman) == 1:
            value += romanValues[roman[0]]
            return value
    while i <= (len(roman)-2):
        if roman[i]+roman[i+1] in romanValues:
            value += romanValues[roman[i]+roman[i+1]]
            i += 1
        elif roman[i] in romanValues:
            value += romanValues[roman[i]]
        if i == (len(roman)-2):
            value += romanValues[roman[-1]]
        i += 1
    return value

def arabToRoman(arab):
    validateArab(arab)
    roman = ""
    remaining = arab
    for i in (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1):
        times =  remaining // i
        remaining = remaining % i
        roman += arabValues[i]*times
    return roman

#test

if __name__ == '__main__':

    for i in range(1,3999):
        if romanToArab(arabToRoman(i)) != i:
            print("fallo en {}".format(i))
            print(romanToArab(arabToRoman(i)))
            print(arabToRoman(i))


