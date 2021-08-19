from tkinter.ttk import*
import shutil
from tkinter import simpledialog
from tkinter import dialog#plz import!
from tkinter import PhotoImage,mainloop,Entry,StringVar,Button,HORIZONTAL,Scale,Listbox,ACTIVE,Menu,END,filedialog,Toplevel
from ttkthemes import ThemedTk
import os
import pygame
from tkinter import messagebox
root=ThemedTk(themebg=True)
root.title('Playlist- Default')
root.set_theme('black')
root.geometry('800x635')
song_Data=StringVar()
val12=0
check=False
has=False
val=0
file=''
times_playlist_created=0
your_playlist=[]
names=[]
c=[]
check1000='NOPE!'
times_called=0
def check_this_bitch():
	print(path1)
def save_name():# healteh bar
	global path1,play_list_name
	if name.get()=='':
		pass
	else:
		r=list_.get(ACTIVE)
		pos=r.index(r)
		names[pos]=name.get()
		for i in names:
		    old=path1[path1.rfind('\\')+1:len(path1)]
		    returned_string=(path1.replace(old,i))
		    Named_to_be=path1.rfind('\\')
		    print(path1[:Named_to_be:]+name.get())
		    
		    os.rename(your_playlist[pos],path1[:Named_to_be:]+"\\"+name.get())#root.title()

		    
		    path1=''
		    path1+=returned_string
		    play_list_name=''
		    play_list_name+=returned_string
		    c.append(returned_string)

		    your_playlist[pos]=returned_string
		list_.delete(pos)
		name12=path1[path1.rfind('\\')+1:len(path1)]
		
		if root.title()=='Playlist- Default':
			boyaah=path1[:Named_to_be:]+"\\"+name.get()
			print('yo!1')
			plist_.insert(pos,f'{name12} - {boyaah}')
		if root.title()!='Playlist- Default':
			print('yo!2')
			boyaah=path1[:Named_to_be:]+"\\"+name.get()
			root.title(f'Playlist - {boyaah}')
			play_List_indict['text']=f'Playlist - {boyaah}'

			list_.insert(pos,f'{name12} - {boyaah}')

		t3.destroy()# create a fun fact option option when user lose in my pygame game!! boi!sssk
def edit():#entry config font
	global name,t3

	t3=Toplevel()
	t3.title('Edit')
	t3.config(bg='#3C3C3C')
	edit_label=Label(t3,text='Edit Playlist Name Here:',font=('Arial',25,'bold')).pack()
	name=Entry(t3,bg='#3C3C3C',fg='yellow',font=('Arial Rounded MT bold',14,'bold'))
	name.pack()
	done=Button(t3,text='Done',font=('Arial',20,'bold'),fg='white',bg='#3C3C3C',activeforeground='white',activebackground='#3C3C3C',command=save_name)
	done.pack()
def question1(dedo):
	d = dialog.Dialog(None, {'title': 'Question',
                      'text':'Which Type Of Task You Want To Do In This Selected Playlist'.title(),
                      'bitmap': dialog.DIALOG_ICON,
                      'default': 'None',
                      'strings': ('Open',
                                  'Edit Name',
                                  'None')})
	if d.num==0:
		pass
	if d.num==1:
		edit()
	if d.num==2:
		pass
def Savee():
	global check1000
	check1000='YUP!'
	
def show_user_own_playlist():
	global list_,times_called,t1
	t1=Toplevel()
	t1.config(bg='#3C3C3C')
	t1.title("Your Created Playlists Are Here!")
	t2=Label(t1,text='Here Is The List Of Playlist You Created:',font=('Arial Rounded MT bold',25,'bold'))
	t2.pack()
	list_=Listbox(t1,width=32,bg="#3C3C3C",fg='cyan',font=('Arial',17,'bold'))
	list_.pack()
	pyaar=0
	list_.insert()
	list_.bind('<Double-Button>',question1)
def CLOSE():
	pygame.mixer.music.stop()
	exit()
root.protocol('WM_DELETE_WINDOW',CLOSE)
open_dir_paths=[]
play_ing_song_name=[]
pygame.mixer.init()
def active_all():
	play['state']='active'
	prev['state']='active'
	next1['state']='active'
	stop['state']='active'
