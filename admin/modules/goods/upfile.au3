;ControlFocus("title","text",controlID) Edit1 = Edit instance 1
ControlFocus("��","","Edit1")

;Set the seconds for the Upload vindov to appear
WinWait("[CLASS:#32770]","",10)

;Set the File name text on the Edit field
ControlSetText("��","","Edit1","E:\wxt\Tpicture\123.jpg")

Sleep(2000)

;Click on the Open button
ControlClick("��","","Button1");


;AutoIt Windows Info   ���ڰ�������ʶWindows�ؼ���Ϣ��

;Compile Script to.exe ���ڽ�AutoIt���� exe ִ���ļ���

;Run Script            ����ִ��AutoIt�ű���

;SciTE Script Editor   ���ڱ�дAutoIt�ű���

;ControlFocus()��������ʶ��Window����

;ControlSetText()�������ļ���������������뱾���ļ���·��

;ControlClick()���ڵ���ϴ������еġ��򿪡���ť��


;�򿪼��±���С����
;���м��±�--Run
;Run("nihao.txt")
;�ҵ����±��������--WinActivate
;WinWaitActive("nihao.txt - ���±�")
;�������������������--Send
;Send("Xiao huo zi zui jin hao ma ?")
;�ر������--WinClose
;WinClose("nihao.txt - ���±�")
;�ҵ��Ի���--WinActivate
;WinActivate("���±�","����")
;����ָ���������--��Y����ݼ�ALT��Y
;Send("!S")