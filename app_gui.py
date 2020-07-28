# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 726,591 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn_connect = wx.Button( self, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btn_connect, 0, wx.ALL, 5 )

		self.btn_disconnect = wx.Button( self, wx.ID_ANY, u"Disconnect", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btn_disconnect, 0, wx.ALL, 5 )

		self.btn_takeOff = wx.Button( self, wx.ID_ANY, u"Take Off", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btn_takeOff, 0, wx.ALL, 5 )

		self.btn_land = wx.Button( self, wx.ID_ANY, u"Land", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer4.Add( self.btn_land, 0, wx.ALL, 5 )


		bSizer3.Add( bSizer4, 0, wx.EXPAND, 5 )

		self.m_notebook2 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel6 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer131 = wx.BoxSizer( wx.HORIZONTAL )

		self.btn_addTakeOff = wx.Button( self.m_panel6, wx.ID_ANY, u"Add Take Off", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer131.Add( self.btn_addTakeOff, 0, wx.ALL, 5 )

		self.btn_addLand = wx.Button( self.m_panel6, wx.ID_ANY, u"Add Land", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer131.Add( self.btn_addLand, 0, wx.ALL, 5 )


		self.m_panel6.SetSizer( bSizer131 )
		self.m_panel6.Layout()
		bSizer131.Fit( self.m_panel6 )
		self.m_notebook2.AddPage( self.m_panel6, u"Take Off/Land", True )
		self.m_panel2 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		self.fld_x = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"x", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.fld_x, 1, wx.ALL, 5 )

		self.fld_y = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"y", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.fld_y, 1, wx.ALL, 5 )

		self.fld_z = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"z", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.fld_z, 1, wx.ALL, 5 )

		self.fld_radians = wx.TextCtrl( self.m_panel2, wx.ID_ANY, u"degrees", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.fld_radians, 1, wx.ALL, 5 )

		self.btn_addRelative = wx.Button( self.m_panel2, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer5.Add( self.btn_addRelative, 0, wx.ALL, 5 )


		self.m_panel2.SetSizer( bSizer5 )
		self.m_panel2.Layout()
		bSizer5.Fit( self.m_panel2 )
		self.m_notebook2.AddPage( self.m_panel2, u"Fly Relative", False )
		self.m_panel3 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

		self.fld_roll = wx.TextCtrl( self.m_panel3, wx.ID_ANY, u"roll", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.fld_roll, 1, wx.ALL, 5 )

		self.fld_pitch = wx.TextCtrl( self.m_panel3, wx.ID_ANY, u"pitch", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.fld_pitch, 1, wx.ALL, 5 )

		self.fld_yaw = wx.TextCtrl( self.m_panel3, wx.ID_ANY, u"yaw", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.fld_yaw, 1, wx.ALL, 5 )

		self.fld_vertical = wx.TextCtrl( self.m_panel3, wx.ID_ANY, u"vertical", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.fld_vertical, 1, wx.ALL, 5 )

		self.fld_duration = wx.TextCtrl( self.m_panel3, wx.ID_ANY, u"duration", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.fld_duration, 1, wx.ALL, 5 )

		self.btn_addDirect = wx.Button( self.m_panel3, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.btn_addDirect, 0, wx.ALL, 5 )


		self.m_panel3.SetSizer( bSizer6 )
		self.m_panel3.Layout()
		bSizer6.Fit( self.m_panel3 )
		self.m_notebook2.AddPage( self.m_panel3, u"Fly Direct", False )
		self.m_panel4 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		self.fld_sleep = wx.TextCtrl( self.m_panel4, wx.ID_ANY, u"sleep", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.fld_sleep, 1, wx.ALL, 5 )

		self.btn_addSleep = wx.Button( self.m_panel4, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer15.Add( self.btn_addSleep, 0, wx.ALL, 5 )


		self.m_panel4.SetSizer( bSizer15 )
		self.m_panel4.Layout()
		bSizer15.Fit( self.m_panel4 )
		self.m_notebook2.AddPage( self.m_panel4, u"Sleep", False )
		self.m_panel5 = wx.Panel( self.m_notebook2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		fld_directionChoices = [ u"front", u"back", u"left", u"right" ]
		self.fld_direction = wx.ComboBox( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, fld_directionChoices, 0 )
		self.fld_direction.SetSelection( 0 )
		bSizer12.Add( self.fld_direction, 1, wx.ALL, 5 )

		self.btn_addFlip = wx.Button( self.m_panel5, wx.ID_ANY, u"Add", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.btn_addFlip, 0, wx.ALL, 5 )


		self.m_panel5.SetSizer( bSizer12 )
		self.m_panel5.Layout()
		bSizer12.Fit( self.m_panel5 )
		self.m_notebook2.AddPage( self.m_panel5, u"Flip", False )

		bSizer3.Add( self.m_notebook2, 1, wx.EXPAND |wx.ALL, 5 )

		bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

		self.lc_commands = wx.ListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_NO_HEADER|wx.LC_REPORT|wx.LC_SINGLE_SEL )
		bSizer14.Add( self.lc_commands, 1, wx.ALL|wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		self.btn_remove = wx.Button( self, wx.ID_ANY, u"Remove", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.btn_remove, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_up = wx.Button( self, wx.ID_ANY, u"Up", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.btn_up, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_down = wx.Button( self, wx.ID_ANY, u"Down", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.btn_down, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_clear = wx.Button( self, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer8.Add( self.btn_clear, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer14.Add( bSizer8, 0, wx.EXPAND, 5 )


		bSizer3.Add( bSizer14, 1, wx.EXPAND, 5 )

		self.btn_runCommands = wx.Button( self, wx.ID_ANY, u"Run Commands", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.btn_runCommands, 0, wx.ALL|wx.EXPAND, 5 )

		self.btn_runFromSelection = wx.Button( self, wx.ID_ANY, u"Run Commands From Selection", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.btn_runFromSelection, 0, wx.ALL|wx.EXPAND, 5 )


		self.SetSizer( bSizer3 )
		self.Layout()
		self.statusBar = self.CreateStatusBar( 2, wx.STB_SIZEGRIP, wx.ID_ANY )

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_connect.Bind( wx.EVT_BUTTON, self.OnConnect )
		self.btn_disconnect.Bind( wx.EVT_BUTTON, self.OnDisconnect )
		self.btn_takeOff.Bind( wx.EVT_BUTTON, self.OnTakeOff )
		self.btn_land.Bind( wx.EVT_BUTTON, self.OnLand )
		self.btn_addTakeOff.Bind( wx.EVT_BUTTON, self.OnAddTakeOff )
		self.btn_addLand.Bind( wx.EVT_BUTTON, self.OnAddLand )
		self.btn_addRelative.Bind( wx.EVT_BUTTON, self.OnAddRelative )
		self.btn_addDirect.Bind( wx.EVT_BUTTON, self.OnAddDirect )
		self.btn_addSleep.Bind( wx.EVT_BUTTON, self.OnAddSleep )
		self.btn_addFlip.Bind( wx.EVT_BUTTON, self.OnAddFlip )
		self.btn_remove.Bind( wx.EVT_BUTTON, self.OnRemove )
		self.btn_up.Bind( wx.EVT_BUTTON, self.OnUp )
		self.btn_down.Bind( wx.EVT_BUTTON, self.OnDown )
		self.btn_clear.Bind( wx.EVT_BUTTON, self.OnClear )
		self.btn_runCommands.Bind( wx.EVT_BUTTON, self.OnRunCommands )
		self.btn_runFromSelection.Bind( wx.EVT_BUTTON, self.OnRunFromSelection )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnConnect( self, event ):
		event.Skip()

	def OnDisconnect( self, event ):
		event.Skip()

	def OnTakeOff( self, event ):
		event.Skip()

	def OnLand( self, event ):
		event.Skip()

	def OnAddTakeOff( self, event ):
		event.Skip()

	def OnAddLand( self, event ):
		event.Skip()

	def OnAddRelative( self, event ):
		event.Skip()

	def OnAddDirect( self, event ):
		event.Skip()

	def OnAddSleep( self, event ):
		event.Skip()

	def OnAddFlip( self, event ):
		event.Skip()

	def OnRemove( self, event ):
		event.Skip()

	def OnUp( self, event ):
		event.Skip()

	def OnDown( self, event ):
		event.Skip()

	def OnClear( self, event ):
		event.Skip()

	def OnRunCommands( self, event ):
		event.Skip()

	def OnRunFromSelection( self, event ):
		event.Skip()


