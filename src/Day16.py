import pathlib

OPCODES = ['addr', 'addi', 'mulr', 'muli', 'banr', 'bani', 'borr', 'bori', 'setr', 'seti',
           'gtri', 'gtir', 'gtrr', 'eqri', 'eqir', 'eqrr']


def count_possible_opcodes(self, reg_in, a, b, c, reg_out):
    t = 0
    for opcode_id in OPCODES:
        if reg_out == self.compute_value(opcode_id, reg_in[:], a, b, c):
            print(f"- OK for {opcode_id}")
            t += 1
    return t


def compute_value(opcode_id, registers, input_a, input_b, input_c):
    if opcode_id == 'addr':
        registers[input_c] = registers[input_a] + registers[input_b]
    elif opcode_id == 'addi':
        registers[input_c] = registers[input_a] + input_b
    elif opcode_id == 'mulr':
        registers[input_c] = registers[input_a] * registers[input_b]
    elif opcode_id == 'muli':
        registers[input_c] = registers[input_a] * input_b
    elif opcode_id == 'banr':
        registers[input_c] = registers[input_a] & registers[input_b]
    elif opcode_id == 'bani':
        registers[input_c] = registers[input_a] & input_b
    elif opcode_id == 'borr':
        registers[input_c] = registers[input_a] | registers[input_b]
    elif opcode_id == 'bori':
        registers[input_c] = registers[input_a] | input_b
    elif opcode_id == 'setr':
        registers[input_c] = registers[input_a]
    elif opcode_id == 'seti':
        registers[input_c] = input_a
    elif opcode_id == 'gtir':
        registers[input_c] = 1 if input_a > registers[input_b] else 0
    elif opcode_id == 'gtri':
        registers[input_c] = 1 if registers[input_a] > input_b else 0
    elif opcode_id == 'gtrr':
        registers[input_c] = 1 if registers[input_a] > registers[input_b] else 0
    elif opcode_id == 'eqir':
        registers[input_c] = 1 if input_a == registers[input_b] else 0
    elif opcode_id == 'eqri':
        registers[input_c] = 1 if registers[input_a] == input_b else 0
    elif opcode_id == 'eqrr':
        registers[input_c] = 1 if registers[input_a] == registers[input_b] else 0
    else:
        raise Exception(f"Wrong opcode_id: {opcode_id}")
    return registers


if __name__ == '__main__':
    with open(f'../inputs/{pathlib.Path(__file__).stem}.txt', 'r') as f:
        samples, test_prg = f.read().split('\n\n\n\n')

samples = samples.split('\n')
before_reg = [eval(reg.replace('Before: ', '')) for reg in samples[::4]]
opcodes = [list(map(int, opcode.split())) for opcode in samples[1::4]]
after_reg = [eval(reg.replace('After: ', '')) for reg in samples[2::4]]
test_prg = [list(map(int, instruction.split())) for instruction in test_prg.split('\n')]

total = 0
candidates = {i: [] for i in range(len(OPCODES))}

for reg_bef, opcode_in, reg_aft in zip(before_reg, opcodes, after_reg):
    print(f"reg_bef={reg_bef}, opcodes_in={opcode_in}, reg_out={reg_aft}")
    possible = []
    for opcode_name in OPCODES:
        if reg_aft == compute_value(opcode_name, reg_bef[:], opcode_in[1], opcode_in[2], opcode_in[3]):
            print(f"- OK for {opcode_name}")
            possible.append(opcode_name)

    if len(possible) >= 3:
        total += 1
    candidates[opcode_in[0]].append(possible)

print(f"The result of first star is {total}")
candidates = {i: [name for name in OPCODES if all(name in turn for turn in candidates[i])] for i in candidates}
while any(len(candidates[c]) > 1 for c in candidates):
    for c in candidates:
        if len(candidates[c]) == 1:
            v = candidates[c][0]
            for j in candidates:
                if j != c and v in candidates[j]:
                    candidates[j].remove(v)
candidates = {i: name[0] for i, name in candidates.items()}

final_registers = [0, 0, 0, 0]
for opcode in test_prg:
    final_registers = compute_value(candidates[opcode[0]], final_registers, opcode[1], opcode[2], opcode[3])
print(f"The result of second star is {final_registers[0]}")
