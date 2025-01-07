import reflex as rx
from portfolio.styles.style import Size,link_button_style

def link_button(address:str,title:str,image:str,is_external:bool=True) ->rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.cond(
                    (image != ''),
                    rx.image(
                        src = image,
                        width = Size.LARGE.value,
                        height = Size.LARGE.value,
                        margin=Size.MEDIUM.value,
                     )
                ),
                rx.text(title),
                align="center"
                
            ),
            style=link_button_style 
        ) ,   
        href= address,
        is_external=is_external
    )