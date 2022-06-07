def saludo ():


    name= input ("¿Cual es tu nombre?")
    print ("Hola" + name.upper())
    age = input ("¿Cuantos años tienes? : ")
    print ("Tienes" + age + "Años y en tres años mas tendre" + (age + 3))


if __name__=='__main__':
    saludo()