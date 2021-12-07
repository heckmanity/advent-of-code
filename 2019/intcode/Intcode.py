from intcode.Operations import Instr_Set
from copy import deepcopy

class Intcode:
    def __init__(self, mem):
        self.memory = mem
        self.pointer = 0
        self.relative_base = 0

        self.instructions = Instr_Set()
        self.memory_reset = deepcopy(self.memory)
        self.outputs = []

        self.running = None
        self.halted = None

        self.chatty = None
        self.pause_on_output = None

    def run(self, *inputs, verbose=False, outpause=False):
        self.chatty = verbose
        self.pause_on_output = outpause

        self.running = True
        self.halted = False
        inputs = list(inputs) if inputs else inputs

        while self.running:
            current_instruction = self.memory[self.pointer]
            op_code = current_instruction % 100
            mode_prefix = str(current_instruction // 100)

            instr_len = self.instructions.get_op_len(op_code)
            arguments = self.memory[self.pointer+1:self.pointer+instr_len]
            in_value = inputs.pop(0) if len(inputs)>0 and op_code==3 else None

            if self.chatty:
                print("Pointer at {}; relative base at {}".format(self.pointer, self.relative_base))
                print("Instruction: {}, {}".format(current_instruction, arguments))
            
            new_pointer = self.instructions.execute(op_code, mode_prefix, self, \
                *arguments, auto_input=in_value)

            if new_pointer is None:
                self.pointer += instr_len
            else:
                self.pointer = new_pointer

    def reset(self):
        self.memory = deepcopy(self.memory_reset)
        self.pointer = 0
        self.relative_base = 0
        self.outputs = []
    
    def expand_memory(self, reqd_addr):
        addition_reqd = (reqd_addr + 1) - len(self.memory)
        self.memory += [0] * addition_reqd
