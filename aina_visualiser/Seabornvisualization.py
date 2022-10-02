import seaborn as sns
from Generalvisualization import Visualization

class Seaborn(Visualization):
    """ Seaborn class for visualizing dataset
    
    Attributes:
              data(float/int): dataset stored in a variable
    """
    def __init__(self, data):
        Visualization.__init__(self)
        self.data = data
        
    def plot_jointplot(self, col1, col2):
        """ Function to output the jointplot of two columns of an instance variable using seaborn.
        
        Args:
            column_name1(int/float): first column we are interested in visualizing
            column_name2(int/float): Second column we are interested to plot
            
        Returns:
                None
        """
                
        # A seaborn jointplot shows bivariate scatterplots and univariate histograms in the same figure
        sns.jointplot(x=col1, y=col2, data=self.data, size=5, kind='hex')
        
    
    def plot_boxplot(self, col1, col2):
        """ Function to output the boxplt of two columns of an instance variable using seaborn
        
        Args:
            column_name1(int/float): first column we are interested in visualizing
            column_name2(int/float): Second column we are interested to plot
            
        Returns:
                None
        """
        
        sns.boxplot(x=col1, y=col2, data=self.data)
        
    def plot_heatmap(self):
        """ Function to output the heatmap correlation of an instance variable using seaborn.
        
        Args:
             Nonw
        Returns:
                None
        """
        # show correlation amongs the data
        sns.heatmap((self.data).corr(), annot=True)
        
        
            
        
        
        
        
    
