
import os,cv2,sys,shutil
 
from xml.dom.minidom import Document
 
def writexml(filename,saveimg,bboxes,xmlpath):
    doc = Document()
 
    annotation = doc.createElement('annotation')

    doc.appendChild(annotation)
 
    folder = doc.createElement('folder')
 
    folder_name = doc.createTextNode('widerface')
    folder.appendChild(folder_name)
    annotation.appendChild(folder)
    filenamenode = doc.createElement('filename')
    filename_name = doc.createTextNode(filename)
    filenamenode.appendChild(filename_name)
    annotation.appendChild(filenamenode)
    source = doc.createElement('source')
    annotation.appendChild(source)
    database = doc.createElement('database')
    database.appendChild(doc.createTextNode('wider face Database'))
    source.appendChild(database)
    annotation_s = doc.createElement('annotation')
    annotation_s.appendChild(doc.createTextNode('PASCAL VOC2007'))
    source.appendChild(annotation_s)
    image = doc.createElement('image')
    image.appendChild(doc.createTextNode('flickr'))
    source.appendChild(image)
    flickrid = doc.createElement('flickrid')
    flickrid.appendChild(doc.createTextNode('-1'))
    source.appendChild(flickrid)
    owner = doc.createElement('owner')
    annotation.appendChild(owner)
    flickrid_o = doc.createElement('flickrid')
    flickrid_o.appendChild(doc.createTextNode('kyle'))
    owner.appendChild(flickrid_o)
    name_o = doc.createElement('name')
    name_o.appendChild(doc.createTextNode('kyle'))
    owner.appendChild(name_o)
 
    size = doc.createElement('size')
    annotation.appendChild(size)
 
    width = doc.createElement('width')
    width.appendChild(doc.createTextNode(str(saveimg.shape[1])))
    height = doc.createElement('height')
    height.appendChild(doc.createTextNode(str(saveimg.shape[0])))
    depth = doc.createElement('depth')
    depth.appendChild(doc.createTextNode(str(saveimg.shape[2])))
 
    size.appendChild(width)
 
    size.appendChild(height)
    size.appendChild(depth)
    segmented = doc.createElement('segmented')
    segmented.appendChild(doc.createTextNode('0'))
    annotation.appendChild(segmented)
    for i in range(len(bboxes)):
        bbox = bboxes[i]
        objects = doc.createElement('object')
        annotation.appendChild(objects)
        object_name = doc.createElement('name')
        object_name.appendChild(doc.createTextNode('face'))
        objects.appendChild(object_name)
        pose = doc.createElement('pose')
        pose.appendChild(doc.createTextNode('Unspecified'))
        objects.appendChild(pose)
        truncated = doc.createElement('truncated')
        truncated.appendChild(doc.createTextNode('1'))
        objects.appendChild(truncated)
        difficult = doc.createElement('difficult')
        difficult.appendChild(doc.createTextNode('0'))
        objects.appendChild(difficult)
        bndbox = doc.createElement('bndbox')
        objects.appendChild(bndbox)
        xmin = doc.createElement('xmin')
        xmin.appendChild(doc.createTextNode(str(bbox[0])))
        bndbox.appendChild(xmin)
        ymin = doc.createElement('ymin')
        ymin.appendChild(doc.createTextNode(str(bbox[1])))
        bndbox.appendChild(ymin)
        xmax = doc.createElement('xmax')
        xmax.appendChild(doc.createTextNode(str(bbox[0] + bbox[2])))
        bndbox.appendChild(xmax)
        ymax = doc.createElement('ymax')
        ymax.appendChild(doc.createTextNode(str(bbox[1] + bbox[3])))
        bndbox.appendChild(ymax)
    f = open(xmlpath, "w")
    f.write(doc.toprettyxml(indent=''))
    f.close()
 
 
rootdir = "/kyle/workspace/dataset/public/widerface"
 
 
def convertimgset(img_set):
    imgdir = rootdir + "/WIDER_" + img_set + "/images"
    gtfilepath = rootdir + "/wider_face_split/wider_face_" + img_set + "_bbx_gt.txt"
 
    fwrite = open(rootdir + "/ImageSets/Main/" + img_set + ".txt", 'w')
 
    index = 0
 
    with open(gtfilepath, 'r') as gtfiles:
        while(True): #true
            filename = gtfiles.readline()[:-1]
            if filename == None or filename == "":
                break
            imgpath = imgdir + "/" + filename
 
            img = cv2.imread(imgpath)
 
            if not img.data:
                break;
 
            numbbox = int(gtfiles.readline())
 
            bboxes = []
 
            print(numbbox)
 
            for i in range(numbbox):
                line = gtfiles.readline()
                lines = line.split(" ")
                lines = lines[0:4]
 
                bbox = (int(lines[0]), int(lines[1]), int(lines[2]), int(lines[3]))
 
                if int(lines[2]) < 40 or int(lines[3]) < 40:
                    continue
 
                bboxes.append(bbox)
 
                #cv2.rectangle(img, (bbox[0],bbox[1]),(bbox[0]+bbox[2],bbox[1]+bbox[3]),color=(255,255,0),thickness=1)
 
            filename = filename.replace("/", "_")
 
            if len(bboxes) == 0:
                print("no face")
                continue
            #cv2.imshow("img", img)
            #cv2.waitKey(0)
 
            cv2.imwrite("{}/JPEGImages/{}".format(rootdir,filename), img)
 
            fwrite.write(filename.split(".")[0] + "\n")
 
            xmlpath = "{}/Annotations/{}.xml".format(rootdir,filename.split(".")[0])
 
            writexml(filename, img, bboxes, xmlpath)
 
            print("success number is ", index)
            index += 1
 
    fwrite.close()
 
if __name__=="__main__":
    img_sets = ["train","val"]
    for img_set in img_sets:
        convertimgset(img_set)
 
#    shutil.move(rootdir + "/ImageSets/Main/" + "train.txt", rootdir + "/ImageSets/Main/" + "trainval.txt")
#    shutil.move(rootdir + "/ImageSets/Main/" + "val.txt", rootdir + "/ImageSets/Main/" + "test.txt")