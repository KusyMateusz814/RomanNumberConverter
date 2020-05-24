import pytest
from converterRomanNumber import converterRomanToModern
from converterRomanNumber import converterModernToRoman
from converterRomanNumber import checkSyntaxInputRomanNumber
#1. Obok siebie moga stać co najwyżej trzy znaki sposrod: I, X, C, M
#metoda checkSyntaxInputRomanNumber zwraca false jesli input ma zly syntax
def test_syntaxInputRomanNumberXXXX():
    result = checkSyntaxInputRomanNumber('XXXX')
 
    assert result == False

def test_syntaxInputRomanNumberXXX():
    result = checkSyntaxInputRomanNumber('XXX')

    assert result == True

def test_syntaxInputRomanNumberCCC():
    result = checkSyntaxInputRomanNumber('CCC')
 
    assert result == True

def test_syntaxInputRomanNumberCCCC():
    result = checkSyntaxInputRomanNumber('CCCC')
 
    assert result == False

def test_syntaxInputRomanNumberMMMM():
    result = checkSyntaxInputRomanNumber('MMMM')
 
    assert result == False

def test_syntaxInputRomanNumberMMM():
    result = checkSyntaxInputRomanNumber('MMM')
 
    assert result == True

def test_syntaxInputRomanNumberIIII():
    result = checkSyntaxInputRomanNumber('III')
 
    assert result == True

def test_syntaxInputRomanNumberIIII():
    result = checkSyntaxInputRomanNumber('IIII')
 
    assert result == False
#2. Obok siebie nie mogą stać dwa znaki: V, L, D
#2. Obok siebie nie mogą stać dwa znaki: V, L, D
def test_syntaxInputRomanNumberVV():
    result = checkSyntaxInputRomanNumber('VV')
 
    assert result

def test_syntaxInputRomanNumberMLL():
    result = checkSyntaxInputRomanNumber('MLL')
 
    assert result

def test_syntaxInputRomanNumberCVV():
    result = checkSyntaxInputRomanNumber('CVV')
 
    assert result

#3. Nie może być dwóch znaków oznaczających liczby mniejsze bezpośrednio przed
#znakiem oznaczającym liczbę większą
def test_syntaxInputRomanNumberIIV():
    result = checkSyntaxInputRomanNumber('IIV','-l')
 
    assert result

def test_syntaxInputRomanNumberXXC():
    result = checkSyntaxInputRomanNumber('XXC','-l')
 
    assert result

def test_syntaxInputRomanNumberCCM():
    result = checkSyntaxInputRomanNumber('LLM','-l')

    assert result
#4. Znakami poprzedzającymi znak oznaczającymi większą liczbę mogą być tylko znaki: I, X, C
def test_syntaxInputRomanNumberII():
    result = checkSyntaxInputRomanNumber('VX','-l')
 
    assert result

def test_syntaxInputRomanNumberXXC():
    result = checkSyntaxInputRomanNumber('DM','-l')
 
    assert result

def test_syntaxInputRomanNumberCCM():
    result = checkSyntaxInputRomanNumber('LM','-l')


def test_converterRomanToModern12():
    result = converterRomanToModern('XII',True) #to samo gdyby bylo ('XII','-l')

    assert result == 12

def test_converterRomanToModern3():
    result = converterRomanToModern('III','-l')

    assert result == 3

def test_converterRomanToModern32():
    result = converterRomanToModern('XXXII','-l')

    assert result == 32
   
def test_converterRomanToModern103():
    result = converterRomanToModern('CIII','-l')

    assert result == 103

def test_converterRomanToModern1523():
    result = converterRomanToModern('MDXXIII','-l')

    assert result == 1523

def test_converterRomanToModern133():
    result = converterRomanToModern('CXXXIII','-l')

    assert result == 133


def test_converterRomanToModern109():
    result = converterRomanToModern('CIX','-l')

    assert result == 109


#def test_converterModernToRoman12():
#    result = converterModernToRoman(12)
#
#    assert result == 'XII'
#
#def test_converterModernToRoman3():
#    result = convertModernToRoman(3)
#
#    assert result == 'III'
#
#def test_converterModernToRoman3():
#    result = converterModernToRoman(32)
#
#    assert result == 'XXXII'
#   
#def test_converterModernToRoman103():
#    result = converterModernToRoman(103)
#
#    assert result == 'CCCIII'
#
#def test_converterModernToRoman():
#    result = converterModernToRoman(1523)
#
#    assert result == 'MCXXIII'
