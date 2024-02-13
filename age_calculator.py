import tkinter
from datetime import date
#create an instance of tkinter window
root=tkinter.Tk()
#title of the window
root.title('AGE CALCULATOR')
#Dimensions of window
root.geometry('500x500')
root.resizable(0,0)
#icon of the window
#root.iconbitmap('c.ico') 

# Set background and font colors
bg_color = '#EDF2F4'
font_color = '#2B2D42'

def display():
   b = input.get()
   d1, m1, y1 = map(int, b.split('-'))
   input.delete(0, tkinter.END)
   today = date.today()
   d2, m2, y2 = today.day, today.month, today.year
   leap_years = 0

   # Count the number of leap years between the given date and today's date
   for year in range(y1, y2):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap_years += 1
    
    # Calculate the number of days, months, and years between the given date and today's date
    days = d2 - d1
    months = m2 - m1
    years = y2 - y1
        
    # Adjust the number of days and months based on leap years and negative differences
    if (months < 0) or (months == 0 and days < 0):
        years -= 1
        months += 12
    if days < 0:
            months -= 1
            if m1 in [1, 3, 5, 7, 8, 10, 12]:
                days += 30
            elif m1 == 2:
                if y1 % 4 == 0 and (y1 % 100 != 0 or y1 % 400 == 0):
                    days += 29
                else:
                    days += 28
            else:
                days += 31
        
    result = f"{years} years, {months} months, and {days} days old"

    # Delete any existing labels in frame_2
    for widget in frame_2.winfo_children():
        widget.destroy()   
    
    # Create a label to display the result
    output_label = tkinter.Label(frame_2, text=result, font=('Arial', 20), bg=bg_color, fg=font_color)
    output_label.pack(pady=10)
    
    # Delete the input data after it is printed
    
    def delete_label():
        output_label.destroy()
    
    # Destroy the output after 4 seconds
    frame_2.after(4000, delete_label)


#define label for text typing
t=tkinter.Label(root,text="ENTER THE DATE OF BIRTH\n\n(DD-MM-YYYY)", font=('Arial', 15, 'bold'),bg=bg_color, fg=font_color)
t.pack(pady=20)

#defining Frames
frame_1=tkinter.Frame(root,width=500, height=100,  bg=bg_color)
frame_1.pack(padx=10,pady=10)

#defining Entry widget
input=tkinter.Entry(frame_1, width=10, font=('Arial', 24), borderwidth=5, fg=font_color, bg='#D9E2EC')
input.grid(row=0,column=0,padx=20,pady=20,ipadx=5,ipady=5)

#define button
submit=tkinter.Button(frame_1,text="SUBMIT",height=2,width=10,border=10,bg='#457B9D', fg='white', font=('Arial', 12, 'bold'),command=display)
submit.grid(row=4,column=0)

#Define frame2
frame_2=tkinter.Frame(root,bg='#F7DC6F',width=500,height=100)
frame_2.pack()
#pack_propogate(0) is used to display output
frame_2.pack_propagate(0)

#run the window
root.mainloop()