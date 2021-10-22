from tkinter import *
from tkinter import font
from PIL import ImageTk, Image
import requests

root = Tk()
root.geometry("600x500")
root.title("Weater Updates")
im = PhotoImage(file = "landscape.png")
Label(root, image = im).place(relheight=1, relwidth=1)

def info():
    try:
        id = '4fd46a4b5c20960a40c3dd4ae44b1c65'
        url = 'https://api.openweathermap.org/data/2.5/weather?'
        params = {'APPID' : id, 'q': ent.get(), 'units': 'metric'}
        request = requests.get(url, params)
        l = request.json()
        need = "Country : %s\nCity : %s\nConditions : %s\nCurrent Temp. (°C) : %s" % (l['sys']['country'],l['name'], str(l['weather'][0]['description']), str(l['main']['temp']))
        need += "\nTemp. Range :" +"(" + str(l['main']['temp_min'])+" - "+str(l['main']['temp_max'])+")"
        need += "\nHumidity :" + (str(l['main']['humidity']))
        big_fra['text'] = need

    except Exception as e:  
        ent.delete(0, END)
        big_fra['text'] = "ERROR..."
    
    



fra = Frame(root, bd = 4, bg= "#99c2ff")
fra.place(relx = 0.11, rely =0.1 , relheight=0.1, relwidth=0.78)
ent = Entry(fra, font=("Arial Baltic",11))
ent.place(relheight=1, relwidth=0.66)
search_btn = Button(fra, text = "View Weather", fg ="BLack"  ,font=("Sitka Display",14), command =info, bg="#ccffe6")
search_btn.place(relheight=1, relx=0.68, relwidth=0.31)
lab = Frame(root, bd=4, bg= "#99c2ff")
lab.place(relx= 0.11, rely = 0.3, relheight=0.55, relwidth=0.78)
big_fra = Label(lab, anchor=N+W, font=('Georgia',16), justify='left', bg ="#ffff99" )
big_fra.place(relheight=1, relwidth=1)
print(font.families())
results = Label(big_fra, anchor='nw', justify='left', bd=4)

root.mainloop()
