from enum import unique
from manim import *
from manim.opengl import *
from beanim import *
from manim_slides import Slide
from afa_functions import *



config.write_to_movie = False
config.renderer = "opengl"



class Intro(Slide):
    def construct(self):
        # self.next_section(skip_animations=True)
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
        
        top = initTop(self, "Representational Measurement", 0)

        self.play(ReplacementTransform(points, top[0:5]), Write(top[-1]))


        mes_def = Tex(r"Loosely speaking, measurement is the quantification of observations.")
        self.play(Write(mes_def))

        sun = SVGMobject("./images/emoji_sun.svg", use_svg_cache=False)
        sunny_cloud = SVGMobject("./images/emoji_sunny_cloud.svg", use_svg_cache=False).next_to(sun)
        cloud = SVGMobject("./images/emoji_cloud.svg", use_svg_cache=False).next_to(sunny_cloud)
        snow_cloud = SVGMobject("./images/emoji_snow_cloud.svg", use_svg_cache=False).next_to(cloud)
        weather = VGroup(sun, sunny_cloud, cloud, snow_cloud).scale(0.3).arrange(DOWN).to_edge(LEFT).shift(RIGHT*2.5+DOWN)

        self.play(Write(weather), mes_def.animate.next_to(self.top, DOWN*0.5), run_time=0.6)

        cels = VGroup(MathTex(r"30^\circ C"),
                    MathTex(r"17^\circ C"),
                    MathTex(r"9^\circ C"),
                    MathTex(r"-2^\circ C"),
                     ).scale(1.3).arrange(DOWN, buff=MED_LARGE_BUFF*1.2).to_edge(RIGHT).shift(LEFT*2.5+DOWN)

        
        arrs = VGroup([DashedVMobject(CurvedArrow(weather[i].get_center()+RIGHT*0.5, cels[i].get_center() + LEFT*0.6, angle=-TAU/8, tip_length=0.2), dashed_ratio=0.7) for i in range(0, 4)])
        self.play(Write(cels), Write(arrs))

        
        weather_box = SurroundingRectangle(weather, color=d_color)
        emp = Tex(r"Empirical\\Structure").next_to(weather_box, DOWN)

        cels_box = SurroundingRectangle(cels, color=d_color)
        num = Tex(r"Numerical\\Structure").next_to(cels_box, DOWN)
        self.play(Write(VGroup(weather_box, emp)))

        self.play(Write(VGroup(cels_box, num)))

        
        func = MathTex(r"\metric").scale(1.5).next_to(arrs, UP)
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
        # self.next_section(skip_animations=False)

        homo_gr1 = VGroup(sun_1, ssim, cl_1).arrange(RIGHT,buff=0.1)
        homo_gr2 = VGroup(midtex, sun_2, midtex2, cl_2, endtex).arrange(RIGHT, buff=0)
        homo_gr = VGroup(homo_gr1,homo_gr2).arrange(RIGHT, buff=0.2).next_to(arrs, DOWN)
        self.play(ReplacementTransform(VGroup(weather[0], weather[2], cels[0], cels[2], arrs[0], arrs[2]).copy(),homo_gr))



        weather_box.add_updater(lambda rect: rect. become(SurroundingRectangle(weather, color=d_color)))
        cels_box.add_updater(lambda rect: rect.become(SurroundingRectangle(cels, color=d_color)))

        emp.add_updater(lambda emp: emp.next_to(weather_box, DOWN))
        num.add_updater(lambda num: num.next_to(cels_box, DOWN))
        
        fat_dash = CurvedArrow(weather.get_center()+RIGHT, cels.get_center() + 1.16*LEFT, angle=-TAU/8, tip_length=0.4, stroke_width=4)
        self.play(weather.animate.arrange_in_grid(rows=2), cels.animate.arrange_in_grid(rows=2), Transform(arrs, fat_dash), func.animate.next_to(fat_dash, UP).shift(LEFT*2))
        
        dp = MathTex(r":").next_to(func, RIGHT*0.3)
        self.play(homo_gr.animate.next_to(dp, RIGHT*0.5), Write(dp))


        existThm2 = Tex(r"Proves existence of homomorphism $\metric$").next_to(homo_gr, UP*2)
        existThm = Tex(r"Existence/Representation Theorem:", color=d_color).scale(1.2).next_to(existThm2, UP)

        self.play(Write(existThm2), Write(existThm))


        fat_dash_dot = DashedVMobject(CurvedArrow(weather.get_center()+RIGHT, cels.get_center() + 1.16*LEFT, angle=TAU/8, tip_length=0.3, stroke_width=4)).shift(DOWN*0.5)

        dels = MathTex(r"\metric'").scale(1.5).next_to(fat_dash_dot, DOWN)

        self.play(Write(fat_dash_dot), Write(dels))

        uniqueThm = Tex(r"Uniqueness Theorem:", color=d_color).scale(1.2).next_to(dels, DOWN)
        uniqueThm2 = Tex(r"Proves ``how many'' such homomorphisms exist").next_to(uniqueThm, DOWN)

        self.play(Write(uniqueThm), Write(uniqueThm2))



        
        self.play(update_list(self.top, 0))
        # self.wipe()

        s1 = Tex(r"CogSci and Psychology are interested in mental representations:").shift(UP*2)
        self.add(s1)
        s2 = Tex(r"How external reality is modelled in the mind.").next_to(s1, DOWN)
        self.add(s2)

        dim = Tex("Dimensional").next_to(s2, DL*2).shift(DOWN*0.5)
        self.add(dim)

        cate = Tex("Catagorizations").next_to(s2, DR*2).shift(DOWN*0.5)
        self.add(cate)



        #ANIM: maybe animate colors
        # dot = Dot(fill_color="#e65639")
        #
        # dot_colors = hex_to_rgb(dot.color)
        #
        # r_dot = Dot(fill_color=rgb_to_color([dot_colors[0], 0.0, 0.0]))
        # g_dot = Dot(fill_color=rgb_to_color([0.0, dot_colors[1], 0.0]))
        # b_dot = Dot(fill_color=rgb_to_color([0.0, 0.0, dot_colors[2]]))


        dim_ex = BulletedList("Color: RGB, HSV",
                              "Speech: pitch, loudness, speech rate").next_to(dim, DOWN)
        self.add(dim_ex)
        # dots=VGroup(dot, r_dot, g_dot, b_dot).arrange(RIGHT).next_to(dim_ex[0], RIGHT)
        # self.add(dots)

        cat_ex = BulletedList("Color: light, dark, warm, cold",
                              "Faces: happy, angry, sad").next_to(cate, DOWN)
        self.add(cat_ex)
        


        c1 = MathTex(r"\bullet", r"\succsim", r"\bullet").scale(1.5)
        c2 = MathTex("(", r"\bullet", "," , r"\bullet", r") \succsim (", r"\bullet", ",", r"\bullet", ")").scale(1.5).next_to(c1, DOWN)

        ques = Tex("?", color=RED).scale(1.5)

        c1[0].set_color(GREEN)
        c1[2].set_color(d_color)

        c2[1].set_color(ORANGE)
        c2[3].set_color(GREEN)
        c2[5].set_color("#eab4fa")
        c2[7].set_color(d_color)

        self.add(c1)

        self.play(Transform(c1[1], ques))
        
        self.add(c2)
        

        self.remove(c1)
        c2.next_to(top, DOWN)

        prox_st = Tex("Proximity Structure", color=d_color).scale(1.5).to_edge(LEFT).shift(RIGHT+DOWN*0.5)
        self.add(prox_st)
        metric = Tex("Metric", color=d_color).scale(1.5).to_edge(RIGHT).shift(LEFT*2+DOWN*0.5)
        self.add(metric)


        ps_def0 = Tex(r"$\langle \ps{A}, \succsim \rangle$ is a PS iff for all $\ps{a}, \ps{b} \in \ps{A}:$")

        ps_def1 = BulletedList(r"$\succsim$ is connected and transitive",
                               r"$(\ps{a}, \ps{b}) \succsim (\ps{a}, \ps{a})$ for $\ps{a} \neq \ps{b}$",
                               r"$(\ps{a}, \ps{a}) \sim (\ps{b}, \ps{b})$ (minimality)",
                               r"$(\ps{a}, \ps{b}) \sim (\ps{b}, \ps{a})$ (symmetry)",
                               buff=MED_SMALL_BUFF)

        ps_def = VGroup(ps_def0, ps_def1).arrange(DOWN).next_to(prox_st, DOWN)

        self.add(ps_def)

        
        met_def0 = Tex(r"$\metric$ is a metric on $X$ iff for all $x, y, z \in X$:")
        met_def1 = BulletedList(r"$\metr{x}{x} = 0$ and $\metr{x}{y} > 0$ if $x \neq y$",
                                r"$\metr{x}{y} = \metr{y}{x}$",
                                r"$\metr{x}{y} + \metr{y}{z} \geq \metr{x}{z}$"
                                ,buff=MED_SMALL_BUFF)

        met_def = VGroup(met_def0, met_def1).arrange(DOWN).next_to(metric, DOWN)

        self.add(met_def)

        homo_tex = Tex(r"$\metric$ homomorphism:").scale(1.2).next_to(top, DOWN)
        


        d1 = MathTex(r"\iff \metric", "(", r"\bullet", "," , r"\bullet", r") \geq \metric (", r"\bullet", ",", r"\bullet", ")").scale(1.5)

        d1[2].set_color(ORANGE)
        d1[4].set_color(GREEN)
        d1[6].set_color("#eab4fa")
        d1[8].set_color(d_color)

        homo_ex = VGroup(c2, d1).arrange(RIGHT).scale(0.7).next_to(homo_tex, DOWN)
        self.add(homo_ex, homo_tex)

        homo_eq = MathTex(r"""
                            (\ps{a}, \ps{b}) \succsim (\ps{c}, \ps{d})
                            \iff
                            \delta(\ps{a}, \ps{b}) \geq \delta(\ps{c}, \ps{d})
        """).scale(1.2).next_to(homo_ex, DOWN)

        self.add(homo_eq)




