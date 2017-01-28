from kivy.app import App
from kivy.app import Widget
from kivy.lang import Builder
from kivy.app import StringProperty

# class Demo1(App): #() for extends/inherits, Demo1 extends from App, Demo1 is a class name-> Capitalise
#     def build(self): #self means this build() belongs to Demo1
#         self.title = "Hello world"
#         self.root = Widget()
#         return self.root


class Demo2(App):
    msg = StringProperty()

    def build(self):
        self.title = "Demo2"
        self.root = Builder.load_file("kivy_demo2.kv")
        return self.root

    def button_press(self, myButton):
        #print("Pressed......", myButton.text)
        if myButton.text == "X":
            myButton.text = "O"
            self.root.ids.my_label.text = "Just change to O"
        else:
            myButton.text = "X"
            self.root.ids.my_label.text = "Just change to X"
        self.msg = self.root.ids.my_input.text
        print(self.msg)

Demo2().run()