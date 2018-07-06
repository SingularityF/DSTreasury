from IPython.display import Javascript

# Run jupyter cells
def exec_below(n):
    display(Javascript("Jupyter.notebook.execute_cell_range(Jupyter.notebook.get_selected_index()+1,Jupyter.notebook.get_selected_index()+1+{})".format(n)))