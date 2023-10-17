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
        x_range=[-5, 5, 1],
        y_range=[-5, 5, 1],
    )
    basel = MathTex(r"f(x) = \sin(x) + x^2")
    basel.move_to(transform_title)
    self.add(grid, basel)
    self.play(
      FadeOut(title),
      FadeIn(basel, shift=UP),
      Create(grid, run_time=3, lag_ratio=0.1)
    )
    graph = grid.plot(lambda x: np.sin(x), color=BLUE, x_range=[-3, 3 * PI])
    self.add(graph)
    self.play(
      Create(graph, run_time=3, lag_ratio=0.1)
    )
    self.wait(10)