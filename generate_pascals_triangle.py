class Solution(object):
    def generate(self, num_rows):
        triangle = [[1]]  # First row is always [1]

        for current_row in range(num_rows - 1):
            previous_row = triangle[current_row]
            new_row = []

            left_pointer = 0
            right_pointer = -1
            row_length = len(previous_row) + 1

            for index in range(row_length):
                if index == 0 or index == row_length - 1:
                    new_row.append(1)
                    left_pointer += 1
                    right_pointer += 1
                else:
                    value = previous_row[left_pointer] + previous_row[right_pointer]
                    new_row.append(value)
                    left_pointer += 1
                    right_pointer += 1

            triangle.append(new_row)

        return triangle
