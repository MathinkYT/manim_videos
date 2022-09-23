from channel import * # channel.py includes Manim and other imports


def position_equation(t):
    return 10 * smooth(t / 5)


class Thumbnail(Scene):
    def construct(self):
        title = Text("¿Qué es la derivada?", weight=BOLD).to_edge(UP)
        ax = Axes(x_range=[0, 5, 1], y_range=[0, 10, 1], x_length=8, y_length=4.5)
        labels = ax.get_axis_labels("x", "y")
        plot = ax.plot(lambda x: 0.4 * x ** 2, color=YELLOW)
        secant_line = ax.get_secant_slope_group(
            2, plot, dx=2, dx_line_color=WHITE, dy_line_color=WHITE,
            dx_label=r"\Delta x", dy_label=r"\Delta y", secant_line_color=BLUE
        )
        dots = VGroup(Dot(ax.i2gp(2, plot)), Dot(ax.i2gp(4, plot)))
        formula = MathTex(r"{dy \over dx} = \lim_{\Delta x \to 0} {\Delta y \over \Delta x}").shift(UP + LEFT)
        video_number = Text("1", weight=BOLD).scale(2).to_corner(DL)
        logo = Logo().scale(0.5).to_corner(DR) # Logo isn't a Manim's mobject, it's on channel.py

        self.add(title, ax, labels, plot, secant_line, dots, formula, SurroundingRectangle(formula, color=RED), video_number, logo)


class Introduccion1(Scene):
    def construct(self):
        title = Text("Introducción", weight=BOLD).to_edge(UP)
        self.add(title)
        self.street = NumberLine(x_range=[0, 10, 1], length=6, include_numbers=True)
        label = Tex("$s$ [m]").next_to(self.street, RIGHT)
        self.car = Car(color=RED).move_to(self.street.n2p(0), aligned_edge=DR) # Car isn't available on Manim, it's only on channel.py
        self.car.t_val = 0
        time = Text("0").to_edge(DR)
        self.play(Write(self.street), Write(label), Write(self.car), Create(time))
        self.wait()

        self.car.add_updater(self.car_updater)
        time.add_updater(self.time_updater)
        self.wait(5)
        self.car.clear_updaters()
        self.wait()

    def car_updater(self, mob, dt):
        mob.t_val += dt
        mob.move_to(self.street.n2p(position_equation(mob.t_val)), aligned_edge=DR)
        return mob
    
    def time_updater(self, mob, dt):
        mob.become(Text(str(math.floor(self.car.t_val + dt))).to_edge(DR))
        return mob


class Introduccion2(Scene):
    def construct(self):
        title = Text("Introducción", weight=BOLD).to_edge(UP)
        self.add(title)
        self.ax = Axes(x_range=[0, 5, 1], y_range=[0, 10, 1], x_length=8, y_length=4.5)
        self.ax.add_coordinates()
        self.street = self.ax.get_y_axis()
        labels = self.ax.get_axis_labels(Tex("$t$ [s]"), Tex("$s$ [m]"))
        self.car = Car(color=RED).rotate(90 * DEGREES).move_to(self.street.n2p(0), aligned_edge=UR)
        self.car.t_val = 0
        self.play(Write(self.car), Write(self.ax), Write(labels))
        self.wait()
        self.plot = self.ax.plot(position_equation, color=YELLOW)
        line = DashedLine().add_updater(self.line_updater)
        self.car.add_updater(self.car_updater)
        self.add(line)
        self.play(Create(self.plot), rate_func=linear, run_time=5)
        self.wait()

        questions = VGroup(
            Tex(r"¿Cuál es la rapidez a los 3 s?"),
            Tex(r"¿Cuál es la función de rapidez $v(t)$?")
        ).scale(0.7).arrange(RIGHT, buff=1.5).to_edge(DOWN)
        self.play(FadeIn(questions[0]))
        self.wait()
        self.play(FadeIn(questions[1]))
        self.wait()
    
    def car_updater(self, mob, dt):
        mob.t_val += dt
        mob.move_to(self.street.n2p(position_equation(mob.t_val)), aligned_edge=UR)
        return mob
    
    def line_updater(self, mob):
        mob.become(DashedLine(self.car.get_corner(UL), self.plot.points[-1]))
        return mob


