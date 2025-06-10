
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
    print("File setup error: {e}")
    exit()


def main():

    code_errors = False
    for c in raw_code:
        try:
            mnemonic = c[0].upper() if  c[0] else "NOP"
            loc_instruct = instr_dict[mnemonic]
            code_out.append(loc_instruct[0])
        except Exception:
            print(f"Error on line {raw_code.index(c)}")
            code_errors = True
    
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