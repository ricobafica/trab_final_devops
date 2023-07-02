# import src.modraizesquadraticas.raizesquadraticas as raizesquadraticas
import src.bhaskara.eq_bhaskara as eq_bhaskara


def calc(raiz):
    print("estou no arquivo que testa bhaskara")
    r1, r2 = eq_bhaskara.raizes(1, 5, -6)
    if raiz == 1:
        return (1*r1**2 + 5*r1 + -6)
    else:
        return (1*r2**2 + 5*r2 + -6)


def test_bhaskara():
    assert calc(1) == 0
    assert calc(2) == 0

#    assert (1*r2**2 + 5*r2 + -6) == 0

# Good Integration Practices
# https://docs.pytest.org/en/latest/explanation/goodpractices.html#goodpractices
