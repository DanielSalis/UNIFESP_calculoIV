from manim import *

class Newtons(Scene):
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


    graph = grid.plot(lambda x: np.sin(x), color=BLUE, x_range=[-5, 5  * PI])
    self.add(graph)
    self.play(
      Create(graph, run_time=3, lag_ratio=0.1)
    )

    self.newtonsMethod(graph, grid, basel, lambda x: np.sin(x) + x**2,  lambda x: np.cos(x) + 2*x, 1, 1e-6, 100)

    self.wait(2)

  def newtonsMethod(self, graph, grid, basel, func, der, x0, tolerance=1e-6, max_iter=100):
    x = x0
    iteracao = 0
    self.play(
      FadeOut(basel),
    )

    while iteracao < max_iter:
        iterTitle = Tex("Iteração: " + str(iteracao))
        iterTitle.to_corner(UP+LEFT)

        xTitle = Tex("x: " + str(x))
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

        # grid.scale(1.1)
        # graph.scale(1.1)

        self.play(
            FadeIn(dot_axes),
        )

        self.play(
          FadeOut(iterTitle),
          FadeOut(xTitle),
          FadeOut(fnTitle),
        )

        self.play(
            FadeOut(dot_axes),
        )

        self.wait(0.5)

        if abs(delta_x) < tolerance:
            return x

        iteracao += 1

    return None