class CasoSimple1(Scene):
    def construct(self):
        title = Text("Casos simples", weight=BOLD).to_edge(UP)
        self.add(title)
        self.wait()

        caso1 = Tex(r"Caso 1: $v(t) = 2\ \mathrm{m/s}$").next_to(title, DOWN)
        self.street = NumberLine(x_range=[0, 10, 1], length=6, include_numbers=True)
        label = Tex("$s$ [m]").next_to(self.street, RIGHT)
        self.car = Car(color=RED).move_to(self.street.n2p(0), aligned_edge=DR)
        self.car.t_val = 0
        time = Text("0").to_edge(DR)
        self.play(Write(caso1))
        self.play(Write(self.car), Write(self.street), Write(label), Create(time))
        self.wait()
        self.car.add_updater(self.car_updater1)
        time.add_updater(self.time_updater)
        self.wait(5)
        self.car.clear_updaters()
        time.clear_updaters()
        self.car.move_to(self.street.n2p(10), aligned_edge=DR) # I added this line due to a Manim bug
        time.become(Text("5").to_edge(DR)) # I added this line due to a Manim bug
        self.wait()

        self.ax = Axes(x_range=[0, 5, 1], y_range=[0, 10, 1], x_length=8, y_length=4)
        self.ax.add_coordinates()
        labels = self.ax.get_axis_labels(Tex("$t$ [s]"), Tex("$s$ [m]"))
        self.street2 = self.ax.get_y_axis()
        self.play(
            ShrinkToCenter(VGroup(self.street, label)),
            self.car.animate.rotate(90 * DEGREES).move_to(self.street2.n2p(0), aligned_edge=UR),
            Uncreate(time)
        )
        self.play(Write(self.ax), Write(labels))
        self.wait()

        self.car.t_val = 0
        self.plot = self.ax.plot(lambda t: 2 * t, color=YELLOW)
        self.car.add_updater(self.car_updater2)
        line = DashedLine().add_updater(self.line_updater)
        self.add(line)
        self.play(Create(self.plot), run_time=5, rate_func=linear)
        self.car.clear_updaters()
        self.car.move_to(self.street2.n2p(10), aligned_edge=UR) # I added this line due to a Manim bug
        line.become(DashedLine(self.car.get_corner(UL), self.plot.points[-1])) # I added this line due to a Manim bug
        self.wait()

        for i in range(6):
            dot = Dot(self.ax.i2gp(i, self.plot))
            anims = [Create(dot)]
            if i > 0:
                tex = MathTex(rf"({i}\ \mathrm{{s}}, {2 * i}\ \mathrm{{m}})").scale(0.7).next_to(dot, DR, buff=0.1)
                anims.append(Write(tex))
            self.play(*anims)
            self.wait()
        
        func_expr = MathTex(r"s(t) = 2\ \mathrm{ {m \over s} } \cdot t").scale(0.9).to_edge(DOWN)
        self.play(GrowFromCenter(func_expr))
        self.play(Create(SurroundingRectangle(func_expr)))
        self.wait()
    
    def car_updater1(self, mob, dt):
        mob.t_val += dt
        mob.move_to(self.street.n2p(2 * (mob.t_val + dt)), aligned_edge=DR)
        return mob
    
    def car_updater2(self, mob, dt):
        mob.t_val += dt
        mob.move_to(self.street2.n2p(2 * (mob.t_val + dt)), aligned_edge=UR)
        return mob
    
    def line_updater(self, mob):
        mob.become(DashedLine(self.car.get_corner(UL), self.plot.points[-1]))
        return mob
    
    def time_updater(self, mob, dt):
        mob.become(Text(str(math.floor(self.car.t_val + dt))).to_edge(DR))
        return mob


class CasoSimple2(Scene):
    def construct(self):
        title = Text("Casos simples", weight=BOLD).to_edge(UP)
        self.add(title)
        self.wait()

        caso1 = Tex(r"Caso 2: $v(t) = 2\ \mathrm{m/s}$ y $s(0) \neq 0$").next_to(title, DOWN)
        self.play(Write(caso1))
        self.wait()

        ax = Axes(x_range=[0, 5, 1], y_range=[0, 10, 1], x_length=8, y_length=4)
        ax.add_coordinates()
        labels = VGroup(ax.get_x_axis_label(Tex("$t$ [s]").scale(0.7)), ax.get_y_axis_label(Tex("$s$ [m]").scale(0.7), direction=RIGHT))
        self.play(Write(ax), Write(labels))
        self.wait()
        
        s0_tracker = ValueTracker(0)
        plot = always_redraw(lambda: ax.plot(lambda t: 2 * t + s0_tracker.get_value(), x_range=[0, (10 - s0_tracker.get_value()) / 2], color=YELLOW))
        s0_tex = always_redraw(lambda: MathTex(rf"s(0\ \mathrm{{s}}) = {round_down(s0_tracker.get_value(), decimals=2)}\ \mathrm{{m}}").to_edge(DOWN))
        # round_down function isn't a Python built-in function, it's from channel.py
        self.play(Write(plot), Write(s0_tex))
        self.wait()
        self.play(s0_tracker.animate.set_value(6))
        self.play(s0_tracker.animate.set_value(3))
        self.wait()

        func_expr = MathTex("s(t) = 2\ \mathrm{ {m \over s} } \cdot t + 3\ \mathrm{m}").scale(0.9).to_edge(DOWN)
        s0_tex.clear_updaters()
        self.play(ReplacementTransform(s0_tex, func_expr))
        self.play(Create(SurroundingRectangle(func_expr)))
        self.wait()


