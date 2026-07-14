# 1. != FUNCTION
# 2. @ = GLOBAL VARIABLES
# 3. # = BUTTON
# 4. $ = LABEL
# 5. [] = FRAME
# 6. € = COMMBO BOX
# 7. % = PROGRESS BAR

from tkinter import*
import ttkbootstrap as ttkb
import tkinter as tk
from ttkbootstrap.constants import*
from tkinter import messagebox
import json

gyroscope_app=ttkb.Window(themename="superhero")
gyroscope_app.title("GYRESCOPE_APP")
gyroscope_app.geometry("1080x700")
gyroscope_app.resizable(False,False)

gyroscope_app.grid_columnconfigure(0, weight=1)
gyroscope_app.grid_columnconfigure(1, weight=1)

gyroscope_app.grid_rowconfigure(2, weight=0)
gyroscope_app.grid_rowconfigure(3, weight=0)

gyroscope_app_main_lable_frame=ttkb.Frame(width=300,height=50,relief=tk.SOLID,style='info.Outline.TButton')#----------------------------------------------------------------------------[] GYROSCOPE MAIN LABEL FRAME
gyroscope_app_main_lable_frame.grid_propagate(False)
gyroscope_app_main_lable_frame.grid(row=0,columnspan=2,pady=20)

gyroscope_app_main_lable=ttkb.Label(gyroscope_app_main_lable_frame,text='GYROSCOPE__GUI', font=('Helvetica',10,'bold'),bootstyle='')
gyroscope_app_main_lable.grid(padx=(75),pady=(15))

meters_frame = ttkb.Frame(width=290,height=540,relief=tk.SOLID,style='danger.Outline.Tbutton')
meters_frame.grid_propagate(False)
meters_frame.grid(row=1,column=0,padx=(20,0),pady=(10,0),sticky='nw')



rpm_value=tk.IntVar()

rpm_lable1=ttkb.Label(meters_frame,text='RPM METER__', font=('Helvetica',10),style='warning.Outline.TButton')
rpm_lable1.grid(row=0,column=0,padx=(20,0),pady=(20,0),sticky='wn')

rpm_meter=ttkb.Meter(meters_frame,
    metersize=150,
    amountmin=0,
    amounttotal=100, 
    amountused=0,
    meterthickness=10,
    subtext="rpm",
    subtextfont=("Helvetica",10,'bold'),
    subtextstyle="danger",
    arcrange=180,
    arcoffset=180,
    wedgesize=5,
    bootstyle='danger',
    interactive=True,
    
)
rpm_meter.grid(row=1,column=0,padx=(60,0),pady=(20,0),sticky='nw')

angle_meter_value=tk.IntVar()

angle_meter_lable=ttkb.Label(meters_frame,text='ANGLE METER__', font=('Helvetica',10),style='warning.Outline.TButton')
angle_meter_lable.grid(row=2,column=0,padx=(20,0),pady=(20,0),sticky='wn')

angle_meter= ttkb.Meter(meters_frame,
    metersize=150,
    amountmin= -5,
    amounttotal=+5,
    amountused=0,
    meterthickness=10,
    subtext="Angle",
    subtextfont=("Helvetica",10,'bold'),
    subtextstyle="success",
    arcrange=180,
    arcoffset=180,
    wedgesize=5,
    interactive=True,
    bootstyle='success'
)
angle_meter.grid(row=3,column=0,padx=(60,0),pady=(20,0),sticky='nw')

weight_frame = ttkb.Frame(width=650,height=80,relief=tk.SOLID)#----------------------------------------------------------------------------------------------------[] WEIGHT INFO FRAME
weight_frame .grid_propagate(False)
weight_frame .grid(row=1,column=1,pady=(10,0),sticky='wn')

weight_lable = ttkb.Label(weight_frame,text='<> WEIGHT (max:50kg) __',font=('Helvetica',10))#----------------------------------------------------------------------------$ WEIGHT LABEL
weight_lable.grid(row=0,column=0,padx=(10,0),pady=(30,0),sticky='wn')

