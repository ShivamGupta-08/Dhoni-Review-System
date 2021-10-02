#how to auto clip the video
#ptz control
import tkinter 
from tkinter.constants import ANCHOR, NW
import PIL.Image,PIL.ImageTk
import cv2
from functools import partial
import threading
import imutils
import time
print("Welcom to drs system")
stream = cv2.VideoCapture("clip.mp4")
flag = True
def play(speed):
    global flag
    print(f"This is play function {speed}")
  
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1+speed)

    grabbed,frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor= tkinter.NW)
    if flag:
        canvas.create_text(150,26 , fill="white",font="Times 26 bold",text="Decision Pending...")
    flag = not flag


SET_WIDTH = 650
SET_HEIGHT=368
def pending(decision):
    frame = cv2.cvtColor(cv2.imread("pending.png"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor= tkinter.NW)

    time.sleep(1)

    frame = cv2.cvtColor(cv2.imread("sponsor.png"),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor= tkinter.NW)

    time.sleep(1)
    if decision == 'out':
        decisionImg = "out.png"
    else:
        decisionImg = "not_out.png"
    frame = cv2.cvtColor(cv2.imread(decisionImg),cv2.COLOR_BGR2RGB)    
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor= tkinter.NW)

def out():
    thread = threading.Thread(target=pending,args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is out")
def not_out():
    thread = threading.Thread(target=pending,args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")
window = tkinter.Tk()
window.title("Dhoni Review System")
cv_img = cv2.cvtColor(cv2.imread("welcome.png"),cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window,width=SET_WIDTH,height=SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canavas= canvas.create_image(0,0, anchor=tkinter.NW,image=photo)
canvas.pack()

btn = tkinter.Button(window,text="<< Previous (Fast)",width=50,command=partial(play,-25))
btn.pack()
btn = tkinter.Button(window,text="<< Previous (Slow)",width=50,command=partial(play,-2))
btn.pack()
btn = tkinter.Button(window,text="Next (Fast) >>",width=50,command=partial(play,25))
btn.pack()
btn = tkinter.Button(window,text="Next (Slow) >>",width=50,command=partial(play,2))
btn.pack()
btn = tkinter.Button(window,text="Give Out",width=50,command=out)
btn.pack()
btn = tkinter.Button(window,text="Give Not Out",width=50,command=not_out)
btn.pack()
window.mainloop()