def _add_folder():
	global dir_name,open_dir_paths,mp3_wav_ogg,val,folder_name
	dir_name=filedialog.askdirectory()
	open_dir_paths.append(dir_name)
	good_boiii=[]
	mp3_wav_ogg=os.listdir(dir_name)
	val=0
	play_List_indict.config(text=f'Playlist - {dir_name}')
	for x in mp3_wav_ogg:
		if str(x).endswith('.mp3') or str(x).endswith('.wav') or str(x).endswith('.ogg'):
			play_list.insert(val,x)
			val+=1
def upause():
	pygame.mixer.music.unpause()
	play['image']=pause_image
	play['command']=pause
	playing_label['text']='Paused - '+play_list.get(ACTIVE)

	play.place(y=500,x=340)
def pause():
	pygame.mixer.music.pause()
	play['image']=play_image
	play['command']=upause

	play.place(y=500,x=340)


def play_the_song():
	global is_playing
	active_all()
	play['image']=pause_image

	try:
		if play['image']==pause_image:
			pause()
		else:
			upause()
			play.place(x=340,y=500)
		try:
			pygame.mixer.music.stop()
			pygame.mixer.music.load(dir_name.replace('/','\\')+'\\'+play_list.get(ACTIVE))
			pygame.mixer.music.play()
		except:
			pass
		playing_label['text']='Playing - '+play_list.get(ACTIVE)
		play_ing_song_name.append(dir_name.replace('/','\\')+'\\'+play_list.get(ACTIVE))
		if play_ing_song_name[0]==play_list.get(ACTIVE):
			pygame.mixer.music.load(dir_name.replace('/','\\')+'\\'+play_list.get(ACTIVE))
			pygame.mixer.music.play()
		else:
			pass


	except Exception as e:
		raise e
		try:
			for x in range(len(dir_name)):
				pygame.mixer.music.load(dir_name[x].replace('/','\\')+'\\'+play_list.get(ACTIVE))
				pygame.mixer.music.play()
		except:
			messagebox.showinfo('Error','Error Occured!')
			raise e
hmm=0
hmm12=0
def set_volume1(self):
	pygame.mixer.music.set_volume(float(volume.get()) /100)
def prev_song():
	global posxD1,hmm12
	a123=play_list.get(0,'end')
	list_fromXd5=list(a123)	
	posxD1=list_fromXd5.index(play_list.get(ACTIVE))
	posxD1+=1
	hmm12+=1
	xdd1=play_list.get(0,'end')
	pos1=list(xdd1)
	YOOOoooYoo12=pos1.index(play_list.get(ACTIVE))
	if hmm12<=1:	
		play_list.selection_set(YOOOoooYoo12-1)
		play_list.selection_clear(YOOOoooYoo12)
		play_list.activate(posxD1-1-1)
		play_list.see(YOOOoooYoo12-1)#ACTIVATE 'R' SEE
		upause()
		try:
			print('FIX THIS: 3')

			play_the_song()
		except:
			print('FIX THIS: 4')

			play_the_song_for_own_playlist_with_button()

	else:
		play_list.selection_set(YOOOoooYoo12-1)
		play_list.selection_clear(YOOOoooYoo12)
		play_list.activate(posxD1-1-1)
		play_list.see(YOOOoooYoo12-1)#ACTIVATE 'R' SEE
		upause()

		try:
			print('FIX THIS: 5')

			play_the_song()
		except:
			print('FIX THIS: 5')

			play_the_song_for_own_playlist_with_button()

def play_the_song_for_own_playlist_with_button():
	pygame.mixer.music.stop()
	pygame.mixer.music.load(path1+'\\'+play_list.get(ACTIVE))
	pygame.mixer.music.play()
	playing_label['text']='Playing - '+play_list.get(ACTIVE)
	play['image']=pause_image
	if play['image']==pause_image:
		pause()
		playing_label['text']='Paused - '+play_list.get(ACTIVE)

	else:
		upause()
		play.place(x=340,y=500)

def play_the_song_for_own_playlist(head_ahce):
	pygame.mixer.music.stop()
	pygame.mixer.music.load(path1+'\\'+play_list.get(ACTIVE))
	pygame.mixer.music.play()
	playing_label['text']='Playing - '+play_list.get(ACTIVE)
	play['image']=pause_image
	if play['image']==pause_image:
		playing_label['text']='Paused - '+play_list.get(ACTIVE)
		pause()
	else:
		upause()
		play.place(x=340,y=500)

