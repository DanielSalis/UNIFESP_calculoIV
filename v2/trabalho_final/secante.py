from manim import *

class Secante(Scene):
    iteractions = 0
    finalValue = 0

    def construct(self):
        title = Tex(r"Método da Secante")
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
            y_range=[-10, 10],
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

        self.secantMethod(graph, grid, basel, lambda x: x**3 - x**2 - 2, 3, 4, 1e-6, 15)

        self.endScene()

        self.wait(2)

    def secantMethod(self, graph, grid, basel, func, x0, x1, tolerance=1e-6, max_iter=15):
        x0_value = x0
        x1_value = x1
        iteracao = 0
        self.play(
            FadeOut(basel),
        )

        while iteracao < max_iter:
            iterTitle = Tex("Iteração: " + str(iteracao))
            iterTitle.to_corner(UP + LEFT)

            x0Title = Tex("x0: " + str(round(x0_value, 4)))
            x0Title.to_corner(UP + RIGHT)

            x1Title = Tex("x1: " + str(round(x1_value, 4)))
            x1Title.next_to(x0Title, DOWN)

            f_x0 = func(x0_value)
            f_x1 = func(x1_value)

            fn0Title = Tex("f(x0): " + str(round(f_x0, 4)))
            fn0Title.next_to(x1Title, DOWN)

            fn1Title = Tex("f(x1): " + str(round(f_x1, 4)))
            fn1Title.next_to(fn0Title, DOWN)

            self.play(
                FadeIn(iterTitle, shift=UP),
                FadeIn(x0Title, shift=UP),
                FadeIn(x1Title, shift=UP),
                FadeIn(fn0Title, shift=UP),
                FadeIn(fn1Title, shift=UP),
            )

            # Cria ponto animado para x0 e x1
            dot_axes_x0 = Dot(grid.coords_to_point(x0_value, f_x0), color=GREEN)
            dot_axes_x1 = Dot(grid.coords_to_point(x1_value, f_x1), color=YELLOW)
            self.add(dot_axes_x0, dot_axes_x1)

            if abs(f_x1 - f_x0) < tolerance:
                return x1_value

            x2_value = x1_value - f_x1 * (x1_value - x0_value) / (f_x1 - f_x0)

            self.play(
                FadeIn(dot_axes_x0),
                FadeIn(dot_axes_x1),
            )

            self.play(
                FadeOut(iterTitle),
                FadeOut(x0Title),
                FadeOut(x1Title),
                FadeOut(fn0Title),
                FadeOut(fn1Title),
            )

            self.wait(duration=0.5)

            x0_value = x1_value
            x1_value = x2_value
            iteracao += 1
            self.iteractions = iteracao
            self.finalValue = x2_value

        return iteracao

    def endScene(self):
        self.clear()

        totalIteractionsTitle = Tex(r"Total de iterações: " + str(self.iteractions))
        finalValueTitle = Tex(r"x final: " + str(round(self.finalValue, 4))).next_to(totalIteractionsTitle, DOWN)
        self.play(
            Write(totalIteractionsTitle),
        )
        self.wait()
        self.play(
            Write(finalValueTitle)
        )
        self.wait()
