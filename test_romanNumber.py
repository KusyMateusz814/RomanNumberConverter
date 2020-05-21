import pytest
#do uzupelniania import do pliku

def test_converterRomanToModern12():
    result = converterRomanToModern('XII')

    assert result == 12

def test_converterRomanToModern3():
    result = converterRomanToModern('III')

    assert result == 3


def test_converterRomanToModern32():
    result = converterRomanToModern('XXXII')

    assert result == 32
   
def test_converterRomanToModern103():
    result = converterRomanToModern('CIII')

    assert result == 103

def test_converterRomanToModern1523():
    result = converterRomanToModern('MCXXIII')

    assert result == 1523


def test_converterModernToRoman12():
    result = converterModernToRoman(12)

    assert result == 'XII'

def test_converterModernToRoman3():
    result = convertModernToRoman(3)

    assert result == 'III'

def test_converterModernToRoman3():
    result = converterModernToRoman(32)

    assert result == 'XXXII'
   
def test_converterModernToRoman103():
    result = converterModernToRoman(103)

    assert result == 'CCCIII'

def test_converterModernToRoman():
    result = converterModernToRoman(1523)

    assert result == 'MCXXIII'
