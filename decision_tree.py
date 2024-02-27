# Name: WCS Decision Tree
# Desciption: This decision tree is for WCS which includes both marine and terrestrial data
# Purpose: WCS will use this for its workers to help categorize, identify, and select data for the organization's projects
# Date Created: 02/14/2024
# Authors: Mikayla Schappert, Naoya Morishita, Claudia

# install wxpython
# pip install wxPython==4.2.0
# pip install -U wxpython

# test
#import wx
#app = wx.App()
#frame = wx.Frame(parent=None, title='WCS Data Search')
#frame.Show()
#app.MainLoop()

# import wx module
import wx as wx
 
# creating application object
app1 = wx.App()
 
# creating a frame
frame = wx.Frame(None, title ="WCS Data Search Tool")
pa = wx.Panel(frame)
 
# Adding a text to the frame object
text1 = wx.StaticText(pa, label ="Welcome to WCS Data Search Tool", pos =(100, 50))
 
# show it
frame.Show()
 
# start the event loop
app1.Mainloop()