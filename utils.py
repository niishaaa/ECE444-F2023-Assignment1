class utils:
    def numRev(int1):
        if isinstance(int1, int):
            intReverse = 0
            while(int1 != 0):
                intReverse = (intReverse * 10) + (int1 % 10)
                int1 = int1//10
            print(intReverse)
        else:
            print("TypeError: Expected input value of integer type")

    def binOctConversion(int2):
        if isinstance(int2, int):
            print(bin(int2))
            print(oct(int2))
        else:
            print("TypeError: Expected input value of integer type")