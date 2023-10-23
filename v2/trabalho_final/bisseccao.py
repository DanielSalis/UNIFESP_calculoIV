from manim import *

class Bisection(Scene):
    iteractions = 0
    finalValue = 0

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

        self.bisectionMethod(graph, grid, basel, lambda x: x**3 - x**2 - 2, -2, 2, 1e-6, 15)

        self.endScene()

        self.wait(2)

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