﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ScrollBar
        self._label1.Location = System.Drawing.Point(68, 25)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(836, 245)
        self._label1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(68, 333)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(125, 49)
        self._button1.TabIndex = 1
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(427, 333)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(125, 49)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(779, 333)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(125, 49)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(1006, 421)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "schedule"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text = " Culinary computer programming alegebra biology gym art world studies english"

    def Button2Click(self, sender, e):
        self._label1.Text = ""         

    def Button3Click(self, sender, e):
        Application.Exit()