def add_song1():
	global dir_name,open_dir_paths,mp3_wav_ogg,val,val12,folder_name
	dir_name123=filedialog.askopenfilename()
	times_called=0
	open_dir_paths12=[]
	open_dir_paths12.append(dir_name123)
	for x in open_dir_paths12:
		if str(x).endswith('.mp3') or str(x).endswith('.wav') or str(x).endswith('.ogg'):
			play_list.insert(val12,x[x.rfind('/')+1:len(x)])
			val12+=1
			shutil.copyfile(x,path1+'\\'+x[x.rfind('/')+1:len(x)]) 
			play_list.delete(val12+1)
		if play_list.get(0)!='':
			active_all()
		else:
			pass
	file.entryconfig(0,command=add_song1)
	play['command']=play_the_song_for_own_playlist_with_button
	# play_List_indict['text']=f'Playlist - {play_list_name}'
def next_song():
	#########Next################
	global posxD,posxD,pos,B,hmm,xd_bop
	a12=play_list.get(0,'end')
	list_fromXd=list(a12)	
	posxD=list_fromXd.index(play_list.get(ACTIVE))
	posxD+=1
	hmm+=1
	xdd=play_list.get(0,'end')
	pos=list(xdd)
	YOOOoooYoo=pos.index(play_list.get(ACTIVE))
	if hmm<=1:		
		print('1')
		play_list.selection_set(YOOOoooYoo+1)
		play_list.selection_clear(YOOOoooYoo)
		play_list.activate(posxD)
		play_list.see(posxD+1)#ACTIVATE 'R' SEE
		play.place(x=350,y=500)
		upause()
		play['image']=pause_image

		try:
			print('FIX THIS: 1')
			play_the_song()
		except:
			print('FIX THIS: 2')

			play_the_song_for_own_playlist_with_button()

	else:
		play_list.activate(posxD)
		play_list.selection_set(YOOOoooYoo+1)
		play_list.selection_clear(posxD-1)
		play_list.see(posxD+1)
		play.place(x=350,y=500)
		upause()

		try:
			play_the_song()
		except:
			play_the_song_for_own_playlist_with_button()

def Play_The_Slected_Song(BTS_IS_MY_FAV_KPOP_GROUP_AND_EXO_ALSO_AND_STRAY_KIDS_AND_BLOCK_B_ALSO):
	pygame.mixer.music.stop()
	try:
		for x in range(len(open_dir_paths)):
			try:
				try:
					print(5+'fff')

				except:
					try:
						pygame.mixer.music.stop()
						pygame.mixer.music.load(dir_name.replace('/','\\')+'\\'+play_list.get(ACTIVE))
						pygame.mixer.music.play()
					except:
						pass
			except Exception as e: 
				messagebox.showinfo('Error','Error Occured!')
				raise e
	except Exception as r1:
		raise r1
	try:
		pygame.mixer.music.stop()
		pygame.mixer.music.load(path1+'\\'+play_list.get(ACTIVE))
		pygame.mixer.music.play()

	except:
		print('I WORKED!')
		pygame.mixer.music.stop()
		try:
			pygame.mixer.music.load(dir_name+'\\'+play_list.get(ACTIVE))
			pygame.mixer.music.play()
		except:
			print('I WORKED!')

	playing_label['text']='Playing - '+play_list.get(ACTIVE)
	play['image']=pause_image
	play['command']=pause
	play['state']='active'
	prev['state']='active'
	next1['state']='active'
	stop['state']='active'
	play.place(y=500,x=340)
def stop():
	pygame.mixer.music.stop()
	play['text']='Play'
	play['command']=play_the_song
	playing_label['text']=''
	play.place(y=500,x=350)
def del_playlist():
	question=messagebox.askquestion('Info!!','Are Your Sure To Clear Playlist It Will Delete The Playlist!')#rip me!
	pygame.mixer.music.stop()
	playing_label['text']=''
	play_List_indict['text']='Playlist'
	play['text']='Play'
	open_dir_paths.clear()
	try:
		open_dir_paths12.clear()
	except:
		pass
	play_list.delete(0,'end')
	files=os.listdir(path1)
	for i in files:
		print('Deleting...')
		os.remove(path1+'\\'+i)
	print('Playlist Deleted!')
