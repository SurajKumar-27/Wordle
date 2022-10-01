from tkinter import *
import tkinter.messagebox
main_window=Tk()
main_window.title('WORDLE')
p1=PhotoImage(file="wordle2.png")
main_window.iconphoto(False,p1)
main_window.geometry("390x590")
main_window.resizable(False, False)
main_window.configure(bg="black")
my_font=('Georgia',15,'bold')
my_font1=(12)
import random
f1=open("Words.txt","r")
k=f1.read()
global a,word
guess=1
key=1
row=13
count=0
a=k.split()
b=random.randint(0,len(a)-1)
word=a[b]
letters=['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
word=word.upper()
color=[]
given_words=Entry(main_window,width=20,borderwidth=1,font=my_font1)
given_words.grid(row=11,column=0,columnspan=5,padx=15,pady=10)
visited = [1,1,1,1,1]
for i in range(0,27):
    color.append(0)
print(word)
def colouring():
    global row,key
    row=13
    key=1
    for l in range(0,26):
        if color[l]==0:
             Label(main_window,text=letters[l],font=my_font,bg='black',fg='white').grid(row=row,column=key,padx=5,pady=5)
        elif color[l]==1:
            Label(main_window,text=letters[l],font=my_font,bg='black',fg='grey').grid(row=row,column=key,padx=5,pady=5)
        elif color[l]==2:
            Label(main_window, text=letters[l], font=my_font, bg='black', fg='#C8D404').grid(row=row, column=key, padx=5,pady=5)
        elif color[l]==3:
            Label(main_window, text=letters[l], font=my_font, bg='black', fg='#4A9602').grid(row=row, column=key, padx=5,pady=5)
        key=key+1
        if key%6==0:
            row=row+1
            key=1
def clicking():
    global guess,count,visited,color,letters
    given = given_words.get()
    if(len(given)!=5):
        tkinter.messagebox.showerror("WORDLE","Please Enter a 5 lettter word")
    else:
        if given in a:
            given=given.upper()
            guess=guess+1
            for j in range(0,5):
                i=0
                if (given[j]==word[j] and visited[j]!=0):
                    visited[j]=0
                    i=1
                    for l in range(0,26):
                        if(given[j]==letters[l] and (color[l]==2 or color[l]==0)):
                            color[l]=3
                    Label(main_window,text=given[j],font=my_font,bg='#4A9602',fg='#FFFFFF').grid(row=guess,column=j,padx=10,pady=10)
                else:
                    for m in range(0,5):
                        if(word[m]==given[j] and j!=m and visited[m]!=0 and given[j] not in given[(j+1):]):
                            visited[m]=0
                            i=1
                            for l in range(0, 26):
                                if (given[j] == letters[l] and color[l]==0):
                                    color[l] =2
                            Label(main_window,text=given[j],font=my_font,bg='#C8D404',fg='#FFFFFF').grid(row=guess,column=j,padx=10,pady=10)
                if(i==0):
                    for l in range(0,26):
                        if(given[j]==letters[l]):
                            color[l]=1
                    Label(main_window,text=given[j],font=my_font,bg='#939393',fg='#FFFFFF').grid(row=guess,column=j,padx=10,pady=10)
            given_words.delete(0,'end')
            colouring()
            if (given == word):
                tkinter.messagebox.showinfo("WORDLE", "Congrats!! Your Guess is Correct")
                count=1
        else:
            tkinter.messagebox.showerror("WORDLE", "Please enter a valid word")
        if(guess>6 and count==0):
            tkinter.messagebox.showinfo("WORDLE",f"Your chances are exhausted. Correct word is {word}")
    visited=[1,1,1,1,1]
B1=Button(main_window,text='Check Word',command=clicking)
B1.grid(row=12,column=6)
main_window.mainloop()