class GeneralizandoCasosSimples(Scene):
    def construct(self):
        title = Text("Casos simples", weight=BOLD).to_edge(UP)
        self.add(title)

        general = VGroup(MathTex("s(t) = vt + s_0"), Tex("Cuando $v$ es constante")).arrange(DOWN)
        self.play(Write(general))
        self.play(Create(SurroundingRectangle(general)))
        self.wait()

        speed = MathTex(r"v = {\Delta s \over \Delta t}").to_edge(DOWN)
        self.play(Write(speed))
        self.play(Create(SurroundingRectangle(speed)))
        self.wait()


class CasoComplejo(Scene):
    def construct(self):
        title = Text("Rapidez en general", weight=BOLD).to_edge(UP)
        self.add(title)

        ax = Axes(x_range=[0, 5, 1], y_range=[0, 10, 1], x_length=8, y_length=4.5)
        ax.add_coordinates()
        labels = ax.get_axis_labels(Tex("$t$ [s]"), Tex("$s$ [m]"))
        plot = ax.plot(position_equation, color=YELLOW)
        self.play(Write(ax), Write(labels))
        self.play(Create(plot))
        self.wait()
        
        questions = VGroup(
            Tex(r"¿Cuál es la rapidez a los 3 s?"),
            Tex(r"¿Cuál es la función de rapidez $v(t)$?")
        ).scale(0.7).arrange(RIGHT, buff=1.5).to_edge(DOWN)
        self.play(FadeIn(questions[0]))
        self.wait()
        self.play(FadeIn(questions[1]))
        self.wait()

        dot = Dot(ax.i2gp(3, plot))
        self.play(Create(dot))
        self.wait()

        tex1 = Tex(r"¿$v(3\ \mathrm{s})$?").next_to(dot, DR, buff=0.1)
        self.play(GrowFromCenter(tex1))
        self.wait()
        self.play(FadeOut(tex1))
        tangent_line = ax.get_secant_slope_group(
            3, plot, dx=0.1, dx_line_color=WHITE, dy_line_color=WHITE,
            secant_line_color=BLUE
        )
        self.bring_to_back(tangent_line)
        self.play(Create(tangent_line))
        self.wait()

        new_question = Tex("¿Cómo calculo la pendiente de la recta tangente?").to_edge(DOWN)
        self.play(FadeOut(questions, shift=DOWN))
        self.play(Write(new_question))
        self.play(ShowPassingFlash(Underline(new_question, color=YELLOW)))
        self.wait()


