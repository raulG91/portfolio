import reflex as rx
from portfolio.components.project import project_box

def projects()->rx.Component:
    
    return rx.vstack(
        rx.heading("Projects",size='8'),
        rx.vstack(
            project_box("Mi coleccion","Manage your videogame collection","/mi_coleccion.png",['/python.svg','/html.svg','/css.svg','/js.svg','/mysql.svg'],"https://github.com/raulG91/mi_coleccion","https://raulg91.pythonanywhere.com/"),
            project_box("Weeding website","Website used for my weeding","/weeding.png",['/python.svg','/html.svg','/css.svg','/js.svg'],"https://github.com/raulG91/weeding","https://www.bodamariaraul.net"),
            project_box("Bankig app","App for bank transactions, created during a hackaton organizated by Caixabank","/caixa_logo.png",['/python.svg','/mysql.svg','/docker.svg'],"https://github.com/raulG91/caixabank-backend-py-bankingapp","https://nuwe.io/es/hackathons/caixabank-tech-challenges-round-1?challenge=caixabank-tech-round-1-python"),
            project_box("Pollen app","Done with Reflex will provide information about pollen data in Andalucia","/Pollen_App.png",['/python.svg','/reflex.png'],"https://github.com/raulG91/pollen_app","https://pollen_app-blue-moon.reflex.run/")

        ),
        align="center",
        width="100%"
    )