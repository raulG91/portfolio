import reflex as rx
from portfolio.styles.style import Size
from portfolio.styles.colors import TextColor
from portfolio.components.link_button import link_button


def show_technology(tech:str)->rx.Component:
    
    return rx.image(
        src = tech,
        width = Size.BIG.value,
        height = Size.BIG .value,
        
    )    
            

def project_box(title:str,description:str,image:str,technology:list[str],source_code:str,live_link:str):
    
    return rx.vstack(
        
        #First there will be an screenshot
        rx.image(src=image,width="200px",height="200px"),
        rx.vstack(
            rx.text(title,font_size = Size.BIG.value,font_weight="bold",color=TextColor.PROJECT_TITLE.value),
            #Set project description
            rx.hstack(
                rx.text(description),
                align="center",
                padding = "5px",
            ),
            #Loop over technologies
            rx.hstack(
                rx.foreach(technology,show_technology),
                spacing= "2",
                justify_content="center"
            ),
            rx.hstack(
                link_button(source_code,"Code","/github.svg"),
                link_button(live_link,"Live",'/live.svg'),
            ),
            align_items="center",
               
         ),
        align_items="center",
        margin_top = "20px",
        width="100%"
        
    )