# Define dictionaries for function and opcode mappings
r_type_functions = {
    "nor": "000",
    "or": "001",
    "add": "010",
    "srl": "011",
    "slt": "100",
    "sll": "101",
    "sub": "110",
    "and": "111",
}

i_type_opcodes = {
    "beq": "001",
    "bne": "010",
    "sw": "011",
    "lw": "101",
    "addi": "110",
}

j_type_opcodes = {
    "jmp": "100",
}

# Function to convert decimal to binary of fixed width
def decimal_to_binary(value, bits):
    if value < 0:
        value = (1 << bits) + value
    return format(value, f"0{bits}b")

# Function to convert binary to hexadecimal
def binary_to_hex(binary):
    return hex(int(binary, 2))[2:].zfill(5)  # 20 bits -> 5 hex digits

# Main assembler function
def assemble(input_file, output_file):
    with open(input_file, "r") as infile, open(output_file, "w") as outfile:
        outfile.write("v2.0 raw\n")
        
        for line in infile:
            line = line.strip().lower()
            if not line:
                continue
            
            parts = line.split()
            instr_type = parts[0]
            
            # NOP instruction processing (fixed bits)
            if instr_type == "nop":
                opcode = "000"
                rd = "0000"
                rs = "0000"
                rt = "0000"
                shamt = "00"
                func = "000"
                binary_instruction = f"{opcode}{rs}{rt}{rd}{shamt}{func}"
                hex_instruction = binary_to_hex(binary_instruction)
                outfile.write(hex_instruction + "\n")

            # Process R-type instructions
            elif instr_type in r_type_functions:
                opcode = "000"
                #if it is srl or sll
                if instr_type == 'srl' or instr_type == 'sll':
                    func = r_type_functions[instr_type]
                    rd = decimal_to_binary(int(parts[1][1:]), 4)
                    rs = decimal_to_binary(int(parts[2][1:]), 4)
                    rt = "0000"
                    shamt = decimal_to_binary(int(parts[3]),2) if len(parts) > 3 else "01"

                # if it is not srl or sll
                else:
                    func = r_type_functions[instr_type]
                    rd = decimal_to_binary(int(parts[1][1:]), 4)
                    rs = decimal_to_binary(int(parts[2][1:]), 4)
                    rt = decimal_to_binary(int(parts[3][1:]), 4)
                    shamt = "00"
                # if len(parts) > 4: 
                #     shamt = decimal_to_binary(int(parts[4]),2)
                # else:
                #     shamt = "00"
                binary_instruction = f"{opcode}{rs}{rt}{rd}{shamt}{func}"
                hex_instruction = binary_to_hex(binary_instruction)
                outfile.write(hex_instruction + "\n")

            # Process I-type instructions
            elif instr_type in i_type_opcodes:
                opcode = i_type_opcodes[instr_type]
                rt_or_rd = decimal_to_binary(int(parts[1][1:]), 4)
                rs = decimal_to_binary(int(parts[2][1:]), 4)
                immediate = decimal_to_binary(int(parts[3]), 9)
                binary_instruction = f"{opcode}{rs}{rt_or_rd}{immediate}"
                hex_instruction = binary_to_hex(binary_instruction)
                outfile.write(hex_instruction + "\n")

            # Process J-type instructions
            elif instr_type in j_type_opcodes:
                opcode = j_type_opcodes[instr_type]
                address = decimal_to_binary(int(parts[1]), 17)
                binary_instruction = f"{opcode}{address}"
                hex_instruction = binary_to_hex(binary_instruction)
                outfile.write(hex_instruction + "\n")
            else:
                raise ValueError(f"Unknown instruction: {instr_type}")


# Run assembler
input_file = "input.txt" 
output_file = "output.txt"
assemble(input_file, output_file)