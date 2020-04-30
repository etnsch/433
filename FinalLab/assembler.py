#Assembler for 433 final lab assignment
#Don't look at the code too closely, it's a pile of hot garbage but it works somehow (usually)
#I got rid of the destination for most commands
#Any command that outputs to a fixed destination (ie accumulator) shouldn't have a destination specified since the destination is built in to the command
#Commands that output to a register (other than accumulator) or memory need a destination

import re

header = 'v2.0 raw\n'
inPath = 'C:\\Users\\ethan\\OneDrive\\Documents\\School\\433\\Lab 5\\assemblyCode.txt'
outPath = 'C:\\Users\\ethan\\OneDrive\\Documents\\School\\433\\Lab 5\\machineCode.txt'

#instruction type 1 - no registers, no immediate values. just opcode
def t1(opcode):
    str = hex(opcode)[2:].zfill(2)
    str = str + '00'
    return str

#instruction type 2 - one register
def t2(opcode, r1):
    str1 = hex(opcode)[2:].zfill(2)
    r = int(r1[1])
    r = r << 1
    str2 = hex(r)[2:]
    str = str1 + str2 + '0'
    return str

#instruction type 3 - two registers
def t3(opcode, r1, r2):
    str1 = hex(opcode)[2:].zfill(2)
    r1temp = int(r1[1])
    r1temp = r1temp << 1
    r2temp = int(r2[1])
    if(r2temp >= 4):
        r2temp = r2temp - 4
        r1temp += 1
    r2temp = r2temp << 2
    str2 = hex(r1temp)[2:]
    str3 = hex(r2temp)[2:]
    str = str1 + str2 + str3
    return str

#instruction type 4 - immediate value
def t4(opcode, data):
    str1 = hex(opcode)[2:].zfill(2)
    if(data[0:2] == '0x'):
        data = re.sub(r'\D', '', data)
        data = data[1:]
        str2 = data.zfill(2)
        str = str1 + str2
        return str
    elif(data[0:2] == '0b'):
        data = re.sub(r'\D', '', data)
        data = data[1:]
        str2 = hex(int(data, 2))[2:].zfill(2)
        str = str1 + str2
        return str
    else:
        data = re.sub(r'\D', '', data)
        str2 = hex(int(data))[2:].zfill(2)
        str = str1 + str2
        return str

#add instruction
def add(argList):
    if(len(argList) != 3):
        print('Invalid number of arguments at line ' + str(curLine))
        return -1

    if(argList[1][0] == 'A'):
        if(argList[2][0] == '%'):
            print('0')
            return t2(0, argList[2])
        else:
            print('1')
            return t4(1, argList[2])
    else:
        print('Invalid argument ' + argList[1][0] + ' at line ' + str(curLine))
        return -1
    return 0

#subtraction instruction
def sub(argList):
    if (len(argList) != 3):
        print('Invalid number of arguments at line ' + str(curLine))
        return -1

    if(argList[1][0] == 'A'):
        if(argList[2][0] == '%'):
            print('2')
            return t2(2, argList[2])
        else:
            print('3')
            return t4(3, argList[2])
    elif(argList[2] == 'A'):
        if(argList[1][0] == '%'):
            print('4')
            return t2(4, argList[1])
        else:
            print('5')
            return t4(5, argList[1])
    else:
        print('Invalid argument at line ' + str(curLine))
        return -1
    return 0

#multiply instruction
def mul(argList):
    if (len(argList) != 3):
        print('Invalid number of arguments at line ' + str(curLine))
        return -1

    if(argList[1][0] == 'A'):
        if (argList[2][0] == '%'):
            print('6')
            return t2(6, argList[2])
        else:
            print('7')
            return t4(7, argList[2])
    else:
        print('Invalid argument ' + argList[1][0] + ' at line ' + str(curLine))
        return -1
    return 0

#signed multiply instruction
def smul(argList):
    if (len(argList) != 3):
        print('Invalid number of arguments at line ' + str(curLine))
        return -1

    if(argList[1][0] == 'A'):
        if(argList[2][0] == '%'):
            print('8')
            return t2(8, argList[2])
        else:
            print('9')
            return t4(9, argList[2])
    else:
        print('Invalid argument ' + argList[1][0] + ' at line ' + str(curLine))
        return -1
    return 0

