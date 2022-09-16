from channel import * # channel.py includes Manim and other imports


config.frame_height, config.frame_width = config.frame_width, config.frame_height
config.pixel_height, config.pixel_width = config.pixel_width, config.pixel_height


class RightTriangle(Polygon):
    def __init__(self, a, b, stroke_color=WHITE, fill_color=BLUE):
        super().__init__(a * RIGHT, b * UP, ORIGIN)
        self.set_stroke(stroke_color)
        self.set_fill(fill_color, opacity=1)
        self.center()
    
    def get_sides(self):
        vertex1 = self.get_vertices()[0]
        vertex2 = self.get_vertices()[1]
        vertex3 = self.get_vertices()[2]
        return VGroup(Line(vertex1, vertex3), Line(vertex2, vertex3), Line(vertex1, vertex2))


class Demo(Scene):
    def construct(self):
        titulo = Text("Demostración visual del teorema de Pitágoras", weight=BOLD, font_size=18)
        titulo.to_edge(UP)
        self.add(titulo)
        tri = RightTriangle(2, 3/2)
        labels = VGroup(
            MathTex("a").scale(0.7).next_to(tri, DOWN),
            MathTex("b").scale(0.7).next_to(tri, LEFT),
            MathTex("c").scale(0.7).move_to(tri.get_sides()[2]).shift(0.2 * UR)
        )
        self.play(Create(tri))
        self.play(Write(labels))
        self.wait()
        
        tri_labels = VGroup(tri, labels)
        self.play(tri_labels.animate.to_edge(LEFT))
        triangles = VGroup()
        triangles.add(tri)

        for i in range(1, 4):
            triangles.add(triangles[i - 1].copy())
            self.play(Rotate(triangles[i], angle=PI / 2, about_point=triangles[i - 1].get_vertices()[0]))
            self.play(triangles[i].animate.next_to(
                triangles[i - 1].get_vertices()[0],
                direction=[RIGHT, UP, LEFT][i - 1],
                buff=0,
                aligned_edge=[DOWN, RIGHT, UP][i - 1]
            ))
        
        self.play(VGroup(triangles, tri_labels[1:]).animate.center())
        labels.add(
            *[MathTex("a").scale(0.7).next_to(triangles[i], [RIGHT, UP, LEFT][i - 1]) for i in range(1, 4)],
            *[MathTex("b").scale(0.7).next_to(triangles[i], [DOWN, RIGHT, UP][i - 1]) for i in range(1, 4)],
            *[MathTex("c").scale(0.7).move_to(triangles[i].get_sides()[2]).shift(0.2 * [UL, DL, DR][i - 1]) for i in range(1, 4)]
        )
        self.play(Write(labels[3:]))
        self.wait()

        br1 = Brace(Line(triangles[0].get_vertices()[2], triangles[1].get_vertices()[2]), DOWN, buff=0.7)
        length1 = MathTex("a {{+}} b").scale(0.7).set_color_by_tex("+", YELLOW)
        br1.put_at_tip(length1)
        self.play(Write(br1))
        self.play(Write(length1))
        self.wait()

        br2 = Brace(Line(triangles[0].get_vertices()[2], triangles[3].get_vertices()[2]), LEFT, buff=0.7)
        length2 = MathTex("a {{+}} b").scale(0.7).set_color_by_tex("+", YELLOW)
        br2.put_at_tip(length2)
        self.play(Write(br2))
        self.play(Write(length2))
        self.wait()

        g = VGroup(
            triangles,
            tri_labels[1:],
            br1, length1,
            br2, length2 
        )
        self.play(Indicate(g))
        self.wait()

        calc_area = MathTex(r"{{(a + b)^2}} = {{4\left({ab \over 2}\right)}} + {{c^2}}")
        calc_area.scale(0.7).shift(4 * DOWN)
        calc_area[1].set_color(YELLOW)
        self.play(Write(calc_area[0]))
        self.wait()
        
        last_g = VGroup(triangles[1:], labels[3:], br1, br2, length1, length2)
        self.play(
            last_g.animate.set_opacity(0.1)
        )
        self.wait()
        self.play(last_g.animate.set_opacity(1))
        self.play(Write(calc_area[1:3]))
        self.wait()

        sq = Square(side_length=5/2).next_to(tri.get_vertices()[0], RIGHT, buff=0, aligned_edge=DL)
        sq.rotate(np.arctan2(4, 3), about_point=tri.get_vertices()[0])
        sq.set_fill(PURPLE, opacity=1)
        tri_group = VGroup(last_g, tri, labels[0:2])
        self.bring_to_back(sq)
        self.play(tri_group.animate.set_opacity(0.1), FadeIn(sq))
        self.wait()
        self.play(FadeOut(sq), tri_group.animate.set_opacity(1))
        self.play(Write(calc_area[3:]))
        self.wait()

        calc_area2 = MathTex("a^2 + {{2ab}} + b^2 {{=}} 2ab {{+ c^2}}")
        calc_area2.scale(0.7).next_to(calc_area, DOWN)
        calc_area2.set_color_by_tex("=", YELLOW)
        self.play(ReplacementTransform(calc_area.copy(), calc_area2))
        self.wait()
        
        cancel_lines = VGroup(CancelLine(calc_area2[1]), CancelLine(calc_area2[4])) # CancelLine is not in Manim by default, it's in channel.py
        self.play(Create(cancel_lines))
        self.wait()
        pythagorean_theorem = MathTex("a^2 + b^2 {{=}} c^2")
        pythagorean_theorem.set_color_by_tex("=", YELLOW)
        pythagorean_theorem.scale(0.7).next_to(calc_area2, DOWN)
        self.play(Write(pythagorean_theorem))
        self.wait()
        self.play(
            FadeOut(triangles[1:], labels[3:], br1, br2, length1, length2, calc_area, calc_area2, cancel_lines),
            VGroup(VGroup(tri, labels[:3]), pythagorean_theorem).animate.scale(2).arrange(DOWN, buff=2)
        )
        self.play(Circumscribe(pythagorean_theorem))
        self.wait()
