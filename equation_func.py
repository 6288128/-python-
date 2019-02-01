class LinearTerm():
    def __init__(self, term):
        self.term = term.strip()

        if self.term[:-1] == '+' or self.term[:-1] == '':
            self.coefficient = 1.0
        elif self.term[:-1] == '-':
            self.coefficient = -1.0
        else:
            self.coefficient = float(self.term[:-1])
        
        self.__class__ = LinearTerm

    def __add__(self, other):
        if other.__class__ == LinearTerm:
            coefficient = self.coefficient + other.coefficient
            if coefficient == 1.0:
                term = self.term[-1]
            elif coefficient == 0.0:
                term = 0
                return int(term)
            elif coefficient == -1.0:
                term = '-' + self.term[-1]
            else:
                term = str(coefficient) + self.term[-1]
            return LinearTerm(term)

    def __sub__(self, other):
        if other.__class__ == LinearTerm:
            coefficient = self.coefficient - other.coefficient
            if coefficient == 1.0:
                term = self.term[-1]
            elif coefficient == -1.0:
                term = '-' + self.term[-1]
            else:
                term = str(coefficient) - self.term[-1]
            return LinearTerm(term)
    
    def __mul__(self, other):
        if other.__class__ == int or other.__class__ == float:
            term = str(self.coefficient * other) + self.term[-1]
            return LinearTerm(term)

    def __truediv__(self, other):
        if other.__class__ == int or other.__class__ == float:
            term = str(self.coefficient / other) + self.term[-1]
            return LinearTerm(term)
    
    def __repr__(self):
        return self.term


class Equation():

    def get_term(self, eq):     #把多项式分成多个单项式，返回list

        term_list =[]
        value_list = []
        sub, add = False, False
        while True:
            if add:
                add = eq.find('+', int(add+1))
            else:
                add = eq.find('+')
            if eq.find('+', int(add)) == -1:
                break
            else:
                value_list.append(add)

        while True:
            if sub:
                sub = eq.find('-', int(sub+1))
            else:
                sub = eq.find('-')
            if eq.find('-', int(sub)) == -1:
                break
            else:
                value_list.append(sub)

        value_list.sort()
        count = 0
        while True:
            if count == 0:
                term_list.append(eq[ : value_list[0]])
            elif count < len(value_list):
                term_list.append(eq[value_list[count-1] : value_list[count]])
            else:
                term_list.append(eq[value_list[-1] : ])
                break
            count += 1
        
        return term_list

    def __init__(self, equation):
        self.equation = equation
        self.equation_left = self.get_term(self.equation.split('=')[0])
        self.equation_right = self.get_term(self.equation.split('=')[1])
                    

    def remove_parenthesis(self):
        pass

    def shift_term(self):   #将未知数移到左，常数移到右
        count = 0
        new_equation_left = []
        new_equation_right = []
        for term in self.equation_left:
            if term.find('x') != -1:
                self.equation_left[count] = LinearTerm(term)
                new_equation_left.append(LinearTerm(term))
            else:
                self.equation_left[count] = float(term)
                new_equation_right.append(float(term) * -1)
            count+=1

        count = 0
        for term in self.equation_right:
            if term.find('x') != -1:
                self.equation_right[count] = LinearTerm(term)
                self.equation_left.append(self.equation_right[count] * -1)
                new_equation_left.append(LinearTerm(term) * -1)
            else:
                self.equation_right[count] = float(term)
                new_equation_right.append(float(term))
            count+=1
        self.equation_left = new_equation_left
        self.equation_right = new_equation_right
    
    def merge_of_similar_terms(self):
        end_term = LinearTerm('-x')
        for term in self.equation_left:
            end_term += term
        self.equation_left = end_term + LinearTerm('x')
        self.equation_right = sum(self.equation_right)

    def coefficient_into_one(self):
        coefficien = self.equation_left.coefficient
        self.equation_left /= coefficien
        self.equation_right /= coefficien


def get_solution(equation):
    eq = Equation(equation)
    eq.shift_term()
    eq.merge_of_similar_terms()
    eq.coefficient_into_one()
    return 'x=' + str(eq.equation_right)