#division instruction
def div(argList):
    if (len(argList) != 3):
        print('Invalid number of arguments at line ' + str(curLine))
        return -1

    if(argList[1][0] == 'A'):
        if(argList[2][0] == '%'):
            print('10')
            return t2(10, argList[2])
        else:
            print('11')
            return t4(11, argList[2])
    elif(argList[2] == 'A'):
        if(argList[1][0] == '%'):
            print('12')
            return t2(12, argList[1])
        else:
            print('13')
            return t4(13, argList[1])
    else:
        print('Invalid argument at line ' + str(curLine))
        return -1
    return 0

#signed division instruction
def sdiv(argList):
    if (len(argList) != 3):
        print('Invalid number of arguments at line ' + str(curLine))
        return -1

    if (argList[1][0] == 'A'):
        if (argList[2][0] == '%'):
            print('14')
            return t2(14, argList[2])
        else:
            print('15')
            return t4(15, argList[2])
    elif (argList[2] == 'A'):
        if (argList[1][0] == '%'):
            print('16')
            return t2(16, argList[1])
        else:
            print('17')
            return t4(17, argList[1])
    else:
        print('Invalid argument at line ' + str(curLine))
        return -1
    return 0

#AND instruction
def nd(argList):
    if (len(argList) != 3):
        print('Invalid number of arguments at line ' + str(curLine))
        return -1

    if (argList[1][0] == 'A'):
        if (argList[2][0] == '%'):
            print('18')
            return t2(18, argList[2])
        else:
            print('19')
            return t4(19, argList[2])
    else:
        print('Invalid argument ' + argList[1][0] + ' at line ' + str(curLine))
        return -1
    return 0

#OR instruction
def ore(argList):
    if (len(argList) != 3):
        print('Invalid number of arguments at line ' + str(curLine))
        return -1

    if (argList[1][0] == 'A'):
        if (argList[2][0] == '%'):
            print('20')
            return t2(20, argList[2])
        else:
            print('21')
            return t4(21, argList[2])
    else:
        print('Invalid argument ' + argList[1][0] + ' at line ' + str(curLine))
        return -1
    return 0

#XOR instruction
def xor(argList):
    if (len(argList) != 3):
        print('Invalid number of arguments at line ' + str(curLine))
        return -1

    if (argList[1][0] == 'A'):
        if (argList[2][0] == '%'):
            print('22')
            return t2(22, argList[2])
        else:
            print('23')
            return t4(23, argList[2])
    else:
        print('Invalid argument ' + argList[1][0] + ' at line ' + str(curLine))
        return -1
    return 0

#left shift instruction
def lsh(argList):
    if (len(argList) != 3):
        print('Invalid number of arguments at line ' + str(curLine))
        return -1

    if (argList[1][0] == 'A'):
        if (argList[2][0] == '%'):
            print('24')
            return t2(24, argList[2])
        else:
            print('25')
            return t4(25, argList[2])
    elif (argList[2] == 'A'):
        if (argList[1][0] == '%'):
            print('26')
            return t2(26, argList[1])
        else:
            print('27')
            return t4(27, argList[1])
    else:
        print('Invalid argument at line ' + str(curLine))
        return -1
    return 0

#right shift instruction
def rsh(argList):
    if (len(argList) != 3):
        print('Invalid number of arguments at line ' + str(curLine))
        return -1

    if (argList[1][0] == 'A'):
        if (argList[2][0] == '%'):
            print('28')
            return t2(28, argList[2])
        else:
            print('29')
            return t4(29, argList[2])
    elif (argList[2] == 'A'):
        if (argList[1][0] == '%'):
            print('30')
            return t2(30, argList[1])
        else:
            print('31')
            return t4(31, argList[1])
    else:
        print('Invalid argument at line ' + str(curLine))
        return -1
    return 0

#arithmetic shift instruction
def ash(argList):
    if (len(argList) != 3):
        print('Invalid number of arguments at line ' + str(curLine))
        return -1

    if (argList[1][0] == 'A'):
        if (argList[2][0] == '%'):
            print('32')
            return t2(32, argList[2])
        else:
            print('33')
            return t4(33, argList[2])
    elif (argList[2] == 'A'):
        if (argList[1][0] == '%'):
            print('34')
            return t2(34, argList[1])
        else:
            print('35')
            return t4(35, argList[1])
    else:
        print('Invalid argument at line ' + str(curLine))
        return -1
    return 0

