#=============================================Importing required libraries============================================
import bs4
import requests
import tkinter as tk
from bs4 import BeautifulSoup

#=============================================Make window=============================================================
root=tk.Tk()

canvas=tk.Canvas(root,width=400,height=300,bg = '#ffffff')
canvas.pack()

root.title("Get Stock Price")

#=============================================Labels===================================================================
label1 = tk.Label(root, text='GET STOCK PRICE ',bg = '#ffffff')
label1.config(font=('roboto', 18,"bold"))
canvas.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Type stock symbol:',bg = '#ffffff',fg="#384DAB")
label2.config(font=('helvetica', 15,"bold"))
canvas.create_window(200, 100, window=label2)

label3 = tk.Label(root, text='(According to yahoo finance)',bg = '#ffffff',fg="#FC0000")
label3.config(font=('helvetica', 8))
canvas.create_window(200, 120, window=label3)
#=============================================Enter stock symbol=======================================================
enter_quote=tk.Entry(root,bg="#EAEAEA")                                                                                            #Take symbol as input
canvas.create_window(200,140,window=enter_quote)

#=============================================Get price function=======================================================
def stockprice():
    quote=enter_quote.get()                                                                                                        #Using entered input here
    URL="https://in.finance.yahoo.com/quote/"+quote+"?p="+quote                                                                    #completing URL
    r=requests.get(URL)                                                                                                            #Checking URL is valid or not, it should give response 200
    stock=bs4.BeautifulSoup(r.text,"html5lib")                                                                                     #Coverting html into text
    s=stock.find_all("div",{"class":"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find("span").text                                     #class of yahoo finance where price of stock is present
    
    #=============================================Labels===============================================================
    label3 = tk.Label(root, text="The current price of "+quote+ " is: ",font=('helvetica', 10), bg="#ffffff")
    canvas.create_window(200, 210, window=label3)
    
    label4 = tk.Label(root, text=s,font=('helvetica', 10, 'bold'),bg="#ffffff")
    canvas.create_window(200, 230, window=label4)

#=============================================Current price===============================================================
button1 = tk.Button(text='Get Current price', command=stockprice, bg='#81C8FF', fg='black', font=('helvetica', 10, 'bold'))
canvas.create_window(200, 180, window=button1)

#=============================================Main loop===================================================================
root.mainloop()
