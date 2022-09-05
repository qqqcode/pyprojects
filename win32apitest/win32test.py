# pip install pywin32

import imp
import win32api as winapi
import win32gui as wingui
import win32ui as winui
import win32con as wincon
import win32com.client
import pythoncom

# win32api.MessageBox(0,"Hello win32","box",win32con.MB_OK,win32con.MB_ICONWARNING)

# a = winapi.GetCursorPos()



def show_window_attr(hwnd):
    if not hwnd:
        return
    WindowName = wingui.GetWindowText(hwnd)
    ClassName = wingui.GetClassName(hwnd)
    HwndPy = hwnd
    HwndSpy = hex(hwnd)
    return (WindowName, ClassName, HwndPy, HwndSpy)
show_window_attr(int(0x000104B8))


def show_top_windows():
    hwndList = []
    wingui.EnumWindows(lambda hwnd, param: param.append(show_window_attr(hwnd)), hwndList)
    return hwndList

list = show_top_windows()

def get_windows(handle,filename):
    # shell = win32com.client.Dispatch("WScript.Shell")
    # shell.SendKeys('%')
    wingui.SetForegroundWindow(handle)
    # hdDC = wingui.GetWindowDC(handle)
    # newhdDC = winui.CreateDCFromHandle(hdDC)
    # saveDC = newhdDC.CreateCompatibleDC()
    # saveBitmap = winui.CreateBitmap()
    # left, top, right, bottom = wingui.GetWindowRect(handle)
    # width = right - left
    # height = bottom - top
    # saveBitmap.CreateCompatibleBitmap(newhdDC, width, height)
    # saveDC.SelectObject(saveBitmap)
    # saveDC.BitBlt((0, 0), (width, height), newhdDC, (0, 0), wincon.SRCCOPY)
    # saveBitmap.SaveBitmapFile(saveDC, filename)
get_windows(int(0x000104B8),"截图.png")