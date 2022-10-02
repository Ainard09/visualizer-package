import numpy as np
import matplotlib.pyplot as plt
from Generalvisualization import Visualization


class Matplotlib(Visualization):
    """ Matplotlib class for visualizing dataset 

    Attributes:
               data(float/int): list of data stored in a variable
    """

    def __init__(self, data):
        Visualization.__init__(self)
        self.data = data

    def plot_histogram(self):
        """Function to output a histogram of the instance variable data using matplotlib pyplot library.

        Args:
                None

        Returns:
                None
        """

        plt.hist(self.data)
        plt.title('Histogram of Data')
        plt.xlabel('dataset')
        plt.ylabel('count')
        plt.show()

    def plot_boxplot(self):
        """ Function to output a boxplot of the instance variable data using matplotlib pylot library.

        Args:
               None

        Returns: 
                 None                 
        """

        plt.figure()
        plt.boxplot(self.data, whis='range')
        plt.xlabel('Dataset number')
        plt.ylabel('count')
        plt.title('Boxplot of Data')
        plt.show()

    def plot_linear(self):
        """Function to output the linear of the instance variable data using matplotlib pyplot library

        Args:
               None

        Returns:
                 None 
        """
        linear_data = np.array(self.data)
        exponential_data = linear_data**2

        plt.figure()
        # plot the linear data and the exponential data
        plt.plot(linear_data, '-o', exponential_data, '-*')
