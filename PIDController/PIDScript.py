import sqlite3 as sq
from guizero import App, Text, TextBox, PushButton, Window, Picture, ListBox
import subprocess
import minimalmodbus
import time
import RPi.GPIO as GPIO

# Connect to database
conn = sq.connect('custom_profiles.db')
c = conn.cursor()


# This function saves profiles into the database.
def set():
    c.execute('''CREATE TABLE if not exists new_profiles
              ( Material_Type text, Seconds real, Barrel_Temp real, Nozzle_Temp real, First_Name text)''')
    columnvalues = material_type.value, time_custom_two.value, barrel_custom_two.value, nozzle_custom_two.value, first_name.value
    # Insert a row of data
    c.execute("INSERT INTO new_profiles VALUES (?,?,?,?,?)", columnvalues)
    # Save (commit) the changes
    conn.commit()
    get()


# This function shows all profiles within the database.
def get():
    listbox.clear()
    for row in c.execute('SELECT * FROM new_profiles'):
        listbox.insert(1, row)

    # This function deletes profiles from the database.


def delete():
    c.execute(
        "DELETE FROM new_profiles WHERE Material_Type = ? AND Seconds = ? AND Barrel_Temp = ? AND Nozzle_Temp = ? AND First_Name = ?",
        listbox.value)
    # Save (commit) the changes
    conn.commit()
    # Refreshes the listbox
    get()


# This function powers off the Raspberry Pi.
def power_off():
    command = "/usr/bin/sudo /sbin/shutdown now"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)


# This function is for the preset 10 second button.
def timer_func():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)
    GPIO.output(21, GPIO.HIGH)
    seconds = 10
    for i in range(seconds):
        print (str(seconds - 1) + " seconds")
        seconds -= 1
        if seconds == 0:
            # write buzzer register
            print ("time's up!")
            GPIO.output(21, GPIO.LOW)
            time.sleep(2)
            GPIO.output(21, GPIO.HIGH)
        time.sleep(1)

# This function is for the preset 15 second button.
def timer_func_two():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)
    GPIO.output(21, GPIO.HIGH)
    seconds = 15
    for i in range(seconds):
        print (str(seconds - 1) + " seconds")
        seconds -= 1
        if seconds == 0:
            print ("time's up!")
            GPIO.output(21, GPIO.LOW)
        time.sleep(2)
        GPIO.output(21, GPIO.HIGH)
    time.sleep(1)


# This function is for the preset 20 second button.
def timer_func_three():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)
    GPIO.output(21, GPIO.HIGH)
    seconds = 20
    for i in range(seconds):
        print (str(seconds - 1) + " seconds")
        seconds -= 1
        if seconds == 0:
            # write buzzer register
            print ("time's up!")
            GPIO.output(21, GPIO.LOW)
        time.sleep(2)
        GPIO.output(21, GPIO.HIGH)
    time.sleep(1)


# This function is for the preset custom seconds button.
def timer_func_four(x):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)
    GPIO.output(21, GPIO.HIGH)
    seconds = int(float(x))
    for i in range(seconds):
        print (str(seconds - 1) + " seconds")
        seconds -= 1
        if seconds == 0:
            print ("time's up!")
            GPIO.output(21, GPIO.LOW)
        time.sleep(2)
        GPIO.output(21, GPIO.HIGH)
    time.sleep(1)


# This function is for the preset PP material temperatures button.
def PP_temp():
    b_temp.value = "320.0"
    n_temp.value = "350.0"
    plastic_selection.value = "PP"
    barrel_controller.write_register(18177, float(b_temp.value), numberOfDecimals=1, functioncode=6, signed=True)
    nozzle_controller.write_register(18177, float(n_temp.value), numberOfDecimals=1, functioncode=6, signed=True)
    window_two.show(wait=False)


# This function is for the preset LDPE material temperatures button.
def LDPE_temp():
    b_temp.value = "365.0"
    n_temp.value = "385.0"
    plastic_selection.value = "LDPE"
    barrel_controller.write_register(18177, float(b_temp.value), numberOfDecimals=1, functioncode=6, signed=True)
    nozzle_controller.write_register(18177, float(n_temp.value), numberOfDecimals=1, functioncode=6, signed=True)
    window_two.show(wait=False)


# This function is for the preset HDPE material temperatures button.
def HDPE_temp():
    b_temp.value = "380.0"
    n_temp.value = "400.0"
    plastic_selection.value = "HDPE"
    barrel_controller.write_register(18177, float(b_temp.value), numberOfDecimals=1, functioncode=6, signed=True)
    nozzle_controller.write_register(18177, float(n_temp.value), numberOfDecimals=1, functioncode=6, signed=True)
    window_two.show(wait=False)


