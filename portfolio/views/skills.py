import reflex as rx
from portfolio.components.skill_grid import skill_grid

def skills()->rx.Component:
    
    skills = {
        
        "Abap":"/sap.svg",
        "Python": "/python.svg",
        "Javascript":"/js.svg",
        "HTML":"/html.svg",
        "CSS": "/css.svg"
    }
            
    return rx.vstack(
        
        rx.heading("<Languages/>",size='8'),
        skill_grid(skills=skills),
        align="center",
        width="100%"
    )