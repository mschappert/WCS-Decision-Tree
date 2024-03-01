import wx
 
# creating application object
app = wx.App()
# creating a frame
frame = wx.Frame(None, title ="WCS Data Search Tool")
pa = wx.Panel(frame)
# Adding a text to the frame object
text1 = wx.StaticText(pa, label ="Welcome to WCS Data Search Tool", pos =(100, 50))
# show it
frame.Show()
# start the event loop
app.MainLoop()