# This function is for the preset ABS material temperatures button.
def ABS_temp():
    b_temp.value = "395.0"
    n_temp.value = "420.0"
    plastic_selection.value = "ABS"
    barrel_controller.write_register(18177, float(b_temp.value), numberOfDecimals=1, functioncode=6, signed=True)
    nozzle_controller.write_register(18177, float(n_temp.value), numberOfDecimals=1, functioncode=6, signed=True)
    window_two.show(wait=False)


# This function is for the preset PA material temperatures button.
def PA_temp():
    b_temp.value = "480.0"
    n_temp.value = "500.0"
    plastic_selection.value = "PA"
    barrel_controller.write_register(18177, float(b_temp.value), numberOfDecimals=1, functioncode=6, signed=True)
    nozzle_controller.write_register(18177, float(n_temp.value), numberOfDecimals=1, functioncode=6, signed=True)
    window_two.show(wait=False)


# This function is to show the Custom Temperatures window.
def Other_temp():
    window_three.show(wait=False)


# This function is to show the Custom Time window.
def Other_time():
    window_five.show(wait=False)


# This function is to show the custom profiles window.
def customp_window():
    window_six.show(wait=False)
    get()


# This function is to set the values of the custom temperatures from the custom temperatures window.
def other_temp_set():
    barrel_controller.write_register(18177, float(barrel_custom.value), numberOfDecimals=1, functioncode=6, signed=True)
    nozzle_controller.write_register(18177, float(nozzle_custom.value), numberOfDecimals=1, functioncode=6, signed=True)


# This function is to set the values chosen in the custom profiles window.
def custom_profiles_set():
    columnvaluestuple = listbox.value
    columnvalueslist = list(columnvaluestuple)
    columnsarray = []
    for column in columnvalueslist:
        columnsarray.append(column)
    barrel_controller.write_register(18177, float(columnsarray[2]), numberOfDecimals=1, functioncode=6, signed=True)
    nozzle_controller.write_register(18177, float(columnsarray[3]), numberOfDecimals=1, functioncode=6, signed=True)
    timer_func_four(columnsarray[1])


# This function sets the value of the custom time window in seconds.
def other_time_set():
    timer_func_four(time_custom.value)


# These functions increment and decrement the nozzle value in the custom time window.
def t_up_fcn():
    time_custom.value = str(float(time_custom.value) + 1)
def t_down_fcn():
    time_custom.value = str(float(time_custom.value) - 1)


# These functions increment and decrement the barrel value in the custom temperatures window.
def b_up_fcn():
    barrel_custom.value = str(float(barrel_custom.value) + 5.0)
def b_down_fcn():
    barrel_custom.value = str(float(barrel_custom.value) - 5.0)


# These functions increment and decrement the nozzle value in the custom temperatures window.
def n_up_fcn():
    nozzle_custom.value = str(float(barrel_custom.value) + 5.0)
def n_down_fcn():
    nozzle_custom.value = str(float(barrel_custom.value) - 5.0)


# custom profile settings
# These functions increment and decrement the time value in the custom profiles window.
def t_up_fcn_two():
    time_custom_two.value = str(float(time_custom_two.value) + 1)
def t_down_fcn_two():
    time_custom_two.value = str(float(time_custom_two.value) - 1)


# These functions increment and decrement the barrel value in the custom profiles window.
def b_up_fcn_two():
    barrel_custom_two.value = str(float(barrel_custom_two.value) + 5.0)
def b_down_fcn_two():
    barrel_custom_two.value = str(float(barrel_custom_two.value) - 5.0)


# These functions increment and decrement the nozzle value in the custom profiles window.
def n_up_fcn_two():
    nozzle_custom_two.value = str(float(barrel_custom_two.value) + 5.0)
def n_down_fcn_two():
    nozzle_custom_two.value = str(float(barrel_custom_two.value) - 5.0)


#This block of code initializes the minimalmodbus paramaters for specifications on the Ink Injection Molding Machine.
minimalmodbus.BAUDRATE = 9600
minimalmodbus.PARITY = 'N'
minimalmodbus.BYTESIZE = 8
minimalmodbus.STOPBITS = 1
minimalmodbus.TIMEOUT = 0.1
minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True
#Initializing the RS485 adapter.
barrel_controller = minimalmodbus.Instrument('/dev/ttyUSB0', 1, mode='ascii')
nozzle_controller = minimalmodbus.Instrument('/dev/ttyUSB0', 2, mode='ascii')

