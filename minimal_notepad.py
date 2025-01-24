import customtkinter as ctk
from customtkinter import filedialog

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

def add_placeholder(event):
    if user_text.get("1.0","end-1c") == "":
        user_text.insert("1.0", "Type here...")
        user_text.configure(fg_color="transparent")

def remove_placeholder(event):
    if user_text.get("1.0", "end-1c") == "Type here...":
        user_text.delete("1.0", "end")
        user_text.configure(fg_color="transparent")

def new_text():
    user_text.delete("1.0",ctk.END)

def save_text():
    file_path = ctk.filedialog.asksaveasfilename(defaultextension=".txt",filetypes=[("Text files", "*.txt"),("All Files","*.*")])

    if file_path:
        with open(file_path,"w") as file:
            file.write(user_text.get("1.0",ctk.END))

def open_text():
    file_path = ctk.filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            user_text.delete("1.0", ctk.END)
            user_text.insert("1.0", content)

app = ctk.CTk()
app.title("Minimal Notepad")
app.geometry("800x550")
app.iconbitmap("notepadicon.ico")

btn_frame = ctk.CTkFrame(master=app,fg_color="transparent",width=70,height=780)
btn_frame.pack(side="left")

open_btn = ctk.CTkButton(master=btn_frame, text="Open", fg_color="transparent", border_width=1, width=50, command=open_text, height=150)
open_btn.pack(padx=20, pady=10, fill="y")

save_btn = ctk.CTkButton(master=btn_frame,text="Save",fg_color="transparent",border_width=1,width=50,command=save_text,height=150)
save_btn.pack(padx=20,pady=10,fill="y")

new_btn = ctk.CTkButton(master=btn_frame,text="New",fg_color="transparent",border_width=1,width=50,command=new_text,height=150)
new_btn.pack(padx=20,pady=10,fill="y")

text_frame = ctk.CTkFrame(master=app,border_width=1)
text_frame.pack(fill="both",expand=True,pady=10,padx=10)

user_text = ctk.CTkTextbox(master=text_frame,fg_color="transparent",font=("Arial",20))
user_text.pack(fill="both",expand=True,pady=10,padx=10)

user_text.insert("1.0", "Type here...")
user_text.configure(fg_color="transparent")

user_text.bind("<FocusIn>", remove_placeholder)
user_text.bind("<FocusOut>", add_placeholder)

app.mainloop()