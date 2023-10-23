from manim import *

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