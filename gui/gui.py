from kivy.app import App
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

class Matty(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        box = self.ids.box
        box.add_widget(FigureCanvasKivyAgg(G.visualize()))

class GraphViz(Widget):
    pass


class GraphApp(App):
    def build(self):
        return Matty()


if __name__ == '__main__':
    GraphApp().run()