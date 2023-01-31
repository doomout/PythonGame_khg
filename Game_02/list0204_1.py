import tkinter

fn1 = ("Times New Roman", 20)
fn2 = ("Times New Roman", 40)
index = 0
timer = 0

key = ""
def key_down(e):
    global key
    key = e.keysym
    
def main():
    global index, timer
    