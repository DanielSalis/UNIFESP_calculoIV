from manim import *

class Newtons(Scene):
  iteractions = 0
  finalValue = 0

  def construct(self):
    title = Tex(r"Método de newton")
    VGroup(title).arrange(DOWN)
    self.play(
      Write(title),
    )
    self.wait()

    transform_title = Tex("Confira a equação:")
    transform_title.to_corner(UP+LEFT)
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

    self.newtonsMethod(graph, grid, basel, lambda x: x**3 - x**2 - 2, lambda x: 3*x**2 - 2*x, 4, 1e-6, 15)

    self.endScene()

    self.wait(2)

  def newtonsMethod(self, graph, grid, basel, func, der, x0, tolerance=1e-6, max_iter=15):
    x = x0
    iteracao = 0
    self.play(
      FadeOut(basel),
    )

    while iteracao < max_iter:
        iterTitle = Tex("Iteração: " + str(iteracao))
        iterTitle.to_corner(UP+LEFT)

        xTitle = Tex("x: " + str(round(x, 4)))
        xTitle.to_corner(UP+RIGHT)

        fnTitle = Tex("f(x): " + str(round(func(x), 4)))
        fnTitle.next_to(xTitle, DOWN)
        self.play(
          FadeIn(iterTitle, shift=UP),
          FadeIn(xTitle, shift=UP),
          FadeIn(fnTitle, shift=UP),
        )

        # Cria ponto animado
        dot_axes = Dot(grid.coords_to_point(x, func(x)), color=YELLOW)
        self.add(dot_axes)

        delta_x = func(x) / der(x)
        x = x - delta_x

        self.play(
            FadeIn(dot_axes),
        )

        self.play(
          FadeOut(iterTitle),
          FadeOut(xTitle),
          FadeOut(fnTitle),
        )

        # self.play(
        #     FadeOut(dot_axes),
        # )

        self.wait(
           duration=0.5
        )

        iteracao = iteracao + 1
        self.iteractions = iteracao
        self.finalValue = x

        if abs(delta_x) < tolerance:
          return x


    return iteracao

  def endScene(self):
    self.clear()

    totalIteractionsTitle = Tex(r"Total de iterações: "+ str(self.iteractions))
    finalValueTitle = Tex(r"x final: " + str(round(self.finalValue, 4))).next_to(totalIteractionsTitle, DOWN)
    self.play(
      Write(totalIteractionsTitle),
    )
    self.wait()
    self.play(
      Write(finalValueTitle)
    )
    self.wait()