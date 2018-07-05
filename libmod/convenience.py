import tkinter as tk
import tkinter.filedialog
import pandas as pd

class Input:
    path2files=[]
    def path_gui(self):
        """Run Tk window to choose files        
        """
        tk_root=tk.Tk()
        tk_root.title("File select window")
        def sel_files_callback(event):
            self.path2files=list(tk.filedialog.askopenfilenames())
            tk_root.destroy()
        def sel_dir_callback(event):
            self.path2files=glob.glob(tk.filedialog.askdirectory()+"/*")
            tk_root.destroy()
        sel_dir_btn=tk.Button(tk_root,text="Select directory")
        sel_files_btn=tk.Button(tk_root,text="Select files")
        sel_files_btn.bind("<ButtonPress-1>",sel_files_callback)
        sel_dir_btn.bind("<ButtonPress-1>",sel_dir_callback)
        sel_files_btn.place(x=50,y=10,width=100)
        sel_dir_btn.place(x=50,y=40,width=100)
        tk_root.mainloop()
        return self.path2files
    
    def universal_load(self,path,enc="utf-8"):
        """Load dataframe by file extension
        """
        if path.endswith("csv"):
            df=pd.read_csv(path,encoding=enc)
        elif path.endswith("xlsx") or path.endswith("xls"):
            df=pd.read_excel(path,encoding=enc)
        elif path.endswith("txt"):
            df=pd.read_table(path,encoding=enc)
        return df