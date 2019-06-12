import easygui as g
import sys

while True:

    g.msgbox("欢迎滕子晗来的冰雪奇缘世界")

    msg = "请选择一个国家成为国王"
    title = "冰雪奇缘世界"
    choices = ['冰雪女王','琪琪国王','热火国王','邋遢大王']
    choice = g.choicebox(msg,title,choices)

    reply = g.buttonbox(title="冰雪世界",image="c:\\Temp\\timg.png",msg = "喜欢你的样子吗？",choices = ["选择","放弃"])
    

    g.msgbox("恭喜你成为了:" + str(choice))

    break
    
