from tkinter import *
#variáveis globais:
p = 100
pontos = 0
pp = 100

#300x250 TAMANHO DA IMAGEM DAS CPU'S
#520 x 60 PERGUNTAS



##########################################################
class Tela:

    def __init__(self, event):

        global p
        global pontos
        global pp
       
        img1 = PhotoImage(file="wallpaper.png")
        self.img = Label(j1, image=img1)
        self.img.img1 = img1
        self.img.place(x=0,y=0)


        img2 = PhotoImage(file="wallpaper.png")
        self.imgg = Label(j1, image=img2)
        self.imgg.img2 = img2
        self.imgg.place(x=0,y=640)

        self.d1 = Label(j1, text="1º Desafio - PROCESSADORES")
        self.d1["font"] = ("Cambria", "50", "bold")
        self.d1.config(bg="white", foreground="red")
        self.d1.place(x="50", y="250")

        self.bt1 = Button(j1, text="INICIAR")
        self.bt1.config(bg="green", foreground="white")
        self.bt1["font"] = ("Arial", "30")
        self.bt1.place(x=390, y=500)
        self.bt1.bind("<Button-1>", self.ex1)


    def ex1(self, event):
        
        global pontos
        global p
        global pp
        self.d1.place(x=10000)
        self.bt1.place(x=10000)
        pontos = Label(j1, text="Pontos:")
        pontos["font"] = ("Arial", "18", "bold")
        pontos.config(bg="white", foreground="red")
        pontos.place(x=820, y=130)
        
        pp = Label(j1,text=p)
        pp["font"] = ("Arial", "18", "bold")
        pp.config(bg="white", foreground="red")
        pp.place(x=920, y=131)

                
        self.p1 = Label(j1, text="Qual o significado da sigla CPU?")
        self.p1["font"] = ("Arial", "30", "bold")
        self.p1.config(bg="black", foreground="lime",)
        self.p1.place(x="180", y="180")

                
        self.r1 = Button(j1, text="1- Unidade cerebral  do computador")
        self.r1["font"] = ("Arial", "25", "bold")
        self.r1.config(bg="#FEBF01", foreground="black")
        self.r1.place(x="210", y="300")
        self.r1.bind("<Button-1>", self.rE)


        self.r2 = Button(j1, text="2- Cérebro do computador unitário")
        self.r2["font"] = ("Arial", "25", "bold")
        self.r2.config(bg="#FEBF01", foreground="black")
        self.r2.place(x="220", y="380")
        self.r2.bind("<Button-1>", self.rE)

        self.r3 = Button(j1, text="3- Unidade central de processamento")
        self.r3["font"] = ("Arial", "25", "bold")
        self.r3.config(bg="#FEBF01", foreground="black")
        self.r3.place(x="200", y="460")
        self.r3.bind("<Button-1>", self.rC)

        self.r4 = Button(j1, text="4- Cérebro da unidade central")
        self.r4["font"] = ("Arial", "25", "bold")
        self.r4.config(bg="#FEBF01", foreground="black")
        self.r4.place(x="260", y="540")
        self.r4.bind("<Button-1>", self.rE)

    def rE(self, event):
        global p
        global pp
        global pontos
        p = p - 50
        pp.place(x=100000)
        
        pp = Label(j1,text=p)
        pp["font"] = ("Arial", "18", "bold")
        pp.config(bg="white", foreground="red")
        
        pp.place(x=920, y=131)

        self.p1.place(x=10000)
        self.p1 = Label(j1, text="Escolha o processador com maior desempenho")
        self.p1["font"] = ("Arial", "30", "bold")
        self.p1.config(bg="black", foreground="lime",)
        self.p1.place(x="50", y="180")

        self.r1.place(x=10000)
        self.r2.place(x=10000)
        self.r3.place(x=10000)
        self.r4.place(x=10000)

        cpu = PhotoImage(file="cpu1.png")
        self.cpuu = Button(j1, image=cpu)
        self.cpuu.cpu = cpu
        self.cpuu.place(x=150,y=300)
        self.cpuu.bind("<Button-1>", self.res)

        cpu2 = PhotoImage(file="cpu2.png")
        self.cpuu2 = Button(j1, image=cpu2)
        self.cpuu2.cpu2 = cpu2
        self.cpuu2.place(x=550,y=300)
        self.cpuu2.bind("<Button-1>", self.res2)

    def rC(self, event):
        
        global p
        global pp
        global pontos
        p = p + 50
        pp.place(x=100000)
        
        pp = Label(j1,text=p)
        pp["font"] = ("Arial", "18", "bold")
        pp.config(bg="white", foreground="red")
        
        pp.place(x=920, y=131)

        self.r1.place(x=10000)
        self.r2.place(x=10000)
        self.r3.place(x=10000)
        self.r4.place(x=10000)
