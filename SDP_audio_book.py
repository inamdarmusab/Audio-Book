from re import S
import pyttsx3
import PyPDF2
import pytesseract
from PIL import Image
import datetime

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

dateAndTime = datetime.datetime.now()
print("\n",dateAndTime)

name = input("\nplease enter your name ")
print("Hi " + name +"," '''\n i am glance! \n
if you want to convert image to speech press 1  \n
if you want to convert pdf to Audiobook press 2\n 
if you want to exit press any " 5 " ''')

speak = pyttsx3.init()




while True:


    number = int(input("\n            ***************enter Number**************\n \n\n                   image to speech press 1                   \n\n                            or                   \n\n                   pdf to Audiobook press 2                   \n\n                   press `5` to exit                   \n\n\n            ****************************************\n\n enter : " ))
    if (number == 1 ):

        class Tesseract:

            img = Image.open('C:\\musab\\python.pvt\\Inkedtxt_LI.jpg')
            output = pytesseract.image_to_string(img)
            print (output)
            print(img)



            speaker = pyttsx3.init()
            speaker.say(output)
            speaker.runAndWait()



    elif (number == 2):

        class pyPDF:

            text_Book = open('C:\\musab\\python.pvt\\RichDadPoorDad.pdf','rb')
            read = PyPDF2.PdfFileReader(text_Book)

            pages = read.numPages
            print(pages)


            speak = pyttsx3.init()
            page = read.getPage(1)
            text = page.extractText()
            speak.say(text)
            speak.runAndWait()

    elif (number == 5):
        print("Thank You " + name + " for Visiting")
        break

    else:
        print(name + " you are Choosing Wrong Option")


    

        


