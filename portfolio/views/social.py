import reflex as rx
from portfolio.components.link_button import link_button
from portfolio.styles.style import Size

def social() -> rx.Component:
    return rx.vstack(
        
        rx.heading("@Social",size='2xl'),
        rx.hstack(
            #Link for GitHub
            link_button("https://github.com/raulG91","Github",image="/github.svg"),
            #Link for Linkedin
            link_button("https://www.linkedin.com/in/raul-garcia-pedrosa-35a014118/","Linkedin",image="/linkedin.svg"),
            spacing= Size.MEDIUM.value
            
        )
    )