class test(Scene):
    def construct(self):
        top = initTop(self, "Representation of Similarity", 1)
        self.add(top)
        self.embed()



        metric = Tex("Metric", color=d_color).scale(1.5).to_edge(RIGHT).shift(LEFT*2+DOWN*0.5)
        self.add(metric)

        mink_metr = Tex("Minkowski Metric: ")
        mink_eq = MathTex(r"\metr[p]{\ve{x}}{\ve{y}} = \left( \sum_{i=1}^{n} |x_i - y_i|^p \right)^{1/p}").next_to(mink_metr, RIGHT)

        mink = VGroup(mink_metr, mink_eq).scale(1.2).arrange(RIGHT).next_to(top, DOWN)

        self.play(ReplacementTransform(metric, mink))


        sep = Line(ORIGIN, DOWN*5)
        self.add(sep)

        ad_m = Tex("AD Model", color=d_color).scale(1.5).shift(LEFT*3.5+UP)

        seg_add = Tex("Segmental Additivity", color=d_color).scale(1.5).shift(RIGHT*3.5+UP)
        self.add(ad_m, seg_add)

        ad_m_func = MathTex(r"\left(",
                            r"\sum", "_{i=1}", "^n",
                            "|", "x", "_i", "-", "y", "_i", "|", "^p",
                            r"\right)", "^{1/p}")
        self.add(ad_m_func)

        ad_dec = VGroup(ad_m_func[5:7], ad_m_func[8:10]).copy()
        ad_diff = VGroup(ad_m_func[4:12]).copy()
        ad_sum = VGroup(ad_m_func[1:4]).copy()
        ad_t_back = VGroup(ad_m_func[-1]).copy()

        ad_m_func.next_to(ad_m, DOWN)

        ad_steps = BulletedList(
            r"Decompose $\ve{x}$ and $\ve{y}$ into $(x_1, \dots x_n)$ and $(y_1, \dots, y_n)$",
            r"Coordinatewise differences $|x_i - y_i|$ and apply $F(x)$",
            r"Sum up the transformed differences",
            r"Transform the sum with $F^{-1}$",
            buff=MED_SMALL_BUFF
            ).scale(0.85).next_to(ad_m_func, DOWN)
        
        self.play(Indicate(ad_dec))
        self.play(ReplacementTransform(ad_dec, ad_steps[0]))
        self.play(Indicate(ad_diff))
        self.play(ReplacementTransform(ad_diff, ad_steps[1]))
        self.play(Indicate(ad_sum))
        self.play(ReplacementTransform(ad_sum, ad_steps[2]))
        self.play(Indicate(ad_t_back))
        self.play(ReplacementTransform(ad_t_back, ad_steps[3]))

        ad_m1 = MathTex(r"G \left( \sum_{i=1}^n F_i(|x_i - y_i|) \right)").next_to(ad_steps, DOWN)
        self.add(ad_m1)


        self.remove(ad_steps, ad_m_func)
        ad_m1.next_to(ad_m, DOWN)

        ad_conds = BulletedList(r"$F_i, G: \mathbb{R}_{\geq 0} \rightarrow \mathbb{R}_{\geq 0}$", "(strictly) increasing").next_to(ad_m1, DOWN*1.5)
        self.add(ad_conds)
