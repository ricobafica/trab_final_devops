import src.bhaskara.eq_bhaskara as eq_bhaskara


def test_rais1():
    print("estou no arquivo que testa bhaskara")
    r1, r2 = eq_bhaskara.raizes(1, 5, -6)
    assert (1*r1**2 + 5*r1 + -6) == 0


def test_raiz2():
    print("estou no arquivo que testa bhaskara")
    r1, r2 = eq_bhaskara.raizes(1, 5, -6)
    # return (1*r2**2 + 5*r2 + -6)
    assert (1*r2**2 + 5*r2 + -6) == 0

# Why PyTest is not collecting tests (collected 0 items)?
# https://stackoverflow.com/questions/37353960/why-pytest-is-not-collecting-tests-collected-0-items

# Good Integration Practices
# https://docs.pytest.org/en/latest/explanation/goodpractices.html#goodpractices
