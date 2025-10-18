import gui
import dearpygui.dearpygui as dpg

def add_my_widgets():
    dpg.add_text("Hello, ClearFrame!")
    dpg.add_button(label="Click Me", callback=lambda: print("Button clicked!"))
    dpg.add_input_text(label="Type Here")

# Create GUI with viewport automatically matching main window
gui.create_gui(
    content_callback=add_my_widgets,
    window_width=300,
    window_height=200,
    viewport_title="My Custom Tool",
    decorated=False,
    resizable=True,
    window_label="Tool Panel"
)

gui.start_gui()
