import xml.etree.ElementTree as gfg 
import csv
import numpy as np
  
  
def GenerateXML(fileName, data, pos) :
      
    root = gfg.Element("annotation")

    m0 = gfg.Element("folder")
    m0.text = "train"
    root.append (m0)
      
    m1 = gfg.Element("filename")
    m1.text = data[0]
    root.append (m1)

    m4 = gfg.Element("path")
    m4.text = data[0]
    root.append (m4)

    m5 = gfg.Element("source")
    root.append (m5)
    m51 = gfg.SubElement(m5, "database")
    m51.text = "Unknown"

    m3 = gfg.Element("size")
    root.append (m3)

    n1 = gfg.SubElement(m3, "width")
    n1.text = data[2]
    n1 = gfg.SubElement(m3, "height")
    n1.text = data[3]

    m6 = gfg.Element("segmented")
    m6.text = "0"
    root.append (m6)
      
    for i in range(int(data[1])):
        m2 = gfg.Element("object")
        root.append (m2)
        
        c1 = gfg.SubElement(m2, "name")
        c1.text = "face"
        c3 = gfg.SubElement(m2, "pose")
        c3.text = "Unspecified"
        c4 = gfg.SubElement(m2, "truncated")
        c4.text = "0"
        c5 = gfg.SubElement(m2, "difficult")
        c5.text = "0"
        c2 = gfg.SubElement(m2, "bndbox")
        
        p1 = gfg.Element("xmin")
        p1.text = pos[i][0]
        p2 = gfg.Element("ymin")
        p2.text = pos[i][1]
        p3 = gfg.Element("xmax")
        p3.text = str(int(pos[i][0]) + int(pos[i][2]))
        p4 = gfg.Element("ymax")
        p4.text = str(int(pos[i][1]) + int(pos[i][3]))
        c2.append (p1)
        c2.append (p2)
        c2.append (p3)
        c2.append (p4)
      
      
    tree = gfg.ElementTree(root)
      
    with open (fileName, "wb") as files :
        tree.write(files)

    print('wwooooow')
  
# Driver Code
if __name__ == "__main__": 
    with open('wider_face_train.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row != []:
                # print(row[2])
                nm = row[0].split(".")[0] + ".xml"
                # print(nm)

                tr = row[4].split()
                tr = np.array(tr)
                tr = np.reshape(tr, (-1, 4))
                # print(tr)

                GenerateXML(nm, row, tr)