class IntuyendoLaDerivada(Scene):
    def construct(self):
        title = Text("Intuyendo la derivada", weight=BOLD).to_edge(UP)
        self.add(title)

        ax = Axes(x_range=[0, 5, 1], y_range=[0, 10, 1], x_length=8, y_length=4.5)
        labels = ax.get_axis_labels("x", "y")
        plot = ax.plot(lambda x: 0.4 * x ** 2, color=YELLOW)
        plot_label = ax.get_graph_label(plot, "f", x_val=5)
        self.play(Write(ax), Write(labels))
        self.play(Create(plot), Create(plot_label))
        self.wait()

        x_tracker = ValueTracker(2)
        dx_tracker = ValueTracker(2)
        secant_line = always_redraw(lambda: ax.get_secant_slope_group(
            x_tracker.get_value(), plot, dx=dx_tracker.get_value(), dx_line_color=WHITE, dy_line_color=WHITE,
            dx_label=r"\Delta x", dy_label=r"\Delta y", secant_line_color=BLUE
        ))
        dots = VGroup(
            always_redraw(lambda: Dot(ax.i2gp(x_tracker.get_value(), plot))),
            always_redraw(lambda: Dot(ax.i2gp(x_tracker.get_value() + dx_tracker.get_value(), plot)))
        )
        self.play(Create(secant_line), Create(dots))
        self.wait()
        
        slope_formula = MathTex(r"m =", r"{\Delta y \over \Delta x}", "=", r"{ f(x + \Delta x) - f(x) \over \Delta x }")
        slope_formula.to_edge(DOWN)
        tex1 = always_redraw(lambda: MathTex("(x, f(x))").next_to(dots[0], UL, buff=0.1))
        tex2 = always_redraw(lambda: MathTex(r"(x + \Delta x, f(x + \Delta x))").next_to(dots[1], UL, buff=0.1))
        self.play(Write(slope_formula[0:2]))
        self.wait()
        self.play(Write(tex1))
        self.wait()
        self.play(Write(tex2))
        self.wait()
        self.play(Write(slope_formula[2:]))
        self.wait()
        self.play(Uncreate(tex1), Uncreate(tex2))

        slope_formula2 = MathTex(r"m =", r"\lim_{\Delta x \to 0}", r"{\Delta y \over \Delta x}", "=", r"\lim_{\Delta x \to 0}", r"{ f(x + \Delta x) - f(x) \over \Delta x }")
        slope_formula2.to_edge(DOWN)
        self.play(TransformMatchingTex(slope_formula, slope_formula2))
        self.wait()
        self.play(dx_tracker.animate.set_value(0.1))
        self.wait()

        derivative_formula = MathTex("f'(x) =", r"\lim_{\Delta x \to 0}", r"{ f(x + \Delta x) - f(x) \over \Delta x }").to_edge(DOWN)
        self.play(TransformMatchingTex(slope_formula2, derivative_formula))
        self.wait()
        self.play(x_tracker.animate.set_value(0))
        self.play(x_tracker.animate.set_value(5))
        self.play(Create(SurroundingRectangle(derivative_formula)))
        self.wait()


class NotacionesDerivadas(Scene):
    def construct(self):
        title = Text("Notaciones para la derivada", weight=BOLD).to_edge(UP)
        self.add(title)

        notaciones = VGroup(
            Tex("Notación de Lagrange"),
            MathTex("f'(x)"),
            Tex("Notación de Leibniz"),
            MathTex("{dy \over dx}"),
            Tex("Notación de Newton"),
            MathTex("\dot y")
        ).arrange(DOWN)
        for i in range(len(notaciones)):
            if i % 2 == 0:
                self.play(FadeIn(notaciones[i]))
            else:
                self.play(GrowFromCenter(notaciones[i]))
                self.wait()


class ResolviendoProblemaRapidez(Scene):
    def construct(self):
        title = Text("Resolviendo el problema inicial", weight=BOLD).to_edge(UP)
        self.add(title)

        ax = Axes(x_range=[0, 5, 1], y_range=[0, 10, 1], x_length=8, y_length=4.5)
        ax.add_coordinates()
        labels = ax.get_axis_labels(Tex("$t$ [s]"), Tex("$s$ [m]"))
        plot = ax.plot(position_equation, color=YELLOW)
        self.play(Write(ax), Write(labels))
        self.play(Create(plot))
        self.wait()

        speed_at_3 = MathTex(r"v(3\ \mathrm{s}) = s'(3\ \mathrm{s})").to_edge(DOWN)
        self.play(Write(speed_at_3))
        self.wait()

        x_tracker = ValueTracker(3)
        dx_tracker = ValueTracker(2)
        secant_line = always_redraw(lambda: ax.get_secant_slope_group(
            x_tracker.get_value(), plot, dx=dx_tracker.get_value(), dx_line_color=WHITE, dy_line_color=WHITE,
            dx_label=r"\Delta t", dy_label=r"\Delta s", secant_line_color=BLUE
        ))
        dots = VGroup(
            always_redraw(lambda: Dot(ax.i2gp(x_tracker.get_value(), plot))),
            always_redraw(lambda: Dot(ax.i2gp(x_tracker.get_value() + dx_tracker.get_value(), plot)))
        )
        self.play(Create(secant_line), Create(dots))
        self.wait()
        self.play(dx_tracker.animate.set_value(0.1))
        self.wait()
        
        final_result = always_redraw(lambda: MathTex(rf"v({round_down(x_tracker.get_value(), decimals=2)}\ \mathrm{{s}}) \approx"
        + rf"{round_down((plot.underlying_function(x_tracker.get_value() + 0.1) - plot.underlying_function(x_tracker.get_value())) / 0.1, decimals=2)}\ \mathrm{{m/s}}").to_edge(DOWN))
        self.play(ReplacementTransform(speed_at_3, final_result))
        self.play(Circumscribe(final_result))
        self.wait()

        self.play(x_tracker.animate(run_time=3).set_value(0))
        self.play(x_tracker.animate(run_time=3).set_value(5))
        self.wait()
