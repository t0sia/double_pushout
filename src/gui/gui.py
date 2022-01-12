from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from src.structures import Graph
from src.structures import Production
from kivy.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg



G = Graph(
    {0: "A", 1: "B", 2: "C"},
    {
        0: [(1, "a"), (2, "b")],
        1: [(0, "a"), (2, "c")],
        2: [(0, "b"), (1, "c")]
    })

D = Graph(
    {0: "D", 1: "E", 2: "F"},
    {
        0: [(1, "a"), (2, "b")],
        1: [(0, "a"), (2, "c")],
        2: [(0, "b"), (1, "c")]
    })

# produkcje przykladowe
L = Graph(
    {0: "D", 1: "E", 2: "F"},
    {
        0: [(1, "a"), (2, "b")],
        1: [(0, "a"), (2, "c")],
        2: [(0, "b"), (1, "c")]
    })

K = Graph(
    {0: "D", 1: "E", 2: "F"},
    {
        0: [(1, "a"), (2, "b")],
        1: [(0, "a"), (2, "c")],
        2: [(0, "b"), (1, "c")]
    })

R = Graph(
    {0: "D", 1: "E", 2: "F"},
    {
        0: [(1, "a"), (2, "b")],
        1: [(0, "a"), (2, "c")],
        2: [(0, "b"), (1, "c")]
    })

pr = Production(L,K,R)
"""
class GraphProd(BoxLayout):
    def __init__(self, prod, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.add_widget(Button(text='Choose', font_size=14,size_hint=(0.4,1)))
        self.add_widget(Label(text="P:", size_hint=(0.1, 1)))
        self.add_widget(Label(text="L:", size_hint=(0.1, 1)))
        self.add_widget(FigureCanvasKivyAgg(prod.left.visualize()))
        self.add_widget(Label(text="K:", size_hint=(0.1, 1)))
        self.add_widget(FigureCanvasKivyAgg(prod.connector.visualize()))
        self.add_widget(Label(text="R:", size_hint=(0.1, 1)))
        self.add_widget(FigureCanvasKivyAgg(prod.right.visualize()))
"""


class Matty(BoxLayout):

    def __init__(self, main_graph, prod_list, **kwargs):
        super().__init__(**kwargs)
        lay1 = BoxLayout(orientation='horizontal', size_hint=(1, 3))
        self.prod_choice = 0 #która produkcja
        self.main_graph = main_graph #aktualny graf
        self.prod_list = prod_list #lista produkcji
        self.buttons = [] #lista buttonów
        self.add_widget(lay1)
        self.box1 = BoxLayout()
        self.box2 = BoxLayout(orientation='vertical')
        self.prodlabel = Label(text="Production: 0")
        self.indexinput = TextInput(size_hint=(1,0.3))
        self.submitbuttton = Button(text="Submit")
        self.submitbuttton.bind(on_press=self.submit)
        lay1.add_widget(self.box1)
        lay1.add_widget(self.box2)
        self.box2.add_widget(self.prodlabel)
        self.box2.add_widget(self.indexinput)
        self.box2.add_widget(self.submitbuttton)
        self.box1.add_widget(FigureCanvasKivyAgg(self.main_graph.visualize()))
        self.lay2 = BoxLayout(orientation='horizontal')
        self.add_widget(self.lay2)

        for cnt, prod in enumerate(prod_list):
            self.buttons.append(Button(text="Choose "+str(cnt+1), font_size=14, size_hint=(0.4, 1)))
            self.buttons[-1].prod_num=cnt
            self.buttons[-1].bind(on_press=self.press)
            self.lay2.add_widget(self.buttons[-1])
            self.lay2.add_widget(Label(text="P:", size_hint=(0.1, 1)))
            self.lay2.add_widget(Label(text="L:", size_hint=(0.1, 1)))
            self.lay2.add_widget(FigureCanvasKivyAgg(prod.left.visualize()))
            self.lay2.add_widget(Label(text="K:", size_hint=(0.1, 1)))
            self.lay2.add_widget(FigureCanvasKivyAgg(prod.connector.visualize()))
            self.lay2.add_widget(Label(text="R:", size_hint=(0.1, 1)))
            self.lay2.add_widget(FigureCanvasKivyAgg(prod.right.visualize()))

    def press(self, instance):
        self.prod_choice = instance.prod_num
        self.prodlabel.text = "Production: "+str(instance.prod_num)

    def submit(self, instance):
        indexes = list(map(int,self.indexinput.text.split(',')))
        print(indexes)

        #self.main_graph = algo(self.main_graph,self.prod_list[self.prod_choice])
        #updategui()




class GraphApp(App):
    def build(self):
        return Matty(G,[pr])


if __name__ == '__main__':
    GraphApp().run()