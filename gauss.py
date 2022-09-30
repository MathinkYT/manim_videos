from channel import * # channel.py includes Manim and other imports


config.frame_height, config.frame_width = config.frame_width, config.frame_height
config.pixel_height, config.pixel_width = config.pixel_width, config.pixel_height


class GaussianSumShape(VGroup):
    def __init__(self, n, side_length=1, stroke_color=WHITE, fill_color=BLUE):
        super().__init__()

        for i in range(n):
            squares = VGroup(*[Square(side_length=side_length, color=stroke_color) \
                .set_fill(fill_color, opacity=1) for _ in range(i + 1)])
            squares.arrange(RIGHT, buff=0)

            if i > 0:
                squares.move_to(self.get_corner(DL), aligned_edge=UL)

            self.add(squares)
        
        self.center()


class ProofGaussianSum(Scene):
    def construct(self):
        for i in range(5):
            lst = range(i + 2)
            nueva_suma = MathTex(f"S = {sum(lst)}", *[f"+{i}" for i in range(i + 2, 6)])

            if i == 0:
                suma = nueva_suma
                self.play(Write(suma))
                self.wait()
            
            else:
                self.play(Transform(suma, nueva_suma))
                self.wait()
        
        self.play(Circumscribe(suma))
        self.wait()
        self.play(FadeOut(suma, shift=DOWN))
        self.wait()

        suma_dificil = MathTex(r"S = 1 + 2 + 3 + 4 + \ldots + 1000")
        self.play(GrowFromCenter(suma_dificil))
        self.play(ShowPassingFlash(Underline(suma_dificil, color=YELLOW)))
        self.wait()
        self.play(suma_dificil.animate.to_edge(UP))
        self.play(suma_dificil.animate.set_opacity(0.1))

        general_sum = MathTex(r"S = 1 + 2 + 3 + 4 + \ldots + n").next_to(suma_dificil, DOWN)
        self.play(Write(general_sum))
        self.wait()
        new_general_sum = MathTex(r"S = \sum_{k = 1}^n k").next_to(suma_dificil, DOWN)
        self.play(Transform(general_sum, new_general_sum))
        self.wait()

        shape = GaussianSumShape(6, side_length=0.7)
        self.play(Write(shape[0]))
        self.play(Write(shape[1]))
        self.play(Write(shape[2:]))

        self.wait()
        br1 = Brace(shape, DOWN)
        tex1 = br1.get_tex("n")
        self.play(Write(br1), Write(tex1))
        self.wait()
        self.play(VGroup(shape, br1, tex1).animate.scale(0.5).to_edge(LEFT))
        
        shape2 = GaussianSumShape(6, side_length=0.7).scale(0.5).to_edge(RIGHT)
        double_general_sum = MathTex(r"2S = 2\sum_{k = 1}^n k").next_to(suma_dificil, DOWN)
        self.play(ReplacementTransform(shape.copy(), shape2), Transform(general_sum, double_general_sum))
        self.play(Rotate(shape2, 180 * DEGREES))
        self.play(shape2.animate.move_to(shape[-1][-1].get_corner(UR), aligned_edge=DR))
        self.play(VGroup(shape, shape2, br1, tex1).animate.scale(2).center())

        double_shape = VGroup(shape, shape2)
        br2 = Brace(double_shape, LEFT)
        tex2 = br2.get_tex("n + 1")
        self.play(Write(br2), Write(tex2))
        self.wait()
        self.play(Indicate(double_shape))
        self.wait()

        new_double_general_sum = MathTex("2", "S", "=", "n(n + 1)").next_to(suma_dificil, DOWN)
        self.play(Transform(general_sum, new_double_general_sum))
        self.wait()

        general_formula = MathTex("S", "={", "n(n + 1)", r"\over", "2}").next_to(suma_dificil, DOWN)
        self.play(TransformMatchingTex(general_sum, general_formula))
        self.play(Circumscribe(general_formula))
        self.wait()

        self.play(FadeOut(double_shape, br1, br2, tex1, tex2, general_formula, shift=DOWN))
        self.play(suma_dificil.animate.set_opacity(1).center())

        tex_strings = [r"S = {1000 \cdot 1001 \over 2}", r"S = 500 \cdot 1001", r"S = 500500"]
        for tex_string in tex_strings:
            resolucion = MathTex(tex_string)
            self.play(Transform(suma_dificil, resolucion))
            self.wait()
        
        self.play(Circumscribe(suma_dificil))
        self.wait()
