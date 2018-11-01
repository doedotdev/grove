class Table:
    
    DIMENSIONS_ERROR = 'DIMENSIONS DO NOT MATCH'
        
    def __init__(self):
        # data
        self.headers = []
        self.data = []
        self.has_data = False
        self.has_headers = False

        # formatting
        self.cell_spacing = []
        self.index = False
        self.padding_left = 0
        self.padding_right = 0

        # stats
        self.total_rows = 0

    def set_cell_spacing(self, row):
        if self.cell_spacing == [] or len(row) == len(self.cell_spacing):
            self.cell_spacing = [None] * len(row)
            return True
        elif len(row) != len(self.cell_spacing):
            print(self.DIMENSIONS_ERROR + ': [' + row[0] + ']...')
            return False
            
    def set_data(self, new_data):
        self.has_data = True
        if isinstance(new_data,list) and isinstance(new_data[0], list) and self.set_cell_spacing(new_data[0]):
            for row in new_data:
                self.append_data(row)

    def check_spacing(self, row):
        for idx, item in enumerate(row):
            item_size = len(item)
            if self.cell_spacing[idx] is None:
                self.cell_spacing[idx] = item_size
            elif len(item) > self.cell_spacing[idx]:
                self.cell_spacing[idx] = item_size

    def set_headers(self, headers):
        if isinstance(headers, list) and self.set_cell_spacing(headers):
            self.check_spacing(headers)
            self.headers = headers
            self.has_headers = True

    def cast_items_to_string(self, row):
        return [str(i) for i in row]
        
    def append_data(self, new_row):
        if isinstance(new_row, list):
            if len(new_row) == len(self.cell_spacing):
                new_row = self.cast_items_to_string(new_row)
                self.data.append(new_row)
                self.total_rows += 1
                self.check_spacing(new_row)

            elif len(new_row) < len(self.cell_spacing):
                for i in range(len(self.cell_spacing) - len(new_row)):
                    new_row.append('None')
                self.append_data(new_row)
            else:
                self.append_data(new_row[:len(self.cell_spacing)])
        else:
            print(self.DIMENSIONS_ERROR + ': [' + new_row[0] + ']...')


    def set_padding(self, left, right):
        self.padding_left = left
        self.padding_right = right

    def print_formatter_line(self):
        for spacing in self.cell_spacing:
            print('=' * (spacing + 3 + self.padding_left + self.padding_right), end="", flush=True)
        print()

    def print_headers(self):
        for idx, header in enumerate(self.headers):
            spacing_diff = self.cell_spacing[idx] - len(header)
            padd = ' ' * spacing_diff
            left = ' ' * self.padding_left
            right = ' ' * self.padding_right
            print('| ' + left + header + padd + right + ' ', end="", flush=True)
        print()

    def print_data(self):
        for row in self.data:
            for idx, item in enumerate(row):
                spacing_diff = self.cell_spacing[idx] - len(item)
                padd = ' ' * spacing_diff
                left = ' ' * self.padding_left
                right = ' ' * self.padding_right
                print('| ' + left + item + padd + right + ' ', end="", flush=True)
            print()

    def print_table(self):
        if self.has_headers:
            self.print_formatter_line()
            self.print_headers()
        if self.has_data:
            self.print_formatter_line()
            self.print_data()
            self.print_formatter_line()

    def print_stats(self):
        print('Columns: ' + str(len(self.cell_spacing)))
        print('Rows: ' + str(self.total_rows))


# table = Table()
# table.set_data([[1, 4345678, 5],[-5, 8, 9]])
# table.append_data([112345678,4,6])
# table.append_data([123, 2345])
# table.append_data([])
# table.append_data([1])
# table.append_data([1,2,3,4,5,6,7,78])
# table.append_data(1)
# table.append_data('hello')
# table.append_data(['hi', 'bye', 'egwegwergwegwerg'])
# table.set_headers(['my', 'table', 'headers'])
# # # table.set_padding(3)
# table.print_table()
# table.print_stats()
# # # table.transpose_data()

# tableNoData = Table()
# tableNoData.print_table()
# tableNoData.print_stats()

# tableJustData = Table()
# tableJustData.set_data([[1,2,3,4,5],[6,7,8,9,0]])
# tableJustData.print_table()
# tableJustData.print_stats()


# tableJustHeader = Table()
# tableJustHeader.set_headers(['one','two','three'])
# tableJustHeader.print_table()
# tableJustHeader.print_stats()


# tableSetBoth = Table()
# tableSetBoth.set_data([[1,2,3],[3,2,1],[4,6,'hello']])
# tableSetBoth.set_headers(['one','two','threewertyui'])
# tableSetBoth.set_headers(['hello'])
# tableSetBoth.set_padding(6,4)
# tableSetBoth.print_table()
# tableSetBoth.print_stats()