# This block of code sets up the buttons and their functionality within the main window.
window_one = App(title="Ink Injection Mold Controller", width=1335, height=65, layout="grid")
PP_button = PushButton(window_one, command=PP_temp, text="PP", grid=[13, 0])
LDPE_button = PushButton(window_one, command=LDPE_temp, text="LDPE", grid=[12, 0])
HDPE_button = PushButton(window_one, command=HDPE_temp, text="HDPE", grid=[11, 0])
ABS_button = PushButton(window_one, command=ABS_temp, text="ABS", grid=[10, 0])
PA_button = PushButton(window_one, command=PA_temp, text="PA", grid=[9, 0])
other_button = PushButton(window_one, command=Other_temp, text="Custom Temp", grid=[14, 0])
timer_button = PushButton(window_one, command=timer_func, text="10 Seconds", grid=[15, 0])
timer_button_two = PushButton(window_one, command=timer_func_two, text="15 Seconds", grid=[16, 0])
timer_button_three = PushButton(window_one, command=timer_func_three, text="20 Seconds", grid=[17, 0])
other_button_two = PushButton(window_one, command=Other_time, text="Custom Time", grid=[18, 0])
power_button = PushButton(window_one, command=power_off, text="Power Off", grid=[19, 0])
custom_button = PushButton(window_one, command=customp_window, text="Custom Profiles", grid=[20, 0])

# Style block for the buttons within the main window.
PA_button.text_color = (255, 30, 30)
PA_button.font = "verdana"
PA_button.text_size = 6
PA_button.bg = "#300000"
ABS_button.text_color = (255, 30, 30)
ABS_button.font = "verdana"
ABS_button.text_size = 6
ABS_button.bg = "#3A0000"
HDPE_button.text_color = (255, 30, 30)
HDPE_button.font = "verdana"
HDPE_button.text_size = 6
HDPE_button.bg = "#440000"
LDPE_button.text_color = (255, 30, 30)
LDPE_button.font = "verdana"
LDPE_button.text_size = 6
LDPE_button.bg = "#4E0000"
PP_button.text_color = (255, 30, 30)
PP_button.font = "verdana"
PP_button.text_size = 6
PP_button.bg = "#580000"
other_button.text_color = (255, 30, 30)
other_button.font = "verdana"
other_button.text_size = 6
other_button.bg = "#620000"
timer_button.text_color = (255, 30, 30)
timer_button.font = "verdana"
timer_button.text_size = 6
timer_button.bg = "#6C0000"
timer_button_two.text_color = (255, 30, 30)
timer_button_two.font = "verdana"
timer_button_two.text_size = 6
timer_button_two.bg = "#6C0000"
timer_button_three.text_color = (255, 30, 30)
timer_button_three.font = "verdana"
timer_button_three.text_size = 6
timer_button_three.bg = "#6C0000"
other_button_two.text_color = (255, 30, 30)
other_button_two.font = "verdana"
other_button_two.text_size = 6
other_button_two.bg = "#620000"
power_button.text_color = (255, 30, 30)
power_button.font = "verdana"
power_button.text_size = 6
power_button.bg = "#620000"
custom_button.text_color = (255, 30, 30)
custom_button.font = "verdana"
custom_button.text_size = 6
custom_button.bg = "#440000"

# This block of code sets up the buttons and their functionality within the second (Setting temperature) window.
window_two = Window(window_one, title="Setting temperature", layout="auto", visible=False)
plastic_selection = Text(window_two)
window_info = Text(window_two)
b_temp = Text(window_two)
n_temp = Text(window_two)
window_two.bg = "white"

# This block of code sets up the buttons and their functionality within the third (custom temperature) window.
window_three = Window(window_one, title="Custom temperature", layout="auto", visible=False)
other_info_two = Text(window_three, text="Barrel Temperature")
barrel_custom = TextBox(window_three, text="400.0")
b_up = PushButton(window_three, text="+", command=b_up_fcn)
b_down = PushButton(window_three, text="-", command=b_down_fcn)
other_info_three = Text(window_three, text="Nozzle Temperature")
nozzle_custom = TextBox(window_three, text="400.0")
n_up = PushButton(window_three, text="+", command=n_up_fcn)
n_down = PushButton(window_three, text="-", command=n_down_fcn)
enter = PushButton(window_three, text="Enter", command=other_temp_set)
window_three.bg = "white"

