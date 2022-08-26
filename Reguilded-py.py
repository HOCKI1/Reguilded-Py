from turtle import onclick
import wx 
import wx.html2 
import webview

class MyBrowser(wx.Frame): 
  def __init__(self, *args, **kwds): 
    wx.Frame.__init__(self, *args, **kwds) 
    sizer = wx.BoxSizer(wx.VERTICAL) 
    self.browser = wx.html2.WebView.New(self) 
    self._navbar = NavBar(self)
    sizer.Add(self.browser, 1, wx.EXPAND, 10) #loading webpage
    sizer.Add(self._navbar, 0, wx.EXPAND) #<<here you can add more navbars to add more buttons
    #*example* sizer.Add(self._navbar2, 0, wx.EXPAND)
    self.SetSizer(sizer)
    self.SetSize(1280,720) #default app resolution

class NavBar(wx.Panel):
  def __init__(self, parent):
    super().__init__(parent)

    #buttons
    button1 = wx.Button(self, style=wx.BU_EXACTFIT,label ="Кнопочка 1", size =(75, 30))
    button1.Bind(wx.EVT_BUTTON, self.OnClick1) #on click button 1
    button1.Bitmap = wx.ArtProvider.GetBitmap(wx.ART_TOOLBAR)

    button2 = wx.Button(self, style=wx.BU_EXACTFIT,label ="Кнопочка 2", size =(75, 30))
    button2.Bind(wx.EVT_BUTTON, self.OnClick2) #on click button 2
    button2.Bitmap = wx.ArtProvider.GetBitmap(wx.ART_TOOLBAR)

    sizer = wx.BoxSizer(wx.HORIZONTAL)
    sizer.Add(button1, 0, wx.ALL, 5) #init button 1
    sizer.Add(button2, 0, wx.ALL, 5) #init button 2
    self.SetSizer(sizer)

  def OnClick1(self, event):
    c = 1337 - 228
    print(f'{c}') #write here your own plugin! I hope in you!!!

  def OnClick2(self, event):
    webview.create_window('Plugin 2!', 'web_plugin/plugin.html', height=400, width=600, resizable=False )
    webview.start()

if __name__ == '__main__': 
  app = wx.App() 
  dialog = MyBrowser(None, -1) 
  dialog.SetTitle('Guilded Py')
  dialog.browser.LoadURL("http://www.guilded.gg") 
  dialog.Show() 
  app.MainLoop() 