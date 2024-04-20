import pythoncom
import win32api
import win32con
import win32gui
import win32com.shell

def CreateContextMenu():
    # Create a context menu
    menu = win32com.shell.Shell().MenuCreate()

    # Add menu items
    win32com.shell.Shell().MenuAdd(menu, -1, "Menu Item 1")
    win32com.shell.Shell().MenuAdd(menu, -1, "Menu Item 2")

    # Display the context menu
    win32com.shell.Shell().MenuInvoke(menu, win32api.GetMessagePos())

    # Clean up
    win32com.shell.Shell().MenuDestroy(menu)

def RegisterContextMenu():
    # Get the class name of the folder window
    folder_class_name = win32gui.FindWindowClass("CabinetWClass")

    # Register the context menu for the folder window
    win32gui.SetClassLong(folder_class_name, win32con.GCL_HCURSOR, win32api.LoadCursor(0, win32con.IDC_ARROW))
    win32gui.SetClassLong(folder_class_name, win32con.GCL_CBWNDEXTRA, 4)
    win32gui.SetClassLong(folder_class_name, win32con.GCL_HMODULE, pythoncom.PySys_GetModuleLoadFlag())
    win32gui.SetClassLong(folder_class_name, win32con.GCL_WNDPROC, win32gui.SetWindowLong(folder_class_name, win32con.GWL_WNDPROC, ContextMenuProc))

def ContextMenuProc(hwnd, msg, wParam, lParam, dword):
    if msg == win32con.WM_RBUTTONDOWN:
        CreateContextMenu()
        return 0
    else:
        return win32gui.DefWindowProc(hwnd, msg, wParam, lParam)
    
RegisterContextMenu()

win32gui.PumpMessages()