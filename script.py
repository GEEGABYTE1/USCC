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





string_name = str(input('What would you like to name your calculator?: '))
string_name = string_name.split(" ")[0]
test = USCC(string_name)
print(test.update_display('hi'))
