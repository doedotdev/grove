class Table:
        
    def __init__(self, cell_spacing, headers, index):
        self.headers = headers
        self.columns = len(headers)
        self.index = index

        self.data = None
        self.cell_spacing = []
        for idx, header in enumerate(headers):
            self.cell_spacing.append(len(header))

    
    def set_data(self, new_data):
        self.data = []
        for row in new_data:
            self.append_data(row)                   
                
        
    def append_data(self, new_data):
        if isinstance(new_data, list):
            if len(new_data) == self.columns:
                self.data.append(new_data)
                for idx, item in enumerate(new_data):
                        if len(str(item)) > self.cell_spacing[idx]:
                            self.cell_spacing[idx] = len(str(item))
            elif len(new_data) < self.columns:
                for i in range(self.columns - len(new_data)):
                    new_data.append('None')
                self.append_data(new_data)
            else:
                self.append_data(new_data[:self.columns])
        else:
            print('no')

    def transpose_data(self):
        return

    def set_padding(self, padding_value):
        for idx, cell_space in enumerate(self.cell_spacing):
            self.cell_spacing[idx] += padding_value

    def print_formatter_line(self):
        for spacing in self.cell_spacing:
            print('=' * (spacing + 3), end="", flush=True)
        print()

    def print_headers(self):
        for idx, header in enumerate(self.headers):
            spacing_diff = self.cell_spacing[idx] - len(header)
            padd = ' ' * spacing_diff
            print('| ' + header + padd + ' ', end="", flush=True)
        print()

    def print_data(self):
        for row in self.data:
            for idx, item in enumerate(row):
                spacing_diff = self.cell_spacing[idx] - len(str(item))
                padd = ' ' * spacing_diff
                print('| ' + str(item) + padd + ' ', end="", flush=True)
            print()

    def print_table(self):
        self.print_formatter_line()
        self.print_headers()
        self.print_formatter_line()
        self.print_data()
        self.print_formatter_line()                 


# table = Table(3, ['one', 'two', 'three'], False)
# table.set_data([[1, 4345678, 5],[-5, 8, 9]])
# table.append_data([112345678,4,6])
# table.append_data([123, 2345])
# table.append_data([])
# table.append_data([1])
# table.append_data([1,2,3,4,5,6,7,78])
# table.append_data(1)
# table.append_data('hello')
# table.append_data(['hi', 'bye', 'egwegwergwegwerg'])
# table.set_padding(3)
# table.print_table()
# table.transpose_data()