weigth_value = tk.StringVar()
weigth_value.set('0')

weight_entybox = ttkb.Entry(weight_frame,bootstyle="danger",textvariable=weigth_value,width=10,justify='center')#---------------------------------------------WEIGHT ENTERING ENTRY BOX
weight_entybox.grid(row=0,column=1,padx=(40,0),pady=(20,0),sticky='wn')

def weight_value_check():
   
    try:
        value2 = int(weigth_value.get())

        if value2 > 0:
            
            if int(weigth_value.get()) <= 50:
                weight_entybox.config(state='disabled')
                weight_button.config(state='disabled')
                
            elif int(weigth_value.get()) > 50:
                    messagebox.showwarning('WARNING!','You have entered an overweight value.'
                                        '\n                        🫤❗'
                                        ' \n Please enter a value less than 50 kg.'
                                        '\n                        🙂')
                    weight_entybox.delete(0, tk.END) 

        else:
            messagebox.showerror('ERROR!','Weight cannot be 0 .'
                                        '\n           🫤❗')
            weight_entybox.delete(0, tk.END)

    except ValueError:
        messagebox.showerror('ERROR❗','Invalid input❗ Please enter numbers only.(1234 ✅)')
        weight_entybox.delete(0,tk.END)


weight_button = ttkb.Button(weight_frame,text='Enter',command=weight_value_check,style='info.Outline.TButton',width=10)#--------------------------------------------------------------# WEIGHT SET BUTTON
weight_button.grid(row=0,column=2,padx=(40,0),pady=(20,0),sticky='wn')

def weight_reset():
    
     weight_entybox.config(state='normal')
     weight_button.config(state='normal')
     weight_entybox.delete(0,tk.END)

weight_button_reset = ttkb.Button(weight_frame,text='Reset',command=weight_reset,style='success.Outline.TButton',width=10)#------------------------------------------------------------- # WEIGHT RESET BUTTON
weight_button_reset.grid(row=0,column=3,padx=(40,0),pady=(20,0),sticky='wn')



box_frame=ttkb.Frame(width=650,height=280,relief=tk.SOLID)#------------------------------------------------------------------------------ [] FRAME ADDING RPM,VOL.WATER,PUMP RATE,TIME FRAME
box_frame.grid_propagate(False)
box_frame.grid(row=1,column=1,pady=110,sticky='wn')



rpm_lable2 = ttkb.Label(box_frame,text='<>rpm Value__',font=('Helvetica',10))#------------------------------------------------------------------------------------------------$ RPM LABEL
rpm_lable2.grid(row=0,padx=(10,0),pady=(20,0),sticky='w')

water_volume_lable = ttkb.Label(box_frame,text='<>Vol. Water__',font=('Helvetica',10,))#-------------------------------------------------------------------------------$ WATER VOLUME LABEL
water_volume_lable.grid(row=1,padx=(10,0),pady=(20,0),sticky='w')

pump_rate_lable = ttkb.Label(box_frame,text='<>Pump rate__',font=('Helvetica',10))#------------------------------------------------------------------------------------$ PUMP RATE LABEL
pump_rate_lable.grid(row=2,padx=(10,0),pady=(20,0),sticky='w')


pump_rate_value = tk.IntVar()#---------------------------------------------------------------------------------------------------------------------------------TEXT VARIABLE FOR COMBOBOX


#file handling------------------------------------------------------------------------------------------------

pumpRate_newValues ='pump_rate_newValues.json'

try:
    with open(pumpRate_newValues,'r') as PRNV:
        PumpRateNewValues_list = json.load(PRNV)

except FileNotFoundError:
    PumpRateNewValues_list = []   
#----------------------------------------------------------------------------------------------------------------"""

pump_rate_combobox = ttkb.Combobox(box_frame,values=PumpRateNewValues_list,width=10,justify='center',textvariable=pump_rate_value,bootstyle='info')#------------------€ PUMP RATE COMBO BOX
pump_rate_combobox.grid(row=2,column=1,padx=(10,0),pady=(10,0),sticky='e')


