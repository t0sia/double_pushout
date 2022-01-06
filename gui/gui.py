from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

from structures import Graph
from kivy.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg



G = Graph(
    ["A", "B", "C"],
    [
        [(1, "a"), (2, "b")],
        [(0, "a"), (2, "c")],
        [(0, "b"), (1, "c")]
    ])

D = Graph(
    ["D", "E", "F"],
    [
        [(1, "a"), (2, "b")],
        [(0, "a"), (2, "c")],
        [(0, "b"), (1, "c")]
    ])

#produkcje przykladowe

L = Graph(
    ["D", "E", "F"],
    [
        [(1, "a"), (2, "b")],
        [(0, "a"), (2, "c")],
        [(0, "b"), (1, "c")]
    ])

K = Graph(
    ["D", "E", "F"],
    [
        [(1, "a"), (2, "b")],
        [(0, "a"), (2, "c")],
        [(0, "b"), (1, "c")]
    ])

R = Graph(
    ["D", "E", "F"],
    [
        [(1, "a"), (2, "b")],
        [(0, "a"), (2, "c")],
        [(0, "b"), (1, "c")]
    ])


class GraphProd(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        self.add_widget(Button(text='Choose', font_size=14))
        self.add_widget(Label(text="P1:", size_hint=(0.1, 1)))
        self.add_widget(Label(text="L:", size_hint=(0.1, 1)))
        self.add_widget(FigureCanvasKivyAgg(L.visualize()))
        self.add_widget(Label(text="K:", size_hint=(0.1, 1)))
        self.add_widget(FigureCanvasKivyAgg(K.visualize()))
        self.add_widget(Label(text="R:", size_hint=(0.1, 1)))
        self.add_widget(FigureCanvasKivyAgg(R.visualize()))

class Matty(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        lay1 = BoxLayout(orientation='horizontal', size_hint=(1, 3))
        self.add_widget(lay1)
        box1 = BoxLayout()
        box2 = BoxLayout()
        lay1.add_widget(box1)
        lay1.add_widget(box2)
        box1.add_widget(FigureCanvasKivyAgg(G.visualize()))
        self.add_widget(GraphProd())
        self.add_widget(GraphProd())
        self.add_widget(GraphProd())
        self.add_widget(GraphProd())







class GraphApp(App):
    def build(self):
        return Matty()


if __name__ == '__main__':
    GraphApp().run()