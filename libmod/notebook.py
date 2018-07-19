from IPython.display import Javascript,clear_output

class Notebook:
    """Static class providing interfaces to Jupyter notebook
    
    Methods:
        exec_below: Execute Jupyter notebook cells below the cell invoking this method
    """
    def exec_below(n):
        """Execute Jupyter notebook cells below the cell invoking this method
        
        Parameters:
            n: Number of cells to execute
        """
        display(Javascript("Jupyter.notebook.execute_cell_range(Jupyter.notebook.get_selected_index()+1,Jupyter.notebook.get_selected_index()+1+{})".format(n)))
        
    def clear():
        """Wrapper of Jupyter notebook clear_output()
        """
        clear_output()