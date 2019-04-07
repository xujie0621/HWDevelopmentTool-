
import Gui
import tkinter

if __name__ == "__main__":

    app = Gui.Application()
    app.mainloop()
    # line = ['Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 14,lostRate: 9,recvBR: 2553\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 15,lostRate: 2,recvBR: 2453\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 16,lostRate: 1,recvBR: 2423\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 14,lostRate: 6,recvBR: 2893\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 15,lostRate: 5,recvBR: 2573\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 16,lostRate: 2,recvBR: 2893\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 11,lostRate: 1,recvBR: 2423\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 10,lostRate: 3,recvBR: 2413\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 17,lostRate: 5,recvBR: 2183\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 11,lostRate: 1,recvBR: 2583\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 15,lostRate: 8,recvBR: 2693\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 17,lostRate: 9,recvBR: 2133\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 12,lostRate: 1,recvBR: 2783\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 14,lostRate: 5,recvBR: 2363\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 13,lostRate: 9,recvBR: 2793\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 18,lostRate: 7,recvBR: 2113\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 19,lostRate: 5,recvBR: 2983\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 11,lostRate: 8,recvBR: 2783\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 15,lostRate: 6,recvBR: 2363\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 13,lostRate: 1,recvBR: 2743\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 14,lostRate: 6,recvBR: 2103\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 15,lostRate: 2,recvBR: 2123\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 16,lostRate: 1,recvBR: 2663\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 17,lostRate: 7,recvBR: 2783\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 19,lostRate: 9,recvBR: 2393\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 18,lostRate: 7,recvBR: 2783\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 17,lostRate: 5,recvBR: 2323\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 14,lostRate: 9,recvBR: 2153\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 15,lostRate: 1,recvBR: 2893\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 12,lostRate: 9,recvBR: 2452\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 15,lostRate: 7,recvBR: 2412\n', 'Line 6554: W:04-01 14:11:45.644 t:0x78ff2f94f0 getCurrentNetState>netState: 0,aveDelay: 14,lostRate: 9,recvBR: 2513\n']
    # pattern = re.compile(r".*aveDelay:\s(\d{1,}).*lostRate:\s(\d{1,}).*recvBR:\s(\d{1,}).*")
    # for i in line:
    #     a = re.match(pattern, i)
    #     print(a.group(1))

    # param1 = ["data.txt","getCurrentNetState","04-01 14:11:46.000","04-01 14:11:56.000"]
    # param2 = ["aveDelay","null","recvBR"]
    #
    # data = []
    # coo = []
    # pf = ParseFile.parseFile(param1)
    # data = pf.FindDataByKeyword()
    # pp = ParseParam.ParseParam(data, param2)
    # coo = pp.getCoordinateFromData()
    #
    # # plot = plotting.plotting(coo, param2)
    # # plot.drawPic()

    #app.mainloop()



