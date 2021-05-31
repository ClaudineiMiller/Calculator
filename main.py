from tkinter import ttk as tk
from tkinter import *
from ttkthemes import ThemedTk
from tkinter import messagebox as mb

class Calculator():
    """ Classe principal - chama a janela window com todos os widgets. """
    def __init__(self):
        """ Inicializador da janela principal """
        self.window = ThemedTk(theme='plastik')
        self.window.title("Basic Calculator")
        self.window.resizable(0, 0)
        self.centraliza_window(360, 325)

        list_buttons_names = [
            ['7', '8', '9', '÷', '⌫', 'c'],
            ['4', '5', '6', 'x', '(', ')'],
            ['1', '2', '3', '−', 'x²', '√'],
            ['0', ',', '%', '+', '=']]

        self.btn_dict = {}
        self.ans_to_print = 0
        self.inp = StringVar()

        self.frame_display = tk.Frame(self.window)
        self.frame_display.pack(fill=BOTH)

        self.label_espaco = tk.Label(self.frame_display, font='Arial 30')
        self.label_espaco.pack(fill='x', ipady=30)

        self.display = tk.Entry(self.frame_display, font='Arial 20', text=self.inp)
        self.display.pack(fill='x', ipady=10)
        self.display.focus()

        self.frame_buttons = tk.Frame(self.window)
        self.frame_buttons.pack(fill="x")

        for i in range(len(list_buttons_names)):
            for j in range(len(list_buttons_names[i])):
                self.btn_dict['btn_{}'.format(str(list_buttons_names[i][j]))] = tk.Button(
                    self.frame_buttons, width=6, text=str(list_buttons_names[i][j]))
                self.btn_dict['btn_{}'.format(str(list_buttons_names[i][j]))].grid(
                    row=i+1, column=j, padx=1, pady=1, ipady=5
                )
                self.btn_dict['btn_'+str(list_buttons_names[i][j])].bind('<Button-1>', self.calculate)
        self.btn_dict['btn_='].grid(column=4, columnspan=2, sticky=E+W)

        print(self.btn_dict.values())

        self.window.mainloop()


    def calculate(self, event):
        self.button = event.widget.cget('text')
        try:
            if self.button == '√':
                ans = float(self.inp.get())**(0.5)
                ans_to_print = str(ans)
                self.inp.set(str(ans))
            elif self.button == 'c':
                self.inp.set('')
                self.display.focus()
            elif self.button == '⌫':
                self.inp.set(self.inp.get()[:len(self.inp.get())-1])
                self.display.focus()
            elif self.button == '=':
                self.ans_to_print = str(eval(self.inp.get()))
                self.inp.set(self.ans_to_print)
            elif self.button == 'x²':
                self.inp.set(self.inp.get() + '**' )
            elif self.button == 'x':
                self.inp.set(self.inp.get()+str('*'))
            elif self.button == '−':
                self.inp.set(self.inp.get()+str('-'))
            elif self.button == '÷':
                self.inp.set(self.inp.get()+str('/'))
            else:
                self.inp.set(self.inp.get()+str(self.button))
        except:
            self.inp.set('Operação Errada')


    def centraliza_window(self, comprimento, altura):
        """
        Dimensiona e centraliza a janela.

        recebe duas variáveis:
        comprimento - a largura da janela
        altura - a altura da janela
        """
        # Dimensões da janela
        self.comprimento = comprimento
        self.altura = altura
        # Resolução da tela
        self.comprimento_screen = self.window.winfo_screenwidth()
        self.altura_screen = self.window.winfo_screenheight()
        # Posição da janela
        self.pos_x = (self.comprimento_screen / 2) - (self.comprimento / 2)
        self.pos_y = (self.altura_screen / 2) - (self.altura / 2) - 10

        self.window.geometry(
            "{}x{}+{}+{}".format(
                int(self.comprimento),
                int(self.altura),
                int(self.pos_x),
                int(self.pos_y),
            )
        )


Calculator()
