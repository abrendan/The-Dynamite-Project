import io
import os
import PySimpleGUI as sg
from PIL import Image


file_types = [("JPEG, PNG (*.jpg,*.png)", "*.jpg", "*png"),
              ("All files (*.*)", "*.*")]

def main():
    layout = [
        [sg.Image(key="-IMAGE-")],
        [
            sg.Text("Image File", background_color=('black')),
            sg.Input(size=(50, 1), key="-FILE-"),
            sg.FileBrowse(file_types=file_types, button_color=('purple', 'black')),
            sg.Button("Load Image", button_color=('purple', 'black'))
        ]
    ]

    window = sg.Window("The Dynamite Project", layout, resizable=True, background_color='black')

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "Load Image":
            filename = values["-FILE-"]
            if os.path.exists(filename):
                image = Image.open(values["-FILE-"])
                image.thumbnail((1600, 1600))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-IMAGE-"].update(data=bio.getvalue())

    window.close()


if __name__ == "__main__":
    main()