def show_created_window_playlist():
	root.title(f'Playlist- {path1}')
	play_list.delete(0,'end')
	playing_label['text']=''
	pygame.mixer.music.stop()
	play_List_indict['text']=f'Playlist- {path1}'
	add_song['text']='Add song'
	add_song['command']=add_song1
def ask_dir_name_to_save():
	global check,path1,dir_name12
	check=True
	dir_name12=simpledialog.askstring("Enter Path To Save The Playlist.",prompt='Enter Path To Save The Playlist.')
	while check:
		if dir_name12==None:
			break
		if len(dir_name12)<=0:
			ask_dir_name_to_save()
		else:
			path1=dir_name12+play_list_name.replace('\\','\\')
			try:
				os.mkdir(path1)
				your_playlist.append(path1)

			except OSError:
				your_playlist.clear()
				ask_dir_name_to_save()
			show_created_window_playlist()
			# messagebox.showinfo('Info','Playlist Created Successfully!!')
			break 
def create_playlist():
	global play_list_name,Looping
	Looping=True
	play_list_name=simpledialog.askstring("Enter Your Playlist Name",prompt='Enter Your Playlist Name.')
	
	while True:
		try:
			if play_list_name==None:
				break
			try:
				if len(play_list_name)<=0:
					create_playlist()

				else:
					messagebox.showinfo("Info",'Playlist Named Successfully!')
					if play_list_name.count('/') or play_list_name.count('\\') or play_list_name.count('<') or play_list_name.count('>') or play_list_name.count('''"''') or play_list_name.count('?') or play_list_name.count('*') or play_list_name.count(':') or play_list_name.count('|'): #/\ <> " ? * : |
						messagebox.showinfo('Info!!','Your Playlist Name Cannot Contains These Charecters:- /\ <> " ? * : | ')
						create_playlist()
					else:
						names.append(play_list_name)
						ask_dir_name_to_save()
						break
			except Exception as test1000:
				raise test1000
				create_playlist()
		except Exception as test:
			raise test
			create_playlist()
def open_single_file():
	global file_name
	file_name=filedialog.askopenfilename()
	if str(file_name).endswith('.mp3') or str(file_name).endswith('.wav') or str(file_name).endswith('.ogg'):
		opened_file_name=file_name[file_name.rfind('/')+1:len(file_name)]
		try:
			play_list.insert(val+1,opened_file_name)# ide that set the prtioty of a vairable  like the varaible name is file_name but ide is suggeted file varioable but i need file_name variable
			messagebox.showinfo('Info',f'{opened_file_name} Added To {folder_name} Playlist')
		except:
			play_list.insert(val+1,opened_file_name)
		open_dir_paths.append(opened_file_name)

