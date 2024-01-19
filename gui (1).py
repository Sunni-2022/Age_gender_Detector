import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import numpy as np
from keras.models import load_model

model = load_model('c:\\Users\\SHAIK SABIHA\\OneDrive\\Desktop\\Age Gender Detector\\Age_sex_Detection.hs')

top = tk.Tk()
top.geometry('800x600')
top.title('Age & Gender Detector')
top.configure(background='#CDCDCD')

label1 = Label(top, background='#CDCDCD', font=('arial', 15, 'bold'))
label2 = Label(top, background="#CDCDCD", font=('arial', 15, "bold"))
sign_image = Label(top)
photo_image = None  # Global variable to prevent garbage collection

def Detect(file_path):
    global photo_image
    image = Image.open(file_path)
    image = image.resize((48, 48))
    image = np.array(image)
    image = np.delete(image, 0, 1)
    image = np.resize(image, (48, 48, 3))
    print(image.shape)
    sex_f = ['Male', 'Female']
    image = np.array([image]) / 255
    pred = model.predict(image)
    age = int(np.round(pred[1][0]))
    sex = int(np.round(pred[0][0]))
    print("predicted Age is:  " + str(age))
    print("predicted Gender is: " + sex_f[sex])
    label1.configure(foreground="#011638", text=age)
    label2.configure(foreground="#011638", text=sex_f[sex])

def show_detect_button(file_path):
    detect_b = Button(top, text='Detect Image', command=lambda: Detect(file_path), padx=10, pady=5)
    detect_b.configure(background='#364156', foreground='White', font=('arial', 10, 'bold'))
    detect_b.place(relx=0.79, rely=0.46)

def upload_image():
    global photo_image
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail((400, 400))  # Adjust the size as needed
        photo_image = ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=photo_image)
        sign_image.image = photo_image  # Store reference to avoid garbage collection
        label1.configure(text='')
        label2.configure(text='')
        show_detect_button(file_path)
    except Exception as e:
        print("Error:", str(e))

upload = Button(top, text="Upload Image", command=upload_image, padx=10, pady=5)
upload.configure(background='#364156', foreground='White', font=('arial', 20, 'bold'))
upload.pack(side='bottom', pady=50)
sign_image.pack(side='bottom', expand='True')

label1.pack(side='bottom', expand='True')
label2.pack(side='bottom', expand='True')

heading = Label(top, text='Age and Gender Detector', pady=20, font=('arial', 20, 'bold'))
heading.configure(background='#CDCDCD', foreground="#364156")
heading.pack()

top.mainloop()