# Style block for the widgets within the custom temperature window.
nozzle_custom.text_size = 5
barrel_custom.text_size = 5
other_info_two.font = "times new roman"
other_info_two.text_size = 10
other_info_three.font = "times new roman"
other_info_three.text_size = 10
b_up.text_color = (255, 30, 30)
b_up.font = "verdana"
b_up.text_size = 10
b_up.bg = "#6C0000"
b_down.text_color = (255, 30, 30)
b_down.font = "verdana"
b_down.text_size = 23
b_down.bg = "#300000"
n_up.text_color = (255, 30, 30)
n_up.font = "verdana"
n_up.text_size = 10
n_up.bg = "#6C0000"
n_down.text_color = (255, 30, 30)
n_down.font = "verdana"
n_down.text_size = 23
n_down.bg = "#300000"
enter.text_size = 10

# This block of code sets up the buttons and their functionality within the fifth (custom time) window.
window_five = Window(window_one, title="Custome Time", layout="auto", visible=False)
other_info_four = Text(window_five, text="Select Custom Time in Seconds")
time_custom = TextBox(window_five, text="10.0")
t_up = PushButton(window_five, text="+", command=t_up_fcn)
t_down = PushButton(window_five, text="-", command=t_down_fcn)
enter_two = PushButton(window_five, text="Enter", command=other_time_set)
window_five.bg = "white"

# Style block for the widgets within the custom time window.
t_up.text_color = (255, 30, 30)
t_up.font = "verdana"
t_up.text_size = 10
t_up.bg = "#6C0000"
t_down.text_color = (255, 30, 30)
t_down.font = "verdana"
t_down.text_size = 13
t_down.bg = "#300000"
enter_two.font = "times new roman"
enter_two.text_size = 10
time_custom.text_size = 13
other_info_four.font = "times new roman"
other_info_four.text_size = 10

# This block of code sets up the buttons and their functionality within the sixth (custom temperatures) window.
window_six = Window(window_one, title="Custom Profiles", layout="auto", height=660, width=670, visible=False)
listbox = ListBox(window_six, items=[], scrollbar=True)
enter_six = PushButton(window_six, text="Delete", command=delete)
title_two = Text(window_six, text="Material Type", font=("verdana", 1))
material_type = TextBox(window_six, text="")
title_five = Text(window_six, text="Seconds", font=("verdana", 1))
time_custom_two = TextBox(window_six, text="10.0")
t_up_two = PushButton(window_six, text="+", command=t_up_fcn_two)
t_down_two = PushButton(window_six, text="-", command=t_down_fcn_two)
title_three = Text(window_six, text="Barrel Temp", font=("verdana", 1))
barrel_custom_two = TextBox(window_six, text="400.0")
b_up_two = PushButton(window_six, text="+", command=b_up_fcn_two)
b_down_two = PushButton(window_six, text="-", command=b_down_fcn_two)
title_four = Text(window_six, text="Nozzle Temp", font=("verdana", 1))
nozzle_custom_two = TextBox(window_six, text="400.0")
n_up_two = PushButton(window_six, text="+", command=n_up_fcn_two)
n_down_two = PushButton(window_six, text="-", command=n_down_fcn_two)
title_one = Text(window_six, text="First Name")
first_name = TextBox(window_six, text="")
enter_four = PushButton(window_six, text="Enter Values", command=custom_profiles_set)
enter_three = PushButton(window_six, text="Save Profile", command=set)
window_six.bg = "white"

# Style block for the widgets within the custom profiles window.
title_one.text_size = 3
title_two.text_size = 3
title_three.text_size = 3
title_four.text_size = 3
title_five.text_size = 3
enter_three.text_size = 3
enter_four.text_size = 3
enter_six.text_size = 3
listbox.width = 32
listbox.height = 4
n_up_two.text_color = (255, 30, 30)
n_up_two.font = "verdana"
n_up_two.text_size = 3
n_up_two.bg = "#6C0000"
n_down_two.text_color = (255, 30, 30)
n_down_two.font = "verdana"
n_down_two.text_size = 3
n_down_two.bg = "#300000"
t_up_two.text_color = (255, 30, 30)
t_up_two.font = "verdana"
t_up_two.text_size = 3
t_up_two.bg = "#6C0000"
t_down_two.text_color = (255, 30, 30)
t_down_two.font = "verdana"
t_down_two.text_size = 3
t_down_two.bg = "#300000"
b_up_two.text_color = (255, 30, 30)
b_up_two.font = "verdana"
b_up_two.text_size = 3
b_up_two.bg = "#6C0000"
b_down_two.text_color = (255, 30, 30)
b_down_two.font = "verdana"
b_down_two.text_size = 3
b_down_two.bg = "#300000"
window_one.display()
