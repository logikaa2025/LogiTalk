from customtkinter import *


class MainWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x300")

        self.frame = CTk(self, width=200, height=self.winfo_height())
        self.frame.pack_propagate(False)
        self.frame.configure(width=0)
        self.frame.place(x=0, y=0)
        self.is_show_menu = False
        self.frame_width = 0

        self.label = CTkLabel(self.frame, text="Ваше ім'я")
        self.label.pack(pady=30)
        self.entry = CTkEntry(self.frame)
        self.entry.pack()
        self.label_theme = CTk0ptionMenu(self.frame, values=["Темна", "Світла"], command=self.change_theme)
        self.label_theme.pack(side="bottom", pady=20)
        self.theme = None
        self.btn = CTkButton(self, text="", command=self.toggle_show_Menu, width=30)
        self.btn.place(x=0, y=0)
        self.Menu_show_speed = 20
        
        self.chat_text = CTkTextbox(self, state="disable")
        self.chat_text.place(x=0, y=30)
        
        self.messege_input = CTkEntry(self, placeholder_text="Введіть повідомлення:")
        self.messege_input.place(x=0, y=250)
        self.send_button = CTkButton(self, text="", width=40, height=30)
        self.send_button.place(x=200, y=250)
        
        self.adaptive_ui()
        
    def toggle_show_menu(self):
        if self.is_show_menu:
            self.is_show_menu = False
            self.clase_menu()
        else:
            self.is_show_menu = True
            self.show_menu()
            
    def show_menu(self):
        if self.frame width <= 200:
            self.frame_width += self.menu_show_speed
            self.frame.configure(width=self.frame_width, height=self.winfo_height())
