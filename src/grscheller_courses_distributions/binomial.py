# Copyright 2024 Geoffrey R. Scheller
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# This module contains software derived from Udacity® exercises.
# Udacity® (https://www.udacity.com/)
#

"""Module for the Binomial class - derived from Udacity exercise template."""

from __future__ import annotations

from typing import List, Tuple
from math import ceil, floor, sqrt
import matplotlib.pyplot as plt
from .distribution import Distribution

__all__ = ['Binomial']

class Binomial(Distribution):
    """ Class for visualizing data as binomial distributions.

    The binomial distribution represents the number of events with probability
    p happening in n numbers of trials.

    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
        n (int) the total number of trials
    """
    def __init__(self, p: float=0.5, n: int=20):
        if not (0.0 <= p <= 1.0) or n < 1:
            msg1 = 'For a binomial distribution, '
            msg2 = msg3 = ''
            if not (0.0 <= p <= 1.0):
                msg2 = '0 <= p <= 1'
            if n < 1:
                msg3 = 'the number of trials n must be at least 1'
            if msg2 and msg3:
                msg = msg1 + msg2 + ' and ' + msg3 + '.'
            else:
                msg = msg1 + msg2 + msg3 + '.'
            raise ValueError(msg)

        self.p: float = p  #: probability of a success
        self.n: int = n    #: number of events
        super().__init__(self.calculate_mean(), self.calculate_stdev())

    def calculate_mean(self) -> float:
        """Calculate the mean from p and n"""
        n = self.n
        p = self.p
        self.mean = mean = n*p
        return mean

    def calculate_stdev(self) -> float:
        """Calculate the standard deviation using p and n"""
        n = self.n
        p = self.p
        self.stdev = stdev = sqrt(n*p*(1-p))
        return stdev

    def replace_stats_with_data(self) -> tuple[float, int]:
        """Function to calculate p and n from the data set"""
        if self.sample:
            mean = self.mean
            var = self.stdev ** 2
            n_estimate = mean*mean/(mean - var)
            n = int(n_estimate)
            if n_estimate - n > 0.5:
                n += 1
            p = 1 - var/mean
        else:
            n = len(self.data)
            p = sum(self.data)/n
            self.mean = n*p
            self.stdev = sqrt(n*p*(1-p))
        return p, n

    def plot_bar(self):
        """Function to output a histogram of the instance variable data using
        matplotlib pyplot library.

        Args:
            None

        Returns:
            None
        """

        # TODO: Use the matplotlib package to plot a bar chart of the data
        #       The x-axis should have the value zero or one
        #       The y-axis should have the count of results for each case
        #
        #       For example, say you have a coin where heads = 1 and tails = 0.
        #       If you flipped a coin 35 times, and the coin landed on
        #       heads 20 times and tails 15 times, the bar chart would have two bars:
        #       0 on the x-axis and 15 on the y-axis
        #       1 on the x-axis and 20 on the y-axis

        #       Make sure to label the chart with a title, x-axis label and y-axis label
        pass

    def pdf(self, k):
        """Probability density function calculator for the gaussian distribution.

        Args:
            k (float): point for calculating the probability density function


        Returns:
            float: probability density function output
        """

        # TODO: Calculate the probability density function for a binomial distribution
        #  For a binomial distribution with n trials and probability p,
        #  the probability density function calculates the likelihood of getting
        #   k positive outcomes.
        #
        #   For example, if you flip a coin n = 60 times, with p = .5,
        #   what's the likelihood that the coin lands on heads 40 out of 60 times?

        pass

    def plot_bar_pdf(self):

        """Function to plot the pdf of the binomial distribution

        Args:
            None

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """

        # TODO: Use a bar chart to plot the probability density function from
        # k = 0 to k = n

        #   Hint: You'll need to use the pdf() method defined above to calculate the
        #   density function for every value of k.

        #   Be sure to label the bar chart with a title, x label and y label

        #   This method should also return the x and y values used to make the chart
        #   The x and y values should be stored in separate lists

    def __add__(self, other):

        """Function to add together two Binomial distributions with equal p

        Args:
            other (Binomial): Binomial instance

        Returns:
            Binomial: Binomial distribution

        """

        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise

        # TODO: Define addition for two binomial distributions. Assume that the
        # p values of the two distributions are the same. The formula for
        # summing two binomial distributions with different p values is more complicated,
        # so you are only expected to implement the case for two distributions with equal p.

        # the try, except statement above will raise an exception if the p values are not equal

        # Hint: You need to instantiate a new binomial object with the correct n, p,
        #   mean and standard deviation values. The __add__ method should return this
        #   new binomial object.

        #   When adding two binomial distributions, the p value remains the same
        #   The new n value is the sum of the n values of the two distributions.

        pass


    def __repr__(self):

        """Function to output the characteristics of the Binomial instance

        Args:
            None

        Returns:
            string: characteristics of the Gaussian

        """

        # TODO: Define the representation method so that the output looks like
        #       mean 5, standard deviation 4.5, p .8, n 20
        #
        #       with the values replaced by whatever the actual distributions values are
        #       The method should return a string in the expected format

        pass
