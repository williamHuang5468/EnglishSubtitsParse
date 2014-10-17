import re

class findSub():
    result = []
    def set_intput_file_path(self, fileName, fileType):
        file = open("%s%s" % (fileName, fileType))
        self.result = self.get_engsub(file)
        file.close()

    def get_engsub(self, file):
        result = []
        for data in file:
            if(re.match(r'[0-9]', data)):
                pass
            else:
                result.append(data.strip())
        return result

    def connectSentence(self, sentenceList):
        result = []
        storeSentence = ""
        for data in sentenceList:
            if(len(data) == 0):
                pass
            elif re.match(r'[^?!.]', data[len(data.strip())-1]):
                storeSentence += "%s " % data.strip()
            else:
                storeSentence += data.strip()
                result.append(storeSentence)
                storeSentence = ""
        return self.consist_string(result)

    def consist_string(self, result):
        is_connect = False
        final_Result = []
        storeString = ""
        for index in range(0, len(result)):
            if is_connect:
                is_connect = False
                continue

            if index == len(result)-1:
                final_Result.append(result[index])
                break

            if len(result[index]) <= 30 and len(result[index+1]) <= 30:
                final_Result.append("%s\t\t%s" % (result[index], result[index+1]))
                is_connect = True
                if index == len(result)-1:
                    break
            else:
                final_Result.append(result[index])
        return final_Result

    def output(self):
        self.result = self.connectSentence(self.result)
        with open(fileName + "_output.txt",'w') as newFile:
            for data in self.result:
                newFile.write(data + "\n")

if __name__ == '__main__':
    model = findSub()
    fileName = "Example/s0101"
    fileType = ".srt"
    model.set_intput_file_path(fileName, fileType)
    model.output()
