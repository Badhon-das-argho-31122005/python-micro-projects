class Matrix:
    def __init__(self, data):
        if not all(isinstance(row, list) for row in data):
            raise ValueError("2D supported only")
        row_length = len(data[0])
        if not all(len(row) == row_length for row in data):
            raise ValueError("Row length must be same")
        self.data = data
        self.rows = len(data)
        self.cols = row_length
    @property
    def shape(self):
        return (self.rows, self.cols)
    def __repr__(self):
        result = "Matrix:(\n"
        for row in self.data:
            result += f"--{row}\n"
        result += ")"
        return result
    def __add__(self, other):
        if self.shape != other.shape:
            raise ValueError("Shape must be same.....")
        new_data = []
        for i in range(self.rows):
            new_row = []
            for j in range(self.cols):
                add = self.data[i][j] + other.data[i][j]
                new_row.append(add)
            new_data.append(new_row)
        return Matrix(new_data)
    def __sub__(self, other):
        if self.shape != other.shape:
            raise ValueError(f"{self.shape} and {other.shape} cannot be added")
        new_data = []
        for i in range(self.rows):
            new_row = []
            for j in range(self.cols):
                sub = self.data[i][j] - other.data[i][j]
                new_row.append(sub)
            new_data.append(new_row)
        return Matrix(new_data)
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            new_data = []
            for i in range(self.rows):
                new_row =[]
                for j in range(self.cols):
                    mul = self.data[i][j] * other 
                    new_row.append(mul)
                new_data.append(new_row)
            return Matrix(new_data)
        elif isinstance(other, Matrix):
            if self.shape != other.shape:
                raise ValueError("shape must be same")  
            new_data =[]
            for i in range(self.rows):
                new_row =[]
                for j in range(self.cols):
                    mul = self.data[i][j] * other.data[i][j] 
                    new_row.append(mul)
                new_data.append(new_row)
            return Matrix(new_data)
        else:
            raise TypeError("unsupported operand for *")
    def __matmul__(self, other):
        if not (isinstance(other, Matrix)):
            raise ValueError("Matrix required")
        if self.cols != other.rows:
            raise ValueError("colums and row should must same")
        new_data =[]
        for i in range(self.rows):
            new_row = []
            for j in range(other.cols):
                mat = 0
                for k in range(self.cols):
                    mat = mat + (self.data[i][k] * other.data[k][j])
                new_row.append(mat)
            new_data.append(new_row)
        return Matrix(new_data)
def take_matrix_input(name):
    print("\n----Input-----")
    rows = int(input("How many rows: "))
    cols = int(input("How many columns: "))
    data = []
    for i in range(rows):
        row_input = input(f"Give {cols} numbers for {i+1} (use space / 1 2 3): ")
        row_list = []
        for x in row_input.split():
            number = float(x)
            row_list.append(number)
        data.append(row_list)
    return Matrix(data)

if __name__ == "__main__":
    print("__________custom matrix calculator________________")
    while True:
        print("\nwhat you want?")
        print("1. matrix + (Addition)")
        print("2. matrix - (Subtraction)")
        print("3. scaler multiplication * ")
        print("4. Matrix multiplication (Dot Product)")
        print("5.  (Exit)")   
        choice = input("\n Your choice(1-5): ")
        if choice == "5":
            print("Good bye")
            break     
        try:
            if choice in ['1', '2', '4']:
                m1 = take_matrix_input("Your first matrix")
                m2 = take_matrix_input("Your second matrix")
                if choice == "1":
                    print("\n (m1+m2)")
                    print(m1+m2)
                elif choice == "2":
                    print("\n (m1 - m2)")
                    print(m1-m2)
                elif choice == "4":
                    print("\n (m1@m2)")
                    print(m1@m2)
            elif choice == "3":
                m1 = take_matrix_input("Your matrix: ")
                num = float(input("Please give your number for multiplication: "))
                print("\n-------(m1*num)")
                print(m1*num)
            else:
                print("something went wrong")
        except ValueError as e:
            print(f"\n [ERROR] = {e}")
            print("please give the right value")
        except Exception as e:
            print(f"[ERROR] Another type of error: {e}")
