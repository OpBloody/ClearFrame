import dearpygui.dearpygui as dpg

width = 400
height = 250
dragging = False
viewport = None

def exit_callback():
    dpg.destroy_context()

def create_gui():
    global viewport
    dpg.create_context()

    viewport = dpg.create_viewport(title="Frameless GUI", width=width, height=height, decorated=False, resizable=False)
    dpg.setup_dearpygui()

    with dpg.window(label="Frameless Window", width=width, height=height,
                    no_collapse=True, no_move=True, no_resize=True, on_close=exit_callback):
        dpg.add_text("Made by Clarifey#clarifey")

    with dpg.handler_registry():
        dpg.add_mouse_down_handler(callback=mouse_down)
        dpg.add_mouse_release_handler(callback=mouse_up)
        dpg.add_mouse_drag_handler(button=dpg.mvMouseButton_Left, callback=mouse_drag)

    dpg.show_viewport()

def mouse_down(sender, app_data):
    global dragging
    x, y = app_data
    if 0 <= y <= 19:
        dragging = True

def mouse_up(sender, app_data):
    global dragging
    dragging = False

def mouse_drag(sender, app_data):
    global dragging
    if dragging:
        _, dx, dy = app_data
        pos = dpg.get_viewport_pos()
        dpg.configure_viewport(viewport, x_pos=pos[0] + dx, y_pos=pos[1] + dy)

def start_gui():
    dpg.start_dearpygui()
    dpg.destroy_context()
