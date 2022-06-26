import os
import sys
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import parse

class Viewer():

    class str:
        xmlDir = 'DTRtst_xml'
        imgDir = 'DTRtst_img'
        curFld = ""
        inptData = ""

    class list:
        xmlFlLists = []
        doc = []
        root = []
        imgDirLists = []
        imgFullLists = [[]]
        imgDirImgLists = []
        density = [[]]
        num = [[]]
        targetId = [[[]]]
        
    class int:
        frameIter1 = 0
        frameIter2 = 0
        targetIter = 0
        sorryCnt = 2

    class double:
        xmlLeft = 0.0
        xmlTop = 0.0
        xmlWidth = 0.0
        xmlHeight = 0.0
        darkCx = 0.0
        darkCy = 0.0
        darkWidth = 0.0
        darkHeight = 0.0

    def getCrnFld(self):
        self.str.curFld = os.getcwd()
        print(self.str.curFld)

    def xmlFileListsSave(self):
        #DTR_xml속 xml파일명들 변수저장 파일명 번 iter 돈다.
    
        self.list.xmlFlLists = os.listdir((self.str.curFld + "\\" + self.str.xmlDir))
        print(self.list.xmlFlLists)
        for xmlFile in self.list.xmlFlLists:
            fullXmlFileName = self.str.curFld + "\\DTRtst_xml\\" + xmlFile
            root1 = ET.parse(fullXmlFileName).getroot()
            root2 = ET.parse(fullXmlFileName)
            
            #xml파일명들에게 첫번째 파일의 내용 저장
            for frame in root1.iter("frame"):
                #print(frame.attrib['density'])
                self.list.density[0].append(frame.attrib['density'])
                #print(frame.attrib['num'])
                self.list.num[0].append(frame.attrib['num'])
                
            #print(self.list.density[0])
            #print(self.list.num[0])

            for ImgCnt, targetList in enumerate(self.list.density):
                for sequence in root1.iter('sequence'):
                    FolderName = sequence.attrib['name']
                print(FolderName)
                ImgRealCnt = ImgCnt + 1
                InptCnt = "%05d"%ImgRealCnt
                print(InptCnt)
                targetDirFull = self.str.curFld + "//DTRtst_img//" + FolderName + "_labels//img" + InptCnt + ".txt"
                f1 = open(targetDirFull, 'w')
                #maxDensityLen = len(self.list.density[0])
                #for densityIter in range(int(self.list.density[0][ImgCnt])):

                
                ImgCnt2 = 0
                for target in root1.iter('target'):
                    self.double.xmlLeft =   float(target.find('box').attrib['left']   )
                    self.double.xmlTop =    float(target.find('box').attrib['top']    )
                    self.double.xmlWidth =  float(target.find('box').attrib['width']  )
                    self.double.xmlHeight = float(target.find('box').attrib['height'] )

                    self.double.darkCx = (self.double.xmlLeft + self.double.xmlWidth / 2) / 960.0
                    self.double.darkCy = (self.double.xmlTop + self.double.xmlHeight / 2) / 540.0
                    self.double.darkWidth = self.double.xmlWidth / 960.0
                    self.double.darkHeight = self.double.xmlHeight / 540.0
                    classes = 0
                    if target.find('attribute').attrib['vehicle_type'] == 'car':
                        classes = 0
                        print(classes)
                    elif target.find('attribute').attrib['vehicle_type'] == 'van':
                        classes = 1
                    elif target.find('attribute').attrib['vehicle_type'] == 'others':
                        classes = 2
                    self.str.inptData = "%d %lf %lf %lf %lf\n"%(classes,self.double.darkCx,self.double.darkCy,self.double.darkWidth,self.double.darkHeight)
                    f1.write(self.str.inptData)
                    self.int.targetIter = self.int.targetIter + 1
                    if self.int.targetIter == int(self.list.density[0][ImgCnt2]):
                        f1.close()
                        ImgCnt2 = ImgCnt2 + 1
                        InptCnt2 = "%05d"%self.int.sorryCnt
                        targetDirFull2 = self.str.curFld + "//DTRtst_img//" + FolderName + "_labels//img" + InptCnt2 + ".txt"
                        f1 = open(targetDirFull2, 'w')
                        self.int.sorryCnt = self.int.sorryCnt + 1
                        self.int.targetIter = 0
                        
                
                

def main():
    App = Viewer()
    #현재경로 변수저장
    App.getCrnFld()
    #DTR_img속 폴더명 변수저장  
    #DTR_img속 폴더명별 이미지 파일명 변수저장
    #App.imgDirListsSave()
    #DTR_xml속 xml파일명들 변수저장
    #xml파일명들에게 첫번째 파일의 내용 저장
    #xml
    App.xmlFileListsSave()
    #첫번째 파일 내용중 density & num , parse
    #num parse의 값을 바탕으로 img속 폴더명별 이미지 파일명의 txt파일 생성
    #txt파일은 DTR_img//MVI_20011_labels//파일명.txt


if __name__ == "__main__":
    main()
