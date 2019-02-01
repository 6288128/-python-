import equation_func

#x = equation_func.LinearTerm(' -6x')
#y = equation_func.LinearTerm('7x ')
#z = sum(x, y)
#print(z)

eq = equation_func.Equation('62+98-x=96+3x')
eq.shift_term()
eq.merge_of_similar_terms()
eq.coefficient_into_one()
print(eq.equation_left,eq.equation_right)