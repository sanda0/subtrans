from deep_translator import GoogleTranslator
import data
import _thread

data.langList = GoogleTranslator.get_supported_languages(as_dict=True)


def getLanList():
    return [*data.langList]

def getFile(name,lan,prog,status_box,ui):
    try:
        data.lan = data.langList[lan]
    except Exception as e:
        print(e)
    data.fileName = name
    print(name,data.lan)
    _thread.start_new_thread(makeNewSub,(prog,status_box,ui))
    

def makeNewSub(prog,status_box,ui):
    tList =[]
    # print(data.fileName)
    try:
        file = open(data.fileName,"r")
        oList = file.readlines()
        file.close()
    except Exception as e:
        # ui.popup_error(str(e))
        print(e)
    # print(oList[2+4])
    i = 2
    while (i < len(oList)):
        tList.append(oList[i])
        i = i+4
    data.max_p_value = len(tList)
    i=2
    c=1
    while (i < len(oList)):
        
        try:
            translated = GoogleTranslator(source='auto', target=data.lan).translate(oList[i])
            # nList.append(translated)
            if(i%10):
                oList[i] = translated+"\n"
            else:
                oList[i] = translated+" >>subtitle by sandakelum priyamantha<< \n"

            status= (c / data.max_p_value) * 100
            print(data.max_p_value,c)
            print(status)
            prog.UpdateBar(status)
            status_box.Update(value="%d%s"%(status,"%"))
        except Exception as e:
            ui.popup_error(str(e))
        i = i+4
        c = c+1
    # print(nList)
    i = 0
    newFile = open(data.fileName+data.lan+".srt",'a')
    status_box.Update(value="File writeing..",)
    while(i< len(oList)):
        newFile.write(oList[i])
        i=i+1
    newFile.close()
    status_box.Update(value="Done!",)






    

