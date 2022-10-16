from manim import *
import math
import decimal


Text.set_default(font="Orbitron")


def round_down(value, decimals):
    if value == int(value):
        return int(value)
        
    with decimal.localcontext() as ctx:
        d = decimal.Decimal(value)
        ctx.rounding = decimal.ROUND_DOWN
        return round(d, decimals)
        

class Car(SVGMobject):
    def __init__(self, color=GRAY):
        super().__init__("_car.svg")
        self.set_color(color)
        self.scale(0.25)


class Logo(VGroup):
    def __init__(self):
        mathink = Text("Mathink", weight=BOLD)
        integral = MathTex(r"\int", color=RED) \
            .scale(2) \
            .shift(2 * LEFT + 1.5 * UP)
        sq = Square(color=BLUE, side_length=1.5, fill_opacity=1).shift(0.5 * LEFT + UP)
        tri = Triangle(color=GREEN, fill_opacity=1).shift(1.5 * UP + LEFT)
        super().__init__(mathink, tri, integral, sq)
        self[0].next_to(self[1:], DOWN)
        self.center()
    
    def animate_logo(self, run_time=2):
        return AnimationGroup(Write(self[0], run_time=run_time), SpiralIn(self[1:], run_time=run_time))


class Apple(SVGMobject):
    def __init__(self):
        super().__init__("_apple.svg")


class Bacteria(SVGMobject):
    def __init__(self):
        super().__init__("_bacteria.svg")


class CancelLine(Line):
    def __init__(self, mobject, color=RED):
        super().__init__(DL, UR, color=RED)
        self.replace(mobject, stretch=True)


class LogoScene(Scene):
    # Render with manim channel.py LogoScene -r 2000,2000
    def construct(self):
        self.add(Logo().scale(2.5))


class BannerScene(Scene):
    # Render with manim channel.py BannerScene -r 2560,1440
    def construct(self):
        emblema = Text("Matemáticas a tu pantalla", weight=BOLD).set_color(YELLOW)
        manzanas = VGroup(*[Apple() for _ in range(6)]).scale(0.7).arrange(RIGHT)
        manzanas.next_to(emblema, DOWN)
        VGroup(emblema, manzanas).scale(0.7).center()
        grid = NumberPlane(
            background_line_style={"stroke_opacity": 0.25},
            axis_config={"stroke_opacity": 0.25}
        )
        logo = Logo().scale(0.5).to_edge(RIGHT, buff=2 * DEFAULT_MOBJECT_TO_EDGE_BUFFER)
        number_of_apples = VGroup(
            Integer(len(manzanas)).scale(2),
            Apple().scale(0.5)
        ).scale(0.7).arrange(RIGHT, buff=0.1).to_edge(LEFT, buff=2 * DEFAULT_MOBJECT_TO_EDGE_BUFFER)
        self.add(grid, emblema, manzanas, logo, number_of_apples)


class Intro(Scene):
    def construct(self):
        logo = Logo()
        self.play(logo.animate_logo())
        self.wait()


class IntroVertical(Scene):
    def construct(self):
        # Render with manim channel.py Intro -r 1080,1920
        logo = Logo().scale(2)
        self.play(logo.animate_logo())
        self.wait()


class InThePreviousVideo(Scene):
    def construct(self):
        self.camera.background_color = "#333333"
        titulo = Text("En el video anterior", weight=BOLD).to_edge(UP)
        rec = ScreenRectangle(stroke_color=WHITE, fill_color=BLACK, fill_opacity=1, height=5)
        self.add(titulo, rec)


class InThisVideo(Scene):
    def construct(self):
        self.camera.background_color = "#333333"
        titulo = Text("En este video veremos", weight=BOLD).to_edge(UP)
        rec = ScreenRectangle(stroke_color=WHITE, fill_color=BLACK, fill_opacity=1, height=5)
        self.add(titulo, rec)


class Outro(Scene):
    def construct(self):
        titulo = Text("¡Gracias por ver!", weight=BOLD)
        titulo.to_edge(UP)
        codigo_fuente = Text(
            "Código fuente: https://github.com/MathinkYT/manim_videos",
            t2c={"https://github.com/MathinkYT/manim_videos": YELLOW},
            font_size=24
        )
        codigo_fuente.to_edge(DOWN)
        self.play(GrowFromCenter(titulo), Write(codigo_fuente))
        self.wait(18)
