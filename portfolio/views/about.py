import reflex as rx

def about_me() -> rx.Component:
    '''Function to create section about me'''
    return rx.vstack(
        
        rx.hstack(
            rx.image(
                src="me.jpeg",
                width = "100px",
                height = "auto",
                border_radius="50px"
            ),
            rx.heading("Raul Garcia",size="8"),
            margin_top = "20px",
            
            ),
            rx.vstack(  
                rx.text(
                    'I finished my degree on IT in 2014, after a small period working as a web developer, in 2015 I started as ABAP developer. After a few years working with ABAP I was moved to integration team, working mainly with SAP Cloud platform integration. Now my role is Integration architect helping customers with their integration scenarios to build the best posible architecture according to their necessities. Even I have been working with SAP for long time I am also interesting in learning other programing languages and technologies, I used to do some courses and projects during my free time to improve my knowlwdge.',
                    margin_top="20px",align="left",padding="10px"
                ),
                #rx.text('After a few years working with ABAP I was moved to integration team, working mainly with SAP Cloud platform integration'),
                #rx.text('Even I have been working with SAP for long time I am also interesting in learning other programing languages and technologies'),
                #align_items="start",
                padding = "5px"
            ),
            align="center"   
               
    )


