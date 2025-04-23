

from threading import Thread

import flet as ft
import mqtt


def index_screen(page, hapticfeedback) -> ft.Column:
    
    def button_callback(e):
        mqtt.connect(ip_address.value)
        Thread(target=mqtt.wait).start()
        page.go("/swip")

    column = ft.Column()
    
    image = ft.Image(
        src="images/heading-2.jpg"
    )
    
    heading = ft.Text(
        "SlidesFlow, the new universe!", 
        weight="bold", 
        theme_style=ft.TextThemeStyle.HEADLINE_LARGE)
    
    text = ft.Text(
        "SlidesFlow is an application that meets a concrete need... Control presentations (PowerPoint and others) with more class",
        theme_style=ft.TextThemeStyle.BODY_LARGE
    )

    ip_address = ft.TextField(
        hint_text="MQTT Server IP Adress"
    )

    connect_button = ft.CupertinoFilledButton(
        "Start adventure",
        expand=True,
        on_click=button_callback
    )

    column.controls = [
        image,
        ft.Container(
            padding=ft.padding.all(20),
            content=ft.Column(
                spacing=15,
                controls=[
                    heading,
                    text,
                    ft.Column(
                        controls=[
                            ip_address,
                            ft.Row(
                                controls=[
                                    connect_button
                                ]
                            )       
                        ]
                    )
                ]
            )
        )
    ]

    return column


def swip_screen() -> ft.Container:    
    
    def on_swipe(e):
        if e.velocity_x < 0:
            mqtt.client.publish(mqtt.SLIDES_TOPIC, 'right')

        elif e.velocity_x > 0:
            mqtt.client.publish(mqtt.SLIDES_TOPIC, 'left')

    return ft.Container(
        expand=True, 
        content=ft.GestureDetector(
            on_pan_end=on_swipe,
            drag_interval=10,
            content=ft.Container(
                expand=True,
                bgcolor=ft.colors.GREEN_200,
                alignment=ft.alignment.center,
                content=ft.Text("Swipe here 👆", size=20, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK),
            )
        )
    )


def main(page: ft.Page):
    
    hapticfeedback = ft.HapticFeedback()
    page.overlay.append(hapticfeedback)

    mqtt.hapticfeedback = hapticfeedback

    def route_change(e):

        page.views.clear()

        if page.route == "/":
            page.views.append(
                ft.View(
                    "/",
                    padding=ft.padding.all(0),
                    controls=[ index_screen(page, hapticfeedback) ]
                )
            )
        
        elif page.route == "/swip":
            page.views.append(
                ft.View(
                    "/swip",
                    padding=ft.padding.all(0),
                    controls=[ swip_screen() ]
                )
            )
        
        page.update()

    
    page.padding = ft.padding.all(0)

    page.on_route_change = route_change
    page.go(page.route)


ft.app(target=main)