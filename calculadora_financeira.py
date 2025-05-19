from tkinter import * 
from tkinter import messagebox
from tkinter import ttk


class CalculadoraFinanceira:
    
    def __init__(self, master=None):
        self.renda = None
        self.custosnecessarios = 0
        self.custosimprevistos = 0
        self.custosdesnecessarios = 0
        self.i = 1
        self.master = master
        master.title("Calculadora Financeira Pessoal")
        master.geometry("600x400")
        master.configure(bg='#f0f0f0')
        
        self.frame_principal = Frame(master, bg='#f0f0f0')
        self.frame_principal.pack(pady=10)
        self.frame_preview = Frame(master, bg='#f0f0f0')
        self.frame_preview.pack(pady=10)
        
        self.titulo = Label(self.frame_principal,
                          text="Controle de Gastos Mensais",
                          font=("Arial", 14, "bold"),
                          bg='#f0f0f0')
        
        self.titulo.grid(row=0, column=0, columnspan=3, pady=10)
        self.label_renda = Label (self.frame_principal,
                                 text = "Informe sua renda",
                                font=("Arial", 14),
                                 bg='#f0f0f0',
                                 anchor= 'w') 
        self.retangulos = Canvas(self.frame_principal, width = 100,height = 40)
        self.retangulos.grid(row = 1, column = 0, columnspan = 3 )
        self.criar_retangulos('lightblue', 'grey', 'grey',1)   
        
                                                                                             
        self.label_renda.grid(row=2, column=0,columnspan=3,padx = 10,pady = 5)
        self.renda1_entry = Entry(self.frame_principal, font= ("Arial", 12))
        self.renda1_entry.grid(row=3, column = 0, columnspan = 3,padx = 10)
        
        
        self.botaoOk = Button(self.frame_principal, 
                              font= ("Arial", 12),
                              text="ok",
                              bg='#4CAF50',
                              fg = 'white',
                              command = self.segundafase)
        self.botaoOk.grid(row = 4,column = 0, columnspan=3,ipadx=20, ipady= 2,padx = 10,pady = 10)

    def segundafase(self):
        try:
         renda = float(self.renda1_entry.get() or 0)

        except ValueError:
            messagebox.showinfo("Erro","Insira uma renda válida")
            self.renda1_entry.delete(0,END)
            return
         
        if(renda <= 0):
            messagebox.showerror("Erro","Insira uma renda válida")
            self.renda1_entry.delete(0,END)
            return
        
        else:
            self.renda = renda
            self.remover_retangulos()
            self.botaoOk.destroy()
            self.renda1_entry.destroy()
            self.label_renda.destroy()
        
        self.criar_retangulos('grey','lightblue','grey',2)
        self.label_segundafase = Label(self.frame_principal,
                                  font= ("Arial", 14),
                                  text="Informe seus gastos abaixo",
                                  )
        self.label_segundafase.grid(row=2, column=0,columnspan=3)
        self.label_titulo = Label(self.frame_principal,
                                  font=("Arial", 12),
                                  text="Título",
                                  )
        self.label_titulo.grid(row=3,column=0,padx=(0,50),pady=10)
        self.label_classificacao = Label(self.frame_principal,
                                  font=("Arial", 12),
                                  text="Classificação",
                                  )
        self.label_classificacao.grid(row=3,column=1, padx=(0,45), pady= 10)
        self.label_custo =  Label(self.frame_principal,
                                  font=("Arial", 12),
                                  text="Custo",
                                  )
        self.label_custo.grid(row=3, column=2, pady= 10)
        self.entry_titulo = Entry(self.frame_principal,
                                  font=("Arial", 12),
                                  width=10)
        self.entry_titulo.grid(row=4,column=0, padx=(0,50))
        classificacoes = ["Necessário", "Imprevisto", "Desnecessário"]
        
        self.classificar = ttk.Combobox(self.frame_principal,values= classificacoes, state="readonly",width= 15)
        self.classificar.grid(row= 4,column = 1, padx=(0,45))
        self.entry_custo = Entry(self.frame_principal,
                                  font=("Arial", 12),
                                  width=10)
        self.entry_custo.grid(row=4,column= 2)
        self.labelprevia = Label(self.frame_preview,
                                 font=("Arial", 12),
                                 text="Prévia de Lançamentos")
        self.labelprevia.grid(row=0, column = 0, columnspan= 2)
        self.botaoadicionar = Button(self.frame_preview, 
                              font= ("Arial", 12),
                              text="Adicionar",
                              bg='#FFD700',
                              fg = 'white',
                              command = self.adicionarpreview)
        
        self.botaoadicionar.grid(row=1,column=0)
        self.botaoconcluir = Button(self.frame_preview, 
                              font= ("Arial", 12),
                              text="Concluir",
                              bg='#4CAF50',
                              fg = 'white',
                              command = self.terceirafase)
        self.botaoconcluir.grid(row=1,column=1)


    
    def adicionarpreview(self):
        if(self.entry_titulo.get().strip() == ""):
            messagebox.showerror("Erro", "Insira um título")
            return
        elif(self.classificar.get().strip() == ""):
            messagebox.showerror("Erro", "Insira uma classificação")
            return
        elif(self.entry_custo.get().strip() == ""):
            messagebox.showerror("Erro", "Insira um custo")
            return

        try: 
         custo = float(self.entry_custo.get() or 0)
        except ValueError:
         messagebox.showerror("Erro","Insira um custo válido")
         self.entry_custo.delete(0,END)
         return   
        if (custo == 0):
            messagebox.showerror("Erro","Insira um custo válido")
            return
        
        elif (self.classificar.get() == "Necessário"):
            self.custosnecessarios += custo
        elif(self.classificar.get() == "Imprevisto"): 
            self.custosimprevistos += custo
        elif(self.classificar.get() == "Desnecessário"):
            self.custosimprevistos += custo
        if self.i == 1:
            self.labelprevia.grid(row=0, column = 1, columnspan=2)
        if self.i < 1000:
            self.label1 = Label(self.frame_preview,
                                font=("Arial", 12),
                                text = self.i,
                                width = 15)
            self.label1.grid(row=self.i, column=0)

            self.label2 = Label(self.frame_preview,
                                font=("Arial", 12),
                                text= self.entry_titulo.get(),
                                width = 15)
            self.label2.grid(row=self.i, column=1)

            self.label3 = Label(self.frame_preview,
                                font=("Arial", 12),
                                text= self.classificar.get(),
                                width = 15)
            self.label3.grid(row=self.i, column=2)
            
            self.label4 = Label(self.frame_preview,
                                font=("Arial", 12),
                                text= custo,
                                width= 15)
            self.label4.grid(row=self.i,column = 3)
            self.i += 1
            self.botaoadicionar.grid(row=self.i, column = 1)
            self.botaoconcluir.grid(row=self.i,column = 2)
            self.entry_titulo.delete("0", END)
            self.entry_custo.delete("0", END)
            self.classificar.set("")

    def terceirafase(self):
        if(self.i == 1):
          messagebox.showerror("Erro", "Insira pelo menos um gasto")
          return
        self.frame_preview.destroy()
        self.entry_custo.destroy()
        self.entry_titulo.destroy()
        self.classificar.destroy()
        self.label_classificacao.destroy()
        self.label_titulo.destroy()
        self.label_custo.destroy()
        self.label_segundafase.destroy()
        self.remover_retangulos()
        self.criar_retangulos('grey','grey','lightblue',3)
        self.labelterceirafase = Label(self.frame_principal,
                                       font=("Arial", 14),
                                       text="Resultados")
        self.labelterceirafase.grid(row=2,column=0,columnspan=2)

        saldo = self.renda - self.custosdesnecessarios - self.custosimprevistos - self.custosnecessarios
        self.labelsaldo1 = Label(self.frame_principal,
                                 font=("Arial", 12),
                                 text="Seu saldo é de:")
        self.labelsaldo1.grid(row=3, column=0)
        
        if(saldo > 0):
            self.labelsaldo2 = Label(self.frame_principal,
                                     font=("Arial", 12),
                                     fg="green",
                                     text=(f"R$ {saldo}"))
        else:
            self.labelsaldo2 = Label(self.frame_principal,
                                     font=("Arial",12),
                                     fg = "red",
                                     text=(f"R$ {saldo}"))
        self.labelsaldo2.grid(row=3,column=1)
        self.labelnecessarios1 = Label(self.frame_principal,
                                       font=("Arial", 12),
                                       text="Seus gastos necessários foram de:")
        self.labelnecessarios1.grid(row=4,column=0)
        self.labelnecessarios2 = Label(self.frame_principal,
                                       font=("Arial", 12),
                                       text=(f"R$ {self.custosnecessarios}"))
        self.labelnecessarios2.grid(row=4,column=1)
        self.labeldesnecessarios1 = Label(self.frame_principal,
                                          font=("Arial", 12),
                                          text="Seus gastos desnecessários foram de:")
        self.labeldesnecessarios1.grid(row=5,column=0)
        self.labeldesnecessarios2 = Label(self.frame_principal,
                                       font=("Arial", 12),
                                       text=(f"R$ {self.custosdesnecessarios}"))
        self.labeldesnecessarios2.grid(row=5,column=1)
        self.labelimprevistos1 = Label(self.frame_principal,
                                          font=("Arial", 12),
                                          text="Seus gastos imprevistos foram de:")
        self.labelimprevistos1.grid(row=6,column=0)
        self.labelimprevistos2 = Label(self.frame_principal,
                                       font=("Arial", 12),
                                       text=(f"R$ {self.custosimprevistos}"))
        self.labelimprevistos2.grid(row=6,column=1)
        
    def criar_retangulos(self,cor1,cor2,cor3,numero):
        self.retangulo1 = self.retangulos.create_rectangle(10,10,35,35, outline = 'black', fill= cor1, tags='retangulo1')
        self.retangulo2 = self.retangulos.create_rectangle(35,10,60,35, outline = 'black', fill= cor2, tags= 'retangulo2')
        self.retangulo3 = self.retangulos.create_rectangle(60,10,85,35, outline= 'black', fill= cor3, tags='retangulo3')
        if(numero == 1):
            self.texto1 = self.retangulos.create_text(22,22,text="1",fill='black',font=("Arial",14))
        elif (numero == 2):
            self.texto2 = self.retangulos.create_text(47,22,text="2",fill='black',font=("Arial",14))
        elif (numero == 3):
            self.texto1 = self.retangulos.create_text(72,22,text="3",fill='black',font=("Arial",14))
    def remover_retangulos(self):
        self.retangulos.delete('retangulo1')
        self.retangulos.delete('retangulo2')
        self.retangulos.delete('retangulo3')
    
 
    def calcular(self): 
        try:
            renda = float(self.renda_entry.get() or 0)
            necessarios = float(self.necessarios_entry.get() or 0)
            imprevistos = float(self.imprevistos_entry.get() or 0)
            desnecessarios = float(self.desnecessarios_entry.get() or 0)
            
            if renda == 0:
                messagebox.showwarning("Aviso", "A renda mensal não pode ser zero!")
                return

            saldo = renda - necessarios - imprevistos - desnecessarios
            percentual = (desnecessarios / renda) * 100 if renda > 0 else 0

            resultado_texto = f"Saldo Disponível: R$ {saldo:.2f}"
            percentual_texto = f"Percentual gasto desnecessariamente: {percentual:.2f}%"

            if saldo >= 0:
                self.label_resultado.config(text=resultado_texto, fg='green')
            else:
                self.label_resultado.config(text=f"Déficit: R$ {abs(saldo):.2f}", fg='red')

            self.label_percentual.config(text=percentual_texto)

        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira apenas números nos campos. \nUse ponto para decimais (ex: 1000.50)")

    
root = Tk()
app = CalculadoraFinanceira(root) 
root.mainloop()     

