# import src.modraizesquadraticas.raizesquadraticas as raizesquadraticas
import src.bhaskara.eq_bhaskara as eq_bhaskara

print("estou no arquivo que testa bhaskara")
r1, r2 = eq_bhaskara.raizes(1, 5, -6)

assert (1*r1**2 + 5*r1 + -6) == 0
assert (1*r2**2 + 5*r2 + -6) == 0

# Good Integration Practices
# https://docs.pytest.org/en/latest/explanation/goodpractices.html#goodpractices
