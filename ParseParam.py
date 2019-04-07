import re
import Timer
class ParseParam:
    __dataList = []
    __keywords = []
    __searchPattern1 = " "
    __searchPattern2 = " "
    __timePattern = " "
    # __coord = []
    # __coordShutter = []
    __num = 0
    def __init__(self, data, startTime):
        self.__dataList = data
        self.__startTime = startTime

    # def getDataListLen(self):
    #     return len(self.__dataList)
    #前三个参数
    def getFisrtThreeCoordinate(self):
        self.__searchPattern1 = re.compile(r".*aveDelay:\s(\d{1,}).*lostRate:\s(\d{1,}).*recvBR:\s(\d{1,}).*")
        #self.__searchPattern2 = re.compile(r".*diftime\s(\d){1,}.*")
        self.__timePattern = re.compile(r".*W:(.*)\st.*")
        sTime = Timer.time()
        difTime = 0
        coord = []
        for item in self.__dataList:
            #前三个参数的正则
            result = re.search(self.__searchPattern1, item)
            if(result):
                tmpList = []
                if(difTime == 0):
                    logTime = re.search(self.__timePattern, item)
                    self.__num = sTime.subTime(self.__startTime,logTime.group(1))
                    difTime = self.__num
                    tmpList.append(difTime)
                else:
                    tmpList.append(difTime)
                tmpList.append(int(result.group(1)))
                tmpList.append(int(result.group(2)))
                tmpList.append(int(result.group(3)))
                difTime += 0.5
                # if(self.__keywords[0] == "aveDelay"):
                #     tmpList.append(int(result1.group(1)))
                # if(self.__keywords[1] == "lostRate"):
                #     tmpList.append(int(result1.group(2)))
                # if (self.__keywords[2] == "recvBR"):
                #     tmpList.append(int(result1.group(3)))
            coord.append(tmpList)

        return coord

    def getStutterCoordinate(self):
        self.__searchPattern2 = re.compile(r".*diftime\s(\d{1,}).*")
        self.__timePattern = re.compile(r".*W:(.*)\st.*")
        sTime = Timer.time()
        coord = []
        tmp = self.__num
        for item in self.__dataList:
            tmpList = []
            result = re.search(self.__searchPattern2, item)
            if (result):
                logTime = re.search(self.__timePattern, item)
                print(logTime.group(1))
                print(self.__startTime)
                difTime = sTime.subTime(self.__startTime, logTime.group(1))
                print(difTime)
                tmpList.append(difTime)
                tmpList.append(int(result.group(1)))
            else:
                tmpList.append(tmp)
                tmpList.append(0)
                tmp += 0.5

            coord.append(tmpList)

        return coord