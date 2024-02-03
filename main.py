import datetime
import tkinter as tk
from tkinter import ttk


#next:計算+總結

def next_page(): #第二視窗+課表數據整理
    global year
    global start
    for i in range(5):
        for j in range(7):
            class_name[i].append(course[i][j].get())
            if not class_name[i][j] in times:
                times[class_name[i][j]]=1
            else:
                times[class_name[i][j]]+=1
    year = year_combobox.get()
    start = start_entry.get()
    
    window.destroy()

def clear_entry(entry): 
    entry.delete(0, 'end')

def holiday(det): #true 新增 false 刪除
    date = holiday_entry.get()
    date = date[:2]+'/'+date[2:]
    if det:
        holiday_arr.append(date)
    else:
        holiday_arr.remove(date)
    clear_entry(holiday_entry)
    holiday_arr.sort()
    holiday_now.config(text='、'.join(holiday_arr))

def makeup(det): #true 新增 false 刪除
    date = makeup_entry.get()
    date = date[:2]+'/'+date[2:]
    if det:
        makeup_arr.append(date)
        makeup_dic[date] = makeup_what_day_entry.get()[:2]+'/'+makeup_what_day_entry.get()[2:]
    else:
        makeup_arr.remove(date)
        del makeup_dic[date]
    clear_entry(makeup_entry)
    clear_entry(makeup_what_day_entry)
    makeup_arr.sort()
    makeup_now.config(text='、'.join(makeup_arr))

def what_day(s): #星期幾
    a = int(year)
    b = int(s[:2])
    c = int(s[3:])
    if b < int(start[:2]):
        a += 1
    return datetime.date(a, b, c).isoweekday()

#initialize
window = tk.Tk()
window.title('請假天數計數器')
window.geometry('400x500')
window.resizable(False, False)

#Combobox
year_combobox = ttk.Combobox(window, values=['2023','2024','2025','2026','2027'], width=10)

#label
warning = tk.Label(text="警告:請先詳閱read.txt", fg="red")
yearlb = tk.Label(text="年份",height=1,fg="blue")
startlb = tk.Label(text="學期開始時間",height=1, fg="blue")
holidaylb = tk.Label(text="國定假日",height=1, fg="blue")
endlb = tk.Label(text="學期結束時間",height=1, fg="blue")
makeuplb = tk.Label(text="補課日",height=1, fg="blue")
status = tk.Label(text="目前狀態",height=1, fg="gray35")
holiday_status = tk.Label(text="國定假日:",height=1, fg="gray35")
makeup_status = tk.Label(text="補課日:",height=1, fg="gray35")
holiday_now = tk.Label(text="", fg="gray35")
makeup_now = tk.Label(text="", fg="gray35")
makeup_what_day = tk.Label(text="補哪天",height=1, fg="blue")

#entry
start_entry = tk.Entry(width=5)
end_entry = tk.Entry(width=5)
holiday_entry = tk.Entry(width=10)
makeup_entry = tk.Entry(width=10)
makeup_what_day_entry = tk.Entry(width=10)

#button
holiday_addbtn = tk.Button(text="新增", command=lambda: holiday(1))
holiday_delbtn = tk.Button(text="刪除", command=lambda: holiday(0))
makeup_addbtn = tk.Button(text="新增", command=lambda: makeup(1))
makeup_delbtn = tk.Button(text="刪除", command=lambda: makeup(0))
next_button = tk.Button(text="下一步", height=5, width=10 , bg="gray69", command=next_page)

#other
holiday_arr = []
makeup_arr = []
makeup_dic = {} #補哪天 代辦
start = ""
end = ""
year = ""
times = {} #每周幾堂
class_name = [[] for i in range(5)] #all

#curriculum
monlb = tk.Label(text="星期一", width=10, bg="red2")
tuelb = tk.Label(text="星期二", width=10, bg="orange")
wedlb = tk.Label(text="星期三", width=10, bg="lightyellow")
thulb = tk.Label(text="星期四", width=10, bg="lightgreen")
frilb = tk.Label(text="星期五", width=10, bg="lightblue")
numberlb1 = tk.Label(text="1", height=2, bg="khaki")
numberlb2 = tk.Label(text="2", height=2, bg="khaki")
numberlb3 = tk.Label(text="3", height=2, bg="khaki")
numberlb4 = tk.Label(text="4", height=2, bg="khaki")
numberlb5 = tk.Label(text="5", height=2, bg="khaki")
numberlb6 = tk.Label(text="6", height=2, bg="khaki")
numberlb7 = tk.Label(text="7", height=2, bg="khaki")

course = []
for i in range(5):
    day = []
    for j in range(7):
        c = tk.Entry(width=10)
        day.append(c)
    course.append(day)



