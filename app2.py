from tkinter import *
class TestQuestion: 
	def __init__(self,text,correct_variant,variant_of_ansver):
		self.text = text 
		self.correct_variant = correct_variant
		self.variant_of_answer= variant_of_ansver 
class Test: 
	def __init__(self,title='test',test_question_list = []):
		self.title = title
		self.test_question_list = test_question_list 
		self.total_questions = len(test_question_list)
	def add_test_question(self): 
		
		pass
	def remove_test_question(self):
		
		pass
	def show_test_question_list(self): 
		pass
class TestInterface: 
	def __init__(self,test):
		self.root = Tk()
		self.root.title(test.title) 
		self.root.geometry("300x300")
		self.font = "Arial 12 bold"
		self.lbl_text = StringVar()
		self.lbl_text.set("для начала теста нажмите 'начать'")
		self.lbl = Label(textvariable=self.lbl_text,font = self.font,wraplength =300)
		self.lbl.pack(side=TOP)
		self.checkbtn_list =[]
		self.score = 0 
		self.variant = StringVar() 
		self.variant.set(0) 
		self.n = 0 
		self.lbl_checked = Label(font = "Arial 12 bold")
		self.lbl_checked.pack(side=BOTTOM) 
		self.btn = Button(text="начать",font = "Arial 12 bold", command=self.change_lbl_text) 
		self.btn.pack(side=BOTTOM)
		self.root.mainloop() 
	def change_lbl_text(self): 
		if self.n< test.total_questions:
			self.btn.config(text="следующий>>", state=DISABLED,command = self.next_quest)
			self.lbl_text.set("Задача № {}\n{}".format(self.n+1,test.test_question_list[self.n].text))
			self.set_check_btn()
			self.lbl_checked.config(text="\nНабрано баллов: {}".format(self.score)) 
		else:
			print("usyo pizdec")
			self.end() 
	def set_check_btn(self): 
		for key,value in test.test_question_list[self.n].variant_of_answer.items(): 
			ch =Checkbutton(text ="{}) {}".format(key,value),font = "Arial 12 bold",onvalue =key,variable =self.variant,command = self.checked)
			ch.pack()
			self.checkbtn_list.append(ch) 
	def remove_check_btn(self): 
		if self.checkbtn_list:
			for ch in self.checkbtn_list:
				ch.destroy() 
			self.checkbtn_list.clear()
	def change_check_btn(self):
		for ch in self.checkbtn_list:
			ch.config(state=DISABLED)
			if ch["onvalue"] == test.test_question_list[self.n].correct_variant: 
				ch.config( disabledforeground="#000", bg="#0f0")
			elif ch["onvalue"]== self.variant.get():
				ch.config(disabledforeground="#000", bg="#f00") 
	def checked(self): 
		if self.variant.get() == test.test_question_list[self.n].correct_variant: 
			self.score+=1 
			self.btn.config(state = NORMAL)
			self.lbl_checked.config(text="Правильно\nНабрано баллов: {}".format(self.score))
		else:
			self.lbl_checked.config(text="Вы ошиблись\nНабрано баллов: {}".format(self.score))
			self.btn.config(text ="Попробовать снова",command = self.reset,state = NORMAL)
		self.change_check_btn() 
	def reset(self): 
		self.n = 0
		self.score = 0
		self.variant.set(0)
		self.remove_check_btn()
		self.lbl_text.set("для начала теста нажмите 'начать'")
		self.lbl_checked.config(text='')
		self.btn.config(text="начать", command=self.change_lbl_text)
	def next_quest(self):
		self.n+=1
		self.variant.set(0)
		self.remove_check_btn()
		self.change_lbl_text() 
	def end(self): 
		self.remove_check_btn()
		self.lbl_checked.config(text="Тест пройден.Вы свободны\nНабрано баллов: {}".format(self.score))
		self.lbl_text.set("Вопросы закончились")
		self.btn.config(text="Пройти тест снова", command=self.reset)
test_question_list=[]
test_question_list.append(TestQuestion("x+2=4", 'a', {'a': 'x=2', 'b': 'x=4', 'c': 'x=3', 'd': 'x=9'}))
test_question_list.append(TestQuestion("2+2*2", 'b', {'a': '8', 'b': '6'}))
test_question_list.append(TestQuestion("В компании (на вечеринке) Вы", 'c', {'a': 'общаетесь со многими, включая и незнакомцев' 'b': 'общаетесь с немногими - Вашими знакомыми'}))
test = Test("тест 8",test_question_list) 
TestInterface(test) 