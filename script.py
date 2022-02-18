class USCC:
    def __init__(self, name):
        self.name = name
        self.number_registers = [0 for i in range(21)]
        self.history_registers = [0 for i in range(10)]
        self.number_index = 1
        self.history_index = 0 
        self.temp_history_index = 0
        self.user_display = ''

    
test = USCC
print(test('my_face'))