from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import filedialog as fd
from tkinter import messagebox
import pandas as pd
import threading as thread
from ULTOTRAPRUEBAMAXCROMATPAPER import algoritmo
from plot import plot
from reporte import generarPDF

class App(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.matrizdatos = None
        self.matrizdatosb = None
        self.matrizpronostico = None
        self.matrizreal = None
        self.t1= None
        self.t2= None
        self.detenerP = False
        self.entrytimevar = None
##        self.messagebox = ttk.Messagebox
        self.estilo = ttk.Style()
        self.estilo.theme_use('clam')

        self.estilo.configure('TButton',font='helvetica 14', foreground='white', background='#2196f3')
        self.estilo.configure('TLabel', font='helvetica 12 bold')
        self.estilo.map("TButton",
            foreground=[('pressed', 'disabled', 'while'), ('active', 'white')],
            background=[('pressed', '!disabled', '#0064bd'), ('active','!disabled','#0077cc' )]
            ) 
        
       
        self.content = ttk.Frame(master, padding=(3,3,12,12))

        self.myFont = font.Font(family='Helvetica', size=14)
        self.btncargarHist = ttk.Button(self.content,text="Cargar Historicos", command= self.abrirHistoricos)
        self.lbnombreArchivo = ttk.Label(self.content, text="Archivo")
        self.resultsContents2 = StringVar()
       
        self.lbtabla1 = ttk.Label(self.content, text="Historico de Datos")
        self.tb1 = ttk.Frame(self.content, borderwidth=5, relief="ridge", width=200, height=200,)

        self.btncargarMeses = ttk.Button(self.content,text="Cargar Datos a Predecir", command = self.abrirMuestra)
        self.lbtime = ttk.Label(self.content, text="Finaliza en:")
        self.lbshow= ttk.Label(self.content,text="0")
        self.lbnombreArchivo2 = ttk.Label(self.content, text="Archivo")
        self.resultsContents3 = StringVar()
        self.lbtabla2 = ttk.Label(self.content, text="Muestra a Estimar")
        self.lbmeses = ttk.Label(self.content, text="Meses a predecir")
        self.lbvalorEstimado = ttk.Label(self.content, text="Valor Estimado")
        self.tb2 = ttk.Frame(self.content, borderwidth=5, relief="ridge", width=200, height=200)

        self.btnIniciar = ttk.Button(self.content,text="Iniciar", command = self.iniciarPrediccion)
        self.btnCancelar = ttk.Button(self.content,text="Graficar" , state='disabled', command = self.mostrarGraficos)
        self.btnreporte = ttk.Button(self.tb1,text="Generar Reporte" , state='disabled', command = self.reporte)
        
        self.lbtiempo = ttk.Label(self.content, text="Tiempo de Ejecución (Minutos)")
##      self.entrytiempovar = StringVar()
        self.entrytiempo = ttk.Entry(self.content, width=10,font=('Arial',12))
        self.entrytiempo.insert(0,'1')
        
        self.lbmejor1 = ttk.Label(self.content, text="Valores estimados")
        self.lbR2= ttk.Label(self.content, text="R^2")

        self.tb3 = ttk.Frame(self.content, borderwidth=5, relief="ridge", width=200, height=200)
        self.tb4 = ttk.Frame(self.content, borderwidth=5, relief="ridge", width=200, height=200)

        self.content.grid(column=0, row=0, sticky=(N, S, E, W))
        self.btncargarHist.grid(column=0, row=0, columnspan=2)
        self.lbnombreArchivo.grid(column=0, row=1, columnspan=2)
        self.lbtabla1.grid(column=0, row=2, columnspan=2)
        self.tb1.grid(column=0, row=3, columnspan=2, rowspan=2, sticky=(N, S, E, W))

        self.btncargarMeses.grid(column=2, row=0, columnspan=2)
        self.lbtabla2.grid(column=2, row=2, columnspan=2, sticky=(N, S, E, W))
        self.lbtime.grid(column=2, row=1)
        self.lbshow.grid(column=3, row=1)
        self.tb2.grid(column=2, row=3,columnspan=2, rowspan=2, sticky=(N, S, E, W))

        self.btnIniciar.grid(column=5, row=0)
        self.btnCancelar.grid(column=5, row=1)
        self.lbtiempo.grid(column=4, row=0)
        self.btnreporte.grid(column=0, row=6)
        self.entrytiempo.grid(column=4, row=1)
       

        self.lbmejor1.grid(column=4, row=2)
        self.lbR2.grid(column=5, row=2)

        self.tb3.grid(column=4, row=3, rowspan=2, sticky=(N, S, E, W) )
        self.tb4.grid(column=5, row=3, rowspan=2, sticky=(N, S, E, W))


        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.content.columnconfigure(0, weight=3)
        self.content.columnconfigure(1, weight=3)
        self.content.columnconfigure(2, weight=3)
        self.content.columnconfigure(3, weight=3)
        self.content.columnconfigure(4, weight=3)
        self.content.columnconfigure(5, weight=3)
        self.content.rowconfigure(3, weight=3)
        self.content.rowconfigure(4, weight=3)
        ##
        ###############IMPORTANTE
        ##Tkinter doesn't allow you to link regular Python lists to a listbox.
        ##As we saw with widgets like entry, we need to use a StringVar as an intermediary. 
        ##choices = ["apple", "orange", "banana"]
        ##choicesvar = StringVar(value=choices)
        ##l = Listbox(parent, listvariable=choicesvar)
        self.resultsContents = StringVar()
        self.resultsContents2 = StringVar()
        self.lbshow['textvariable'] = self.resultsContents
       

        #creación de Listbox  
        self.lbdatosH = Listbox(self.tb1, height=20, width=50)

        self.lbdatosH.grid(column=0, row=0, columnspan=2,sticky=(N,E,W),pady=5, padx=5)
        self.s = ttk.Scrollbar(self.tb1, orient=VERTICAL, command=self.lbdatosH.yview)
        self.scrollh = ttk.Scrollbar(self.tb1, orient=HORIZONTAL, command=self.lbdatosH.xview)
        self.scrollh.grid(column=0, row=1, columnspan=2, sticky=(W,E))
        self.s.grid(column=1, row=0, sticky=(N,S,E))
        self.lbdatosH['yscrollcommand'] = self.s.set
        self.lbdatosH['xscrollcommand'] = self.scrollh.set

        

        #creación de Listbox
        self.lisdatosMuestra = Listbox(self.tb2, height=20, width=25)
        self.lisdatosMuestra.grid(column=0, row=0, columnspan=2,sticky=(N,E,W),pady=5, padx=5)
        self.s = ttk.Scrollbar(self.tb2, orient=VERTICAL, command=self.lisdatosMuestra.yview)
        self.s.grid(column=1, row=0, sticky=(N,S,E))
        self.lisdatosMuestra['yscrollcommand'] = self.s.set


        #creación de Listbox
        self.lbdatosPred = Listbox(self.tb3, height=20,width=50)

        self.lbdatosPred.grid(column=0, row=0, columnspan=2,sticky=(N,E,W), pady=5, padx=5)
        self.s = ttk.Scrollbar(self.tb3, orient=VERTICAL, command=self.lbdatosPred.yview)
        self.scrollh2 = ttk.Scrollbar(self.tb3, orient=HORIZONTAL, command=self.lbdatosPred.xview)
        self.scrollh2.grid(column=0, row=1, columnspan=2, sticky=(W,E))
        ##scrollh.grid(column=0, row=1, columnspan=2, sticky=(W,E))
        self.s.grid(column=1, row=0, sticky=(N,S,E))
        self.lbdatosPred['yscrollcommand'] = self.s.set
        self.lbdatosPred['xscrollcommand'] = self.scrollh2.set
        

        self.lisdatosR = Listbox(self.tb4, height=20, width=25)
        self.lisdatosR.grid(column=0, row=0, columnspan=2,sticky=(N,E,W),pady=5, padx=5)
        self.s = ttk.Scrollbar(self.tb4, orient=VERTICAL, command=self.lisdatosR.yview)
        self.scrollh3 = ttk.Scrollbar(self.tb4, orient=HORIZONTAL, command=self.lisdatosR.xview)
        self.scrollh3.grid(column=0, row=1, columnspan=2, sticky=(W,E))
        self.s.grid(column=1, row=0, sticky=(N,S,E))
        self.lisdatosR['yscrollcommand'] = self.s.set
        self.lisdatosR['xscrollcommand'] = self.scrollh3.set
            
    rutaArchivo = None
    def abrirHistoricos(self):
        rutaArchivo = fd.askopenfilename()
        print(rutaArchivo)
        if rutaArchivo is not None and rutaArchivo != '':
            print('No es none',rutaArchivo)
            self.lbnombreArchivo['textvariable'] = self.resultsContents2
            self.resultsContents2.set(rutaArchivo.split('/')[-1])
            self.cargarTablaHistoricos(rutaArchivo)
            
        else:
            print('Error  abrir archivo')
            
    def abrirMuestra(self):
        rutaArchivo = fd.askopenfilename()
        print(rutaArchivo)
        if rutaArchivo is not None and rutaArchivo != '':
            
##            self.resultsContents.set(rutaArchivo.split('/')[-1])
            self.cargarTablaMuestras(rutaArchivo)   
        else:
            print('Error  abrir archivo')
            
    def cargarTablaHistoricos(self, rutaArchivo):
        datos = self.leerDatos(rutaArchivo)
        self.lbdatosH.delete(0,'end')
        if datos is not None:
            self.matrizdatos = datos
            ff = ''
            for i in datos:
                for j in i:
                    ff += str(j )+'        '
                self.lbdatosH.insert('end', ff)
                ff = ''
    def cargarTablaMuestras(self, rutaArchivo):
        datos = self.leerDatos(rutaArchivo)
        self.lisdatosMuestra.delete(0,'end')
        if datos is not None:
            self.matrizdatosb = datos
            ff = ''
            for i in datos:
                for j in i:
                    ff += str(j )+'        '
                self.lisdatosMuestra.insert('end', ff)
                ff = ''
     ##IMPLEMENTAR LA LECTURA DE LOS DATOS GENERAL , FILTRANDO SOLO LAS COLUMNAS Y FILAS CON DATOS
    def leerDatos(self,pathfile):
        try:
            matrizdatos = pd.read_excel(pathfile, header=None)
            matrizdatos = matrizdatos.dropna()
            return matrizdatos.to_numpy()
        except:
            print("Error file ")
            return None
        
    
    def cargaValorEstimados(self):
        ff = ''
        for i in self.matrizpronostico:
            self.lbdatosPred.insert('end', round(i,4))
            
    def convertir_a_minutos(self):
        
        try:
            if self.entrytiempo.get() != '':
                entrada = int(self.entrytiempo.get())
                self.entrytimevar = entrada*60
             
        except:
            print('error conversión dato')
    def iniciarPrediccion(self):
        self.convertir_a_minutos()
        
        if (self.matrizdatos is not None and self.matrizdatos != '' ) and (self.matrizdatosb is not None and  self.matrizdatosb != '') and (self.entrytimevar > 0):
            
            matrizdatos = self.matrizdatos.copy()
            matrizdatosb = self.matrizdatosb.copy()
            self.resultsContents.set(self.entrytimevar)
            self.t1 = thread.Thread(target=algoritmo, args=(self,matrizdatos, matrizdatosb))
            self.t1.start()
            self.schedule_check(self.t1)
        else:
           
            msj = 'Verifique que haya cargado los datos correctamente y que el tiempo de ejecución sea mayor a 0'
            messagebox.showerror(title='Error', message=msj)

    def mostrarGraficos(self):
        if(self.matrizpronostico is not None) and (self.matrizreal is not None):
            plot(self.matrizreal,self.matrizpronostico)
        else:
           
            msj = 'No se puede graficar datos inconclusos'
            messagebox.showerror(title='Error', message=msj)
    def reporte(self):
        if(self.matrizpronostico is not None) and (self.matrizreal is not None):
            self.t2 = thread.Thread(target=generarPDF, args=(self.matrizreal, self.matrizpronostico))
            self.t2.start()
##            generarPDF(self.matrizreal,self.matrizpronostico)
        else:
            msj = 'No se puede generar reportes con datos inconclusos'
            messagebox.showerror(title='Error', message=msj)
    def schedule_check(self,t):
        """
        Programar la ejecución de la función `check_if_done()` dentro de 
        un segundo.
        """
        self.after(1000, self.check_if_done, t)

    def check_if_done(self,t):
        # Si el hilo ha finalizado, restaruar el botón y mostrar un mensaje.
        if not t.is_alive():
            
            # Restablecer el botón.
            self.btnIniciar.config(text="Iniciar",command=self.iniciarPrediccion)
            self.btnCancelar.config(state='active')
            self.btnreporte.config(state='active')
            print(self.matrizpronostico)
            if self.matrizpronostico is not None:
                
                self.cargaValorEstimados()
            
            
        else:
            self.btnIniciar.config(text="Detener",command=self.detener)
            self.btnCancelar.config(state='disabled')
            print('ALIVE')
            
            self.resultsContents.set(int(self.resultsContents.get())-1)
            # Si no, volver a chequear en unos momentos.
            self.schedule_check(t)
    def detener(self):
        self.detenerP= True
        
        self.schedule_check(self.t1)
            
        print("detener")
root = Tk()
myapp = App(root)
myapp.master.title("APLICATIVO PROYECTO INVESTIGACIÓN")
myapp.master.minsize(1000, 600)
myapp.master.geometry('1200x600')
myapp.mainloop()


