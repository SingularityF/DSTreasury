import tkinter as tk
import tkinter.filedialog
import pandas as pd
import glob
import os

class Input:
    filename=""
    path2file=""
    path2files=[]
    def path_gui(self,message=""):
        """Run Tk window to choose files        
        """
        tk_root=tk.Tk()
        tk_root.title("File selector")
        tk_root.configure(background='white')
        tk_root.attributes("-topmost", True)
        def sel_files_callback(event):
            self.path2files=list(tk.filedialog.askopenfilenames())
            try:
                self.path2file=self.path2files[0]
                self.filename=os.path.basename(self.path2file).split(".")[0]
            except:
                pass
            tk_root.destroy()
        def sel_dir_callback(event):
            self.path2files=glob.glob(tk.filedialog.askdirectory()+"/*")
            try:
                self.path2file=self.path2files[0]
                self.filename=os.path.basename(self.path2file).split(".")[0]
            except:
                pass
            tk_root.destroy()
        msg_txt=tk.Text(tk_root)
        msg_txt.insert(1.0, message)
        msg_txt.config(state=tk.DISABLED)
        msg_txt.config(wrap=tk.WORD)
        sel_dir_btn=tk.Button(tk_root,text="Select directory")
        sel_files_btn=tk.Button(tk_root,text="Select files")
        sel_files_btn.bind("<ButtonPress-1>",sel_files_callback)
        sel_dir_btn.bind("<ButtonPress-1>",sel_dir_callback)
        sel_files_btn.place(x=50,y=100,width=100)
        sel_dir_btn.place(x=50,y=130,width=100)
        msg_txt.place(x=-1,y=-1,width=200,height=80)
        tk_root.mainloop()
        return self.path2files
    
    def load_single(self,sheet_name=0,enc="utf-8"):
        """Load the first selected file and return dataframe
        """
        return self.universal_load(self.path2file,sheet_name=sheet_name,enc=enc)
    
    def universal_load(self,path,sheet_name=0,enc="utf-8"):
        """Load dataframe by file extension
        """
        if path.endswith("csv"):
            df=pd.read_csv(path,encoding=enc)
        elif path.endswith("xlsx") or path.endswith("xls"):
            df=pd.read_excel(path,sheet_name=sheet_name,encoding=enc)
        elif path.endswith("txt"):
            df=pd.read_table(path,encoding=enc)
        return df
    
class Output:
    def prepare_dir(name):
        """Create folders if they're not already there
        """
        if not os.path.exists(name):
            os.makedirs(name)
