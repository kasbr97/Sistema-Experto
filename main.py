"""
Systema Experto - Diagnóstico de enfermedades
Alumnos:
    Víctor Baldeón
    Kevin Burga
"""
from tkinter import * 
from tkinter.ttk import *
  

def ventana_preguntas():
    ventana = Tk()
    ventana.title('Preguntas')
    
    pregunta=Label(ventana ,justify=CENTER, text="Pregunta 1", wraplength=450, pad=10)
    pregunta.pack()
    pregunta.config(font=("Arial", 25))
    
    #Agrega 5 Radio Buttons
    values = {"RadioButton 1" : "1", 
              "RadioButton 2" : "2", 
              "RadioButton 3" : "3", 
              "RadioButton 4" : "4", 
              "RadioButton 5" : "5"} 
    
    for (text, value) in values.items(): 
        Radiobutton(ventana, text = text, variable = v, 
           value = value).pack(side = TOP, ipady = 5)
        
    #el command debe enviar a un método que registre la seleccion del radio button
    btn = Button(ventana, text = 'Continuar',  
                              command = ventana.destroy).pack(side='top', pady=10)
    

def main():
    master = Tk() 
    #Tamaño de la ventana
    #master.geometry("500x400") 
    master.title('Diagnóstico de Enfermedades')
    
    
    titulo=Label(master,justify=CENTER, text='Diagnóstico de Enfermedades', wraplength=450, pad=10)
    titulo.pack()
    titulo.config(font=("Courier", 35))
    
    descrip = "Descripción sobre la aplicación"
    
    description=Label(master,justify=CENTER, text=descrip, wraplength=450, pad=10)
    description.pack()
    
    
      
    btn = Button(master, text = 'Comenzar',  
                              command = ventana_preguntas).pack(side='top', pady=20)
    

    mainloop() 


main()