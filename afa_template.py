from ..my_imports import *
from ..objects import *
from ..tables_and_plots import *
from ..text_and_organisation import *

# Here you can modify almost all parameters of objects used in these libraries. In this way you can generate new homogenous templates for your presentations.
# First you have all the variables. You can find each of the classes attributes these variables modify down in the file.

##### ---- DARK DEPTHS TEMPLATE ---- #####

# Color of the background
bg_color = "#F5ECFE"

# Font color and text size for any text and MathTex
tex_temp = TexTemplate()
tex_temp.add_to_preamble(
    r"""
    \input{afa_template.tex}
    """
)

t_size = 30
t_color = "#011638"

# Design of all the surrounding boxes (titles, refs, bullet points, vacua and similar) and general opacities
d_presence_1 = (
    "back_frame"  # What type of decorator surrounding the main title and section titles
)
d_presence_2 = "box"  # What type of decorator surrounding bulleted lists
d_ref = "none"  # What type of decorator surrounding references. Notice that refs that do not go to the UR corner should be individually modified to have a box. Refs have the color of the decorator
d_color = "#531196"  # Color of all decorators
d_s_w = 0.6  # Stroke width of all decorator and surrounding boxes
c_rad = 0.1  # Curvature of the corners of such objects
c_rad_dir_title = [1, 1, 1, 1]  # Which corners get curved for titles
c_rad_dir_boxes = [1, 1, 1, 1]  # Same, but for boxes
f_opa = 0.1  # Opacity of background of things
tight = 0.4  # How tight is the decorator with respect to the object it contains.
s_opa = 0.8  # Stroke opacity of the border
dot_size = 2  # How big the bullet points are

# Color homogenisation
h_1 = "#742F46"
h_2 = "#9F4160"
h_3 = "#45386B"
b_color = "#742F46"
v_color = "#45386B"

config.background_color = bg_color

# Definition of Tex defaults. This will change font and its color.
# Carefull! It seems that there exist some FontTemplates which do not automatically scale the parenthesis. This drove me crazy for some hours. Be aware of what font you choose.


Tex.set_default(tex_template=tex_temp, color=BLACK)
MathTex.set_default(tex_template=tex_temp, color=BLACK)
Text.set_default(color=BLACK)

# Titles #Note that the corner_rad can be negative!
# It seems that back_frame fits good both with box in text and nothing as decorator.

Title_General.set_default(  # Be careful with general size and observe that title_sections are defined to UL corner by default.
    text_size=t_size,
    text_color=t_color,
    decorator_presence=d_presence_1,
    decorator_color=d_color,
    decorator_stroke_width=d_s_w,
    corner_rad=c_rad,
    corner_rad_direction=c_rad_dir_title,
    fill_opa=f_opa,
    tightness=tight,
    stroke_opa=s_opa,
)

# Bulleted Box and References recommended to mirror if two different boxes are displayed close to each other

Text_General.set_default(  # Be careful with general size
    text_size=t_size,
    text_color=t_color,
    decorator_presence=d_presence_2,
    decorator_color=d_color,
    decorator_stroke_width=d_s_w,
    corner_rad=c_rad,
    corner_rad_direction=c_rad_dir_boxes,
    fill_opa=f_opa,
    tightness=tight,
    stroke_opa=s_opa,
    dot_scale=dot_size,
)

Ref.set_default(
    text_color=d_color, decorator_presence=d_ref
)  # Each reference will require its own definition, as one can play with the boxes and flip them to close the design and so on. To think if this can be optimised.

# Any equation
Eq_General.set_default(
    text_size=t_size,
    text_color=t_color,
    decorator_presence="no",
    decorator_color=d_color,
    decorator_stroke_width=d_s_w,
    corner_rad=c_rad,
    corner_rad_direction=c_rad_dir_boxes,
    fill_opa=f_opa,
    tightness=tight,
)

# Any Table
Table_General.set_default(
    text_color=t_color,
    hlight_1_color=h_1,
    hlight_2_color=h_2,
    hlight_3_color=h_3,
    corner_rad=c_rad,
    corner_rad_direction=c_rad_dir_boxes,
    decorator_color=t_color,
    decorator_stroke_w=d_s_w,
    stroke_opa=s_opa,
    fill_opa=f_opa,
)

# Any Plot (There are things to change and solve)
Plot_General.set_default(
    func_main_color=h_1,
    func_2_color=h_2,
    func_3_color=h_3,
    text_color=t_color,
    axis_opacity=s_opa,
    axis_stroke=d_s_w,
    decorator_presence="no",
    decorator_color=h_1,
    decorator_stroke_w=d_s_w,
    corner_rad=c_rad,
    corner_rad_direction=c_rad_dir_boxes,
    fill_opa=0,
    stroke_w=d_s_w,
    stroke_opa=s_opa,
    tightness=tight,
)

# Figures and Objects
Brane_General.set_default(  # Any brane appearing in objects
    brane_color=h_1, brane_fill_opa=0.1, brane_text_color=t_color, brane_stroke_w=2
)

Vacuum_General.set_default(  # Any vacuum appearing in objects
    vacuum_color=h_3,
    vacuum_fill_opa=f_opa,
    vacuum_stroke_w=d_s_w,
    direction_corner_rad=c_rad_dir_boxes,
    corner_rad=c_rad,
    vacuum_text_color=t_color,
)

AdS_Jc.set_default(arrow_color=h_1)


# Black hole
Black_Hole.set_default(bh_size=1, bh_color=t_color, bh_fill_opa=0.7)

# Random Photo Frame
Photo.set_default(
    decorator_style="techno",
    text_size=t_size,
    text_color=t_color,
    decorator_color=h_1,
    pin_color=h_1,
    corner_rad=c_rad,
    decorator_stroke_w=5 * d_s_w,
)  # Recommended high width to not see picture borders

# Post-it
Post_It.set_default(text_color=t_color, text_size=t_size, pin_color=h_2)

####################################################
