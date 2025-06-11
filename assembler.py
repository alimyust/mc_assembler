
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
    for rc in raw_code:
        mnemonic = rc[0].upper() if  rc[0] else "NOP"
        if mnemonic not in instr_dict:
            print(f"Incorrect Mnemonic on {raw_code.index(rc)}")
            code_errors = True
            continue
        loc_instruct = instr_dict[mnemonic]
        code_out.append(loc_instruct[0])
        if mnemonic == "NOP": continue

        for i in range(1, len(rc) - 1):
            print(rc)
            if rc[i][0].upper() == 'R':
                code_out[raw_code.index(rc)] += str(rc[i][1])


        # print(f"{loc_instruct} VS {rc}")
    print(code_out)

    # code_errors = False
    # for rc in raw_code:
    #     for l in rc:
    #         logicfr()

    """
    for rc in raw_code => rc = ["NOR", "4", "12"]

        case len 1
            NOP
        case len 2
            2logic()
        case len 3
            3logic()
        case len 4
            4logic()
        else:
            break:
        0000 0000 0000 
    

    
    """
        
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