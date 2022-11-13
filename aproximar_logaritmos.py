from channel import * # channel.py includes Manim and other imports


config.frame_height, config.frame_width = config.frame_width, config.frame_height
config.pixel_height, config.pixel_width = config.pixel_width, config.pixel_height


class LogaritmosExactos(Scene):
    def construct(self):
        # self.add_sound("audio_aproximar_logaritmos.mp3")
        # Intro.construct(self)
        # self.clear()
        texto = Text("¡A que no sabías esto!", weight=BOLD)
        self.play(GrowFromCenter(texto))
        self.play(ShrinkToCenter(texto))
        
        initial_parts = ["\\log_", "2\\relax", "5\\relax"]
        tex_to_color_map = {
            "b\\relax": BLUE, "a\\relax": YELLOW, "n\\relax": GREEN, "2\\relax": BLUE, "5\\relax": YELLOW,
            2*"\\relax": GREEN, 3*"\\relax": ORANGE, 4*"\\relax": PURPLE
        }
        log = MathTex(*initial_parts).set_color_by_tex_to_color_map(tex_to_color_map)
        sin_calc = Text("¡Sin calculadora!", weight=BOLD).next_to(log, DOWN)
        self.play(Write(log))
        self.wait(2)
        self.play(GrowFromCenter(sin_calc))
        self.play(ShrinkToCenter(sin_calc))
        self.wait(2)
        prop1 = MathTex(
            "\\log_", "b\\relax", "a\\relax", "=", "\\log_", "b\\relax", "\\bigg(", "{a\\relax", "\\over",
            "b\\relax^", "n\\relax}", "\\bigg)", "+", "n\\relax", "\\ (", "a\\relax", ">", "b\\relax", ")"
        ).next_to(log, DOWN, buff=3.5*DEFAULT_MOBJECT_TO_MOBJECT_BUFFER).set_color_by_tex_to_color_map(tex_to_color_map)
        prop2 = MathTex(
            "\\log_", "b\\relax", "a\\relax", "=", "{1", "\\over", "\\log_", "a\\relax", "b\\relax}", "\\ (",
            "a\\relax", "<", "b\\relax", ")"
        ).next_to(prop1, DOWN).set_color_by_tex_to_color_map(tex_to_color_map)
        self.play(Write(prop1))
        self.play(Write(prop2))
        self.wait(5)
        
        log_2 = MathTex(
            *initial_parts, "=", "\\log_", "2\\relax", "\\bigg(", "{5\\relax", "\\over", "2\\relax^", "n\\relax}",
            "\\bigg)", "+", "n\\relax"
        ).set_color_by_tex_to_color_map(tex_to_color_map)
        self.play(TransformMatchingTex(log, log_2))
        self.wait(2)
        log_3 = MathTex(
            *initial_parts, "=", "\\log_", "2\\relax", "\\bigg(", "{5\\relax", "\\over", "2\\relax^", "1\\relax\\relax}",
            "\\bigg)", "+", "1\\relax\\relax"
        ).set_color_by_tex_to_color_map(tex_to_color_map)
        log_4 = MathTex(
            *initial_parts, "=", "\\log_", "2\\relax", "2.5\\relax\\relax\\relax", "+", "1\\relax\\relax"
        ).set_color_by_tex_to_color_map(tex_to_color_map)
        self.play(TransformMatchingTex(log_2, log_3))
        self.wait()
        self.play(TransformMatchingTex(log_3, log_4))
        self.wait()
        
        log_5 = MathTex(
            *initial_parts, "=", "\\log_", "2\\relax", "\\bigg(", "{5\\relax", "\\over", "2\\relax^", "2\\relax\\relax}",
            "\\bigg)", "+", "2\\relax\\relax"
        ).set_color_by_tex_to_color_map(tex_to_color_map)
        log_6 = MathTex(
            *initial_parts, "=", "\\log_", "2\\relax", "1.25\\relax\\relax\\relax", "+", "2\\relax\\relax"
        ).set_color_by_tex_to_color_map(tex_to_color_map)
        self.play(TransformMatchingTex(log_4, log_5))
        self.wait()
        self.play(TransformMatchingTex(log_5, log_6))
        self.wait(3)

        log_7 = MathTex(
            *initial_parts, "=", "{1", "\\over", "\\log_{", "1.25\\relax\\relax\\relax}", "2\\relax}", "+", "2\\relax\\relax"
        ).set_color_by_tex_to_color_map(tex_to_color_map)
        self.play(TransformMatchingTex(log_6, log_7))
        self.wait(4)

        log_8 = MathTex(
            *initial_parts, "=", "{1", "\\over", "\\log_{", "1.25\\relax\\relax\\relax}", "\\bigg(\\displaystyle", "{2\\relax", "\\over",
            "1.25\\relax\\relax\\relax^", "1\\relax\\relax}", "\\bigg)", "+", "1\\relax\\relax}", "+", "2\\relax\\relax"
        ).set_color_by_tex_to_color_map(tex_to_color_map)
        log_9 = MathTex(
            *initial_parts, "=", "{1", "\\over", "\\log_{", "1.25\\relax\\relax\\relax}", "1.6\\relax\\relax\\relax\\relax",
            "+", "1\\relax\\relax}", "+", "2\\relax\\relax"
        ).set_color_by_tex_to_color_map(tex_to_color_map)
        log_10 = MathTex(
            *initial_parts, "=", "{1", "\\over", "\\log_{", "1.25\\relax\\relax\\relax}", "\\bigg(\\displaystyle", "{2\\relax", "\\over",
            "1.25\\relax\\relax\\relax^", "2\\relax\\relax}", "\\bigg)", "+", "2\\relax\\relax}", "+", "2\\relax\\relax"
        ).set_color_by_tex_to_color_map(tex_to_color_map)
        log_11 = MathTex(
            *initial_parts, "=", "{1", "\\over", "\\log_{", "1.25\\relax\\relax\\relax}", "1.28\\relax\\relax\\relax\\relax",
            "+", "2\\relax\\relax}", "+", "2\\relax\\relax"
        ).set_color_by_tex_to_color_map(tex_to_color_map)
        self.play(TransformMatchingTex(log_7, log_8))
        self.wait(0.5)
        self.play(TransformMatchingTex(log_8, log_9))
        self.wait(0.5)
        self.play(TransformMatchingTex(log_9, log_10))
        self.wait(0.5)
        self.play(TransformMatchingTex(log_10, log_11))
        self.wait(4)

        log_12 = MathTex(
            *initial_parts, "\\approx", "{1", "\\over", "\\log_{", "1.25\\relax\\relax\\relax}", "1.25\\relax\\relax\\relax\\relax",
            "+", "2\\relax\\relax}", "+", "2\\relax\\relax"
        ).set_color_by_tex_to_color_map(tex_to_color_map)
        prop3 = MathTex("\\log_", "b\\relax", "b\\relax", "=", "1\\relax\\relax\\relax\\relax") \
            .set_color_by_tex_to_color_map(tex_to_color_map).next_to(prop2, DOWN)
        self.play(TransformMatchingTex(log_11, log_12), FadeIn(prop3))
        self.wait(3)

        log_13 = MathTex(
            *initial_parts, "\\approx", "{1", "\\over", "1", "+", "2\\relax\\relax}", "+", "2\\relax\\relax"
        ).set_color_by_tex_to_color_map(tex_to_color_map)
        self.play(TransformMatchingTex(log_12, log_13))
        self.wait()

        log_final = MathTex(*initial_parts, "\\approx", "2.\\overline{3\\relax\\relax\\relax}") \
            .set_color_by_tex_to_color_map(tex_to_color_map)
        real_val = MathTex("\\text{Valor real: }", *initial_parts, "=", f"{np.log2(5)}\\ldots\\relax\\relax\\relax") \
            .set_color_by_tex_to_color_map(tex_to_color_map).scale(0.75).next_to(log_final, DOWN)
        funciona = Text("Funciona para cualquier logaritmo", font_size=DEFAULT_FONT_SIZE/2, weight=BOLD)
        de = Text("de base número natural mayor a 1", font_size=DEFAULT_FONT_SIZE/2, weight=BOLD)
        funciona_para = VGroup(funciona, de).arrange(DOWN).next_to(real_val, DOWN)
        self.play(TransformMatchingTex(log_13, log_final))
        self.play(FadeIn(real_val), FadeOut(prop1, prop2, prop3))
        self.play(GrowFromCenter(funciona_para))
