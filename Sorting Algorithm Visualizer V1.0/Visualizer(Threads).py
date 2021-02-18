import tkinter as tk
import numpy as np
import time
import threading

# Global Variables
"""
AlgorithmSelected :> to get the Selected Algorithm.
MaxVal :> to get the Max Value from Configure frame
MinVal :> to get the Max Value from Configure frame
Columns :> to get the count of columns from Configure frame
Speed :> to get the Speed of the Visualization from Configure frame
----
Algorithms :> Algorithms that are Implemented
Canvas Height , Canvas Width :> Geometry of Canvas 
Offset , Spacing :> Configurations of the Rectangles in Canvas
SORTING :> Indicator if the program is sorting or not
"""
Algorithms = ["Bubble Sort","Insertion Sort","Selection Sort","Quick Sort","Merge Sort"]
Canvas_Height = 720
Canvas_Width = 975
offset = 13
spacing = 7
SORTING = False
data = []
thr = threading.Thread(target=None)

"""
Algorithms
Bubble Sort
Selection Sort
Insertion Sort
Quick Sort
Merge Sort
"""
# Bubble Sort
def Bubble_Sort(iterable,ms,callback):
    global SORTING
    n = len(iterable)
    SORTING = True
    for i in range(n-1):
        for j in range(-1+n-i):
            if iterable[j]> iterable[j+1]:
                iterable[j],iterable[j+1] = iterable[j+1],iterable[j]
                colorarr = ["coral"]*len(iterable)
                colorarr[j] = 'lightblue'; colorarr[j+1] = 'cyan'
                callback(iterable,colorarr)
                time.sleep(ms)
            
            if not SORTING:
                return
    colorarr = ["coral"]*len(iterable)
    callback(iterable,colorarr)
    Sort()

# Selection Sort
def Selection_Sort(iterable,ms,callback):
    global SORTING
    SORTING = True
    n = len(iterable)
    for i in range(n):
        m = max(iterable) + 1
        for j in range(i,n):
                if iterable[j]<m:
                    m = iterable[j]
                    ind = j
        if iterable[i]!=iterable[ind]:
            iterable[i],iterable[ind] = iterable[ind],iterable[i]
            colorarr = ["coral"]*len(iterable)
            colorarr[i] = 'lightblue'; colorarr[ind] = 'cyan'
            callback(iterable,colorarr)
            time.sleep(ms)
        if not SORTING:
            return
    colorarr = ["coral"]*len(iterable)
    callback(iterable,colorarr)
    Sort()

# Insertion Sort
def Insertion_Sort(iterable,ms,callback):
    global SORTING
    SORTING = True
    for i in range(1,len(iterable)):
        cur = iterable[i]
        j = i-1
        while j>=0 and cur < iterable[j]:
            iterable[j+1] = iterable[j]
            j-=1
            colorarr = ["coral"]*len(iterable)
            colorarr[i] = 'lightblue'; colorarr[j+1] = 'cyan'
            callback(iterable,colorarr)
            time.sleep(ms)
            if not SORTING:
                return
            
        iterable[j+1] = cur
    colorarr = ["coral"]*len(iterable)
    callback(iterable,colorarr)
    Sort()

# Quick Sort 
def Partition(iterable,head,tail,callback,ms):
    border = head
    pivot = iterable[tail]
    
    colorArr = getColorArray_qs(len(iterable),head,tail,border,border)
    callback(iterable,colorArr)
    time.sleep(ms)
    
    for j in range(head,tail):
        if iterable[j]<pivot:
            
            colorArr = getColorArray_qs(len(iterable),head,tail,border,j,True)
            callback(iterable,colorArr)
            time.sleep(ms)
            if not SORTING:
                return 
            iterable[border] , iterable[j] = iterable[j],iterable[border]
            border+=1
            
    # Swap pivot with border value
    colorArr = getColorArray_qs(len(iterable),head,tail,border,tail,True)
    callback(iterable,colorArr)
    time.sleep(ms)
    
    iterable[border],iterable[tail] = iterable[tail],iterable[border]
    return border

def Quick_Sort(iterable,head,tail,callback,ms):
    global SORTING
    SORTING = True
    if head<tail and SORTING:
        partitionIdx = Partition(iterable,head,tail,callback,ms)
        # Left Partition
        Quick_Sort(iterable,head,partitionIdx-1,callback,ms)
        # Right Partition
        Quick_Sort(iterable,partitionIdx+1,tail,callback,ms)
    
