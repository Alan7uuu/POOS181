from tkinter import Tk,Frame,Button,messagebox
def mostrarmensaje():
    messagebox.showinfo("AVISO","ESTE MENSAJE ES PARA AVISAR ALGO")
    messagebox.showerror("TODO FALLO CON EXITO")
    print(messagebox.askokcancel("Pregunta:", "el o ella jugo con tu corazon"))
    print(messagebox.askquestion("¿si o no?"))
    print(messagebox.askretrycancel("si o no?"))
    print(messagebox.askyesno("si o no?"))
    print(messagebox.askyesnocancel("¿si o no?"))
# 5 funciones para agregar a botones
def agregarboton():
    botonverd.config(text="+",bg="green", fg="white")
    botonnuevo= Button(seccion3,text="BotonNuevoo")
    botonnuevo.pack()

#1. instanciamos un objeto ventana
ventana= Tk()
ventana.title("Practica 11: 3 Frames")
ventana.geometry("600x400")

#2.definir la secciones de la ventana
seccion1=Frame(ventana, bg= "green")
seccion1.pack(expand= True,fill='both')
seccion2=Frame(ventana, bg= "blue")
seccion2.pack(expand= True,fill='both')
seccion3=Frame(ventana, bg= "white")
seccion3.pack(expand= True,fill='both')

#botones
botonazul=Button(seccion1, text="boton azul", bg="blue",fg="white", command=mostrarmensaje)
botonazul.place(x=60, y=60)
botonverd=Button(seccion1, text="boton verde", bg="green", fg="white", command=agregarboton)
botonverd.grid(row=0 ,column=1)
botonegro=Button(seccion1, text="boton negro", bg="black", fg="white")
botonegro.grid(row=1, column=1)
botonred=Button(seccion3,text="boton rojo", bg="red")
botonred.pack()
#main ejecucion de la ventana// el main debe ir al final ya que no se ejecutaria bien

ventana.mainloop()