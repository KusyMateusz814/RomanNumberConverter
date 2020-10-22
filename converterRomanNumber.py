import sys
import argparse
import logging

#roman_modern
rom_mod = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} 

#http://www.math.edu.pl/system-rzymski
#1. Obok siebie mogą stać co najwyżej trzy znaki spośród: I, X, C lub M.
#2. Obok siebie nie mogą stać dwa znaki: V, L, D.
#3. Nie może być dwóch znaków oznaczających liczby mniejsze bezpośrednio przed znakiem oznaczającym liczbę większą.
#4. Znakami poprzedzającymi znak oznaczający większą liczbę mogą być tylko znaki: I, X, C.
def checkSyntaxInputRomanNumber(romanNumber):
    logging.debug("checkSyntaxInputRomanNumber")
    logging.debug("romanNumber")
    #1
    tabFirstRule = ['I', 'X', 'C', 'M']
    tabSecondRule = ['V','L','D']
    vSumLetter=0
    good_syntax=True
    for i in range(len(romanNumber)):
        if i == 0:
            vSum=1
            beforeLetter=romanNumber[0]
            lastLetter=romanNumber[0]
            dominateLetter=romanNumber[0]
        else:
            lastLetter=romanNumber[i]
            beforeLetter=romanNumber[i-1]
            if lastLetter == beforeLetter:
                if lastLetter in tabFirstRule:
                    if vSum < 3:
                        vSum += 1
                    else:
                        print("Nie możesz użyć 3 znaków pod rząd !")
                        good_syntax=False
                        break
                else:
                   print("Nie możesz użyć tego znaku wiecej niż raz po sobie !")
                   good_syntax=False
                   break
            else:
                vSum=1
            
          
        logging.debug("i:"+str(i))
        logging.debug("  vSum:"+str(vSum))
        logging.debug("  lastletter:"+str(lastLetter))
    return good_syntax  

def def_params():
    parser = argparse.ArgumentParser(
            description='testowy opis'
    )
    parser.add_argument("-l", "--loghami", action='store_true',  help="increase output verbosity", required=False)
    parser.add_argument("-c", "--convert", help="liczba do konwersji", required=True)
    args = parser.parse_args()
    if args.loghami:
        logging.basicConfig(level=logging.DEBUG)
    return args

def converterModernToRoman(modernNumber):
    print("modernToRoman")
    return 'brak'

#Wyjaśnienie - uwaga i =0 nie sprawdzamy
###schemat działania MCM -> 
### I) iteracji dodajemy 1000 - jest pierwszą liczbą
### II) iteracji - sprawdzamy czy C jest mniejsze od M - jest , a wiec dodajemy mamy 1100
### III) iteracji - sprawdzamy czy M jest mniejsze od C - NIE jest - a więc trzeba odjąc
### ale nie tylko raz - a dwa, bo w poprzednim kroku zbędnie dodaliśmy
def converterRomanToModern(romanNumber, loghami):
    logging.debug("romanToModern")    
    val=0
    for i in range(len(romanNumber)):
        logging.debug("i:"+str(i))
        if i > 0 and rom_mod[romanNumber[i]] > rom_mod[romanNumber[i-1]]:
            val += rom_mod[romanNumber[i]] - 2 * rom_mod[romanNumber[i-1]]
        else:
            val += rom_mod[romanNumber[i]]
        logging.debug(val)
    return val

def main():
    args=def_params()
    #if args.loghami:
    logging.debug("parametry:"+str(args))
    output_number=0
    if len(sys.argv) > 1:
        number = args.convert
        if number.isnumeric():
            output_number = converterModernToRoman(number, args.loghami)
        else:
            if checkSyntaxInputRomanNumber(number) == True:
                output_number = converterRomanToModern(number, args.loghami)
                print("Wynik:" + str(output_number))
            else:
                print("Błąd w syntaksie!")
if __name__ == "__main__":
    main()

