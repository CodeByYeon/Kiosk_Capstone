import tkinter

mainwindow = tkinter.Tk()

mainwindow.title("키오스크 매니저") #타이틀 이름
mainwindow.geometry("480x800+100+100")  #해상도를 480*800으로 설정했고 X,Y좌표 100/100으로 설정함
mainwindow.resizable(False, False) #윈도우 사이즈 편집 불가로 변경

headersentence = tkinter.Label(mainwindow, text="초보도\n쉽고 간편하게\n주문하세요!", height=7,font=("Arial", 20, "bold"))
headersentence.pack()

infozoom = tkinter.Label(mainwindow,text="글씨 크기", font=("Arial", 15, "bold"))
infozoom.place(x=365,y=30)
zoominbutton = tkinter.Button(mainwindow,text="+", overrelief="solid", width=2, height=1,justify="left",font=("Arial",20,"bold"))
zoominbutton.place(x=330,y=70)
zoomoutbutton = tkinter.Button(mainwindow,text="-", overrelief="solid", width=2, height=1,justify="left",font=("Arial",20,"bold"))
zoomoutbutton.place(x=400,y=70)
takeoutbutton = tkinter.Button(mainwindow,text="포장", overrelief="solid", width=7, height=15,justify="left",font=("Arial",17,"bold"))
takeoutbutton.place(x=50,y=300)
eatherebutton = tkinter.Button(mainwindow,text="매장", overrelief="solid", width=7, height=15,justify="right",font=("Arial",17,"bold"))
eatherebutton.place(x=300,y=300)


mainwindow.mainloop()