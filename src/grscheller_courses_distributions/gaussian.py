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

"""Module for the Gaussian class - derived from Udacity exercise template."""

from __future__ import annotations

from typing import List, Tuple
from math import exp, pi, sqrt
import matplotlib.pyplot as plt
from .distribution import Distribution

__all__ = ['Gaussian']

class Gaussian(Distribution):
    """ Class for visualizing data as Gaussian distributions.

    The Gaussian, also called Normal, distribution is a continuous probability
    distribution with probability density function
    ```
       f(x) = (1/√(2πσ²))exp(-(x-μ)²/2σ²)
    ```
    where

    * μ = mu = mean value of the distribution
    * σ = sigma = standard deviation of the distribution

    """
    def __init__(self, mu: float=0.0, sigma: float=1.0):
        if sigma <= 0:
            msg = 'For a Gaussian distribution, sigma must be greater than 0'
            raise ValueError(msg)
        super().__init__(mu, sigma)

    def calculate_mean(self) -> float:
        """Calculate the mean from the data set"""
        return self.calculate_data_mean()

    def calculate_stdev(self, sample: bool = True) -> float:
        """Calculate the stdev from the data set"""
        return self.calculate_data_stdev(sample)

    def read_data_file(self, file_name: str, sample: bool=True) -> None:
        super().read_data_file(file_name, sample)
        self.mu = self.mean
        self.sigma = self.stdev

    def plot_histogram(self) -> None:
        """Produce a histogram of the data using the matplotlib pyplot library."""

        fig, axis = plt.subplots()
        axis.hist(self.data)
        axis.set_title('Histogram of Data')
        axis.set_ylabel('Data')
        axis.set_ylabel('Count')
        plt.show()

    def pdf(self, x: float) -> float:
        """Gaussian probability density function for this Gaussian object."""
        c = 1.0/sqrt(2*pi)

        mu = self.mean
        sigma = self.stdev

        return (c/sigma)*exp(-0.5*((x - mu)/sigma)**2)

    def plot_histogram_pdf(self, n_spaces: int = 50) -> Tuple[List[float], List[float]]:
        """Method to plot the normalized histogram of the data and a plot of the
        probability density function along the same range

        Args:
            n_spaces (int): number of data points

        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot

        """

        min_xs = min(self.data)
        max_xs = max(self.data)

        # calculates the interval between x values
        interval = 1.0 * (max_xs - min_xs) / n_spaces

        xs: List[float] = []
        ys: List[float] = []

        # calculate the x values to visualize
        for i in range(n_spaces):
            x = min_xs + interval*i
            xs.append(x)
            ys.append(self.pdf(x))

        # make the plots
        fig, axes = plt.subplots(2,sharex=True)
        fig.subplots_adjust(hspace=.5)
        axes[0].hist(self.data, density=True)
        axes[0].set_title('Normed Histogram of Data')
        axes[0].set_ylabel('Density')

        axes[1].plot(xs, ys)
        axes[1].set_title('Normal Distribution for \n Sample Mean and Sample Standard Deviation')
        axes[0].set_ylabel('Density')
        plt.show()

        return xs, ys

    def __add__(self, other: Gaussian) -> Gaussian:
        """D method to add together two Gaussian distributions

        Args:
            other (Gaussian): Gaussian instance

        Returns:
            Gaussian: Gaussian distribution

        """
        return Gaussian(self.mean + other.mean, sqrt(self.stdev**2 + other.stdev**2))

    def __repr__(self) -> str:
        """Magic method to output the characteristics of the Gaussian instance

        Args:
            None

        Returns:
            string: characteristics of the Gaussian

        """
        repr_str = "mean {}, standard deviation {}"
        return repr_str.format(self.mean, self.stdev)
