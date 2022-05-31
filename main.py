import tkinter
from tkinter import *
from textblob import TextBlob

root = Tk()
root.title("Spelling Checke")
root.geometry("700x400")
root.config(background= "#dae6f6")

#  def 
def check_spelling ():
	word=enter_text.get()
	a = TextBlob(word)
	right = str(a.correct())
	
	cs = Label(root,text="Correct Text Is:",font=("poppins",20),bg="#dae6f6",)
	cs.place(x=100,y=250)
	spell.config(text=right)
	
# heading code
heading = Label(root,text="Spelling Checke",font = ("Trebuchet MS",30,"bold"),bg="#dae6f6",fg="#364971")
heading.pack(pady=(50,0))

# enter box
enter_text = Entry(root,justify= "center",width=30,font=("poppins",20),bg="white",border=2)
enter_text.pack(pady=10)
enter_text.focus()

# Button 
button = Button(root,text="check"
,font=("arial",20,"bold"),fg="white",bg="red",command=check_spelling)
button.pack()
                 
spell = Label(root,font=("poppins",20),bg="#dae6f6",fg="#364971")
spell.place(x=350,y=250)

                 
                 
                 
root.mainloop()
