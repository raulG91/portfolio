import reflex as rx
from portfolio.styles.style import link_button_style,navbar_style,Size

def navbar()->rx.Component:
    #Create the button to Download CV
    return rx.hstack(
            rx.hstack(
                rx.button(
                    rx.icon(tag="download",height = Size.BIG.value,),
                    rx.text("Download CV"),
                    on_click=rx.download(
                    url="/documents/CV_Raul_garcia pdf",
                    filename="CV_Raul_garcia pdf",
                    ),
                    style= link_button_style,
             
                ),               
             ),
            justify_content="right" , 
            #style= navbar_style,   
        )
    
    