def pump_rate_select():
    
    try:
        
        value = int(pump_rate_combobox.get())
        
        if value > 0:   
            
            pump_rate_combobox.config(state='disabled')
            print(int(pump_rate_value.get()))
        
        else:
            
            pump_rate_combobox.config(state='normal')
            messagebox.showerror('ERROR!','Pump Rate cannot be 0 .'
                                        '\n           🫤❗')
    
    except ValueError:
        
        messagebox.showerror('ERROR❗','            Invalid input🫤❗' 
                                '\nPlease enter numbers only.(1234 ✅)')
        pump_rate_combobox.delete(0,tk.END)
   
pump_rate_set_button = ttkb.Button(box_frame,text='Set',command=pump_rate_select,style='warning.Outline.TButton',width=10)#----------------------------------------# PUMP RATE SET BUTTON
pump_rate_set_button.grid(row=2,column=2,padx=(10,0),pady=(10,0),sticky='e')

def add_new_pump_rate_enter_button_select():#---------------------------------------------------------------------------------------------------------! ADD NEW PUPM RATE BUTTON FUNCTION
    
    try:
        value = int(pump_rate_combobox.get())

        if value > 0:
            if value not in PumpRateNewValues_list:
                PumpRateNewValues_list.append(value)

                    
                with open(pumpRate_newValues, 'w') as PRNV:
                    json.dump(PumpRateNewValues_list, PRNV)

                
                pump_rate_combobox['values'] = PumpRateNewValues_list

            pump_rate_combobox.config(state='normal')
            pump_rate_combobox.delete(0,tk.END)

        else:
                pump_rate_combobox.config(state='normal')
                messagebox.showerror('ERROR!','Pump Rate cannot be 0 .'
                                        '\n           🫤❗')
                
    except ValueError:
        messagebox.showerror('ERROR❗','            Invalid input🫤❗' 
                                '\nPlease enter numbers only.(1234 ✅)')
        pump_rate_combobox.delete(0,tk.END)


new_pump_rate_add_button = ttkb.Button(box_frame,text='+Add',command=add_new_pump_rate_enter_button_select,style='success.Outline.TButton',width=10)#----------# NEW PUMP RATE ADD BUTTON 
new_pump_rate_add_button.grid(row=2,column=3,padx=(10,0),pady=(10,0),sticky='e')

pump_time_lable = ttkb.Label(box_frame,text='<>Time__',font=('Helvetica',10))#----------------------------------------------------------------------------------------------$ TIME LABLE
pump_time_lable.grid(row=3,padx=(10,0),pady=(20,0),sticky='w')

#time code -------------------------------------------------------------------------------------------------------------------------------

time1 =tk.IntVar(value=0)
time2 = tk.IntVar(value=10)

set_minute = tk.StringVar(value=str(time1.get()))
set_second = tk.StringVar(value=str(time2.get()))

timer_id = None #-----------------------------------------------------------------------------------------------------------------------------------------------------------GLOBAL VALUES
temp = 0
addition1 = 0   
value1 = 0
progress_bar_percentage_lable_variable = 0
remaining_time = 0
start_ardiuno =0
countdount_ardiuno =0
pause_ardiuno =0
resume_ardiuno =0
stop_ardiuno =0

progress = ttkb.Progressbar(box_frame,length=150, maximum=100)#-------------------------------------------------------------------------------------% WATER PUMPING PERCENTAGE PROGRESS BAR
progress.grid(row=4,padx=(20,0),pady=(30,0),sticky='w')

value = tk.IntVar()

