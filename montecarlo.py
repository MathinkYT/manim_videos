from channel import * # channel.py includes Manim and other imports
from random import uniform


config.frame_height, config.frame_width = config.frame_width, config.frame_height
config.pixel_height, config.pixel_width = config.pixel_width, config.pixel_height


class TextDigital7(Text):
    def __init__(self, text, **kwargs):
        super().__init__(text, font="Digital-7", **kwargs)


class Montecarlo(Scene):
    def construct(self):
        self.initial_part()
        self.montecarlo()
    
    def initial_part(self):
        def next_to_updater(m):
            def updater(mob):
                mob.next_to(m, DOWN, buff=0.2)
                return mob
            return updater
            
        self.circle = Circle(color=WHITE, radius=1.5).set_fill(RED_E, opacity=1)
        self.square = Square(color=WHITE, side_length=3).set_fill(BLUE, opacity=1)
        self.play(DrawBorderThenFill(self.square), DrawBorderThenFill(self.circle))
        self.wait()

        radius = Line(self.circle.get_center(), self.circle.get_right())
        r = MathTex("r").next_to(radius, UP)
        self.play(Create(VGroup(radius, r)))
        self.wait()

        radius_2 = Line(self.circle.get_center(), self.circle.get_left())
        copy = VGroup(radius, radius_2).copy()
        br = Brace(copy, DOWN)
        tex = br.get_tex("2r", buff=0.2)
        self.play(Create(radius_2))
        self.play(Write(VGroup(br, tex)))
        self.wait()
        br.add_updater(next_to_updater(copy))
        tex.add_updater(next_to_updater(br))
        self.play(copy.animate.move_to(self.square.get_bottom()))
        br.clear_updaters()
        tex.clear_updaters()
        self.play(FadeOut(radius_2, copy))
        self.wait()

        formula = MathTex(r"{A_\circ", r"\over", r"A_\square}") \
            .set_color_by_tex_to_color_map({r"\circ": RED, r"\square": BLUE}).to_edge(UP)
        formula_2 = MathTex(r"{A_\circ", r"\over", r"A_\square}", "=", r"{\pi", "r^2", r"\over", "(2r)^2}") \
            .set_color_by_tex_to_color_map({r"\circ": RED, r"\square": BLUE, r"\pi": GREEN}).to_edge(UP)
        formula_3 = MathTex(r"{A_\circ", r"\over", r"A_\square}", "=", r"{\pi", "r^2", r"\over", "4r^2}") \
            .set_color_by_tex_to_color_map({r"\circ": RED, r"\square": BLUE, r"\pi": GREEN}).to_edge(UP)
        formula_4 = MathTex(r"{A_\circ", r"\over", r"A_\square}", "=", r"{\pi", r"\over", "4}") \
            .set_color_by_tex_to_color_map({r"\circ": RED, r"\square": BLUE, r"\pi": GREEN}).to_edge(UP)
        formula_5 = MathTex("4", r"\cdot", r"{A_\circ", r"\over", r"A_\square}", "=", r"\pi") \
            .set_color_by_tex_to_color_map({r"\circ": RED, r"\square": BLUE, r"\pi": GREEN}).to_edge(UP)
        formula_final = MathTex(r"\pi", "=", "4", r"\cdot", r"{A_\circ", r"\over", r"A_\square}") \
            .set_color_by_tex_to_color_map({r"\circ": RED, r"\square": BLUE, r"\pi": GREEN}).to_edge(UP)
        self.play(Write(formula))
        self.wait()
        self.play(TransformMatchingTex(formula, formula_2))
        self.wait()
        self.play(TransformMatchingTex(formula_2, formula_3, transform_mismatches=True))
        self.wait()
        cancels = VGroup(CancelLine(formula_3[-3]), CancelLine(formula_3[-1][1:3])) # CancelLine isn't a Manim mobject, it's in channel.py
        self.play(*[Create(mob) for mob in cancels])
        self.wait()
        self.play(*[Uncreate(mob) for mob in cancels])
        self.play(TransformMatchingTex(formula_3, formula_4))
        self.wait()
        self.play(TransformMatchingTex(formula_4, formula_5, key_map={"4}": "4"}))
        self.wait()
        self.play(TransformMatchingTex(formula_5, formula_final))
        self.play(Circumscribe(formula_final))
        self.wait()
        self.play(Uncreate(VGroup(br, tex, radius, r)))
        self.wait()

        self.formula_final_2 = MathTex(r"\pi", r"\approx", "4", r"\cdot", r"{n_\circ", r"\over", r"n_\square}") \
            .set_color_by_tex_to_color_map({r"\circ": RED, r"\square": BLUE, r"\pi": GREEN}).to_edge(UP)
        self.play(ReplacementTransform(formula_final, self.formula_final_2))
        self.wait()
    
    def montecarlo(self):
        self.play(*[mob.animate.set_fill(opacity=0) for mob in VGroup(self.circle, self.square)])
        self.wait()

        TOTAL_DOTS = 10_000
        MIN_X, MAX_X = self.square.get_left()[0], self.square.get_right()[0]
        MIN_Y, MAX_Y = self.square.get_bottom()[1], self.square.get_top()[1]
        RADIUS = self.circle.radius

        dots = VGroup()

        for _ in range(TOTAL_DOTS): dots.add(Dot(uniform(MIN_X, MAX_X)*RIGHT + uniform(MIN_Y, MAX_Y)*UP, radius=0.02, color=BLUE))
        def is_inside_circle(dot: Dot): return dot.get_x()**2 + dot.get_y()**2 <= RADIUS**2
        dots_in_circle = filter(is_inside_circle, dots)
        for dot in dots_in_circle: dot.set_color(RED_E)
        dots_on_screen = VGroup()
        n_circ = MobjectTable([[MathTex(r"n_\circ", color=RED_E), Integer(0, mob_class=TextDigital7)]]) \
            .to_edge(DOWN)
        n_sq = MobjectTable([[MathTex(r"n_\square", color=BLUE), Integer(0, mob_class=TextDigital7)]]) \
            .next_to(n_circ, UP)
        pi = MobjectTable([[MathTex(r"\pi", color=GREEN), DecimalNumber(num_decimal_places=4, mob_class=TextDigital7)]]) \
                .next_to(n_sq, UP)
        
        self.play(*[table.create() for table in VGroup(n_sq, n_circ)])
        counter_sq = 0
        counter_circ = 0
        
        def update_dots(mob, alpha):
            nonlocal counter_sq, counter_circ
            mob.add(*dots[counter_sq:int(alpha * TOTAL_DOTS)])
            self.add(*dots[counter_sq:int(alpha * TOTAL_DOTS)])
            counter_sq = len(mob)
            dots_in_circle_on_screen = list(filter(is_inside_circle, mob))
            counter_circ = len(dots_in_circle_on_screen)
            return mob

        def update_pi(mob: MobjectTable): return mob.get_entries()[1] \
            .set_value(4 * counter_circ / counter_sq) if counter_sq != 0 else 0
        def update_n_sq(mob: MobjectTable): return mob.get_entries()[1] \
            .set_value(counter_sq)
        def update_n_circ(mob: MobjectTable): return mob.get_entries()[1] \
            .set_value(counter_circ)
        
        self.play(
            UpdateFromAlphaFunc(dots_on_screen, update_dots, run_time=10),
            FadeIn(pi),
            UpdateFromFunc(pi, update_pi, run_time=10),
            UpdateFromFunc(n_sq, update_n_sq, run_time=10),
            UpdateFromFunc(n_circ, update_n_circ, run_time=10)
        )
        self.wait()
