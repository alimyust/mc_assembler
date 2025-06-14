
import csv
import string

# Reading Instruction Set
p = f"mc_assembler/"
instr_dict = {}
code_out = []

try:

    with open(p + 'instruction_set.csv', newline='') as csvfile:
        instr_set = [row for row in csv.reader(csvfile)]
        for row in instr_set:
            instr_dict[row[0]] = row[1:]

    with open(p + 'code/code.txt', newline='') as f:
        raw_code = [line.rstrip("\n").rstrip("\r").split(" ") for line in f.readlines()]

except Exception as e:
    print(f"File setup error: {e}")
    exit()

def int_to_bin(num:int, bit_len:int) -> str:
    num = str(bin(num))[2:]
    while len(num) < bit_len:
        num = "0" + num
    return num        


def main():

    code_errors = False
    instruction_size = 16
    
    for rc in raw_code:
        mnemonic = rc[0].upper() if  rc[0] else "NOP"
        if mnemonic not in instr_dict:
            print(f"Incorrect Mnemonic on {raw_code.index(rc)}")
            code_errors = True
            continue

        loc_instruct = instr_dict[mnemonic] 
        code_out.append(loc_instruct[0])
        if mnemonic == "NOP": continue

        for i in range(1, len(rc)):
            if rc[i][0].upper() == 'R':
                code_out[raw_code.index(rc)] += int_to_bin(int(rc[i][1]), 4)
            elif rc[i].isdigit():
                code_out[raw_code.index(rc)] += int_to_bin(int(rc[i]), 8)
            else:
                print(f"INVALID OUTPUT ON {raw_code.index(rc)}")
                code_errors = True
   
    for i in range(len(code_out)):
        code_out[i] += "0" * (instruction_size - len(code_out[i]))

    # Prevents writing if there are errors in the file
    if code_errors: 
        exit()

    #Writing the file all at once incase there were errors earlier
    with open(p + "output/out_1.txt", "w") as f:
        for line in code_out:
            f.write(line + "\n")

    exit()
              
if __name__ == '__main__':
    main()