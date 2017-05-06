import re
import sys
import os

# If the subtitle has not comma or symbol like .?!
class findSub():
    result = []
    def set_intput_file_path(self, fileName, fileType):
        file = open("%s%s" % (fileName, fileType))
        self.result = self.get_engsub(file)
        file.close()

    def get_engsub(self, file):
        return [data.strip() for data in file if not re.match(r'[0-9]', data)]

    def connectSentence(self, sentenceList):
        result = []
        storeSentence = ""
        count = 0
        extractString = [] 
        extractString.append("<font color=\"#E5E5E5\">")
        extractString.append("<font color=\"#CCCCCC\">")
        extractString.append("</font>")

        for data in sentenceList:
            if(len(data) == 0):
                pass
            else:
                string = data.strip()
                string = string.replace(extractString[0], '')
                string = string.replace(extractString[1], '')
                string = string.replace(extractString[2], '')
                storeSentence += "%s " % string
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
        print("Finish Task")

if __name__ == '__main__':
    model = findSub()
    #fileName = "Example/Government Surveillance"
    fileName = "Youtube Subtitle/" + str(sys.argv[1])
    fileType = ".srt"
    if os.path.isfile(fileName+fileType):
        model.set_intput_file_path(fileName, fileType)
        model.output()
    else:
        print("File not exist : ", fileName)