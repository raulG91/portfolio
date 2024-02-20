"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config

import reflex as rx
import  portfolio.styles.style as Styles
from  portfolio.views.navbar import navbar
from portfolio.views.about import about_me
from portfolio.views.social import social
from portfolio.views.projects import projects
from portfolio.views.skills import skills
from portfolio.views.contact import contact

filename = f"{config.app_name}/{config.app_name}.py"

metadata = [
    {"char_set":"UTF-8"},
    {"author": "Raul Garcia"},
    {"og:description": "Portforlio Raul Garcia"},
    {"og:title": "Portfolio Raul Garcia"},
    {"og:locale": "en_US"}
    ]
class State(rx.State):
    """The app state."""

    pass

@rx.page(title = "Portfolio Raul Garcia",
         description = "Portfolio Raul Garcia",
         meta= metadata)

def index() -> rx.Component:
    #Load diferent components 
    return  rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                about_me(),
                social(),
                projects(),
                skills(),
                contact()
            )
        )
    )

# Create app instance and add index page.
app = rx.App(stylesheets=Styles.STYLESHEET,
             style=Styles.style)
app.add_page(index)
