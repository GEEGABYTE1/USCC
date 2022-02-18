class USCC:
    def __init__(self, name):
        self.name = name
        self.number_registers = [0 for i in range(21)]
        self.history_registers = [0 for i in range(10)]
        self.number_index = 1
        self.history_index = 0 
        self.temp_history_index = 0
        self.user_display = ''

    def update_display(self, to_update):
        self.user_display = to_update
        print(self.user_display)
        print("Welcome to USCC {}!".format(self.name))
        print('-'*24)
        print('\n')

    def store_value_to_register(self, value_to_store):
        if self.number_index >= 21:
            self.number_index = 1
        
        value = self.bin_to_int(value_to_store)
        self.number_registers[self.number_index] = value
        print("{value} was added to {number_add}".format(value=value, number_add=self.number_index))
        self.number_index += 1

    def bin_to_int(self, binary):
        binary = str(binary)
        binary_split = []
        for num in range(len(binary) - 1, -1, -1):
            binary_split.append(binary[num])
        max_exponent = len(binary_split)
        
        exponents = []
        for exponent in range(max_exponent - 1, -1, -1):
            if binary_split[exponent] == '1':
                exponents.append(exponent)
            else:
                continue
        
        result = 0 
        for exponent in exponents:
            result += 2 ** int(exponent)
        
        return result








string_name = str(input('What would you like to name your calculator?: '))
string_name = string_name.split(" ")[0]
test = USCC(string_name)
print(test.bin_to_int('100110001'))
