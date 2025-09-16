from tkinter import *
import translators as ts

screen=Tk()
screen.geometry("700x300")
screen.title("Language Translator")
screen.config(background="Pink")

Label(screen,text="Choose a language",font="arial 12",bg="white",fg="red").grid(row=0,column=1,pady=15)
LanguageChoice={'hi/Hindi','en/English','bn/Bengali','ur/Urdu','id/Indonesian','fr/French','es/Spanish','de/German'}
InputLanguage=StringVar()
InputLanguage.set('en/English')

TranslatedLanguage=StringVar()
TranslatedLanguage.set('bn/Bengali')

InputLanguageChoise=OptionMenu(screen,InputLanguage,*LanguageChoice).grid(row=1,column=2,padx=10,pady=10)
NewlanguageChoise=OptionMenu(screen,TranslatedLanguage,*LanguageChoice).grid(row=1,column=2,padx=10,pady=10)
TextVar=StringVar()
outputvar=StringVar()
Label(screen,text="Translated language",font="Arial 12",bg="white",fg="red").grid(row=0,column=2)
TexBox=Entry(screen,textvariable=TextVar,width=30,font="arial 10").grid(row=2,column=1)
TexBox1=Entry(screen,textvariable=outputvar,width=30,font="Arial 10").grid(row=2,column=3)
Label(screen,text="Enter text",font="Arial 14",bg="white",fg="red").grid(row=2,column=0)
Label(screen,text="Output text",font="Arial 14",bg="white",fg="red").grid(row=2,column=2)
def Translate():
   translat = ts.translate_text(
    TextVar.get(),
    translator="google",
    from_language=InputLanguage.get()[:2],
    to_language=TranslatedLanguage.get()[:2])

   outputvar.set(translat)
Button(screen,text="Translate",command=Translate,font="Arial 14",bg="Bisque").grid(row=7,column=1,columnspan=3,padx=10,pady=10)

screen.mainloop()