# Name: WCS Decision Tree
# Desciption: This decision tree is for WCS which includes both marine and terrestrial data
# Purpose: WCS will use this for its workers to help categorize, identify, and select data for the organization's projects
# Date Created: 02/14/2024
# Authors: Mikayla Schappert, Naoya Morishita, Claudia Buszta, Apple

# make sure to run python 3.10
# pip install -U wxPython

# import wx module
import wx
 
# creating application object
#app = wx.App()
# creating a frame
#frame = wx.Frame(None, title ="WCS Data Search Tool")
#pa = wx.Panel(frame)
# Adding a text to the frame object
#text1 = wx.StaticText(pa, label ="Welcome to WCS Data Search Tool", pos =(100, 50))
# show it
#frame.Show()
# start the event loop
#app.MainLoop()

# Create Frame
class MyFrame(wx.Frame):
    def __init__(
        self, title="WCS Data Search Tool", pos=wx.DefaultPosition,
        size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE):
        
        wx.Frame.__init__(self, parent, title=title)
        panel = wx.Panel(self, -1)

        button = wx.Button(panel, 1003, "Close Me")
        button.SetPosition((15, 15))
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        
    def OnCloseMe(self, event):
        self.Close(True)
        
    def OnCloseWindow(self, event):
        self.Destroy()

# Create Panel
class TestPanel(wx.Panel):
    def __init__(self, parent, log):
        self.log = log
        wx.Panel.__init__(self, parent, -1)

        b = wx.Button(self, -1, "Create and Show a Frame", (50,50))
        self.Bind(wx.EVT_BUTTON, self.OnButton, b)


    def OnButton(self, evt):
        win = MyFrame(self, -1, "This is a wx.Frame", size=(350, 200),
                  style = wx.DEFAULT_FRAME_STYLE)
        win.Show(True)

def runTest(frame, nb, log):
    win = TestPanel(nb, log)
    return win

# testing things BELOW
if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None, title="Hello World")
    frame.Show()
    app.MainLoop()

def main():
    app = MyFrame(False)
    app.MainLoop()

if __name__ == '__main__':
    app = wx.App()
    app.MainLoop()

# Search bar widget
#class Search(wx.SearchCtrl):
#    def __init__(self):
#        (parent, 
#        id=ID_ANY, 
#        value="", 
#        pos=DefaultPosition,
#        size=DefaultSize, 
#        style=0, 
#        validator=DefaultValidator,
#        name=SearchCtrlNameStr)
# Date: 02/14/2024
# Authors: Mikayla Schappert, Naoya Morishita, Claudia Buszta

# Say something
