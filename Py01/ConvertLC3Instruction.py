import numpy as np

add_cmd = np.array(['0', '0', '0', '1'])
and_cmd = np.array(['0', '1', '0', '1'])

br_cmd = np.array(['0', '0', '0', '0'])
jmp_cmd = np.array(['1', '1', '0', '0'])
jsr_cmd = np.array(['0', '1', '0', '0'])
jsrr_cmd = np.array(['0', '1', '0', '1'])

def hex_to_bin(s):
    # my_hexdata = "1a"
    scale = 16  ## equals to hexadecimal
    num_of_bits = 16
    res = bin(int(s, scale))[2:].zfill(num_of_bits)
    return res


def get_instruction(s):
    bin_str = hex_to_bin(s)
    ins = np.array(list(bin_str))
    command = ins[:4]
    dr = ins[4:7]
    therest = ins[7:16]
    if np.array_equal(command, add_cmd):
        command = "ADD"
    elif np.array_equal(command, and_cmd):
        command = "AND"
    return command, dr, therest


command, dr, therest = get_instruction("5832")
print("Command: ", command)
print("DR:      ", dr)
print("therest: ", therest)
