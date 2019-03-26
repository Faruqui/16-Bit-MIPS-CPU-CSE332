import re

codes = {
    #Registers
    'r0': '000',
    'r1': '001',
    'r2': '010',
    'r3': '011',
    'r4': '100',
    'r5': '101',
    'r6': '110',
    'r7': '111',

    '$0': '000',
    '$1': '001',
    '$2': '010',
    '$3': '011',
    '$4': '100',
    '$5': '101',
    '$6': '110',
    '$7': '111',

    #i-format opcodes
    'andi'  : '0001',
    'addi'  : '0010',
    'subi'  : '0011',
    'beq'   : '0101',
    'bne'   : '0110',
    'bge'   : '0111',
    'ble'   : '1000',
    'lw'    : '1001',
    'sw'    : '1010',
    'lui'   : '1011',
    'ori'   : '1100',
}

rformat_opcodes = ['add', 'sub', 'and', 'or', 'addu', 'subu']

for key in rformat_opcodes:
    codes[key] = '0000'

funct = {
    'add'   : '000',
    'sub'   : '001',
    'and'   : '010',
    'or'    : '011',
    'addu'  : '100',
    'subu'  : '101',
}

def is_rformat(opcode):
    for e in rformat_opcodes:
        if e == opcode:
            return True
    return False

def is_code(opcode):
    for e in codes:
        if e == opcode:
            return True
    return False

#Turn each line of assembly code into a list, i.e. sperate the opcodes and operands
def list_codes(line):
    test = ['[^,() ]+']
    for pat in test:
        line = (re.findall(pat, line))
    return line

#swap the position of Rs, Rt Rd
def rearrange_list(list):
    try:
        if is_rformat(list[0]):
            temp = list[3]
            list[3] = list[1]
            list[1] = temp
        elif list[0] not in('lw', 'sw', 'lui', 'ori') :
            temp = list[2]
            list[2] = list[1]
            list[1] = temp
        else:
            if list[0] == "lui":
                src = list[2]
                list [2] = "r0"
                list.append(src)
            if list[0] == "lw":
                dest = list[1]
                src = list [3]
                val = list[2]
                list [1] = src
                list [2] = dest
                list [3] = val
            if list[0] == "sw":
                dest = list[3]
                src = list [1]
                val = list[2]
                list [1] = src
                list [2] = dest
                list [3] = val
    except:
        print("Error in source code")
    return list

#Decode one line of assembly code(in list format) and return machine code in a list
def decode_line(line):
    decoded_line = []
    rearrange_list(line)

    if is_rformat(line[0]):
        for e in line:
            if is_code(e):
                decoded_line.append(codes[e])
        decoded_line.append(funct[line[0]])
    else:
        for e in line:
            if is_code(e):
                decoded_line.append(codes[e])
        if line[0] not in ('lui', 'ori'):
            number = int(line[3])
            binary = f'{number:04b}'
            decoded_line.append(binary)
        else:
            number = int(line[3],16)
            binary = f'{number:04b}'
            decoded_line.append(binary)
    return decoded_line


def compile_code(assembly_code):
    line = list_codes(assembly_code)
    line = decode_line(line)
    return line

#open source code file
f = open("source.txt", "r")
#file_lines = f.readlines()
file_lines = [line for line in f.readlines() if line.strip()]

print(f"Line is: {file_lines}")

#open compiled code files
f2= open("compiled.txt","w")

for line in file_lines:
    line = line.rstrip()
    print (f'Assembly code : {line}')
    print ("Machine code : ", end=" ")
    try:
        machine_code = compile_code(line)
    except:
        machine_code = ['ERROR in source code']

    for e in machine_code:
        #f2.write(f'{codes[e]} ')
        f2.write("%s "%e)
        print(e, end=" ")
    f2.write("\n")
    print()


f.close()
f2.close()
