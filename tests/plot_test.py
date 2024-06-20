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

class Test_Gaussian:

    def test_plot_data_read(self) -> None:
        gauss = Gaussian(100, 30)
        gauss.read_data_file('data/numbers.txt')
        gauss.plot_histogram()

    def test_plot_pdf_readonly(self) -> None:
        gauss = Gaussian(100, 30)
        gauss.read_data_file('data/numbers.txt')
        gauss.plot_histogram_pdf()

    def test_plot_pdf_readcalc(self) -> None:
        gauss = Gaussian(25, 2)
        gauss.read_data_file('data/numbers.txt')
        gauss.calculate_data_stdev(True)
        gauss.plot_histogram_pdf()

class Test_Binomial:

    def test_plot_data(self) -> None:
        bernoulli = Binomial(0.4, 20)
        bernoulli.read_data_file('data/numbers_binomial.txt')
        bernoulli.plot_histogram()

    def test_plot_pdf_readonly(self) -> None:
        bernoulli = Binomial(0.4, 20)
        bernoulli.read_data_file('data/numbers_binomial.txt')
        bernoulli.plot_histogram_pdf()

    def test_plot_pdf_readcalc(self) -> None:
        bernoulli = Binomial(0.4, 20)
        bernoulli.read_data_file('data/numbers_binomial.txt')
        bernoulli.replace_stats_with_data()
        bernoulli.plot_histogram_pdf()
