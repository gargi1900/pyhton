from tkinter import *
import requests
BACKGROUND_COLOR = "#B1DDC6"


def get_quote():
    response = requests.get("https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=20, pady=20, bg="white")

canvas = Canvas(width=600, height=500, bg=BACKGROUND_COLOR, highlightthickness=0)
background_img = PhotoImage(file="quote_image.png")
canvas.create_image(300, 207, image=background_img)
quote_text = canvas.create_text(
    300,
    207,
    text="Kanye Quote Goes HERE",
    width=300,
    font=("Arial", 15, "bold"),
    fill="black"
)
canvas.grid(row=0, column=2, rowspan=5, columnspan=4)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, bg="white", highlightthickness=0, command=get_quote)
kanye_button.grid(row=4, column=3)

window.mainloop()
