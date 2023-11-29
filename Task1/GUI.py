import numpy as np
import pandas as pd
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import Perceptron
import Adaline



class Task1:
    def perceptron_selected(self):
        print("perceptron")

        
    def adaline_selected(self):
        print("adaline")

    def classify_data(self):
        user_input = self.get_user_input()
        result_window = Toplevel(self.root)
        result_window.title("Classification Results")

        selected_features = user_input['selected_features']

        global feature1_value
        global feature2_value

        def submit_data():
            f1=float(feature1.get())
            f2=float(feature2.get())

            if user_input["selected_algorithm"]=="Perceptron":
                selected_features = [feature for feature in user_input['selected_features'] if feature != '0']
                selected_classes = [X for X in user_input['selected_classes'] if X != '0']
                learning_rate = float(user_input['learning_rate'])

                # Convert epochs to an integer (if it's not already)
                epochs = int(user_input['epochs'])
                sample = np.array([f1, f2])

                bias = int(user_input['bias'])

                Perceptron.perceptron_window(selected_features, selected_classes, learning_rate, epochs,bias,sample)
            else:
                selected_features = [feature for feature in user_input['selected_features'] if feature != '0']
                selected_classes = [X for X in user_input['selected_classes'] if X != '0']
                learning_rate = float(user_input['learning_rate'])

                # Convert epochs to an integer (if it's not already)
                epochs = int(user_input['epochs'])
                sample = np.array([f1, f2])
                bias = int(user_input['bias'])
                mse_threshold=float(user_input['mse_threshold'])
                sample = np.array([f1, f2])

                Adaline.adaline_window(selected_features, selected_classes, learning_rate, epochs,mse_threshold,bias,sample)
            result_window.destroy()

        label1 = Label(result_window, text="Feature 1:", font=("arial", 12))
        label1.pack()
        feature1 = Entry(result_window, font=("arial", 12), width=30)
        feature1.insert(0, selected_features[0])
        feature1.pack()

        label2 = Label(result_window, text="Feature 2:", font=("arial", 12))
        label2.pack()
        feature2 = Entry(result_window, font=("arial", 12), width=30)
        feature2.insert(0, selected_features[1])
        feature2.pack()

        # Create a "Submit" button
        submit_button = Button(result_window, text="Submit", command=submit_data, bg=self.mainColor, fg=self.foregroundColor)
        submit_button.config(font=("arial", 12))
        submit_button.pack()

    def __init__(self):

        self.mainColor='#053654'
        self.secondColor = '#053654'
        self.foregroundColor = '#ffffff'
        self.root=tk.Tk()
        self.root.title("Task1")
        self.root.geometry("880x570")

        self.setting_background()

        self.objects()

        self.placing_widgets()
        # Create a "Classify" button
        self.classify_button = Button(self.root, text="Classify", command=self.classify_data, bg=self.mainColor, fg=self.foregroundColor)
        self.classify_button.config(font=("arial", 20))

        # Place the "Classify" button lower on your window
        self.classify_button.place(anchor='center', relx=0.6, y=540)

        self.root.mainloop()

        
    def get_user_input(self):
        selected_features = []
        if self.Area_value.get():
            selected_features.append(self.Area_value.get())
        if self.Perimeter_value.get():
            selected_features.append(self.Perimeter_value.get())
        if self.Major_value.get():
            selected_features.append(self.Major_value.get())
        if self.Minor_value.get():
            selected_features.append(self.Minor_value.get())
        if self.Roundness_value.get():
            selected_features.append(self.Roundness_value.get())

        selected_classes = []
        if self.BOMBAY_value.get():
            selected_classes.append(self.BOMBAY_value.get())
        if self.CALI_value.get():
            selected_classes.append(self.CALI_value.get())
        if self.SIRA_value.get():
            selected_classes.append(self.SIRA_value.get())

        learning_rate = self.number_value.get()
        epochs = self.number2_value.get()
        mse_threshold = self.number3_value.get()

        bias = self.bias_value.get()
        selected_algorithm = "Perceptron" if self.type_value.get() == "bits" else "Adaline"

        return {
            'selected_features': selected_features,
            'selected_classes': selected_classes,
            'learning_rate': learning_rate,
            'epochs': epochs,
            'mse_threshold': mse_threshold,
            'bias': bias,
            'selected_algorithm': selected_algorithm
        }

    def setting_background(self):
        self.image = Image.open("Photos/Internal_Background.png")
        self.Internal_BG = ImageTk.PhotoImage(self.image)
        self.Internal_BG_label = Label(self.root, image=self.Internal_BG)
        
    def objects(self):
        self.select_two_feature = Image.open("Photos/Select Two Features.png")
        self.select_two_feature_image = ImageTk.PhotoImage(self.select_two_feature)
        self.select_two_feature_label = Label(self.root, image=self.select_two_feature_image, background=self.mainColor) 



        self.Area_value = StringVar(value=0)
        self.Perimeter_value = StringVar(value=0)
        self.Major_value = StringVar(value=0)
        self.Minor_value = StringVar(value=0)
        self.Roundness_value = StringVar(value=0)

        self.Area_Image = PhotoImage(file="Photos/Area.png")
        self.Area_CheckButton = Checkbutton(self.root, variable=self.Area_value, onvalue="Area",
                                    offvalue="", background=self.mainColor, image=self.Area_Image,
                                    selectimage=self.Area_Image, activebackground=self.mainColor)

        self.Perimeter_Image = PhotoImage(file="Photos/Perimeter.png")
        self.Perimeter_CheckButton = Checkbutton(self.root, variable=self.Perimeter_value, onvalue="Perimeter",
                                         offvalue="", background=self.mainColor, image=self.Perimeter_Image,
                                         selectimage=self.Perimeter_Image, activebackground=self.mainColor)

        self.Major_Image = PhotoImage(file="Photos/Major Axis.png")
        self.Major_CheckButton = Checkbutton(self.root, variable=self.Major_value, onvalue="MajorAxisLength",
                                     offvalue="", background=self.mainColor, image=self.Major_Image,
                                     selectimage=self.Major_Image, activebackground=self.mainColor)

        self.Minor_Image = PhotoImage(file="Photos/Minor Axis.png")
        self.Minor_CheckButton = Checkbutton(self.root, variable=self.Minor_value, onvalue="MinorAxisLength",
                                     offvalue="", background=self.mainColor, image=self.Minor_Image,
                                     selectimage=self.Minor_Image, activebackground=self.mainColor)

        self.Roundness_Image = PhotoImage(file="Photos/Roundness.png")
        self.Roundness_CheckButton = Checkbutton(self.root, variable=self.Roundness_value, onvalue="roundnes",
                                         offvalue="", background=self.mainColor, image=self.Roundness_Image,
                                         selectimage=self.Roundness_Image, activebackground=self.mainColor)

        self.select_two_classes = Image.open("Photos/Select Two Classes.png")
        self.select_two_classes_image = ImageTk.PhotoImage(self.select_two_classes)
        self.select_two_classes_label = Label(self.root, image=self.select_two_classes_image, background=self.mainColor)

        self.BOMBAY_value = StringVar(value=0)
        self.CALI_value = StringVar(value=0)
        self.SIRA_value = StringVar(value=0)
        
        self.Bombay_Image = PhotoImage(file="Photos/BOMBAY.png")
        self.Bombay_CheckButton = Checkbutton(self.root, variable=self.BOMBAY_value, onvalue="BOMBAY",
                                     offvalue="", background=self.mainColor, image=self.Bombay_Image,
                                     selectimage=self.Bombay_Image, activebackground=self.mainColor)

        self.Cali_Image = PhotoImage(file="Photos/CALI.png")
        self.Cali_CheckButton = Checkbutton(self.root, variable=self.CALI_value, onvalue="CALI",
                                     offvalue="", background=self.mainColor, image=self.Cali_Image,
                                     selectimage=self.Cali_Image, activebackground=self.mainColor)

        self.Sira_Image = PhotoImage(file="Photos/SIRA.png")
        self.Sira_CheckButton = Checkbutton(self.root, variable=self.SIRA_value, onvalue="SIRA",
                                         offvalue="", background=self.mainColor, image=self.Sira_Image,
                                         selectimage=self.Sira_Image, activebackground=self.mainColor)
        
        self.Enter_Learning_rate = Image.open("Photos/Enter Learning Rate.png")
        self.Enter_Learning_rate_image = ImageTk.PhotoImage(self.Enter_Learning_rate)
        self.Enter_Learning_rate_label = Label(self.root, image=self.Enter_Learning_rate_image, background=self.mainColor)
        
        self.input = Image.open("Photos/Input.png")
        self.input_image = ImageTk.PhotoImage(self.input)
        self.input_label = Label(self.root, image=self.input_image, background=self.mainColor)
        self.number_value = StringVar(value="")
        self.numberEntry = Entry(self.root, width=15, font=("arial", 28), bd=0, textvariable=self.number_value,background=self.mainColor,foreground=self.foregroundColor )


        self.Enter_Epochs = Image.open("Photos/Enter number of Epochs.png")
        self.Enter_Epochs_image = ImageTk.PhotoImage(self.Enter_Epochs)
        self.Enter_Epochs_label = Label(self.root, image=self.Enter_Epochs_image, background=self.mainColor)
        
        self.input2 = Image.open("Photos/Input.png")
        self.input2_image = ImageTk.PhotoImage(self.input2)
        self.input2_label = Label(self.root, image=self.input2_image, background=self.mainColor)
        self.number2_value = StringVar(value="")
        self.number2Entry = Entry(self.root, width=15, font=("arial", 28), bd=0, textvariable=self.number2_value,background=self.mainColor,foreground=self.foregroundColor )


        self.mse = Image.open("Photos/Enter mse Threshold.png")
        self.mse_image = ImageTk.PhotoImage(self.mse)
        self.mse_label = Label(self.root, image=self.mse_image, background=self.mainColor)
        
        self.input3 = Image.open("Photos/Input.png")
        self.input3_image = ImageTk.PhotoImage(self.input3)
        self.input3_label = Label(self.root, image=self.input3_image, background=self.mainColor)
        self.number3_value = StringVar(value="")
        self.number3Entry = Entry(self.root, width=15, font=("arial", 28), bd=0, textvariable=self.number3_value,background=self.mainColor,foreground=self.foregroundColor )
         
        self.bias_value = StringVar(value=0)
        self.Bias_Image = PhotoImage(file="Photos/Bias.png")
        self.Bias_radio_Button = Checkbutton(self.root, variable=self.bias_value,
                onvalue=1,offvalue=0, background=self.mainColor, image=self.Bias_Image, activebackground=self.mainColor)


        self.Choose_Algorithm = Image.open("Photos/Choose Algorithm.png")
        self.Choose_Algorithm_image = ImageTk.PhotoImage(self.Choose_Algorithm)
        self.Choose_Algorithm_label = Label(self.root, image=self.Choose_Algorithm_image, background=self.mainColor)

        self.type_value = StringVar(value="none")
        self.Perceptron_Image = PhotoImage(file="Photos/Perceptron.png")
        self.Perceptron_RadioButton = Radiobutton(self.root, variable=self.type_value,
                                           value="bits", background=self.mainColor, image=self.Perceptron_Image,
                                           activebackground=self.mainColor)
        self.Adaline_Image = PhotoImage(file="Photos/Adaline.png")
        self.Adaline_RadioButton = Radiobutton(self.root, variable=self.type_value,
                                             value="level", background=self.mainColor, image=self.Adaline_Image,
                                             activebackground=self.mainColor)

    def placing_widgets(self):
        self.Internal_BG_label.place(x=0, y=0)
        self.select_two_feature_label.place(anchor='center', relx=0.2, y=30)
        self.Area_CheckButton.place(relx=0.05, rely=0.1)
        self.Perimeter_CheckButton.place(relx=0.25, rely=0.1)
        self.Major_CheckButton.place(relx=0.45, rely=0.1)
        self.Minor_CheckButton.place(relx=0.65, rely=0.1)
        self.Roundness_CheckButton.place(relx=0.85, rely=0.1)
        self.select_two_classes_label.place(anchor='center',relx=0.19,y=120)
        self.Bombay_CheckButton.place(relx=0.05,rely=0.25)
        self.Cali_CheckButton.place(relx=0.25,rely=0.25)
        self.Sira_CheckButton.place(relx=0.45,rely=0.25)
        self.Enter_Learning_rate_label.place(anchor='center',relx=0.21,y=210)
        self.input_label.place(anchor='center', relx=0.70, y=210)
        self.numberEntry.place(anchor="center",relx=0.70,y=210)
        self.Enter_Epochs_label.place(anchor='center',relx=0.25,y=290)
        self.input2_label.place(anchor='center', relx=0.70, y=290)
        self.number2Entry.place(anchor="center",relx=0.70,y=290)
        self.mse_label.place(anchor='center',relx=0.21,y=370)
        self.input3_label.place(anchor='center', relx=0.70, y=370)
        self.number3Entry.place(anchor="center",relx=0.70,y=370)
        self.Bias_radio_Button.place(anchor='center', relx=0.06, y=440)
        self.Choose_Algorithm_label.place(anchor='center',relx=0.19,y=500)
        self.Perceptron_RadioButton.place(anchor='center', relx=0.50, y=500)
        self.Adaline_RadioButton.place(anchor='center', relx=0.75, y=500)
