# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
# http://www.wxformbuilder.org/
##
# PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
# Class MyFrame1
###########################################################################

from pyplot import *


class MyFrame1(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Graph Builder", pos=wx.DefaultPosition,
                          size=wx.Size(170, 250), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BTNFACE))

        gSizer2 = wx.GridSizer(0, 2, 0, 0)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText1 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Enter the first function", wx.DefaultPosition,
                                           wx.DefaultSize, wx.ALIGN_CENTRE)
        self.m_staticText1.Wrap(-1)
        bSizer2.Add(self.m_staticText1, 0, wx.ALL, 5)

        self.m_textCtrl1 = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_CENTRE)
        bSizer2.Add(self.m_textCtrl1, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText2 = wx.StaticText(self.m_panel1, wx.ID_ANY, u"Enter the second function", wx.DefaultPosition,
                                           wx.DefaultSize, wx.ALIGN_CENTRE)
        self.m_staticText2.Wrap(-1)
        bSizer2.Add(self.m_staticText2, 0, wx.ALL | wx.EXPAND, 5)

        self.m_textCtrl2 = wx.TextCtrl(self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize,
                                       wx.TE_CENTRE)
        bSizer2.Add(self.m_textCtrl2, 0, wx.ALL | wx.EXPAND, 5)

        self.m_button1 = wx.Button(self.m_panel1, wx.ID_ANY, u"Build intersection", wx.DefaultPosition, wx.DefaultSize,
                                   0)
        bSizer2.Add(self.m_button1, 0, wx.ALL | wx.EXPAND, 5)
        self.m_button2 = wx.Button(self.m_panel1, wx.ID_ANY, u"Settings", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.m_button2, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel1.SetSizer(bSizer2)
        self.m_panel1.Layout()
        bSizer2.Fit(self.m_panel1)
        gSizer2.Add(self.m_panel1, 1, wx.ALL, 5)

        self.m_panel4 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        bSizer4 = wx.BoxSizer(wx.VERTICAL)
        self.m_panel4.Show(False)
        self.m_staticText4 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Set the X axis", wx.DefaultPosition,
                                           wx.DefaultSize, wx.ALIGN_CENTRE)
        self.m_staticText4.Wrap(-1)
        bSizer4.Add(self.m_staticText4, 0, wx.ALL | wx.EXPAND, 5)

        self.m_slider1 = wx.Slider(self.m_panel4, wx.ID_ANY, 25, 0, 50, wx.DefaultPosition, wx.DefaultSize,
                                   wx.SL_HORIZONTAL)
        bSizer4.Add(self.m_slider1, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText6 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Set the Y axis", wx.DefaultPosition,
                                           wx.DefaultSize, wx.ALIGN_CENTRE)
        self.m_staticText6.Wrap(-1)
        bSizer4.Add(self.m_staticText6, 0, wx.ALL | wx.EXPAND, 5)

        self.m_slider2 = wx.Slider(self.m_panel4, wx.ID_ANY, 25, 0, 50, wx.DefaultPosition, wx.DefaultSize,
                                   wx.SL_HORIZONTAL)
        bSizer4.Add(self.m_slider2, 0, wx.ALL | wx.EXPAND, 5)

        self.m_staticText7 = wx.StaticText(self.m_panel4, wx.ID_ANY, u"Set the graph range", wx.DefaultPosition,
                                           wx.DefaultSize, wx.ALIGN_CENTRE)
        self.m_staticText7.Wrap(-1)
        bSizer4.Add(self.m_staticText7, 0, wx.ALL | wx.EXPAND, 5)

        self.m_slider3 = wx.Slider(self.m_panel4, wx.ID_ANY, 25, 0, 50, wx.DefaultPosition, wx.DefaultSize,
                                   wx.SL_HORIZONTAL)
        bSizer4.Add(self.m_slider3, 0, wx.ALL | wx.EXPAND, 5)

        self.m_panel4.SetSizer(bSizer4)
        self.m_panel4.Layout()
        bSizer4.Fit(self.m_panel4)
        gSizer2.Add(self.m_panel4, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(gSizer2)
        self.Layout()

        self.Centre(wx.BOTH)
        # Connect Events
        self.m_button1.Bind(wx.EVT_BUTTON, self.build)
        self.m_button2.Bind(wx.EVT_BUTTON, self.show_settings)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def build(self, event):
        makeGraph(self.m_textCtrl1.GetValue(), self.m_textCtrl2.GetValue(), int(self.m_slider1.GetValue()),
                  int(self.m_slider2.GetValue()), int(self.m_slider3.GetValue()), 'r', 'g')
        print(self.m_textCtrl1.GetValue())
        event.Skip()

    def show_settings(self, event):
        if self.GetSize()[0] < 250:
            self.SetSize((350, 250))
        self.m_panel4.Show(True)
        event.Skip()


app = wx.App()
frame = MyFrame1(None)
frame.Show(True)
app.MainLoop()
