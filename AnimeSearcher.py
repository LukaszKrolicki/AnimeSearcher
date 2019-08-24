import tkinter as tk
from PIL import ImageTk, Image
from tkinter import font
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.request
import requests
import shutil
import time

HEIGHT=850
WIDTH=900

root=tk.Tk()
text = tk.Text(root)
bgimage=ImageTk.PhotoImage(Image.open('21591.jpg'))
bgimage2=ImageTk.PhotoImage(Image.open('87215 (1).jpg'))


def anime_s(anime3,label8,label4,label5,label6,label20,label21,label3):
    try:
        request = Request('https://kitsu.io/api/edge', headers={'User-Agent': 'Mozilla/5.0'})

        anime2 = ""
        for letter in anime3:
            if letter == " ":
                letter = "%20"
                anime2 = anime2 + letter
            else:
                anime2 = anime2 + letter

        url = 'https://kitsu.io/api/edge/anime?filter[text]=' + str(anime2)

        headers = {
            'Accept': 'application/vnd.api+json',
            'Content-Type': 'application/vnd.api+json'
        }

        request = requests.request("GET", url=url, headers=headers)
        anime = request.json()
        poster = anime['data'][0]['attributes']['posterImage']['medium']
        r = requests.get(poster, stream=True, headers={'User-agent': 'Mozilla/5.0'})
        if r.status_code == 200:
            with open("img.jpg", 'wb') as f:
                r.raw.decode_content = True
                shutil.copyfileobj(r.raw, f)

        name = anime['data'][0]['attributes']['slug']
        desc = anime['data'][0]['attributes']['synopsis']
        rating = anime['data'][0]['attributes']['averageRating']
        popularity = anime['data'][0]['attributes']['popularityRank']
        start_date = anime['data'][0]['attributes']['startDate']
        end_date = anime['data'][0]['attributes']['endDate']

        label8['text']=format(name)
        label4['text'] = format("Description: "+desc)
        label5['text']=format("Rating: " + rating)
        label6['text']=format("Popularity rank: " + str(popularity))
        label20['text']=format("Start Date: " + str(start_date))

        global aimage
        aimage = ImageTk.PhotoImage(Image.open('img.jpg'))
        label3.config(image=aimage)

        if end_date==None:
            end_date="On Going"
            label21['text'] = format("End Date: " + str(end_date))
        else:
            label21['text'] = format("End Date: " + str(end_date))
    except:
        label8['text']=format("Not Found")


def OpenNewWindow(): # new window definition
    frame.destroy()
    frame2 = tk.Frame(root, bg="#ffc266")
    frame2.place(relx=0, rely=0, relwidth=1, relheight=1)

    label2 = tk.Label(frame2, image=bgimage2)
    label2.place(relx=0, rely=0, relwidth=1, relheight=1)

    frame3 = tk.Frame(label2, bg="#d966ff",bd=10)
    frame3.place(relx=0.175, rely=0.07, relwidth=0.65, relheight=0.1)

    enter = tk.Entry(frame3, bg="#e699ff",font=('Conthrax Sb',15))
    enter.place(relx=0, rely=0, relwidth=0.75, relheight=1)

    button = tk.Button(frame3, text="Search", bg="#d966ff",command=lambda: anime_s(enter.get(),label8,label4,label5,label6,label20,label21,label3),font=('Conthrax Sb',15))
    button.place(relx=0.77, rely=0, relwidth=0.23, relheight=1)


    frame4 = tk.Frame(label2, bg="#e699ff",bd=10)
    frame4.place(relx=0.175, rely=0.25, relwidth=0.65, relheight=0.6)

    label3 = tk.Label(frame4, bg="#d966ff",text="image",font=('Conthrax Sb',20))
    label3.place(relx=0, rely=0.08, relwidth=0.5, relheight=0.6)

    label4 = tk.Label(frame4, bg="#d966ff",text="Description",anchor='nw',wraplength=250,justify='left',font=('Courier',8))
    label4.place(relx=0.52, rely=0.08, relwidth=0.48, relheight=0.68)

    label5 = tk.Label(frame4, bg="#d966ff",text="Rate",font=('Conthrax Sb',20))
    label5.place(relx=0, rely=0.78, relwidth=0.5, relheight=0.1)

    label6 = tk.Label(frame4, bg="#d966ff",text="Popularity",font=('Conthrax Sb',12))
    label6.place(relx=0, rely=0.90, relwidth=0.5, relheight=0.1)

    label20 = tk.Label(frame4, bg="#d966ff",text="Start Date",font=('Conthrax Sb',12))
    label20.place(relx=0.52, rely=0.78, relwidth=0.48, relheight=0.1)

    label21 = tk.Label(frame4, bg="#d966ff",text="End Date",font=('Conthrax Sb',12))
    label21.place(relx=0.52, rely=0.90, relwidth=0.48, relheight=0.1)

    label7 = tk.Label(frame4, bg="#d966ff", text="More Info", font=('Conthrax Sb',10))
    label7.place(relx=0, rely=0.7, relwidth=0.25, relheight=0.05)

    label8 = tk.Label(frame4, bg="#d966ff",font=('Conthrax Sb',15),text="Ttitle")
    label8.place(relx=0, rely=0, relwidth=1, relheight=0.07)


font=('Conthrax Sb',18)


canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

frame=tk.Frame(root,bg="#ffc266")
frame.place(relx=0,rely=0,relwidth=1,relheight=1)

label1=tk.Label(frame,image=bgimage)
label1.place(relx=0,rely=0,relwidth=1,relheight=1)
#label1.attributes("-alpha", 0.5)

button=tk.Button(frame, text="Start",command =OpenNewWindow,bg="#7300e6",font=('Conthrax Sb',20),fg="#330066",
activebackground= "#5900b3", highlightcolor="#5900b3")
button.place(relx=0.375,rely=0.6,relwidth=0.25,relheight=0.07)


root.mainloop()