#cmp instruction - status flags only
def cmp(argList):
    if (len(argList) != 3):
        print('Invalid number of arguments at line ' + str(curLine))
        return -1

    if (argList[1][0] == 'A'):
        if (argList[2][0] == '%'):
            print('36')
            return t2(36, argList[2])
        else:
            print('37')
            return t4(37, argList[2])
    else:
        print('Invalid argument ' + argList[1][0] + ' at line ' + str(curLine))
        return -1
    return 0

#test instruction - status flags only
def test(argList):
    if (len(argList) != 3):
        print('Invalid number of arguments at line ' + str(curLine))
        return -1

    if (argList[1][0] == 'A'):
        if (argList[2][0] == '%'):
            print('38')
            return t2(38, argList[2])
        else:
            print('39')
            return t4(39, argList[2])
    else:
        print('Invalid argument ' + argList[1][0] + ' at line ' + str(curLine))
        return -1
    return 0

#move instruction
def mov(argList):
    if(len(argList) == 2):
        if(argList[1] == 'B'):
            print('40')
            return t1(40)
        elif(argList[1] == 'F'):
            print('41')
            return t1(41)
        elif(argList[1][0] == '%'):
            print('42')
            return t2(42, argList[1])
        elif(argList[1][0] == '['):
            if(argList[1][1] == '%'):
                print('44')
                return t2(44, argList[1][1:])
            else:
                print('45')
                return t4(45, argList[1])
        else:
            print('43')
            return t4(43, argList[1])

    elif(len(argList) == 5 and argList[1] == 'PC' and argList[2] == 'L' and argList[3] == '->' and argList[4] == 'A'):
        print('46')
        return t1(46)

    elif(len(argList) == 8 and argList[1] == 'PC' and argList[2] == 'L,' and argList[3] == 'PC' and argList[4] == 'H' and argList[5] == '->' and argList[6] == 'A,' and argList[7][0] == '%'):
        print('47')
        return t2(47, argList[7])

    elif(len(argList) == 4 and argList[1] == 'A' and argList[2] == '->' and argList[3][0] == '%'):
        print('48')
        return t2(48, argList[3])

    elif(len(argList) == 4 and argList[1][0] == '%' and argList[2] == '->' and argList[3][0] == '%'):
        print('49')
        return t3(49, argList[1], argList[3])

    #Legal?
    #elif(len(argList) == 4 and argList[2] == '->' and argList[3][0] == '%'):
    #    print('50')
    #    return t4(50, argList[1])

    elif (len(argList) == 4 and argList[1] == 'A' and argList[2] == '->' and argList[3][0] == 'F'):
        print('50')
        return t1(50)

    elif (len(argList) == 8 and argList[1] == 'A,' and argList[2][0] == '%' and argList[3] == '->' and argList[4] == 'PC' and argList[5] == 'L,' and argList[6] == 'PC' and argList[7] == 'H'):
        print('51')
        return t2(51, argList[2])

    elif (len(argList) == 4 and argList[1] == 'A' and argList[2] == '->' and argList[3][0] == '['):
        if(argList[3][1] == '%'):
            print('52')
            return t2(52, argList[3][1:])
        else:
            print('53')
            return t4(53, argList[3][1:])

    else:
        print('idk man something is probably wrong')
        return -1
    return 0


Instructions = {
    'add': add,
    'sub': sub,
    'mul': mul,
    'smul': smul,
    'div': div,
    'sdiv': sdiv,
    'and': nd,
    'or': ore,
    'xor': xor,
    'lsh': lsh,
    'rsh': rsh,
    'ash': ash,
    'cmp': cmp,
    'test': test,
    'mov': mov
}

def assemble(line):
    list = line.split()
    inst = list[0].lower()
    try:
        return Instructions[inst](list)
    except:
        print('Invalid command at line ' + str(curLine))

def main():
    inFile = open(inPath, 'r')
    try:
        outFile = open(outPath, 'w')
    except:
        print('I guess if you see this there was a file error of some kind, idk')

    outFile.write(header)

    global curLine
    curLine = 0

    for line in inFile:
        curLine += 1
        temp = assemble(line)
        if(temp == -1):
            print('something went wrong')
            return
        outFile.write(temp + ' ')

    inFile.close()
    outFile.close()

if __name__== '__main__':
    main()
