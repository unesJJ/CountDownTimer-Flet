import flet as ft
from time import sleep

def main(page: ft.Page):
    page.title = "counte down timer V0.2"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    #hf = ft.HapticFeedback()

    txt_number = ft.TextField(value="10", text_align=ft.TextAlign.CENTER, width=100)
    
    def Count(e):
        while int(txt_number.value) > 0:
            if btn.data == "paused":
                break
            sleep(1)
            txt_number.value = str(int(txt_number.value) - 1)
            page.update()
        
        if int(txt_number.value) == 0:
            #hf.vibrate()
            return

    def pause_btn_clicked(e):
        btn.icon = ft.icons.PLAY_CIRCLE_FILL_OUTLINED
        btn.on_click = play_btn_clicked
        btn.data = "paused"
        btn.icon_color="red"
        page.update()

    def play_btn_clicked(e):
        btn.icon = ft.icons.PAUSE_CIRCLE_FILLED_ROUNDED
        btn.on_click = pause_btn_clicked
        btn.data = "played"
        btn.icon_color="blue"
        page.update()
        Count(e)
    
    
    btn = ft.IconButton(icon=ft.icons.PLAY_CIRCLE_FILL_OUTLINED, icon_size=70, icon_color="red", on_click=play_btn_clicked, data="paused")

    page.add(
        ft.Row([txt_number],alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(
            [btn],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )

ft.app(main)
