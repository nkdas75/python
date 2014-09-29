def trywithelse():
    fileOpened = False
    try:
        f = open("someFile.txt")
    except FileNotFoundError as e:
        fileOpened = True
        print ("File not found exception :: " + e.strerror)
    else:
        print ("File opened")
        f.close()
    finally:
        # do all house keeping work like closing the file/ closing network connection etc here!
        if fileOpened :
            print ("FileNotFoundError was encountered. So file was not opened")
        else:
            print("File closed")

trywithelse()
