import sys

#roman_modern
rom_mod = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} 

def converterModernToRoman(modernNumber):
    print("modernToRoman")
    return 'brak'

#Wyjaśnienie - uwaga i =0 nie sprawdzamy
###schemat działania MCM -> 
### I) iteracji dodajemy 1000 - jest pierwszą liczbą
### II) iteracji - sprawdzamy czy C jest mniejsze od M - jest , a wiec dodajemy mamy 1100
### III) iteracji - sprawdzamy czy M jest mniejsze od C - NIE jest - a więc trzeba odjąc
### ale nie tylko raz - a dwa, bo w poprzednim kroku zbędnie dodaliśmy
def converterRomanToModern(romanNumber):
    print("romanToModern")
    val=0
    for i in range(len(romanNumber)):
        print("i:"+str(i))
        if i > 0 and rom_mod[romanNumber[i]] > rom_mod[romanNumber[i-1]]:
            val += rom_mod[romanNumber[i]] - 2 * rom_mod[romanNumber[i-1]]
        else:
            val = val + rom_mod[romanNumber[i]]
        print(val)
    return val

def main():
    print(sys.argv)
    output_number=0
    if len(sys.argv) > 1:
        number = sys.argv[1]
        if number.isnumeric():
            output_number = converterModernToRoman(number)
        else:
            output_number = converterRomanToModern(number)
        print("Hell NO" + str(output_number))
if __name__ == "__main__":
    main()

