import tkinter
import customtkinter
import os
from PIL import Image
import tkinter.messagebox as messagebox
from CTkPDFViewer import *
import pyglet

# Import font
pyglet.font.add_file('fonts/GameOfSquids-1GMVL.ttf')


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("EnCIVILopedia")
        self.geometry("1000x800")
        self.resizable(False, False)
        self.center_window()

        root = customtkinter.CTk()

        # exit confirmation
        self.protocol("WM_DELETE_WINDOW", self.confirm_exit)

        # icon
        script_dir = os.path.dirname(os.path.realpath(__file__))
        icon_path = os.path.join(script_dir, "assets", "logo.ico")
        self.iconbitmap(icon_path)

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "logo.png")), size=(160, 160))

        # bg images
        self.large_test_home = customtkinter.CTkImage(Image.open(os.path.join(image_path, "home-modified.png")), size=(600, 140))
        self.large_test_more = customtkinter.CTkImage(Image.open(os.path.join(image_path, "more-modified.png")), size=(600, 140))
        self.large_test_image1 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_bg1-modified.png")), size=(600, 140))
        self.large_test_image2 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_bg2-modified.png")), size=(600, 140))
        self.large_test_image3 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_bg3-modified.png")), size=(600, 140))
        self.large_test_image4 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_bg4-modified.png")), size=(600, 140))
        self.large_test_image5 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "large_bg5-modified.png")), size=(600, 140))
        
        # icon images
        self.home_image_icon = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_icon.png")), size=(50, 50))
        self.more_image_icon = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "more_icon.png")), size=(50, 50))
        self.image_frame_icon1 = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "icon1.png")), size=(50, 50))
        self.image_frame_icon2 = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "icon2.png")), size=(50, 50))
        self.image_frame_icon3 = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "icon3.png")), size=(50, 50))
        self.image_frame_icon4 = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "icon4.png")), size=(50, 50))
        self.image_frame_icon5 = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "icon5.png")), size=(50, 50))


        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(9, weight=1)

        self.navigation_frame_image = customtkinter.CTkLabel(self.navigation_frame, text="", image=self.logo_image, compound="center")
        self.navigation_frame_image.grid(row=0, column=0, padx=20, pady=20)

        # Frames Button
        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.home_image_icon, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_1_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Structural Engineering",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.image_frame_icon3, anchor="w", command=self.frame_1_button_event)
        self.frame_1_button.grid(row=2, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Transportation Engineering",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.image_frame_icon5, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=3, column=0, sticky="ew")

        self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Water Resources Engineering",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.image_frame_icon1, anchor="w", command=self.frame_3_button_event)
        self.frame_3_button.grid(row=4, column=0, sticky="ew")

        self.frame_4_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Construction Engineering & Management",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.image_frame_icon4, anchor="w", command=self.frame_4_button_event)
        self.frame_4_button.grid(row=5, column=0, sticky="ew")

        self.frame_5_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Geotechnical Engineering",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.image_frame_icon2, anchor="w", command=self.frame_5_button_event)
        self.frame_5_button.grid(row=6, column=0, sticky="ew")

        self.more_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="More",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.more_image_icon, anchor="w", command=self.more_button_event)
        self.more_button.grid(row=7, column=0, sticky="ew")


        # appearnce mode
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Dark", "Light", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=9, column=0, padx=20, pady=20, sticky="s")

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)
        self.home_frame.grid_rowconfigure(1, weight=1)

        # home header
        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="EnCIVILopedia", image=self.large_test_home, font=('Game Of Squids', 20, 'italic'), text_color="white")
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        # home textbox
        self.home_textbox = customtkinter.CTkTextbox(self.home_frame)
        self.home_textbox.grid(row = 1, column = 0, padx=(20, 0), pady=(20, 0))
        self.home_textbox.place(relx=0.5, rely=0.33, anchor=tkinter.CENTER)
        self.home_textbox.configure(state="disabled")
        self.home_textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)

        # create first frame
        self.first_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.first_frame.grid_columnconfigure(0, weight=1)
        self.first_frame.grid_rowconfigure(1, weight=1)

        # first header
        self.first_frame_large_image_label = customtkinter.CTkLabel(self.first_frame, text="Structural Engineering", image=self.large_test_image1, font=('Game Of Squids', 20, 'italic'), text_color="white")
        self.first_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        # create second frame
        self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.second_frame.grid_columnconfigure(0, weight=1)
        self.second_frame.grid_rowconfigure(1, weight=1)

        # second header
        self.second_frame_large_image_label = customtkinter.CTkLabel(self.second_frame, text="Transportation Engineering", image=self.large_test_image5, font=('Game Of Squids', 20, 'italic'), text_color="white")
        self.second_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        # create third frame
        self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.third_frame.grid_columnconfigure(0, weight=1)
        self.third_frame.grid_rowconfigure(1, weight=1)

        # third header
        self.third_frame_large_image_label = customtkinter.CTkLabel(self.third_frame, text="Water Resources Engineering", image=self.large_test_image4, font=('Game Of Squids', 20, 'italic'), text_color="white")
        self.third_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        # create fourth frame
        self.fourth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fourth_frame.grid_columnconfigure(0, weight=1)
        self.fourth_frame.grid_rowconfigure(1, weight=1)

        # fourth header
        self.fourth_frame_large_image_label = customtkinter.CTkLabel(self.fourth_frame, text="Construction Engineering & Management", image=self.large_test_image3, font=('Game Of Squids', 20, 'italic'), text_color="white")
        self.fourth_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        # create fifth frame
        self.fifth_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.fifth_frame.grid_columnconfigure(0, weight=1)
        self.fifth_frame.grid_rowconfigure(1, weight=1)

        # fifth header
        self.fifth_frame_large_image_label = customtkinter.CTkLabel(self.fifth_frame, text="Geotechnical Engineering", image=self.large_test_image2, font=('Game Of Squids', 20, 'italic'), text_color="white")
        self.fifth_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        # create more frame
        self.more_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.more_frame.grid_columnconfigure(0, weight=1)
        self.more_frame.grid_rowconfigure(1, weight=1)

        # more header
        self.more_frame_large_image_label = customtkinter.CTkLabel(self.more_frame, text="More", image=self.large_test_more, font=('Game Of Squids', 20, 'italic'), text_color="white")
        self.more_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_1_button.configure(fg_color=("gray75", "gray25") if name == "frame_1" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")
        self.frame_4_button.configure(fg_color=("gray75", "gray25") if name == "frame_4" else "transparent")
        self.frame_5_button.configure(fg_color=("gray75", "gray25") if name == "frame_5" else "transparent")
        self.more_button.configure(fg_color=("gray75", "gray25") if name == "more" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()

        if name == "frame_1":
            self.first_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.first_frame.grid_forget()

        if name == "frame_2":
            self.second_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.second_frame.grid_forget()

        if name == "frame_3":
            self.third_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.third_frame.grid_forget()

        if name == "frame_4":
            self.fourth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fourth_frame.grid_forget()

        if name == "frame_5":
            self.fifth_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.fifth_frame.grid_forget()
        
        if name == "more":
            self.more_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.more_frame.grid_forget()

    
    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_1_button_event(self):
        self.select_frame_by_name("frame_1")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def frame_3_button_event(self):
        self.select_frame_by_name("frame_3")

    def frame_4_button_event(self):
        self.select_frame_by_name("frame_4")
    
    def frame_5_button_event(self):
        self.select_frame_by_name("frame_5")

    def more_button_event(self):
        self.select_frame_by_name("more")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    
    def center_window(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width - 1000) // 2
        y = (screen_height - 800) // 2 

        self.geometry(f"1000x800+{x}+{y}")
    

    def confirm_exit(self):
        result = messagebox.askyesno("Confirm Exit", "Are you sure you want to exit the application?")
        if result:
            self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()