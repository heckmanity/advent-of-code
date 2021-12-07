class Instr_Set:
    def __init__(self):
        self.operations = {
             1: self.IC_add,
             2: self.IC_mult,
             3: self.IC_input,
             4: self.IC_output,
             5: self.IC_jump_if_true,
             6: self.IC_jump_if_false,
             7: self.IC_less_than,
             8: self.IC_equals,
             9: self.adj_rel_base,
            99: self.halt
        }
        self.op_length = {
             1: 4,
             2: 4,
             3: 2,
             4: 2,
             5: 3,
             6: 3,
             7: 4,
             8: 4,
             9: 2,
            99: 1
        } 
        self.param_types = {
             1: ['R', 'R', 'W'],
             2: ['R', 'R', 'W'],
             3: ['W'],
             4: ['R'],
             5: ['R', 'R'],
             6: ['R', 'R'],
             7: ['R', 'R', 'W'],
             8: ['R', 'R', 'W'],
             9: ['R'],
            99: ['X']
        }

    def get_op_len(self, op_code):
        return self.op_length[op_code]

    def execute(self, op_code, mode_prefix, *args, auto_input=None):
        modes = [int(b) for b in mode_prefix[::-1]]
        diff = self.op_length[op_code] - len(modes) - 1
        modes += [0] * diff
        for i in range(len(modes)):
            if self.param_types[op_code][i]=='W':
                if modes[i]==2:
                    modes[i] = 9
                if modes[i]==0:
                    modes[i] = 1

        if auto_input is not None:
            return self.operations[op_code](*args, modes, val_to_use=auto_input)
        else:
            return self.operations[op_code](*args, modes)

    def parse_args(self, prefix, arg_list, status):
        tape = status.memory
        rel_base = status.relative_base

        assert len(arg_list)==len(prefix)

        new_list = []
        for i in range(len(prefix)):
            if prefix[i]==0:
                if arg_list[i] >= len(status.memory):
                    status.expand_memory(arg_list[i])
                next_arg = tape[arg_list[i]]
            if prefix[i]==1:
                next_arg = arg_list[i]
            if prefix[i]==2:
                if arg_list[i] + rel_base >= len(status.memory):
                    status.expand_memory(arg_list[i] + rel_base)
                next_arg = tape[arg_list[i] + rel_base]
            if prefix[i]==9:  #CAREFUL...
                next_arg = arg_list[i] + rel_base
            
            # next_arg = modes[i] * arg_list[i]
            # if arg_list[i] >= 0 and arg_list[i] < len(tape):
            #     next_arg += (1-modes[i]) * tape[arg_list[i]]

            new_list.append(next_arg)
        return new_list

    def IC_add(self, state, A, B, regO, prefix):
        A, B, regO = self.parse_args(prefix, [A,B,regO], state)
        if regO >= len(state.memory):
            state.expand_memory(regO)
        state.memory[regO] = A + B
        return None
    
    def IC_mult(self, state, A, B, regO, prefix):
        A, B, regO = self.parse_args(prefix, [A,B,regO], state)
        if regO >= len(state.memory):
            state.expand_memory(regO)
        state.memory[regO] = A * B
        return None
    
    def IC_input(self, state, store_reg, prefix, val_to_use=None):
        in_value = val_to_use if val_to_use is not None else int(input("\nInput?: "))
        store_reg = self.parse_args(prefix, [store_reg], state)[0]
        if store_reg >= len(state.memory):
            state.expand_memory(store_reg)
        state.memory[store_reg] = in_value
        return None

    def IC_output(self, state, regO, prefix):
        out_value = self.parse_args(prefix, [regO], state)[0]
        state.outputs.append(out_value)
        if state.chatty:
            print("Output: {}".format(out_value))
        if state.pause_on_output:
            state.running = False
        return None
    
    def IC_jump_if_true(self, state, compare, jmp_pnt, prefix):
        C, J = self.parse_args(prefix, [compare, jmp_pnt], state)
        if not(C==0):
            return J
        return None
    
    def IC_jump_if_false(self, state, compare, jmp_pnt, prefix):
        C, J = self.parse_args(prefix, [compare, jmp_pnt], state)
        if C==0:
            return J
        return None

    def IC_less_than(self, state, A, B, regO, prefix):
        A, B, regO = self.parse_args(prefix, [A,B,regO], state)
        if regO >= len(state.memory):
            state.expand_memory(regO)
        state.memory[regO] = 1 * (A < B)
        return None

    def IC_equals(self, state, A, B, regO, prefix):
        A, B, regO = self.parse_args(prefix, [A,B,regO], state)
        if regO >= len(state.memory):
            state.expand_memory(regO)
        state.memory[regO] = 1 * (A == B)
        return None

    def adj_rel_base(self, state, reg, prefix):
        reg = self.parse_args(prefix, [reg], state)
        state.relative_base += reg[0]
        return None
    
    def halt(self, state, prefix):
        state.running = False
        state.halted = True
        # print(state.memory)
        return None
    