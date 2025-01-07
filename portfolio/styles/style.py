from enum import Enum
from .colors import TextColor,GlobalColors
import reflex as rx

STYLESHEET = ["https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,300..800;1,300..800&display=swap"]

class Size(Enum):
    ZERO = "0px !important"
    SMALL = "0.5em"
    MEDIUM = "0.8em"
    DEFAULT = "1em"
    LARGE = "1.5em"
    BIG = "2em"
    VERY_BIG = "4em"

box_style = {
    "border":"2px"
}

style = {
    
    "font_family": "Open Sans",
    "background": GlobalColors.BACKGROUND.value,
    "color": TextColor.BODY.value,
    rx.heading: {
        "margin_top": "40px",
        "margin_bottom": "40px",

    },

}
link_button_style = {
    
    "width":"100%",
    "height": "100%",
    "border_radius": Size.SMALL.value,
    "border": Size.SMALL.value,
    "color": TextColor.HEADER.value,
    "background_color": GlobalColors.CONTENT_BUTTON.value,
         "white_space": "normal",
        "text_align": "start",
        "_hover": {
            "background_color": GlobalColors.SECONDARY.value
        }
    
}

style_box = {
    "border_width": "thin",
    "border_color": GlobalColors.SECONDARY.value,
    "border_radius": "5px",
    "padding" : "10px",
    "background":GlobalColors.CONTENT_BUTTON.value
}
navbar_style = {
    
    "z_index": "1",
    "position":"fixed",
    "width":"100%",
    "margin_bottom":"30px",
    "height": "40px"
}
