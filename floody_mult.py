import pyautogui, pyperclip, time

print('''
                                                       0
======  =         ====       ====     =====    =    / =
======  =       =       =  =       =  =     =    =   =
==      =       =   =   =  =   =   =  =     =      =
===     =       =   =   =  =   =   =  =     =      =
==      ======  =       =  =       =  =     =      =
==      ======    ====       ====     =====        =
''')


def sleep_time(sleep=5): # default sleep time
  print()
  while sleep > 0:
    print(f'Open the app and the script will automatically begin copy-pasting in {sleep} seconds!', end='\r')
    time.sleep(1)
    sleep -= 1

def file():
  global agressive
  file_name = input('Enter the name of file or press "enter" to set it by default (flooder.txt): ')

  if file_name == '':
    file_name = 'flooder.txt'
  while True:
    try:
      read = open(file_name, 'r')
      break
    except FileNotFoundError:
      file_name = input('Enter the name of file: ')

  sleep_time()

  if agressive == 'y': # checking for agressive mode
    for line in read:
      pyperclip.copy(line)
      pyautogui.hotkey('ctrl', 'v')
      pyautogui.press('enter')
  else:
    for line in read:
      for word in line:
        pyperclip.copy(word)
        pyautogui.hotkey('ctrl', 'v', interval=0.001)
      pyautogui.press('enter')    

def phrase():
  global agressive
  phrase_input = input('Please enter the phrase: ')

  while True:  # checking if a phrase is empty
    if phrase_input.split()  == []:
      phrase_input = input('The phrase shouldn\'t be empty! Enter it again: ')
    else:
      break
  while True:  # check if user did a right input
    try:
      how_many = int(input('Repeats: '))
      break
    except ValueError:
      continue

  sleep_time()

  i = 1
  if agressive == 'y': # check for agressive mode
    pyperclip.copy(phrase_input)
    while i <= how_many:
      pyautogui.hotkey('ctrl', 'v')
      pyautogui.press('enter')
      i += 1
  else:
    while i <= how_many:
      for letter in ' '.join(phrase_input.split()):
        pyperclip.copy(letter)
        pyautogui.hotkey('ctrl', 'v', interval=0.001)
      pyautogui.press('enter')
      i += 1

while True: # repeating program
  while True: # main menu
    choose = input('\nAre you going to use a file or a phrase or maybe you need help (f for file or p for phrase or h for help): ')
    if choose == 'f':
      agressive = input('Are you going to use a program in agressive mode? ')
      file()
      print('\nProgram successfully completed!')
      break
    elif choose == 'p':
      agressive = input('Are you going to use a program in agressive mode? ')
      phrase()
      print('\nProgram successfully completed!')
      break
    elif choose == 'h':
      print('\nHi! This is [multilang] floody - a simple program that allows you to flood to someone reeallly anoying :) It has 2 modes: normal and agressive. Normal imitates human-like typing, while agressive just do the work without any delays.')
    else:
      continue
  repeat = input('Do you want to continue? (y/n): ')
  if repeat != 'y':
    break