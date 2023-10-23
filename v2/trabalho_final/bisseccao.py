from manim import *

def bisectionMethod(self, graph, grid, basel, func, a, b, tolerance=1e-6, max_iter=15):
    iteracao = 0
    self.play(
        FadeOut(basel),
    )

    while iteracao < max_iter:
        iterTitle = Tex("Iteração: " + str(iteracao))
        iterTitle.to_corner(UP + LEFT)

        aTitle = Tex("a: " + str(round(a, 4)))
        aTitle.to_corner(UP + RIGHT)

        bTitle = Tex("b: " + str(round(b, 4)))
        bTitle.next_to(aTitle, DOWN)

        c = (a + b) / 2
        cTitle = Tex("c: " + str(round(c, 4)))
        cTitle.next_to(bTitle, DOWN)

        f_a = func(a)
        f_b = func(b)
        f_c = func(c)

        fnATitle = Tex("f(a): " + str(round(f_a, 4)))
        fnATitle.next_to(cTitle, DOWN)

        fnBTitle = Tex("f(b): " + str(round(f_b, 4)))
        fnBTitle.next_to(fnATitle, DOWN)

        fnCTitle = Tex("f(c): " + str(round(f_c, 4)))
        fnCTitle.next_to(fnBTitle, DOWN)

        self.play(
            FadeIn(iterTitle, shift=UP),
            FadeIn(aTitle, shift=UP),
            FadeIn(bTitle, shift=UP),
            FadeIn(cTitle, shift=UP),
            FadeIn(fnATitle, shift=UP),
            FadeIn(fnBTitle, shift=UP),
            FadeIn(fnCTitle, shift=UP),
        )

        # Cria pontos animados para a, b e c
        dot_axes_a = Dot(grid.coords_to_point(a, f_a), color=RED)
        dot_axes_b = Dot(grid.coords_to_point(b, f_b), color=GREEN)
        dot_axes_c = Dot(grid.coords_to_point(c, f_c), color=YELLOW)
        self.add(dot_axes_a, dot_axes_b, dot_axes_c)

        if abs(b - a) < tolerance:
            return c

        if f_a * f_c < 0:
            b = c
        else:
            a = c

        self.play(
            FadeIn(dot_axes_a),
            FadeIn(dot_axes_b),
            FadeIn(dot_axes_c),
        )

        self.play(
            FadeOut(iterTitle),
            FadeOut(aTitle),
            FadeOut(bTitle),
            FadeOut(cTitle),
            FadeOut(fnATitle),
            FadeOut(fnBTitle),
            FadeOut(fnCTitle),
        )

        self.wait(duration=0.5)

        iteracao += 1
        self.iteractions = iteracao
        self.finalValue = c

    return iteracao