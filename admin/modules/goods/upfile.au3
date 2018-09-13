;ControlFocus("title","text",controlID) Edit1 = Edit instance 1
ControlFocus("打开","","Edit1")

;Set the seconds for the Upload vindov to appear
WinWait("[CLASS:#32770]","",10)

;Set the File name text on the Edit field
ControlSetText("打开","","Edit1","E:\wxt\Tpicture\123.jpg")

Sleep(2000)

;Click on the Open button
ControlClick("打开","","Button1");


;AutoIt Windows Info   用于帮助我们识Windows控件信息。

;Compile Script to.exe 用于将AutoIt生成 exe 执行文件。

;Run Script            用于执行AutoIt脚本。

;SciTE Script Editor   用于编写AutoIt脚本。

;ControlFocus()方法用于识别Window窗口

;ControlSetText()用于向“文件名”输入框内输入本地文件的路径

;ControlClick()用于点击上传窗口中的“打开”按钮。


;打开记事本的小程序
;运行记事本--Run
;Run("nihao.txt")
;找到记事本的输入框--WinActivate
;WinWaitActive("nihao.txt - 记事本")
;往输入框里面输入内容--Send
;Send("Xiao huo zi zui jin hao ma ?")
;关闭输入框--WinClose
;WinClose("nihao.txt - 记事本")
;找到对话框--WinActivate
;WinActivate("记事本","保存")
;输入指令让其操作--！Y：快捷键ALT加Y
;Send("!S")