#position
monlb.grid(row=0, column=1)
tuelb.grid(row=0, column=2)
wedlb.grid(row=0, column=3)
thulb.grid(row=0, column=4)
frilb.grid(row=0, column=5)
numberlb1.grid(row=1, column=0)
numberlb2.grid(row=2, column=0)
numberlb3.grid(row=3, column=0)
numberlb4.grid(row=4, column=0)
numberlb5.grid(row=5, column=0)
numberlb6.grid(row=6, column=0)
numberlb7.grid(row=7, column=0)
warning.place(x=5,y=275)
yearlb.place(x=0,y=300)
year_combobox.place(x=30,y=300)
startlb.place(x=130,y=300)
start_entry.place(x=210,y=300)
endlb.place(x=260,y=300)
end_entry.place(x=340,y=300)
holidaylb.place(x=0,y=330)
holiday_entry.place(x=60,y=330)
makeuplb.place(x=0,y=360)
makeup_entry.place(x=50,y=360)
holiday_addbtn.place(x=140, y=330)
holiday_delbtn.place(x=180, y=330)
makeup_addbtn.place(x=260, y=360)
makeup_delbtn.place(x=300, y=360)
status.place(x=0, y=400)
holiday_status.place(x=0, y=420)
makeup_status.place(x=0, y=440)
holiday_now.place(x=55, y=420)
makeup_now.place(x=45, y=440)
next_button.place(x=310, y=400)
makeup_what_day.place(x=130,y=360)
makeup_what_day_entry.place(x=180,y=360)


for i in range(5):
    for j in range(7):
        course[i][j].grid(row=j+1, column=i+1)




window.mainloop()




#second frame

total = {} #各科請了幾節
period = {} #第幾節請假 整天->[]

def cal():
    for i in period:
        j = period[i]
        d = what_day(i)-1
        if i in makeup_dic:
            d = what_day(makeup_dic[i])-1
        print(i, d)
        if j==[]: #整天
            for s in class_name[d]:
                times[s]-=1
        else:
            for s in j:
                times[class_name[d][s-1]]-=1
    print(total)
    new_window.destroy()

def switch(val):
    for i in check_btn:
        i.deselect()
        if val:
            i.config(state="normal")
        else:
            i.config(state="disabled")

def relocate():
    j = 0
    for i in range(len(period_lb)):
        if(i>=16):
            j=200
        period_lb[i].place(x=0+j,y=170+(i%16)*20)

def add():
    l = []
    for i in check_btn_value:
        if i.get()!=0:
            l.append(str(i.get()))
    date = date_entry.get()
    clear_entry(date_entry)
    date = date[:2]+'/'+date[2:]
    s = ""
    if len(l)==0:
        s = f"{date}整天"
    else:
        s = date+"第"
        s += '、'.join(l)
        s += "節" 
    q = [int(i) for i in l]
    period[date] = q
    period_lb.append(tk.Label(text=s, fg="gray35"))
    relocate()

def delete():
    l = []
    date = del_date_entry.get()
    date = date[:2]+'/'+date[2:]
    clear_entry(del_date_entry)
    period[date] = []
    for i in period_lb:
        a = i.cget("text")[:5]
        if a==date:
            i.config(text="")
            period_lb.remove(i)
    relocate()


#initialize
new_window = tk.Tk()
new_window.title('請假天數計數器')
new_window.geometry('400x500')
new_window.resizable(False, False)


#label
text1 = tk.Label(text="請假日期",height=1, fg="blue")
text2 = tk.Label(text="請假類別",height=1, fg="blue")
text3 = tk.Label(text="刪除日期",height=1, fg="blue")
text4 = tk.Label(text="目前狀態:",height=1, fg="blue")
period_lb = []

#radiobutton
val = 1
whole_day = tk.Radiobutton(text="全天", variable=val, value=1, height=1, command=lambda: switch(0))
whole_day.select()
not_whole_day = tk.Radiobutton(text="特定節數", variable=val, value=0, height=1, command=lambda: switch(1))

#entry
date_entry = tk.Entry(width=8)
del_date_entry = tk.Entry(width=8)

#checkbutton
check_btn_value = [tk.IntVar() for i in range(7)]
check_btn = [tk.Checkbutton(text=f"第{i+1}節課", variable=check_btn_value[i], onvalue=i+1, offvalue=0) for i in range(7)]
switch(0)

#button
addbtn = tk.Button(text="新增", height=1, width=5 , bg="gray69", command=lambda: add())
delbtn = tk.Button(text="刪除", height=1, width=5 , bg="gray69",command=lambda: delete())
finalize =  tk.Button(text="計算", height=5, width=10 , bg="gray69", command=cal)


#position
text1.place(x=0, y=0)
date_entry.place(x=60,y=0)
text2.place(x=130, y=0)
whole_day.place(x=180,y=0)
not_whole_day.place(x=230,y=0)
for i in range(4):
    check_btn[i].place(x=0+i*80,y=20)
for i in range(4,7):
    check_btn[i].place(x=0+(i-4)*80,y=40)
addbtn.place(x=250, y=60)
text3.place(x=0, y=110)
del_date_entry.place(x=60,y=110)
delbtn.place(x=140, y=110)
text4.place(x=0, y=150)
finalize.place(x=310, y=400)


#caculate


for i in times: #總堂數
    times[i]*=18

print(times)

for i in holiday_arr: #扣除國定假日
    d = what_day(i)-1
    for j in class_name[d]:
        times[j]-=1

print(times)

for i in times: #可請總堂數
    times[i]//=3


new_window.mainloop()


#initialize
final = tk.Tk()
final.title('請假天數計數器')
final.geometry('400x500')
final.resizable(False, False)


result = []
for i in times:
    a = tk.Label(text=f"{i}:尚可請{times[i]}節")
    result.append(a)
for i in result:
    i.pack()

final.mainloop()