prev_image=PhotoImage(file='previous.png')
play_image=PhotoImage(file='play.png')
next_image=PhotoImage(file='next.png')
# stop_image=PhotoImage(file='stop.png')
pause_image=PhotoImage(file='pause.png')
prev=Button(root,image=prev_image,font=('Arial',20,'bold'),fg='white',bg='#3C3C3C',activeforeground='white',activebackground='#3C3C3C',command=prev_song,state='disabled')
prev.place(y=500,x=231)
play=Button(root,image=play_image,font=('Arial',20,'bold'),fg='white',bg='#3C3C3C',activeforeground='white',activebackground='#3C3C3C',command=play_the_song,state='disabled')
play.place(y=500,x=350)
next1=Button(root,image=next_image,font=('Arial',20,'bold'),fg='white',bg='#3C3C3C',activeforeground='white',activebackground='#3C3C3C',command=next_song,state='disabled')
next1.place(y=500,x=330+130)
stop=Button(root,text='Stop',font=('Arial',20,'bold'),fg='white',bg='#3C3C3C',activeforeground='white',activebackground='#3C3C3C',command=stop,state='disabled')
stop.place(y=570,x=347)# we can increase image size in tkinter by chaing the font size!!,entry conifg,#image creator like a person need a image of cat he/she write the requirment of image like i want a image in black color blue eyes etc.
progressbar=Progressbar(root,length=545)
progressbar.start(10)
progressbar.place(x=1,y=465)
volume_indict_=Label(root,text='Volume:',font=('Arial',15,'bold'))
volume_indict_.place(y=500)
volume=Scale(root,from_=0,to=100,orient=HORIZONTAL,tickinterval=20,length=150,background='#3C3C3C',fg='white',activebackground='#3C3C3C',command=set_volume1)
volume.place(y=530,x=1)
volume.set(50)
lyrics_indict=Label(root,text='Lyrics',font=('Arial',20,'bold'))
lyrics_indict.place(x=200,y=150)
lyrics=Listbox(root,bg='#3C3C3C',width=55,fg='orange',font=('Arial',12,'bold'))
lyrics.place(x=1,y=200)
lyrics.insert(0,"blackpink!".upper())
play_list=Listbox(root,width=32,bg="#3C3C3C",fg='cyan',font=('Arial',12,'bold'),listvar=song_Data)
play_list.place(x=505,y=60)
play_List_indict=Label(root,text='Playlist - Default',font=('Arial',20,'bold'))
play_List_indict.place(x=400,y=10)
add_song=Button(root,text='Add Folder',font=('Arial',20,'bold'),fg='white',bg='#3C3C3C',activeforeground='white',activebackground='#3C3C3C',command=_add_folder)
add_song.place(x=555,y=270)
playing_label=Label(root,text='',font=('Arial',15,'bold'))
playing_label.place(x=1,y=425)
clear=Button(root,text='Clear Playlist',font=('Arial',20,'bold'),fg='white',bg='#3C3C3C',activeforeground='white',activebackground='#3C3C3C',command=del_playlist)
clear.place(x=545,y=350)
menubar = Menu(root)  
file = Menu(menubar, tearoff=0)  
file.add_command(label="Open Media",command=open_single_file)  
file.add_command(label="Create Playlist",command=create_playlist)  
file.add_command(label="Recent Media")  
file.add_command(label="Recent Playlist")  
file.add_command(label="Your Playlists",command=show_user_own_playlist)  
menubar.add_cascade(label="File", menu=file) 
root.config(menu=menubar)
# filepath and player vs player.!
# fix resu me pause bug and complete menu options.
# add player vs player and crete a bouncing effect when user get 1 point rock paper sicors. 
# send this project to pyguru
# create aplying sound label
play_list.bind('<Double-Button>',Play_The_Slected_Song)

mainloop()
# # create a player vs player mode...!
# # from musixmatch import musixmatch
# # api_key='ffb75ae490c3bfde65848de87864a7d8'
# # musixmatch=musixmatch.Musixmatch(api_key)
# # print(musixmatch.matcher_lyrics_get('blackpink', 'du du du du '))
# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import showinfo

# # create the root window
# root = tk.Tk()
# root.geometry('200x100')
# root.resizable(False, False)
# root.title('Listbox')

# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

# # create a list box
# langs = ('Java', 'C#', 'C', 'C++', 'Python',
#         'Go', 'JavaScript', 'PHP', 'Swift')

# langs_var = tk.StringVar(value=langs)

# listbox = tk.Listbox(
#     root,
#     height=6,
#     selectmode='single')
# for x in langs:
# 	val=0
# 	listbox.insert(0,x)
# 	val+=1

# listbox.grid(
#     column=0,
#     row=0,
#     sticky='nwes'
# )
# def op():
# 	global val
# 	val+=1
# 	listbox.select_set(val)
# 	listbox.itemconfig(val-1,fg='black')

# 	listbox.select_clear(val-1)
# 	listbox.itemconfig(val-1,fg='grey')



# 	root.after(1000,op)
# val=0
# listbox.selection_set(0)
# listbox.itemconfig(len(langs)-1,fg='grey')
# root.after(1000,op)


# # everthing in python is object and pop() removes the elemtnt and return its. and del delte the keyword
# # handle event
# # slection_set method is op.
# # select_clear is alos op.
# def items_selected(event):
#     """ handle item selected event
#     """
#     # get selected indices
#     selected_indices = listbox.curselection()
#     # get selected items
#     selected_langs = ",".join([listbox.get(i) for i in selected_indices])
#     msg = f'Your selected: {selected_langs}'

#     showinfo(
#         title='Information',
#         message=msg)

# create own module bitch!

# root.mainloop()
# learn about audio and coced and explore tkinter more!
# speed function 
