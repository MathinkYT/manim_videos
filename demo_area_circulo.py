from channel import * # channel.py includes Manim and other imports


config.frame_height, config.frame_width = config.frame_width, config.frame_height
config.pixel_height, config.pixel_width = config.pixel_width, config.pixel_height


class Demo(Scene):
    def construct(self):
        titulo = Text("Área de un círculo", weight=BOLD)
        subtitulo = Text("Demostración", weight=BOLD)
        titulos = VGroup(titulo, subtitulo).arrange(DOWN)
        self.play(DrawBorderThenFill(titulos))
        self.wait(2)
        self.play(Uncreate(titulos))

        circle = Circle(color=WHITE) \
            .set_fill(BLUE, opacity=0.5)
        line = Line(circle.get_center(), circle.get_right())
        r_tex = MathTex("r") \
            .set_background_stroke(color=BLACK, width=4).next_to(line, UP)
        self.play(Create(circle))
        self.play(Create(line))
        self.play(Write(r_tex))
        self.wait()

        c_group = VGroup(circle, line, r_tex)
        self.play(c_group.animate.to_edge(UP))
        radius = circle.radius
        annulus_g = VGroup()
        rectangles = VGroup()
        lst = list(range(2, 5))
        lst.append(20)
        
        for i in lst:
            for j in range(i):
                annulus = Annulus(j * radius / i, (j + 1) * radius / i, stroke_width=2) \
                    .set_fill(BLUE, opacity=0.5).move_to(circle)
                annulus_g.add(annulus)
                rectangle = Rectangle(height=radius / i, width=2 * PI * (j + 1) * radius / i, stroke_width=2) \
                    .set_fill(BLUE, opacity=1)
                rectangles.add(rectangle)
                self.bring_to_back(annulus)
                if i != 20:
                    self.play(Create(annulus))
            
            if i == 20:
                self.bring_to_back(annulus_g)
                self.play(Create(annulus_g))

            rectangles.arrange(DOWN, buff=0)
            self.play(ReplacementTransform(annulus_g.copy(), rectangles))
            self.wait()
            if i != 20:
                self.play(FadeOut(annulus_g, rectangles))
                annulus_g = VGroup()
                rectangles = VGroup()
        
        self.wait()
        perimeter_line = Line(ORIGIN, 2 * PI * radius * RIGHT).next_to(rectangles, DOWN)
        self.play(ReplacementTransform(Circle(color=WHITE).move_to(circle), perimeter_line))
        self.wait()

        brace = Brace(perimeter_line, DOWN)
        p_tex = brace.get_tex(r"P = 2\pi r")
        self.play(Write(brace))
        self.play(Write(p_tex))
        self.wait()

        radius_line = Line(ORIGIN, radius * UP).next_to(rectangles, RIGHT)
        self.play(ReplacementTransform(line.copy(), radius_line))
        self.wait()

        r_tex2 = MathTex("r") \
            .next_to(rectangles, UP).shift(RIGHT)
        arrow = CurvedArrow(radius_line.get_end(), r_tex2.get_right())
        self.play(Create(arrow))
        self.play(Create(r_tex2))
        self.wait()

        self.play(FadeOut(rectangles))
        triangle = Triangle(color=WHITE) \
            .set_fill(BLUE, opacity=1).replace(rectangles, stretch=True)
        self.play(Create(triangle))
        self.wait()
        
        area1 = MathTex(r"A = {2\pi r \cdot r \over 2}").to_edge(DOWN)
        area2 = MathTex(r"A = ", r"{2", r"\pi r^2 \over", r"2}").to_edge(DOWN)
        cancels = VGroup(
            CancelLine(area2[1]),
            CancelLine(area2[3])
        )

        self.play(Write(area1))
        self.wait()
        self.play(ReplacementTransform(area1, area2))
        self.wait()
        self.play(Create(cancels))
        self.wait()
        self.play(Uncreate(cancels))
        self.wait()

        result = MathTex(r"A = \pi r^2").scale(2).next_to(c_group.copy().scale(2).center(), DOWN)
        self.play(
            FadeOut(annulus_g, perimeter_line, radius_line, r_tex2, p_tex, arrow, brace, triangle),
            c_group.animate.scale(2).center(),
            ReplacementTransform(area2, result)
        )
        self.play(Circumscribe(result))
        self.wait()
