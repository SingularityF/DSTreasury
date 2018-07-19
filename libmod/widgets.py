import ipywidgets as widgets
from .notebook import *
from .frames import *

class Widgets:
    """A static class to create widgets
    
    Methods:
        options: Create a dropdown list with options
        show_df_ui: Display a UI for viewing dataframes in Jupyter notebook
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
    
    def show_df_ui(df,transpose=False,default="Hide"):
        """Display a UI for viewing dataframes in Jupyter notebook
        Parameters:
            df: Input dataframe
            transpose: Transpose dataframe before output
            default: Default behavior when executing cell, takes value ["Head","Tail","Random","Full","Hide"]
        """
        def make_btn(val):
            btn_widget=widgets.Button(
                value=False,
                description=val,
                disabled=False,
                button_style='',
                layout=widgets.Layout(width="80px"),
            )
            return btn_widget
        
        def show_head():
            if not transpose:
                display(df.head(10))
            else:
                display(df.head(10).transpose())
        def show_tail():
            if not transpose:
                display(df.tail(10))
            else:
                display(df.tail(10).transpose())
        def show_full():
            if not transpose:
                display(df)
            else:
                display(df.transpose())
        def show_random():
            if not transpose:
                display(Frames.smart_sample(df,10))
            else:
                display(Frames.smart_sample(df,10).transpose())
        def hide_output():
            pass
        
        def refresh():
            Notebook.clear()
            Widgets.show_df_ui(df,transpose=transpose)
            
        def show_head_refresh(b):
            refresh()
            show_head()
        def show_tail_refresh(b):
            refresh()
            show_tail()
        def show_full_refresh(b):
            refresh()
            show_full()
        def show_random_refresh(b):
            refresh()
            show_random()
        def hide_output_refresh(b):
            refresh()
        
        behaviors={
            "Hide": hide_output,
            "Head": show_head,
            "Tail": show_tail,
            "Random": show_random,
            "Full": show_full
        }
        
        btn_head=make_btn("Head")
        btn_random=make_btn("Random")
        btn_tail=make_btn("Tail")
        btn_full=make_btn("Full")
        btn_hide=make_btn("Hide")
        
        btn_head.on_click(show_head_refresh)
        btn_tail.on_click(show_tail_refresh)
        btn_full.on_click(show_full_refresh)
        btn_random.on_click(show_random_refresh)
        btn_hide.on_click(hide_output_refresh)
        
        ui_group=widgets.HBox([
        widgets.Label(value="Show dataframe: "),
        btn_head,
        btn_random,
        btn_tail,
        btn_full,
        btn_hide,
        ])
        display(ui_group)
        if default in behaviors:
            behaviors[default]()