# from tkinter import *
# # from tkinter import ttk
import customtkinter
import tkinter
import loaded



customtkinter.set_ctk_parent_class(tkinter.Tk)


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"

# Тему можно создать свою, подключив json файл
# customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"
customtkinter.set_default_color_theme("./my_files/blue.json")
# customtkinter.set_default_color_theme("./my_files/dark-blue.json")

app = customtkinter.CTk()
app.title("Dounload from YouTube")
app.geometry("400x150")

# frame_1 = customtkinter.CTkFrame(master=app,  width=300, height=50, border_width=2, border_color="lightblue")
# frame_1.grid(row=0, column=0)
# frame_1.pack(pady=20, padx=20)

# text_link = customtkinter.CTkLabel(frame_1, text="URL:", fg_color="transparent", text_color="lightblue", anchor="w")
# # text_link.pack()

# frame_1 = customtkinter.CTkFrame(app, padding="10 10 20 20", border_width=2, border_color="lightgray")
# frame_1.grid(column=0, row=0, sticky="nsew")

text_link = customtkinter.CTkLabel(app, text="URL: ") # text_color="lightblue"
text_link.grid(row=0, column=0, padx=20, pady=20)


entry_link = customtkinter.CTkEntry(app, placeholder_text="Enter video link ")
entry_link.grid(row=0, column=1, padx=20, sticky="ew", columnspan=2)
app.columnconfigure(1, weight=1)

link = entry_link.cget("textvariable")

text_title = customtkinter.CTkLabel(app, text="Name") #, text_color="blue"
text_title.grid(row=2, column=0, padx=20)

text_video_name = customtkinter.CTkLabel(app, text="", text_color="lightblue")
text_video_name.grid(row=2, column=1, padx=20, sticky="w", columnspan=2)

text_autor = customtkinter.CTkLabel(app, text="Autor") #, text_color="blue"
text_autor.grid(row=4, column=0, padx=20)

text_video_autor = customtkinter.CTkLabel(app, text="", text_color="lightblue")
text_video_autor.grid(row=4, column=1, padx=20, sticky="w", columnspan=2)


video = loaded.download_video("https://youtu.be/tNSjC0sZiy8") # ("https://youtu.be/tNSjC0sZiy8")
text_video_name.configure(text=video["title"])
text_video_autor.configure(text=video["author"])


app.mainloop()