import tkinter as tk
def draw(Canvas):
    pass 
def makeCanvas(w,h):
    root=tk.Tk()
    canvas=tk.Canvas(root,width=w,height=h)
    canvas.configure(bd=0,highlightthickness=0)
    canvas.create_rectangle(10,50,110,100, fill="yellow") 
    canvas.pack()
    draw(canvas) 
    root.mainloop()
makeCanvas(400,400) 

# def mostCommonFirstLetter(string):
#     s=string.split()
#     d={}
#     s1=[]
#     for i in range (len(s)):
#         s1.append(s[i][0])
#         d[s1[i]]=s1.count(s1[i])
#     k=max(zip(d.values(),d.keys()))[1]
#     return k
# string="do you have a voting plan for the election happening next month?"
# print("mostCommonFirstLetter:",mostCommonFirstLetter(string)) 