#########################################################################################
        self.p1.place(x=10000)
        self.p1 = Label(j1, text="Escolha o processador com maior desempenho")
        self.p1["font"] = ("Arial", "30", "bold")
        self.p1.config(bg="black", foreground="lime",)
        self.p1.place(x="50", y="180")
        
        
        cpu = PhotoImage(file="cpu1.png")
        self.cpuu = Button(j1, image=cpu)
        self.cpuu.cpu = cpu
        self.cpuu.place(x=150,y=300)
        self.cpuu.bind("<Button-1>", self.res)

        cpu2 = PhotoImage(file="cpu2.png")
        self.cpuu2 = Button(j1, image=cpu2)
        self.cpuu2.cpu2 = cpu2
        self.cpuu2.place(x=550,y=300)
        self.cpuu2.bind("<Button-1>", self.res2)

    def res(self, event):
        
        global p
        global pp
        global pontos
        p = p + 50
        pp.place(x=100000)
        
        pp = Label(j1,text=p)
        pp["font"] = ("Arial", "18", "bold")
        pp.config(bg="white", foreground="red")
        
        pp.place(x=920, y=131)
        self.cpuu.place(x=100000)
        self.cpuu2.place(x=100000)

        self.p1.place(x=10000)
        self.p1 = Label(j1, text="Se fossemos comparar o CPU com uma parte do “corpo” do computador,\n qual parte ele seria ?")
        self.p1["font"] = ("Arial", "20", "bold")
        self.p1.config(bg="black", foreground="lime",)
        self.p1.place(x="7", y="180")
        ######################################
        
        #P1
        p1 = PhotoImage(file="p1.png")
        self.pp1 = Button(j1, image=p1)
        self.pp1.p1 = p1
        self.pp1.place(x=230,y=300)
        self.pp1.bind("<Button-1>", self.resC)
        

        #P2
        p2 = PhotoImage(file="p2.png")
        self.pp2 = Button(j1, image=p2)
        self.pp2.p2 = p2
        self.pp2.place(x=230,y=380)
        self.pp2.bind("<Button-1>", self.resE)
        
    

        #P3
        p3 = PhotoImage(file="p3.png")
        self.pp3 = Button(j1, image=p3)
        self.pp3.p3 = p3
        self.pp3.place(x=230,y=460)
        self.pp3.bind("<Button-1>", self.resE)


        #P4
        p4 = PhotoImage(file="p4.png")
        self.pp4 = Button(j1, image=p4)
        self.pp4.p4 = p4
        self.pp4.place(x=230,y=540)
        self.pp4.bind("<Button-1>", self.resE)
        
        
    def res2(self, event):

        global p
        global pp
        global pontos
        p = p - 50
        pp.place(x=100000)
        
        pp = Label(j1,text=p)
        pp["font"] = ("Arial", "18", "bold")
        pp.config(bg="white", foreground="red")
        
        pp.place(x=920, y=131)
        
        self.cpuu.place(x=100000)
        self.cpuu2.place(x=100000)

        self.p1.place(x=10000)
        self.p1 = Label(j1, text="Se fossemos comparar o CPU com uma parte do “corpo” do computador,\n qual parte ele seria ?")
        self.p1["font"] = ("Arial", "20", "bold")
        self.p1.config(bg="black", foreground="lime",)
        self.p1.place(x="7", y="180")

        #P1
        p1 = PhotoImage(file="p1.png")
        self.pp1 = Button(j1, image=p1)
        self.pp1.p1 = p1
        self.pp1.place(x=230,y=300)
        self.pp1.bind("<Button-1>", self.resC)

        #P2
        p2 = PhotoImage(file="p2.png")
        self.pp2 = Button(j1, image=p2)
        self.pp2.p2 = p2
        self.pp2.place(x=230,y=380)
        self.pp2.bind("<Button-1>", self.resE)


        #P3
        p3 = PhotoImage(file="p3.png")
        self.pp3 = Button(j1, image=p3)
        self.pp3.p3 = p3
        self.pp3.place(x=230,y=460)
        self.pp3.bind("<Button-1>", self.resE)


        #P4
        p4 = PhotoImage(file="p4.png")
        self.pp4 = Button(j1, image=p4)
        self.pp4.p4 = p4
        self.pp4.place(x=230,y=540)
        self.pp4.bind("<Button-1>", self.resE)

    def resE(self,event):

        global p
        global pp
        global pontos
        p = p - 50
        pp.place(x=100000)
        
        pp = Label(j1,text=p)
        pp["font"] = ("Arial", "18", "bold")
        pp.config(bg="white", foreground="red")
        
        pp.place(x=920, y=131)

        self.pp1.place(x=10000)
        self.pp2.place(x=10000)
        self.pp3.place(x=10000)
        self.pp4.place(x=10000)

        self.p1.place(x=10000)

        self.p1.place(x=10000)
        self.p1 = Label(j1, text="Qual unidade de medida define a velocidade do CPU?")
        self.p1["font"] = ("Arial", "26", "bold")
        self.p1.config(bg="black", foreground="lime",)
        self.p1.place(x="50", y="180")