def start_pump_water(value):#---------------------------------------------------------------------------------------------------------------------------! PUMP/EMPTY START BUTTON FUNCTION
   
    global temp, addition1,value1,remaining_time,start_ardiuno

    value1 = value
    start_ardiuno =1

    print(start_ardiuno)

    if value1 == 1:
        progress.config(bootstyle='success-striped')
        empty_pause_button.config(state='disabled')
        empty_resume_button.config(state='disabled')
        
    
    elif value1 == 2:
       progress.config(bootstyle='danger-striped') 
       pump_pause_button.config(state='disabled')
       pump_resume_button.config(state='disabled')
    
    stop_pump_water()  

    try:
        temp =  int(set_minute.get()) * 60 + int(set_second.get())
        
        if temp <= 0:
            print("Enter time greater than 0")
            return
        
        addition1 = temp  
        remaining_time = temp
        
        progress['value'] = 0  
        countdown()
       
    except:
        print("Enter valid numbers")


    
def countdown():#-----------------------------------------------------------------------------------------------------------------------------------! PUMP/EMPTY START COUNTDOWN FUNCTION
    
    global temp, timer_id  ,value1  ,progress_bar_percentage_lable_variable,remaining_time,countdount_ardiuno
    
    
    if temp < 0:
        return
    mins = set_minute
    secs = set_second
    mins, secs = divmod(temp, 60)
    
    if addition1 > 0:
        
        progress['value'] = (1 - temp / addition1) * 100
        progress_bar_percentage_lable_variable = int(progress['value'])
        progress_bar_percentage_label.config( text=f'{progress_bar_percentage_lable_variable}%')
        tube_state_not_sealed()
        
        if value1 == 1:
            empty_button.config(state='disabled')
            pump_button.config(state='disabled')
           
            if progress['value'] == 100 :

                countdount_ardiuno = "full"
                print(str(countdount_ardiuno))

                pump_button.config(state='disabled')           
                empty_button.config(state='normal')

                pump_pause_button.config(state='disabled')
                pump_resume_button.config(state='disabled')

                empty_pause_button.config(state='normal')
                empty_resume_button.config(state='normal')

                messagebox.showinfo('Done','The tube was successfully filled.'
                                        '\n                 ✅')
                
                progress['value'] = 0
                value1 = 0
                

        elif value1 == 2:

            empty_button.config(state='disabled')
            pump_button.config(state='disabled')
            
            if progress['value'] == 100 :

                countdount_ardiuno = "full"
                print(str(countdount_ardiuno))

                empty_pause_button.config(state='disabled')
                empty_resume_button.config(state='disabled')

                messagebox.showinfo('Done','Tube successfully emptied.'
                                        '\n                 ✅')
                progress['value'] = 0
                

    remaining_time = temp
     
    temp -= 1

    timer_id = gyroscope_app.after(1000, countdown)
    
def pause_button():#------------------------------------------------------------------------------------------------------------------------------------! PUMP/EMPTY PAUSE BUTTON FUNCTION

    global timer_id,remaining_time,temp,pause_ardiuno,value1

    if value1 in (1,2):
        pause_ardiuno =1

        print(pause_ardiuno)

        if time1:
            gyroscope_app.after_cancel(timer_id)
            timer_id = None

        remaining_time = temp

def resume_button():#-----------------------------------------------------------------------------------------------------------------------------------! PUMP/EMPTY RESUME BUTTON FUNCTION

    global remaining_time,temp,resume_ardiuno,value1

    if value1 in (1,2):
        resume_ardiuno =1  
        remaining_time = temp

        print(resume_ardiuno)

        countdown()
    

def stop_pump_water():#-----------------------------------------------------------------------------------------------------------------------------------! PUMP/EMPTY STOP BUTTON FUNCTION

    global timer_id,stop_ardiuno

    stop_ardiuno =1

    print(stop_ardiuno)

    if timer_id:
        gyroscope_app.after_cancel(timer_id)
        timer_id = None

    pump_button.config(state='normal')  
    empty_button.config(state='normal') 
    
#-----------------------------------------------------------------------------------------------------------------------------------------------------
progress_bar_percentage_label = ttkb.Label(box_frame,text=f'{progress_bar_percentage_lable_variable}%',style='warning.Outline.TButton')#----------$ WATER PUMPING/EMPTY PERCENTAGE LABEL
progress_bar_percentage_label.grid(row=4,column=0,padx=(180,0),pady=(10,0),sticky='n')

