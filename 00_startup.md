
### Interacting with the [ D1 mini](https://wiki.wemos.cc/products:d1:d1_mini) ###

![](https://wiki.wemos.cc/_media/products:d1:d1_mini_v3.0.0_1_16x9.jpg)

---

 ### WINDOWS

 *prerequisite* python3 installed

 - install rshell

``` 
C:\Users\your_name>python3 -m pip install rshell
``` 
or perhaps if you already have it

```
C:\Users\your_name>python3 -m pip install --upgrade rshell 
```

- Plug in the micropython board USB cable to pc

- using Device Manager check port name **USB-SERIAL CH340** device is on

- if device is not showing, download [drivers](https://wiki.wemos.cc/downloads) from wemos website

---
so lets use rshell
- rshell has lots of functions password protection, editor selection etc
```
C:\Users\your_name>rshell -h
```

lets start with the basics - file management & getting to the repl
--- 

- in a terminal window

```
C:\Users\your_name>python3 rshell -p COM4 
```
COM4 is just an example, use the port device manager says

you should then get rshell booting and connecting with the board

```

Using buffer-size of 32
Connecting to COM4 (buffer-size 32)..
Setting time ... Feb 08, 2019 17:52:03
Evaluating board_name ... pyboard
Retrieving time epoch ... Jan 01, 2000
Welcome to rshell. Use Control-D (or the exit command) to exit rshell.
home/your_name>

```
- note the name of your board is always **pyboard** 

---

you now have access to the board and your pc directories
 - list the files on your board (remember it was called **pyboard**)
 ```
 C:\Users\your_name> ls /pyboard
 main.py
 boot.py

C:\Users\your_name>
 ```

 - copy files from your pc onto the board
 ```
 C:\Users\your_name> cp Documents/new.py /pyboard
 ```

note: use a forward slash in rshell even when addressing your pc path

---

now start the repl !
```
C:\Users:\your_name> repl
Entering REPL. Use Control-X to exit.
repl_serial_to_stdout dev = <rshell.main.DeviceSerial object at 0x7f7e14d1b56748>
>
MicroPython v1.9.4-8-ga9a3caad0 on 2018-05-11; ESP module with ESP8266
Type "help()" for more information.
>>>

```

- Ctrl+X leaves the repl
- Ctrl+C leaves rshell back to the terminal prompt