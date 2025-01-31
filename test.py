from kiwisolver import Constraint
from scipy import optimize, integrate
import numpy as np

def func(x: np.array):
    return -x.T @ x


x0 = np.array([1, -1])
constraints = []
constraint1 = optimize.LinearConstraint(np.ones(2), 0, 0)
constraint2 = optimize.NonlinearConstraint(lambda x: np.array([1,2]).T @ x, -2, 4)
constraints.extend([constraint1, constraint2])
optimize_result = optimize.minimize(lambda x: x[0]**2 + x[1]**2, x0, method='SLSQP', constraints=constraints)

area, error = integrate.dblquad(lambda y, x, t: t*x**2, 0, 1, lambda x: 0, lambda x: x, args=(1,))