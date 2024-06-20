# Using pytest for testing
#
# WARNING: Plotting tests depend on user input!!!
#          This is considered bad practice except for
#          single user/maintainer projects.
# 
#          - pytest must be run with the -s option
#          - test data hard coded, run tests from project root
#
# Example: $ pytest -s tests/plot_test.py
#

from grscheller_courses_distributions.gaussian import Gaussian
from grscheller_courses_distributions.binomial import Binomial

gauss = Gaussian(25, 2)
bernoulli = Binomial(0.4, 20)

def plot_viewable(plot_name: str) -> bool:
    print(f'\nDid the {plot_name} plot display correctly? ([y] or n) ', end='')
    ans = input()
    return True if ans != 'n' else False

class Test_Gaussian:

    def test_plot_histogram(self) -> None:
        gauss.plot_histogram()
        if plot_viewable('histogram'):
            assert True
        else:
            assert False

    def test_plot_histogram_pdf(self) -> None:
        gauss.plot_histogram_pdf()
        if plot_viewable('histogram_pdf'):
            assert True
        else:
            assert False

class Test_Binomial:

    def test_plot_histogram(self) -> None:
        gauss.plot_histogram()
        if plot_viewable('histogram'):
            assert True
        else:
            assert False

    def test_plot_histogram_pdf(self) -> None:
        gauss.plot_histogram_pdf()
        if plot_viewable('histogram_pdf'):
            assert True
        else:
            assert False
