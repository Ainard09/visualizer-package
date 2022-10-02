class Visualization:
    
    def __init__(self):
        """ Visualiztion class for visualizing from a data set
        
        Attribute:
        data_list (list of floats): a list of floats extracted from the data file
        """
        self.data = []
        
    def read_data_file(self, file_name):
        """ Function to read in data from a txt file. The txt file should have
        one number (float) per line. The numbers are stored in the data attribute.

        Args:
            file_name (string): name of a file to read from

        Returns:
            None
        """

        with open(file_name) as file:
            data_list = []
            line = file.readline()
            while line:
                data_list.append(int(line))
                line = file.readline()

        self.data = data_list