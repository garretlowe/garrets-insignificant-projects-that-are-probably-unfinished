from tkinter import *
from tkinter.ttk import *
# import main


RACES = ('Altmer', 'Argonian', 'Bosmer', 'Breton', 'Dunmer', 'Imperial', 'Khajiit', 'Nord', 'Orsimer', 'Redguard')
SEXES = ('Female', 'Male', 'Both')

window = Tk()

frame_left = Frame(master=window, width=200, height=300)
frame_left.pack(fill=BOTH, side=LEFT, expand=True)

frame_right = Frame(master=window, width=300, height=300)
frame_right.pack(fill=BOTH, side=LEFT, expand=True)

chosen_race = StringVar(window, RACES[0])
chosen_sex = StringVar(window, 'Both')
ancient_names = BooleanVar(window, False)
family_names = BooleanVar(window, False)

def button_pressed():
	print(f'{chosen_race.get()}, {chosen_sex.get()}, {ancient_names.get()}, {family_names.get()}')

def create_argonian_frame():
	frame_argonian = Frame(master=frame_right)
	frame_argonian.pack(fill=BOTH, side=TOP)
	Label(master=frame_argonian, text='Argonian').pack(anchor=NW)
	return frame_argonian
	
current_race_frame = create_argonian_frame()

def combobox_changed(event):
	if current_race_frame is not None:
		current_race_frame.destroy()
		#current_race_frame = None
	if chosen_race.get() == 'Argonian':
		current_race_frame = create_argonian_frame()
	
	
def determine_generation_method(race, sex, ancient_names, family_names):
	pass

frame_race = Frame(master=frame_left)
frame_race.pack(fill=BOTH, side=TOP)
cb_race = Combobox(master=frame_race, values=RACES, state='readonly', textvariable=chosen_race)
cb_race.bind('<<ComboboxSelected>>', combobox_changed)
cb_race.current(newindex=0)
cb_race.pack(side=LEFT)

frame_sexes = Frame(master=frame_left)
frame_sexes.pack(fill=BOTH, side=TOP)
for sex in SEXES:
	Radiobutton(master=frame_sexes, text=sex, variable=chosen_sex, value=sex).pack(anchor=NW)

Button(master = frame_left, text='Generate...', command=button_pressed).pack(anchor=SW)

frame_eras = Frame(master=frame_right)
frame_eras.pack(fill=BOTH, side=TOP)
Radiobutton(master=frame_eras, text='1st/2nd Era', variable=ancient_names, value=True).pack(anchor=NW)
Radiobutton(master=frame_eras, text='3rd/4th Era', variable=ancient_names, value=False).pack(anchor=NW)

frame_family_name = Frame(master=frame_right)
frame_family_name.pack(fill=BOTH, side=TOP)
Checkbutton(master=frame_family_name, text='Generate Family Name', variable=family_names, onvalue=True, offvalue=False).pack(anchor=NW)


window.mainloop()
