import reflex as rx
from portfolio.styles.style import style_box,Size

def contact()->rx.Component:
    return rx.vstack(
        rx.heading("Contact me",size="8"),
        rx.box(
            rx.link("rgarciapedrosa@gmail.com",href="mailto:rgarciapedrosa@gmail.com",is_external=True,text_decoration="underline",font_size = Size.LARGE.value),
            style=style_box,
        ),
        align="center",
        width="100%"
    )
        