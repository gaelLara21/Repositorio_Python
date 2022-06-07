def saludo ():

    #Lineas a ejecutarse
    name= input ("¿Cual es tu nombre?")
    print ("Hola" + name)
    age = input ("¿Cuantos años tienes? : ")
    print ("Tienes" + age + "Años y en tres años mas tendre" + (age + 3))


    if __name__=='__main__':
      saludo()