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

    def load_value_from_register(self, register_address):
        index = self.bin_to_int(register_address)
        int_value = int(self.number_registers[index])
        return int_value

    def store_to_history_register(self, result_to_store):
        if self.history_index >= 9:
            self.history_index = 0
        bin_history = self.int_to_bin(result_to_store)
        self.store_to_history_register[self.history_index] = bin_history
        self.history_index += 1
        self.temp_history_index = self.history_index

    def add(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 + num2
        return calculated_value

    def multiply(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 * num2
        return calculated_value

    def subtraction(self, address_num1, address_num2):
        num1 = self.load_value_from_register(address_num1)
        num2 = self.load_value_from_register(address_num2)
        calculated_value = num1 - num2
        return calculated_value

    def divide(self, address_num1, address_num2):
        try:
            num1 = self.load_value_from_register(address_num1)
            num2 = self.load_value_from_register(address_num2)
            calculate_value = 0 
            if num2 != 0:
                calculate_value = int(num1 / num2)
            
        except:
            print("Division by 0 error: {}/{}".format(num1/num2))
           
        return calculate_value


    def int_to_bin(self, integer):
        exponents = []
        counter = 0
        remainder = 0
        mod = 0
        while integer >= 1:
            while mod != 1:
                result_mod = integer // (2 ** counter)
                mod = result_mod
                counter += 1
            counter -= 1
            exponents.append(counter)
            integer = integer - (2 ** counter)
            counter = 0 
            mod = 0
        
        binary_num = ''
        for i in range(max(exponents), -1, -1):
            if i in exponents:
                binary_num += '1'
            else:
                binary_num += '0'
        
        return binary_num
        
        

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
print(test.int_to_bin(206))
