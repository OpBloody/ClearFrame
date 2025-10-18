import dearpygui.dearpygui as dpg

dragging = False
viewport = None

def exit_callback():
    dpg.destroy_context()

def create_gui(
    content_callback=None,
    window_width=400,
    window_height=250,
    viewport_title="Frameless GUI",
    decorated=False,
    resizable=False,
    window_label="Main Window",
):
    """
    Creates a frameless, draggable GUI where the viewport matches the main window size.

    Parameters:
    - content_callback: function with no args to add widgets inside the main window
    - window_width / window_height: size of the main window and viewport
    - viewport_title: title of the viewport
    - decorated: whether the viewport has borders/titlebar
    - resizable: whether the viewport is resizable
    - window_label: title of the main window inside the viewport
    """
    global viewport, dragging
    dragging = False
    dpg.create_context()

    # Viewport size matches the window size
    viewport = dpg.create_viewport(
        title=viewport_title,
        width=window_width,
        height=window_height,
        decorated=decorated,
        resizable=resizable
    )
    dpg.setup_dearpygui()

    with dpg.window(
        label=window_label,
        width=window_width,
        height=window_height,
        no_collapse=True,
        no_move=True,
        no_resize=True,
        on_close=exit_callback
    ):
        if content_callback:
            content_callback()

    # Drag handlers
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
