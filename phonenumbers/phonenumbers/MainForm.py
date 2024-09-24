import System.Drawing
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
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ButtonHighlight
        self._label1.Location = System.Drawing.Point(232, 31)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(511, 207)
        self._label1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(232, 303)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(134, 61)
        self._button1.TabIndex = 2
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = True
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(422, 303)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(134, 61)
        self._button2.TabIndex = 3
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Location = System.Drawing.Point(609, 303)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(134, 61)
        self._button3.TabIndex = 4
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label2.Location = System.Drawing.Point(266, 72)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 5
        self._label2.Text = "6083716280"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label3.Location = System.Drawing.Point(266, 95)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 6
        self._label3.Text = "6086073567"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label4.Location = System.Drawing.Point(266, 118)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(100, 23)
        self._label4.TabIndex = 7
        self._label4.Text = "6087548331"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label5.Location = System.Drawing.Point(266, 141)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(100, 23)
        self._label5.TabIndex = 8
        self._label5.Text = "2627310839"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label6.Location = System.Drawing.Point(266, 164)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(100, 23)
        self._label6.TabIndex = 9
        self._label6.Text = "7147814636"
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label7.Location = System.Drawing.Point(266, 187)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(100, 23)
        self._label7.TabIndex = 10
        self._label7.Text = "4079392273"
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(1004, 418)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "phonenumbers"
        self.ResumeLayout(False)

