from manim import *
from manim.opengl import *
from beanim import *
from manim_slides import Slide
from afa_functions import *



config.write_to_movie = False
# config.renderer = "opengl"



class Intro(Slide):
    def construct(self):
        self.next_section(skip_animations=True)
        title = Title_Presentation(title= "Representational Measurement of Similarity: The Additive-Difference Model, Revisited",
                                    affiliation= "TU Darmstadt",
                                    author= "Arthur Liske")
        self.add(title)

        points = BulletedList(r"Representational Measurement",
                 r"Representation of Similarity",
                 r"Unique Representation Theorem",
                 r"Homogeneity Theorem",
                 r"Discussion",
                buff=MED_SMALL_BUFF)

        self.wipe(title, points)
        
        initTop(self, "Representational Measurement")

        self.play(Transform(points, self.top[0:5]))
        sun = SVGMobject("./images/emoji_sun.svg", use_svg_cache=False)
        sunny_cloud = SVGMobject("./images/emoji_sunny_cloud.svg", use_svg_cache=False).next_to(sun)
        cloud = SVGMobject("./images/emoji_cloud.svg", use_svg_cache=False).next_to(sunny_cloud)
        snow_cloud = SVGMobject("./images/emoji_snow_cloud.svg", use_svg_cache=False).next_to(cloud)
        weather = VGroup(sun, sunny_cloud, cloud, snow_cloud).scale(0.3).arrange(DOWN).to_edge(LEFT).shift(RIGHT*2.5+DOWN)
        self.add(weather)

        cels = VGroup(MathTex(r"30^\circ C"),
                    MathTex(r"17^\circ C"),
                    MathTex(r"9^\circ C"),
                    MathTex(r"-2^\circ C"),
                     ).scale(1.3).arrange(DOWN, buff=MED_LARGE_BUFF*1.2).to_edge(RIGHT).shift(LEFT*2.5+DOWN)

        self.add(cels)
        
        arrs = VGroup([DashedVMobject(CurvedArrow(weather[i].get_center()+RIGHT*0.5, cels[i].get_center() + LEFT*0.6, angle=-TAU/8, tip_length=0.2), dashed_ratio=0.7) for i in range(0, 4)])
        self.add(arrs)

        
        weather_box = SurroundingRectangle(weather, color=d_color)
        emp = Tex(r"Empirical\\Structure").next_to(weather_box, DOWN)

        cels_box = SurroundingRectangle(cels, color=d_color)
        num = Tex(r"Numerical\\Structure").next_to(cels_box, DOWN)
        self.play(Write(VGroup(weather_box, emp)))

        self.play(Write(VGroup(cels_box, num)))

        
        func = MathTex(r"\metric").next_to(arrs, UP)
        self.play(Write(func))

        # sun <= clouds <=> f(sun) <= f(clouds)
        sun_1 = weather[0].copy().scale(0.5)
        ssim = MathTex(r"\quad \succsim ~")
        cl_1 = weather[2].copy().scale(0.5)
        midtex = MathTex(r"~ \iff \metric(")
        sun_2 = sun_1.copy()
        midtex2 = MathTex(r") \geq \metric(")
        cl_2 = cl_1.copy()
        endtex = MathTex(r")")
        self.next_section(skip_animations=False)

        homo_gr1 = VGroup(sun_1, ssim, cl_1).arrange(RIGHT,buff=0.1)
        homo_gr2 = VGroup(midtex, sun_2, midtex2, cl_2, endtex).arrange(RIGHT, buff=0)
        homo_gr = VGroup(homo_gr1,homo_gr2).arrange(RIGHT, buff=0.2).next_to(arrs, DOWN)
        self.play(ReplacementTransform(VGroup(weather[0], weather[2], cels[0], cels[2], arrs[0], arrs[2]).copy(),homo_gr))



        weather_box.add_updater(lambda rect: rect. become(SurroundingRectangle(weather, color=d_color)))
        cels_box.add_updater(lambda rect: rect.become(SurroundingRectangle(cels, color=d_color)))

        emp.add_updater(lambda emp: emp.next_to(weather_box, DOWN))
        num.add_updater(lambda num: num.next_to(cels_box, DOWN))
        
        fat_dash = CurvedArrow(weather.get_center()+RIGHT, cels.get_center() + 1.16*LEFT, angle=-TAU/8, tip_length=0.4, stroke_width=4)
        self.play(weather.animate.arrange_in_grid(rows=2), cels.animate.arrange_in_grid(rows=2), Transform(arrs, fat_dash), func.animate.scale(1.5).next_to(fat_dash, UP).shift(LEFT*2))
        
        dp = MathTex(r":").next_to(func, RIGHT*0.3)
        self.play(homo_gr.animate.next_to(dp, RIGHT*0.5), Write(dp))

        self.wait(2)

        # homo_eq = MathTex(r"\ps{a} \succsim \ps{b} \iff \metro{\ps{a}} \geq \metro{\ps{b}}").next_to(homo_gr, DOWN)
        # self.play(FadeIn(homo_eq, shift=DOWN*0.5))





class test(Scene):
    def construct(self):
        initTop(self, "Representational Measurement")
        sun = SVGMobject("./images/emoji_sun.svg", use_svg_cache=False)
        sunny_cloud = SVGMobject("./images/emoji_sunny_cloud.svg", use_svg_cache=False).next_to(sun)
        cloud = SVGMobject("./images/emoji_cloud.svg", use_svg_cache=False).next_to(sunny_cloud)
        snow_cloud = SVGMobject("./images/emoji_snow_cloud.svg", use_svg_cache=False).next_to(cloud)
        weather = VGroup(sun, sunny_cloud, cloud, snow_cloud).scale(0.3).arrange(DOWN).to_edge(LEFT).shift(RIGHT*2.5+DOWN)
        self.add(weather)

        cels = VGroup(MathTex(r"30^\circ C"),
                    MathTex(r"17^\circ C"),
                    MathTex(r"9^\circ C"),
                    MathTex(r"-2^\circ C"),
                     ).scale(1.3).arrange(DOWN, buff=MED_LARGE_BUFF*1.2).to_edge(RIGHT).shift(LEFT*2.5+DOWN)

        self.add(cels)
        
        arrs = VGroup([DashedVMobject(CurvedArrow(weather[i].get_center()+RIGHT*0.5, cels[i].get_center() + LEFT*0.6, angle=-TAU/8, tip_length=0.2), dashed_ratio=0.7) for i in range(0, 4)])
        self.embed()
        self.add(arrs)

        func = MathTex(r"\metric").next_to(arrs, UP)
        self.add(func)

        # sun <= clouds <=> f(sun) <= f(clouds)
        sun_1 = weather[0].copy().scale(0.5)
        ssim = MathTex(r"\quad \succsim ~")
        cl_1 = weather[2].copy().scale(0.5)
        midtex = MathTex(r"~ \iff \metric(")
        sun_2 = sun_1.copy()
        midtex2 = MathTex(r") \geq \metric(")
        cl_2 = cl_1.copy()
        endtex = MathTex(r")")

        homo_gr1 = VGroup(sun_1, ssim, cl_1).arrange(RIGHT,buff=0.1)
        homo_gr2 = VGroup(midtex, sun_2, midtex2, cl_2, endtex).arrange(RIGHT, buff=0)
        homo_gr = VGroup(homo_gr1,homo_gr2).arrange(RIGHT, buff=0.2).next_to(arrs, DOWN)
        self.add(homo_gr)


        

        



