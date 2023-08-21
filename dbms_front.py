from tkinter import *
import tkinter.messagebox as mess
import pymysql

root = Tk()
root.geometry('700x500')
root.title("IPL AUCTION")
head= Label(root,text = 'IPL AUCTION',font=('bold',30),)
head.place(x = 250,y = 5)
name_player = Label(root,text = 'PLAYER NAME:',font = ('bold',15))
name_player.place(x = 15,y=105)
name_entry = Entry(font=('bold',15),bd=5,bg='pink')
name_entry.place( x = 220,y = 105)

player_id = Label(root,text = 'PLAYER ID:',font = ('bold',15))
player_id.place(x = 15,y=65)
id_entry = Entry(font=('bold',15),bd=5,bg='pink')
id_entry.place( x = 220,y = 65)


country = Label(root,text = 'COUNTRY:',font = ('bold',15))
country.place(x = 15,y=145)
country_entry = Entry(font=('bold',15),bd=5,bg='pink')
country_entry.place( x = 220,y = 145)


t_id = Label(root,text = 'TEAM ID:',font = ('bold',15))
t_id.place(x = 15,y=185)
tid_entry = Entry(font=('bold',15),bd=5,bg='pink')
tid_entry.place( x = 220,y = 185)


leag = Label(root,text = 'LEAGUES:',font = ('bold',15))
leag.place(x = 15,y=225)
leag_entry = Entry(font=('bold',15),bd=5,bg='pink')
leag_entry.place( x = 220,y = 225)


sold_amt = Label(root,text = 'SOLD AMOUNT:',font = ('bold',15))
sold_amt.place(x = 15,y=265)
amt_entry = Entry(font=('bold',15),bd=5,bg='pink')
amt_entry.place( x = 220,y = 265)

insert = Button(root,text ='INSERT ',font=('bold',15),bg = 'black',bd = 5,fg = 'white')
insert.place(x=550,y=65)

delete = Button(root,text ='DELETE',font=('bold',15),bg = 'black',bd = 5,fg = 'white')
delete.place(x=550,y=125)

update = Button(root,text ='UPDATE',font=('bold',15),bg = 'black',bd = 5,fg = 'white')
update.place(x=550,y=185)

select = Button(root,text ='SELECT ',font=('bold',15),bg = 'black',bd = 5,fg = 'white')
select.place(x=550,y=245)

root.mainloop()
