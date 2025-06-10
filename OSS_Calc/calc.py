import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.grid(row =0, column=0, columnspan= 4, sticky="nsew",padx = 0, pady= 0 )
        #self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10) //pack -> grid (목적: 정렬)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
        ]

        for i in range(1,5): #1~5행 세로 크기 지정
            root.grid_rowconfigure(i, weight = 1)
        for j in range(4): #1~4 열 가로 크기 지정
            root.grid_columnconfigure(j,weight =1)


        for r, row in enumerate(buttons, start =1):
            for c, char in enumerate(row):
                btn = tk.Button(root, text=char, font=("Arial", 18), command=lambda ch=char: self.on_click(ch))
                btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)
    
        equal_btn = tk.Button(root, text='=', font=("Arial", 18), command=lambda: self.on_click('='))
        equal_btn.grid(row=5, column=0, columnspan=4, sticky="nsew", padx=2, pady=2)
        root.grid_rowconfigure(5, weight=1)
        """
        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")
        """
    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)



