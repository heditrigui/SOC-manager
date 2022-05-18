import subprocess
import sys
import PySimpleGUI as sg

def main():
    layout = [  [sg.Text('enter your username')],
            [sg.Input(key='_INPUT_')],             # input field where you'll type command
            [sg.Output(size=(60,15))],          # an output area where all print output will go
            [sg.Button('Run'), sg.Button('Exit')] ]     # a couple of buttons

    window = sg.Window('LOGIN', layout)
    
    while True:      
    	      # Event Loop
        event, values = window.Read()
        #username = values['-INPUT-'] 
        if event in (None, 'Exit'):         # checks if user wants to 
            exit
            break

        if event == 'Run':                  # the two lines of code needed to get button and run command
            runCommand(cmd=values['_INPUT_'], window=window)

    window.Close()

# This function does the actual "running" of the command.  Also watches for any output. If found output is printed
def runCommand(cmd, timeout=None, window=None):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ''
    for line in p.stdout:
        line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
        output += line
        print(line)
        window.Refresh() if window else None        # yes, a 1-line if, so shoot me
    retval = p.wait(timeout)
    return (retval, output)                         # also return the output just for fun
    
main()

