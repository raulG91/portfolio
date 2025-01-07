import reflex as rx

def display_skill(skill:list)->rx.Component:
    return rx.hstack(
        rx.image(src=skill[1]),
        rx.text(skill[0]),
        align="center"
        
    )

def skill_grid(skills:dict)->rx.Component:
   return rx.grid(
        rx.foreach(
            skills,
            display_skill
        ),
        columns="3"
        
    )