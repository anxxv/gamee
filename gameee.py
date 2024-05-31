import tkinter as tk
from tkinter import messagebox


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Programming Quiz Game")

        self.current_level = 0
        self.score = 0

        self.languages = {
            "C#": [
                {"question": "Что такое C#?",
                 "options": ["Язык программирования", "Браузер", "Операционная система", "Текстовый редактор"],
                 "answer": "Язык программирования"},
                {"question": "Какой символ используется для обозначения директив препроцессора в C#?",
                 "options": ["@", "#", "$", "%"], "answer": "#"},
                {"question": "Какой метод используется для запуска консольного приложения в C#?",
                 "options": ["Main()", "Start()", "Run()", "Execute()"], "answer": "Main()"},
                {"question": "Какой тип данных используется для хранения больших целых чисел в C#?",
                 "options": ["int", "long", "short", "byte"], "answer": "long"},
                {"question": "Какой из следующих типов является ссылочным типом в C#?",
                 "options": ["int", "bool", "char", "string"], "answer": "string"},
                {"question": "Какой модификатор доступа позволяет доступ только внутри одного класса?",
                 "options": ["public", "private", "protected", "internal"], "answer": "private"},
                {"question": "Что такое интерфейс в C#?",
                 "options": ["Класс с частичной реализацией методов", "Абстрактный класс",
                             "Набор методов и свойств без реализации", "Тип данных"],
                 "answer": "Набор методов и свойств без реализации"},
                {"question": "Какой из следующих методов вызывается при создании объекта?",
                 "options": ["Finalize", "Dispose", "Initialize", "Constructor"], "answer": "Constructor"},
                {"question": "Какой тип данных используется для работы с символами в C#?",
                 "options": ["string", "char", "int", "float"], "answer": "char"},
                {"question": "Что такое namespace в C#?",
                 "options": ["Контейнер для классов и других типов", "Модуль программы", "Файл кода", "Тип данных"],
                 "answer": "Контейнер для классов и других типов"},
                {"question": "Какой оператор используется для приведения типов в C#?",
                 "options": ["as", "is", "cast", "convert"], "answer": "as"},
                {"question": "Какой метод используется для очистки ресурсов в C#?",
                 "options": ["Dispose", "Clear", "Release", "Finalize"], "answer": "Dispose"},
                {"question": "Какое ключевое слово используется для создания константы в C#?",
                 "options": ["const", "final", "static", "readonly"], "answer": "const"},
                {"question": "Что делает ключевое слово 'virtual' в C#?",
                 "options": ["Создает виртуальную машину", "Позволяет переопределение метода в производном классе",
                             "Создает копию объекта", "Выделяет память"],
                 "answer": "Позволяет переопределение метода в производном классе"},
                {"question": "Какое ключевое слово используется для создания экземпляра объекта?",
                 "options": ["create", "new", "instance", "make"], "answer": "new"},
                {"question": "Какой тип исключения используется для обозначения ошибок ввода-вывода в C#?",
                 "options": ["IOException", "FileNotFoundException", "InputException", "OutputException"],
                 "answer": "IOException"},
                {"question": "Что такое делегат в C#?",
                 "options": ["Тип данных", "Указатель на метод", "Событие", "Интерфейс"],
                 "answer": "Указатель на метод"},
                {"question": "Какое ключевое слово используется для обработки исключений в C#?",
                 "options": ["try", "catch", "throw", "all of the above"], "answer": "all of the above"},
                {"question": "Какое ключевое слово используется для наследования класса в C#?",
                 "options": ["extend", "inherit", "base", "derive"], "answer": "base"}
            ],
            "Rust": [
                {"question": "Что такое Rust?",
                 "options": ["Язык программирования", "Браузер", "Операционная система", "Текстовый редактор"],
                 "answer": "Язык программирования"},
                {"question": "Какое ключевое слово используется для создания неизменяемой переменной в Rust?",
                 "options": ["let", "var", "const", "static"], "answer": "let"},
                {"question": "Какое ключевое слово используется для создания функции в Rust?",
                 "options": ["fn", "function", "def", "func"], "answer": "fn"},
                {"question": "Какой тип данных используется для работы с символами в Rust?",
                 "options": ["str", "char", "string", "symbol"], "answer": "char"},
                {"question": "Какое ключевое слово используется для создания структуры в Rust?",
                 "options": ["struct", "class", "object", "record"], "answer": "struct"},
                {"question": "Какой метод вызывается для создания нового экземпляра структуры в Rust?",
                 "options": ["new", "create", "build", "init"], "answer": "new"},
                {"question": "Какое ключевое слово используется для сопоставления с образцом в Rust?",
                 "options": ["match", "case", "switch", "if"], "answer": "match"},
                {"question": "Какой модификатор доступа позволяет доступ только внутри одного модуля в Rust?",
                 "options": ["pub", "priv", "mod", "crate"], "answer": "crate"},
                {"question": "Какое ключевое слово используется для объявления константы в Rust?",
                 "options": ["const", "let", "static", "final"], "answer": "const"},
                {"question": "Какое ключевое слово используется для указания области видимости переменной в Rust?",
                 "options": ["let", "mut", "scope", "pub"], "answer": "let"},
                {"question": "Какой тип данных используется для хранения целых чисел в Rust?",
                 "options": ["int", "i32", "i64", "integer"], "answer": "i32"},
                {"question": "Какое ключевое слово используется для создания перечисления в Rust?",
                 "options": ["enum", "enumclass", "enumeration", "enumtype"], "answer": "enum"},
                {"question": "Что делает ключевое слово 'unsafe' в Rust?",
                 "options": ["Отключает проверки безопасности", "Создает новый поток",
                             "Позволяет использование небезопасного кода", "Выделяет память"],
                 "answer": "Позволяет использование небезопасного кода"},
                {
                    "question": "Какое ключевое слово используется для имплементации методов структуры или перечисления в Rust?",
                    "options": ["impl", "extend", "class", "implement"], "answer": "impl"},
                {"question": "Какой тип данных используется для хранения вещественных чисел в Rust?",
                 "options": ["float", "f32", "double", "decimal"], "answer": "f32"},
                {"question": "Какое ключевое слово используется для определения цикла в Rust?",
                 "options": ["loop", "while", "for", "repeat"], "answer": "loop"},
                {"question": "Какое ключевое слово используется для приведения типов в Rust?",
                 "options": ["as", "to", "cast", "convert"], "answer": "as"},
                {"question": "Какое ключевое слово используется для объявления макроса в Rust?",
                 "options": ["macro", "fn", "def", "macro_rules!"], "answer": "macro_rules!"},
                {"question": "Какое ключевое слово используется для создания асинхронной функции в Rust?",
                 "options": ["async", "await", "future", "promise"], "answer": "async"},
                {"question": "Какое ключевое слово используется для объявления внешней функции в Rust?",
                 "options": ["extern", "external", "foreign", "native"], "answer": "extern"}
            ]
        }

        self.language_var = tk.StringVar()
        self.language_var.set("C#")

        self.langProg()

    def langProg(self):
        language_frame = tk.Frame(self.root)
        language_frame.pack(pady=20)

        tk.Label(language_frame, text="Выберите язык программирования:", font=("Arial", 16)).pack(pady=10)

        for language in self.languages.keys():
            tk.Radiobutton(language_frame, text=language, variable=self.language_var, value=language,
                           font=("Arial", 14)).pack(anchor=tk.W)

        tk.Button(language_frame, text="Начать квиз", command=self.sQuiz, font=("Arial", 14)).pack(pady=20)

    def sQuiz(self):
        self.current_level = 0
        self.score = 0
        self.selected_language = self.language_var.get()
        self.questions = self.languages[self.selected_language]

        for widget in self.root.winfo_children():
            widget.destroy()

        self.Z()
        self.Questions()

    def Z(self):
        self.question_label = tk.Label(self.root, text="", font=("Arial", 16))
        self.question_label.pack(pady=20)

        self.option_var = tk.StringVar()

        self.option_buttons = []
        for _ in range(4):
            btn = tk.Radiobutton(self.root, text="", variable=self.option_var, font=("Arial", 14), value="")
            btn.pack(anchor=tk.W, padx=20, pady=5)
            self.option_buttons.append(btn)

        self.submit_button = tk.Button(self.root, text="Ответить", command=self.Answ, font=("Arial", 14))
        self.submit_button.pack(pady=20)

    def Questions(self):
        question_data = self.questions[self.current_level]
        self.question_label.config(text=question_data["question"])

        for i, option in enumerate(question_data["options"]):
            self.option_buttons[i].config(text=option, value=option)

        self.option_var.set("")

    def Answ(self):
        selected_option = self.option_var.get()
        if not selected_option:
            messagebox.showwarning("Внимание", "Пожалуйста, выберите ответ.")
            return

        question_data = self.questions[self.current_level]
        if selected_option == question_data["answer"]:
            self.score += 1

        self.current_level += 1
        if self.current_level < len(self.questions):
            self.Questions()
        else:
            self.Rezult()

    def Rezult(self):
        messagebox.showinfo("Результат", f"Вы ответили правильно на {self.score} из {len(self.questions)} вопросов.")
        self.root.quit()


root = tk.Tk()
app = QuizApp(root)
root.mainloop()