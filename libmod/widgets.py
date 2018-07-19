import ipywidgets as widgets

class Widgets:
    """A static class to create widgets
    
    Methods:
        options: Create a dropdown list with options
    """
    def options(opts,callback=lambda x:print(x),label="Select"):
        """Create dropdown lists
        
        Parameters:
            opts: A list of options, should be unique
            callback: A callback function that takes options as parameter
            label: The label to prompt users what to choose
        """
        label_widget=widgets.Label(value=label)
        dropdown_widget=widgets.Dropdown(
        options=["",*opts],
        value="",
        disabled=False,
        )
        def on_change(change):
            if change['type'] == 'change' and change['name'] == 'value':
                callback(change['new'])
        dropdown_widget.observe(on_change)
        return widgets.VBox([label_widget, dropdown_widget])
