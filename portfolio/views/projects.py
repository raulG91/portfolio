import reflex as rx
from portfolio.components.project import project_box

def projects()->rx.Component:
    
    return rx.vstack(
        rx.heading("Projects",size='2xl'),
        rx.vstack(
            project_box("Mi coleccion","Manage your videogame collection","/mi_coleccion.png",['/python.svg','/html.svg','/css.svg','/js.svg'],"https://github.com/raulG91/mi_coleccion","https://raulg91.pythonanywhere.com/"),
            project_box("Weeding website","Website used for my weeding","/weeding.png",['/python.svg','/html.svg','/css.svg','/js.svg'],"https://github.com/raulG91/weeding","https://www.bodamariaraul.net")
        )
    )