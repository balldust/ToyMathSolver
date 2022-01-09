import math


class LinearEquationSolver:

    def __init__(self, matrix):
        self._extended_multiplier_matrix = matrix
        self._nrows = len(matrix)
        self._ncols = len(matrix[0])

    def solve_linear_system(self):
        self._perform_gaussian_elimination()
        return self._get_variable_values_by_backward_substitution()

    def _perform_gaussian_elimination(self):
        for row1 in range(self._nrows):
            for row2 in range(row1+1, self._nrows):
                self._perform_pivoting(row1)
                pivot_element = self._extended_multiplier_matrix[row1][row1]
                multiplier = self._extended_multiplier_matrix[row2][row1] / pivot_element
                for col in range(row1, self._ncols):
                    self._extended_multiplier_matrix[row2][col] = self._extended_multiplier_matrix[row2][col]\
                                                                  - multiplier \
                                                                  * self._extended_multiplier_matrix[row1][col]

    def _perform_pivoting(self, init_row):
        current_pivot_row = init_row
        current_pivot_element = self._extended_multiplier_matrix[current_pivot_row][init_row]
        for row in range(init_row, self._nrows):
            pivot_element_to_check = self._extended_multiplier_matrix[row][init_row]
            if math.fabs(pivot_element_to_check) > math.fabs(current_pivot_element):
                current_pivot_row = row
                current_pivot_element = pivot_element_to_check
            self._reassign_rows_based_on_pivoting(init_row, current_pivot_row)

    def _reassign_rows_based_on_pivoting(self, init_row, current_pivot_row):
        if current_pivot_row != init_row:
            old_pivot_row = self._extended_multiplier_matrix[init_row]
            self._extended_multiplier_matrix[init_row] = self._extended_multiplier_matrix[current_pivot_row]
            self._extended_multiplier_matrix[current_pivot_row] = old_pivot_row

    def _get_variable_values_by_backward_substitution(self):
        calculated_vars = self._nrows*[0]
        self._calculate_last_variable(calculated_vars)
        for row in range(self._nrows - 2, -1, -1):
            val_to_add = self._extended_multiplier_matrix[row][-1] / self._extended_multiplier_matrix[row][row]
            for col in range(row+1, self._ncols - 1):
                val_to_add = val_to_add - self._extended_multiplier_matrix[row][col] * calculated_vars[col]\
                             / self._extended_multiplier_matrix[row][row]
            calculated_vars[row] = val_to_add
        return calculated_vars

    def _calculate_last_variable(self, calculated_vars):
        if self._extended_multiplier_matrix[-1][-2] != 0:
            calculated_vars[-1] = self._extended_multiplier_matrix[-1][-1]\
                                  / self._extended_multiplier_matrix[-1][-2]
        else:
            calculated_vars[-1] = 0
