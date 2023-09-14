import unittest

class utils:
    def reversed(self, int1):
        if isinstance(int1, int):
            intReverse = 0
            while(int1 != 0):
                intReverse = (intReverse * 10) + (int1 % 10)
                int1 = int1//10
            return intReverse
        else:
            raise TypeError("Expected input value of integer type for reversed arg")

    def formatter(self, int2):
        if isinstance(int2, int):
            return bin(int2), oct(int2)
        else:
            raise TypeError("TypeError: Expected input value of integer type for formatter arg")
