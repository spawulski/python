"""
Docstring for guitest.

Doing the guitest tutorial
"""

from guizero import App, Text, TextBox, PushButton, Slider, Picture


def say_my_name():
    """Value for MyName is set for the welcome message."""
    welcome_message.value = my_name.value


def change_text_size(slider_value):
    """Change the size of the text with a slider."""
    welcome_message.size = slider_value


app = App(title="Hello world")
welcome_message = Text(app, text="Welcome to my app", size=40,
                       font="Helvetica", color="lightblue")

my_name = TextBox(app, width=40)

update_text = PushButton(app, command=say_my_name, text="Display my name")
text_size = Slider(app, command=change_text_size, start=10, end=80)
my_cat = Picture(app, image="fox.gif")
app.display()