##################################################################################
        #U1
        u1 = PhotoImage(file="u1.png")
        self.uu1 = Button(j1, image=u1)
        self.uu1.u1 = u1
        self.uu1.place(x=230,y=300)
        self.uu1.bind("<Button-1>",self.ressE)
     

        #U2
        u2 = PhotoImage(file="u2.png")
        self.uu2 = Button(j1, image=u2)
        self.uu2.u2 = u2
        self.uu2.place(x=230,y=380)
        self.uu2.bind("<Button-1>",self.ressC)
        


        #U3
        u3 = PhotoImage(file="u3.png")
        self.uu3 = Button(j1, image=u3)
        self.uu3.u3 = u3
        self.uu3.place(x=230,y=460)
        self.uu3.bind("<Button-1>",self.ressE)


        #U4
        u4 = PhotoImage(file="u4.png")
        self.uu4 = Button(j1, image=u4)
        self.uu4.u4 = u4
        self.uu4.place(x=230,y=540)
        self.uu4.bind("<Button-1>",self.ressE)

        

    def resC(self,event):

        global p
        global pp
        global pontos
        p = p + 50
        pp.place(x=100000)
        
        pp = Label(j1,text=p)
        pp["font"] = ("Arial", "18", "bold")
        pp.config(bg="white", foreground="red")
        
        pp.place(x=920, y=131)

        self.pp1.place(x=10000)
        self.pp2.place(x=10000)
        self.pp3.place(x=10000)
        self.pp4.place(x=10000)

        self.p1.place(x=10000)

        self.p1.place(x=10000)
        self.p1 = Label(j1, text="Qual unidade de medida define a velocidade do CPU?")
        self.p1["font"] = ("Arial", "26", "bold")
        self.p1.config(bg="black", foreground="lime",)
        self.p1.place(x="50", y="180")
###################################################################

     #U1
        u1 = PhotoImage(file="u1.png")
        self.uu1 = Button(j1, image=u1)
        self.uu1.u1 = u1
        self.uu1.place(x=230,y=300)
        self.uu1.bind("<Button-1>",self.ressE)
     

        #P2
        u2 = PhotoImage(file="u2.png")
        self.uu2 = Button(j1, image=u2)
        self.uu2.u2 = u2
        self.uu2.place(x=230,y=380)
        self.uu2.bind("<Button-1>",self.ressC)
        


        #P3
        u3 = PhotoImage(file="u3.png")
        self.uu3 = Button(j1, image=u3)
        self.uu3.u3 = u3
        self.uu3.place(x=230,y=460)
        self.uu3.bind("<Button-1>",self.ressE)
        


        #P4
        u4 = PhotoImage(file="u4.png")
        self.uu4 = Button(j1, image=u4)
        self.uu4.u4 = u4
        self.uu4.place(x=230,y=540)
        self.uu4.bind("<Button-1>",self.ressE)

    def ressE(self, event):

        global p
        global pp
        global pontos
        p = p - 50
        pp.place(x=100000)
        
        pp = Label(j1,text=p)
        pp["font"] = ("Arial", "18", "bold")
        pp.config(bg="white", foreground="red")
        pp.place(x=920, y=131)

        self.p1.place(x=100000)

        self.uu1.place(x=91000)
        self.uu2.place(x=91000)
        self.uu3.place(x=91000)
        self.uu4.place(x=91000)
#####################################################################
        self.d1 = Label(j1, text="2º Desafio - Memória RAM")
        self.d1["font"] = ("Cambria", "50", "bold")
        self.d1.config(bg="white", foreground="red")
        self.d1.place(x="100", y="250")

        self.bt1 = Button(j1, text="INICIAR")
        self.bt1.config(bg="green", foreground="white")
        self.bt1["font"] = ("Arial", "30")
        self.bt1.place(x=390, y=500)

    def ressC(self, event):

        global p
        global pp
        global pontos
        p = p + 50
        pp.place(x=100000)
        
        pp = Label(j1,text=p)
        pp["font"] = ("Arial", "18", "bold")
        pp.config(bg="white", foreground="red")
        
        pp.place(x=920, y=131)
        self.p1.place(x=100000)

        self.uu1.place(x=91000)
        self.uu2.place(x=91000)
        self.uu3.place(x=91000)
        self.uu4.place(x=91000)
#################################################################
        self.d1 = Label(j1, text="2º Desafio - Memória RAM")
        self.d1["font"] = ("Cambria", "50", "bold")
        self.d1.config(bg="white", foreground="red")
        self.d1.place(x="100", y="250")

        self.bt1 = Button(j1, text="INICIAR")
        self.bt1.config(bg="green", foreground="white")
        self.bt1["font"] = ("Arial", "30")
        self.bt1.place(x=390, y=500)
        
    
    

j1 = Tk()
Tela(j1)
j1.title("Simulador - Módulo 2                 |                    BY EDUARDO")
j1.geometry("1000x700+100+30")
j1.config(bg="white")
j1.resizable(width=False, height=False)
j1.mainloop()
