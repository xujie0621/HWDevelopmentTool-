import matplotlib
matplotlib.use('TkAgg')

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure

import tkinter as tk
import tkinter.messagebox
import os
import ParseFile
import ParseParam
import tkinter.filedialog



class Application(tk.Tk):
    '''
    文件夹选择程序
        界面与逻辑分离
    '''
    __laste1 = ""
    __laste2 = ""
    __laste3 = ""
    def __init__(self):
        '''初始化'''
        super().__init__()  # 有点相当于tk.Tk()
        self.wm_title("Embed matplotlib in tkinter")
        self.createWidgets()

    def createWidgets(self):
        '''界面'''
        fig = Figure(figsize=(16, 9), dpi=80)
        self.ax = fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=1)

        toolbar = NavigationToolbar2Tk(self.canvas, self)
        toolbar.update()
        frame1 = tk.Frame(master=self).pack(side=tk.LEFT, padx=5)
        entryVar1 = tk.StringVar()
        entryVar2 = tk.StringVar()
        entryVar3 = tk.StringVar()
        #标签控件
        tk.Label(master=frame1,text="请输入文件地址：",font=("微软雅黑", 12),fg="blue").pack(side=tk.TOP,anchor="nw")
        #输入框
        entry1 = tk.Entry(master=frame1,font=("华文楷体", 18), textvariable=entryVar1).pack(side=tk.TOP, anchor="nw")
        tk.Button(master=frame1, text='选择文件', font=("微软雅黑", 8), command=lambda: self.selectFile(entryVar1)). \
            pack(side=tk.TOP, anchor="nw")
        tk.Label(master=frame1, text="请输入起始时间：", font=("微软雅黑", 12), fg="blue").pack(side=tk.TOP, anchor="nw")
        tk.Entry(master=frame1, font=("华文楷体", 18), textvariable = entryVar2).pack(side=tk.TOP, anchor="nw")
        tk.Label(master=frame1, text="请输入结束时间：", font=("微软雅黑", 12), fg="blue").pack(side=tk.TOP, anchor="nw")
        tk.Entry(master=frame1, font=("华文楷体", 18), textvariable=entryVar3).pack(side=tk.TOP, anchor="nw")
        frame2 = tk.Frame(master=self).pack(side=tk.LEFT, padx=5)
        checkVar1 = tk.IntVar()
        checkVar2 = tk.IntVar()
        checkVar3 = tk.IntVar()
        checkVar4 = tk.IntVar()
        C1 = tk.Checkbutton(master=frame2, text="aveDelay", variable=checkVar1, \
                         onvalue=1, offvalue=0, height=1, font=("微软雅黑", 14), \
                         width=10)
        C2 = tk.Checkbutton(master=frame2, text="lostRate", variable=checkVar2, \
                         onvalue=1, offvalue=0, height=1, font=("微软雅黑", 14), \
                         width=10)
        C3 = tk.Checkbutton(master=frame2, text="recvBR", variable=checkVar3, \
                            onvalue=1, offvalue=0, height=1, font=("微软雅黑", 14), \
                            width=10)
        C4 = tk.Checkbutton(master=frame2, text="diftime", variable=checkVar4, \
                            onvalue=1, offvalue=0, height=1, font=("微软雅黑", 14), \
                            width=10)
        C1.pack(side=tk.LEFT)
        C2.pack(side=tk.LEFT)
        C3.pack(side=tk.LEFT)
        C4.pack(side=tk.LEFT)
        # filename = tk.filedialog.askopenfilename()
        # print(filename)
        footframe = tk.Frame(master=self).pack(side=tk.LEFT)
        tk.Button(master=footframe, text='绘图',font = ("微软雅黑", 18), \
                  command=lambda: self.getDataAndParam(entryVar1.get(),entryVar2.get(),entryVar3.get(), \
                                               checkVar1.get(),checkVar2.get(),checkVar3.get(), \
                                               checkVar4.get())).pack(side=tk.TOP, anchor='n')

    def selectFile(self, entryVar):
        filename = tkinter.filedialog.askopenfilename()
        entryVar.set(filename)

    def getDataAndParam(self,e1,e2,e3,c1,c2,c3,c4):
        ret = self.checkParam(e1,e2,e3,c1,c2,c3,c4)
        if(ret):
            return 0
        if(self.__laste1 == e1 and self.__laste2 == e2 and self.__laste3 == e3):
            self.__plottingParam = self.changeNumtoStr([c1, c2, c3, c4])
            self.draw()
        else:
            paramList = [e1, e2, e3]
            pf = ParseFile.parseFile(paramList)
            dataList = pf.FindDataByKeyword()
            pp = ParseParam.ParseParam(dataList, e2)
            self.__plottingData = pp.getFisrtThreeCoordinate()
            self.__plottingShutterData = pp.getStutterCoordinate()
            self.__plottingParam = self.changeNumtoStr([c1, c2, c3, c4])
            self.__laste1 = e1
            self.__laste2 = e2
            self.__laste3 = e3
            self.draw()


    def changeNumtoStr(self, numList):
        strList = []
        if(numList[0] == 1):
            strList.append("aveDelay")
        else:
            strList.append("null")
        if (numList[1] == 1):
            strList.append("lostRate")
        else:
            strList.append("null")
        if (numList[2] == 1):
            strList.append("recvBR")
        else:
            strList.append("null")
        if (numList[3] == 1):
            strList.append("diftime")
        else:
            strList.append("null")
        return strList



    def checkParam(self,e1,e2,e3,c1,c2,c3,c4):
        if(os.path.exists(e1) == False):
            tk.messagebox.showerror("error","文件地址不存在")
            return 1
        if(len(e2) == 0):
            tk.messagebox.showerror("error","开始时间为空")
            return 1
        if(len(e3) == 0):
            tk.messagebox.showerror("error", "结束时间为空")
            return 1
        if(c1 ==0 and c2 == 0 and c3 == 0 and c4 ==0):
            tk.messagebox.showerror("error", "至少选择一个复选框")
        return 0
    def draw(self):
        '''绘图逻辑'''

        self.ax.clear()  # 清除原来的Axes区域

        array1 = np.array(self.__plottingData)
        array2 = np.array(self.__plottingShutterData)
        print(array2)
        if (self.__plottingParam[0] == "aveDelay"):
            self.ax.plot(array1[:, 0], array1[:, 1], color="green", label="aveDelay")

        if (self.__plottingParam[1] == "lostRate"):
            self.ax.plot(array1[:, 0], array1[:, 2], color="red", label="lostRate")

        if (self.__plottingParam[2] == "recvBR"):
            self.ax.plot(array1[:, 0], array1[:, 3] / 200, color="blue", label="recvBR")

        if (self.__plottingParam[3] == "diftime"):
            self.ax.plot(array2[:, 0], array2[:, 1] / 30, color="yellow", label="diftime")

        self.ax.set_xlabel("time/s")
        self.ax.set_ylabel("value")
        self.ax.legend()
        self.canvas.draw()

    def _quit(self):
        '''退出'''
        self.quit()  # 停止 mainloop
        self.destroy()  # 销毁所有部件

