from manim import *
from bisseccao import bisectionMethod
from newton import newtonsMethod
from secante import secantMethod

class mainClass(Scene):
    iteractions = 0
    finalValue = 0
    methodType = "bisection"
    funcao_lambda = lambda x: x**3 - x**2 - 2

    def construct(self):
        title = Tex(r"Método da Bissecção")
        VGroup(title).arrange(DOWN)
        self.play(
            Write(title),
        )
        self.wait()

        transform_title = Tex("Confira a equação:")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
        )
        self.wait()

        grid = Axes(
            x_range=[-5, 5],
            y_range=[-5, 5],
        ).add_coordinates()
        basel = MathTex(r"f(x) = \sin(x) + x^2")
        basel.move_to(transform_title)
        grid.center()
        self.add(grid, basel)
        self.play(
            FadeOut(title),
            FadeIn(basel, shift=UP),
            Create(grid, run_time=3, lag_ratio=0.1)
        )

        graph = grid.plot(lambda x: x**3 - x**2 - 2, color=BLUE)
        self.add(graph)
        self.play(
            Create(graph, run_time=3, lag_ratio=0.1)
        )

        if self.methodType == 'bisection':
          bisectionMethod(self, graph, grid, basel, lambda x: x**3 - x**2 - 2, -2, 2, 1e-6, 15)

        elif self.methodType == 'newton':
          newtonsMethod(self, graph, grid, basel, lambda x: x**3 - x**2 - 2, lambda x: 3*x**2 - 2*x, 4, 1e-6, 15)

        elif self.methodType == 'secante':
          secantMethod(self, graph, grid, basel, lambda x: x**3 - x**2 - 2, 3, 4, 1e-6, 15)

        self.endScene()

        self.wait(2)


    def endScene(self):
        self.clear()

        totalIteractionsTitle = Tex(r"Total de iterações: " + str(self.iteractions))
        finalValueTitle = Tex(r"c final: " + str(round(self.finalValue, 4))).next_to(totalIteractionsTitle, DOWN)
        self.play(
            Write(totalIteractionsTitle),
        )
        self.wait()
        self.play(
            Write(finalValueTitle)
        )
        self.wait()