pump_button = ttkb.Button(box_frame,text='🔼Pump',command=lambda:start_pump_water(1),style='info.Outline.TButton',width=10)#---------------------------------------# WATER PUMP BUTTON
pump_button.grid(row=4,column=1,padx=(20,0),pady=(10,0),sticky='w')

pump_pause_button = ttkb.Button(box_frame,text='⏸️pause',command =pause_button,style='warning.Outline.TButton',width=10)#--------------------------------------# WATER PUMP PAUSE BUTTON
pump_pause_button.grid(row=4,column=2,padx=(20,0),pady=(10,0),sticky='w')

pump_resume_button = ttkb.Button(box_frame,text='⏯️resume',command =resume_button,style='success.Outline.TButton',width=10)#----------------------------------# WATER PUMP RESUME BUTTON
pump_resume_button.grid(row=4,column=3,padx=(20,0),pady=(10,0),sticky='w')

empty_button = ttkb.Button(box_frame,text='🔽Empty',command=lambda:start_pump_water(2),style='danger.Outline.TButton',width=10)#------------------------------------# WATER EMPTY BUTTON
empty_button.grid(row=5,column=1,padx=(20,0),pady=(10,0),sticky='e')

empty_pause_button = ttkb.Button(box_frame,text='⏸️pause',command =pause_button,style='warning.Outline.TButton',width=10)#-------------------------------------# WATER EMPTY PAUSE BUTTON
empty_pause_button.grid(row=5,column=2,padx=(20,0),pady=(10,0),sticky='w')

empty_resume_button = ttkb.Button(box_frame,text='⏯️resume',command =resume_button,style='success.Outline.TButton',width=10)#---------------------------------# WATER EMPTY RESUME BUTTON
empty_resume_button.grid(row=5,column=3,padx=(20,0),pady=(10,0),sticky='w')


tube_state_frame = ttkb.Frame(width=650,height=120,relief=tk.SOLID)#----------------------------------------------------------------------------[] TUBE STATE INFO FRAME
tube_state_frame.grid_propagate(False)
tube_state_frame.grid(row=1,column=1,pady=410,sticky='wn')


tube_lable = ttkb.Label(tube_state_frame,text='<> TUBE STATE__', font=('Helvetica',10))
tube_lable.grid(row=0,column=0,padx=(10,0),pady=(30,0),sticky='wn')

tube_state_canvas = ttkb.Canvas(tube_state_frame,width=50, height=50, bg="#d5d5e7", highlightthickness=0)
tube_state_canvas.grid(row=0,column=1,padx=(100,0),pady=(10,0),sticky='wn')

circle = tube_state_canvas.create_oval(20, 20, 40, 40, fill="red", outline='white',width=2)
tube_state_canvas.itemconfig(circle, fill="#edf5f1") 

tube_state_label1 = ttkb.Label(tube_state_frame,text ='',width='15',style='info.Outline.TButton',justify='center')
tube_state_label1.grid(row=0,column=2,padx=(150,0),pady=(20,0),sticky='wn')


def tube_state_seal():
    tube_state_canvas.itemconfig(circle, fill="#53d996") 
    tube_state_label1.config(text='SEALED')
    tube_state_label1.config(style='success.Outline.TButton')

def tube_state_not_sealed():
    tube_state_canvas.itemconfig(circle, fill="#d95c53")
    tube_state_label1.config(style='danger.Outline.TButton') 
    tube_state_label1.config(text='NOT SEALED 🫤')

main_start_button = ttkb.Button(tube_state_frame,text='▶️START',width=10,style='success.Outline.TButton')
main_start_button.grid(row=1,column=1,padx=(20,0),pady=(10,10),sticky='nw')

main_stop_button = ttkb.Button(tube_state_frame,text='⏸️STOP',width=10,style='danger.Outline.TButton')
main_stop_button.grid(row=1,column=2,padx=(10,0),pady=(10,10),sticky='nw')

gyroscope_app.mainloop()