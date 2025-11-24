import sys
import copy
import numpy as np

class Matrix:
    data : list[list]
    shape : tuple

    def ft_create_zero_matrix(self, data):
        values = data[0]
        rows = values[0]
        columns = values[1] - 1
        print(rows, columns)
        for i in range(rows):
            to_add = [0]
            for j in range(columns):
                to_add.append(0)
            self.data.append(to_add)  

    def ft_create_matrix(self, data):
        self.data = copy.copy(data[0])

    def ft_check_rows_of_data(self, data):
        for row in data:
            if not isinstance(row, list) :
                print('Error: Verify your lists')
                sys.exit(1)
            for lst in row:
                if not isinstance(lst, list) :
                    print('Error: Verify your lists of lists')
                    sys.exit(1)
                for value in lst:
                    if not isinstance(value, int) and not isinstance(value, float):
                        print('Error: Verify your lists of lists')
                        sys.exit(1)

    def ft_take_a_choice(self, data):
        choice = ''
        if len(data) > 1:
            print("One argument is authorized in the Matrix class")
            sys.exit(1)

        if isinstance(data[0], tuple):
            for value in data[0]:
                if not isinstance(value, int):
                    return choice
            choice = '1'
            return choice
    
        self.ft_check_rows_of_data(data)
        if choice != '1':
            choice = '2'
        return choice

    def ft_define_shape_of_data(self):
        rows = len(self.data)
        max_columns = len(self.data[0])
        for row in self.data:
            columns = 0
            for value in row:
                columns += 1
            if columns > max_columns:
                print(f"Columns: {columns}, max: {max_columns}")
                print("The lists don't have the same dimensions.")
                sys.exit(1)
        self.shape = (rows, max_columns)

    def __init__(self, *data):
        self.data = []
        choice = self.ft_take_a_choice(data)
        if choice == '1':
            self.ft_create_zero_matrix(data)
        elif choice == '2':
            self.ft_create_matrix(data)
        elif choice == 'columns':
            print('Rows don\'t have the same number of columns')
            sys.exit(1)
        else:
            print('Error')
            sys.exit(1)
        self.ft_define_shape_of_data()

    def __str__(self):
        return "[" + "\n ".join(str(row) for row in self.data) + "]"

    def __add__(self, other):
        
        if not isinstance(other, list[list]):
            raise ValueError('List[] type')


        result = self.data + other

        # for i in 



        return result
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self):
        [...]

    def __rsub__(self):
        [...]

    def __truediv__(self):
        [...]

    def __rtruediv__(self):
        [...]

    def __mul__(self):
        [...]

    def __rmul__(self):
        [...]

    def __repr__(self):
        [...]

    def T(self):
        [...]

    # def shape(self):
    #     return f"{self.shape}"

def main():
    print('-----------Case shape-----------')
    case1 = (5, 3)
    m1_alpha = Matrix(case1)
    m1 = np.zeros(case1)

    print(f"Custom function: \n{m1_alpha}, shape {m1_alpha.shape}")
    print(f"Original function: \n{m1}, shape {m1.shape}")
    print('-----------Case lists -----------')
    case2 = [[1, 2, 4], [4, 3, 1]]
    m2_alpha = Matrix(case2)
    m2 = np.array(case2, np.float32)
    print(f"Custom function: \n {m2_alpha}")
    print(f"Original function: \n {m2}")

    print('-----------Case 3 -----------')
    case3 = [[1, 2, 4], [4, 3, 1]]
    m3_alpha = Matrix(case3)
    m3 = np.array(case3, np.float32)
    print(f"Custom function: \n {m3_alpha}")
    print(f"Original function: \n {m3}")

    
    m4 = m2 + m3

    print(f"Result sum m2 and m3:c sum \n{m4}")

    m4_alpha =  m2_alpha + m3_alpha
    print(f"Result custom sum m2 and m3: \n{m4_alpha}")

if __name__ == "__main__":
    main()