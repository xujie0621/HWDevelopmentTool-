import re
import datetime
import Timer
#import tkinter
import tkinter.messagebox #弹窗库

class parseFile:
    __filePath = ' '
    def __init__(self, param):
        self.__param = param

    def FindDataByKeyword(self):
        filterData = []
        self.__filePath = self.__param[0]
        fo = open(self.__filePath, "r")
        lines = fo.read().splitlines()
        fo.close()
        filtLines = self.TimeFilter(lines)
        for line in filtLines:
            m = re.search(r"getCurrentNetState", line)
            if (m):
                filterData.append(line)
            m = re.search(r"Dec_Status", line)
            if (m):
                filterData.append(line)
        return filterData


    def TimeFilter(self, data):
        listFilter = []
        t = Timer.time()
        pattren = re.compile(r".*W:(.*)\st.*")
        for item in data:
            result = re.search(pattren, item)
            startTime = self.__param[1]
            endTime = self.__param[2]
            logTime = result.group(1)
            cFlag = t.compareTime(startTime, endTime, logTime)
            if(cFlag):
                listFilter.append(item)
        if len(listFilter):
            return listFilter
        else:
            print("input time error")
            return -1



    # def CompareTime(self, s_time, e_time, log_time):
    #     start_t = datetime.datetime.strptime(s_time, '%m-%d %H:%M:%S.%f')
    #     end_t = datetime.datetime.strptime(e_time, '%m-%d %H:%M:%S.%f')
    #     log_t = datetime.datetime.strptime(log_time, '%m-%d %H:%M:%S.%f')
    #
    #     if(log_t >= start_t and log_t <= end_t):
    #         return True