def getColorArray_qs(iterableLength,head,tail,border,crntidx,isSwapping = False):
    colorArray = []
    for i in range(iterableLength):
        if i>=head and i<=tail:
            colorArray.append("coral")
        else:
            colorArray.append("lightcoral")
        if i==tail:
            colorArray[i] = 'lightblue'
        elif i==border: 
            colorArray[i] = "blue"
        elif i == crntidx:
            colorArray[i] = 'cyan'
    
        if isSwapping:
            if i==border or i== crntidx:
                colorArray[i] = 'green'
    return colorArray

# Merge Sort
def merge_sort(iterable, callback, timeTick):
    merge_sort_alg(iterable,0, len(iterable)-1, callback, timeTick)
    Sort()

def merge_sort_alg(iterable, left, right, callback, timeTick):
    if left < right:
        middle = (left + right) // 2
        merge_sort_alg(iterable, left, middle, callback, timeTick)
        merge_sort_alg(iterable, middle+1, right, callback, timeTick)
        merge(iterable, left, middle, right, callback, timeTick)

def merge(iterable, left, middle, right, callback, timeTick):
    callback(iterable, getColorArray(len(iterable), left, middle, right))
    time.sleep(timeTick)

    leftPart = iterable[left:middle+1]
    rightPart = iterable[middle+1: right+1]

    leftIdx = rightIdx = 0

    for iterableIdx in range(left, right+1):
        if leftIdx < len(leftPart) and rightIdx < len(rightPart):
            if leftPart[leftIdx] <= rightPart[rightIdx]:
                iterable[iterableIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                iterable[iterableIdx] = rightPart[rightIdx]
                rightIdx += 1
        
        elif leftIdx < len(leftPart):
            iterable[iterableIdx] = leftPart[leftIdx]
            leftIdx += 1
        else:
            iterable[iterableIdx] = rightPart[rightIdx]
            rightIdx += 1
    
    callback(iterable, ["green" if x >= left and x <= right else "coral" for x in range(len(iterable))])
    time.sleep(timeTick)

def getColorArray(leght, left, middle, right):
    colorArray = []

    for i in range(leght):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("cyan")
            else:
                colorArray.append("lightblue")
        else:
            colorArray.append("coral")

    return colorArray

"""
Functions:
Create UI :> Function to create the gui of the visualizer
Generate :> Generates a random array of length {columns} from the gui
with a max element of {max} from the gui and a min element of {min} from the gui
Visualize :> visualizes a selected algorithm while sorting the data
Sort :> sorts the data in an ascending order and displays it
Descending Sort :> Sorts the data in a descending order and displays it
"""
    
def Generate():
    terminate()
    # Referencing Global Variables
    global data
    global colorarr
    
    # Generating random data
    Min = getMinValue();Max = getMaxValue()
    cols = getColsCount()
    data = list(np.ceil((Max-Min)*np.random.rand(cols) + Min))
    colorarr = ['coral']*cols
    return draw_data(data,colorarr)

def draw_data(data,colorarr):
    Canvas.delete("all")
    # Scalable Column width 
    x_width = Canvas_Width/(len(data)+1)
    # Drawing the Data
    normalized_data = [i/max(data) for i in data]
    for i,Height in enumerate(normalized_data):
        # Top Left
        x0 = i * x_width + offset + spacing
        y0 = Canvas_Height - Height * 700
        
        # Bottom Right
        x1 = (i+1) * x_width + offset
        y1 = Canvas_Height
        
        Canvas.create_rectangle(x0,y0,x1,y1,fill=colorarr[i])
        Canvas.create_text(x0,y0,anchor=tk.SW,text=str(data[i]))
    # to prevent the time module from freezing the window
    Master.update_idletasks()
    

def Visualize():
    # Referencing global variables
    global thr
    
    terminate()
    
    algo = GetSelectedAlgorithm()
    if algo=='Bubble Sort':
        thr = threading.Thread(target = Bubble_Sort, args = (data,float(Speed.get()),draw_data))
        thr.start()
    elif algo=='Selection Sort':
        thr = threading.Thread(target = Selection_Sort, args = (data,float(Speed.get()),draw_data))
        thr.start()        
    elif algo=="Insertion Sort":
        thr = threading.Thread(target=Insertion_Sort, args = (data,float(Speed.get()),draw_data))
        thr.start()
    elif algo=="Quick Sort":
        thr =  threading.Thread(target=Quick_Sort,args=(data, 0,len(data)-1,draw_data, float(Speed.get())))
        thr.start()
    elif algo=="Merge Sort":
        thr =  threading.Thread(target=merge_sort,args=(data, draw_data,float(Speed.get())))
        thr.start()

def Descendingsort():
    terminate()
    # Referencing Global Variables
    global data
    data.sort(reverse=True)
    return draw_data(data,['coral']*getColsCount())

def Sort():
    terminate()
    # Referencing Global Variables
    global data
    data = sorted(data)
    return draw_data(data,['coral']*getColsCount())

def terminate():
    # Referencing Global Variables
    global SORTING
    global thr

    del thr
    thr = threading.Thread(target=None)
    if SORTING:
        SORTING = False

def GetSelectedAlgorithm():
    """ Returns the Selected Algorithm """
    return AlgorithmSelected.get()
    
def getMaxValue():
    """ Function to get the Max Value from Entry """
    return int(MaxVal.get())

def getMinValue():
    """ Function to get the Min Value from Entry """
    return int(MinVal.get())

def getColsCount():
    """ Function to get the Count of Columns Value from Entry """
    return int(Columns.get())

def Create_UI(root):
    # Referencing global Variables
    global AlgorithmSelected
    global Canvas
    global MaxVal
    global MinVal
    global Columns
    global Speed
    global Master 
    
    # Root Configuration
    Master = root
    Master.title("Sorting Algorithms Visualizer")
    Master.geometry("1300x800")
    Master.resizable(False,False)
    Master.config(bg='#f0f0f0')
    # Canvas for holding Data
    Canvas = tk.Canvas(Master,bg='white')
    Canvas.place(relx=0.03,rely=0.05,relheight=0.9,relwidth=0.75)        
    # Main Frame for configuration of the Visualizer
    ConfigFrame = tk.Frame(Master,bg='lightgray',bd=3)
    ConfigFrame.place(relx=0.81,rely=0.05,relheight=0.9,relwidth=0.16)        
    # Main Label
    tk.Label(ConfigFrame,text="Sorting Algorithms\nVisualizer",width=100,height=3
             ,font=('helveta',16),fg='#0f0f0f').pack()
    # Main Buttons
    generate = tk.Button(ConfigFrame,text='Generate',font=("helveta",16)
                                ,height=1,width=100,command=Generate)
    descending = tk.Button(ConfigFrame,text='Descending',font=("helveta",16)
                                ,height=1,width=100,command=Descendingsort)
    visualize = tk.Button(ConfigFrame,text='Visualize',font=("helveta",16)
                                 ,height=1,width=100,command=Visualize)
    sort = tk.Button(ConfigFrame,text='Instant Sort',font=("helveta",16)
                                 ,height=1,width=100,command=Sort)
    generate.pack()
    descending.pack()
    visualize.pack()
    sort.pack()
    
    # Values Label
    # Min, Max, Column count, Speed Scales
    tk.Label(ConfigFrame,text="Values",font=("Helveta",16),height=2,width=100).pack()
    tk.Label(ConfigFrame,text="10-1000",width=100,font=("Helveta",12)).pack()
    MinVal = tk.StringVar();MinVal.set("10")
    Min_Scale = tk.Scale(ConfigFrame,variable = MinVal,from_=10,to=100,length=200,digits=2,resolution=0.2,
                            orient = tk.HORIZONTAL)
    Min_Scale.pack()
    MaxVal = tk.StringVar();MaxVal.set("1000")
    Max_Scale = tk.Scale(ConfigFrame,variable = MaxVal,from_=500,to=1000,length=200,digits=2,resolution=0.2,
                            orient = tk.HORIZONTAL)
    Max_Scale.pack()
    tk.Label(ConfigFrame,text="Count of Columns",width=100,font=("Helveta",18)).pack()
    Columns = tk.StringVar();Columns.set("15")
    Cols_Scale = tk.Scale(ConfigFrame,variable = Columns,from_=5,to=49,length=200,digits=2,resolution=0.2,
                            orient = tk.HORIZONTAL)
    Cols_Scale.pack()
    Speed = tk.StringVar()
    Scale = tk.Scale(ConfigFrame,variable = Speed,from_=0.05,to=1.0,length=200,digits=3,resolution=0.05,
                            orient = tk.HORIZONTAL,label='Speed of Visualization')
    Scale.pack()
    # Algorithms Drop Box
    tk.Label(ConfigFrame,text="Algorithm",font=("Helveta",14),height=1,width=100).pack()
    AlgorithmSelected = tk.StringVar()
    AlgorithmSelected.set("Bubble Sort")
    OptionMenu = tk.OptionMenu(ConfigFrame,AlgorithmSelected,*Algorithms)
    OptionMenu["width"] = 100;OptionMenu["height"] = 1
    OptionMenu["font"] = ("Helveta",15);OptionMenu["fg"] = 'darkblue'
    OptionMenu.pack()

def main():
    root = tk.Tk()
    Create_UI(root)
    root.mainloop()

if __name__=='__main__':
    main()
    
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    