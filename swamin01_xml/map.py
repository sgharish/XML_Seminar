import array
import numpy as np
import matplotlib.pyplot as plt
from jinja2 import FileSystemLoader, Environment
import os
from xml.dom import minidom

XML_File = 'test.xml'
CRITERIA_File = 'criteria.xml'
CURRENT_DIR = os.path.dirname(__file__)
template_path = os.path.join(CURRENT_DIR, "Template_e")
temp_ev = Environment(loader=FileSystemLoader(template_path))

x_cor = np.random.randint(0,200,size=(10))
y_cor = np.random.randint(0,100,size=(10))

#print(x_cor)
#print(y_cor)


def bubbleSort(arr):
    n = len(arr)


    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


    return arr


x_ode = bubbleSort(x_cor)

def xmod(arr):
    for i in range(6,10):
        if (arr[i]-arr[i-1]) <= 30 :
            arr[i] = arr[i] + 40
    return arr

#print(x_ode)

x_de = xmod(x_ode)
#print(x_de)

def y_ode(arr):
    n = len(arr)

    for i in range(1,5):
        if (arr[i]>arr[i-1]) & (arr[i] - arr[i-1]) >= 20:
             arr[i] = arr[i]
        else:
            arr[i] = arr[i-1]

    for i in range(6,10):
        if (arr[i]- arr[i-1]) <= 40:
            arr[i] = arr[i] + 20

    return arr

y_ods = y_ode(y_cor)
w = 4
#print(y_ods)

def create_la():
    laneSegments = []
    arr = x_de
    arr1 = y_ods
    for i in range(10):
        position = {'x':arr[i],'y':arr1[i]}
        laneSegments.append(position)
    return laneSegments

'''def xml_creator():
    root = minidom.Document()

    xml = root.createElement('environment')
    root.appendChild(xml)

    lanes = root.createElement('lanes')
    xml.appendChild(lanes)

    lane = root.createElement('lane')
    lanes.appendChild(lane)

    for i in range(10):
        product = root.createElement('laneSegement')
        product.setAttribute('x',str(x_de[i]))
        product.setAttribute('y',str(y_ods[i]))
        lane.appendChild(product)

    xml_str = root.toprettyxml(indent="\t")
    save_path_file = "att.xml"

    with open(save_path_file, "w") as f:
        f.write(xml_str)'''


#x_xml = xml_creator()
#with open(XML_File, 'w') as out:
 #   out.write(x_xml)
#print(x_xml)

def cone():
    conei = []
    arr = x_de
    arr1 = y_ods
    if arr1[0]%10 ==arr1[4]%10 == 0:
        cone = {'x': arr[3], 'y': arr1[3]}
        conei.append(cone)
    for i in range(6,9):
        if  arr1[i]%5 ==0 & arr1[i] > arr1[9-i-1]:
            cone = {'x': arr[i] - 3, 'y': arr1[i]-3}
            conei.append(cone)
        elif arr1[i]%10 ==0 & arr1[i] < arr1[9-i-1]:
            cone = {'x': arr[i] + 10, 'y': arr1[i] + 10}
            conei.append(cone)
        else:
            pass
    return conei

def bump():
    bumpi = []
    arr = x_de
    arr1 = y_ods
    if arr1[0] ==arr1[5]:
        bump = {'x': arr[4] + 10, 'y': arr1[4]}
        bumpi.append(bump)
    for i in range(6,9):
        if  arr1[i]%6 ==1:
            bump = {'x': arr[i] - 3, 'y': arr1[i] - 3}
            bumpi.append(bump)
        else:
            pass
    return bumpi
def mid_lix():
    x_cy = []
    arr = x_de
    for i in range(9):
        x_cy[0] = (arr[7] + arr[8]) / 2
    return x_cy
def mid_liy():
    y_cy = []
    arr1 = y_ods
    for i in range (9):
        y_cy[0] = (arr1[7] + arr1[8]) / 2
    return y_cy

def cylinder():
    cylinderi = []
    x_c = []
    y_c = []
    arr = x_de
    arr1 = y_ods
    if arr1[0] ==arr1[5]:
        cylinder = {'x': arr[5] , 'y': arr1[5] - 5}
        cylinderi.append(cylinder)
    else:
        cylinder = {'x': (arr[7] + arr[8]) / 2,'y': (arr1[7] + arr1[8]) / 2}
        cylinderi.append(cylinder)
    return cylinderi

def cube():
    arr = x_de
    arr1 = y_ods
    cubei = []
    cube = {'x': arr[9] , 'y': arr1[9]}
    cubei.append(cube)
    for i in range (9):
        if arr[i]%10 == 0:
            cube = {'x':arr[i],'y':arr1[i]-3}
            cubei.append(cube)
    return cubei

def start_pt():
    start = []
    arr = x_de
    arr1 = y_ods
    pos = {'x': arr[0],'y': arr1[0]}
    start.append(pos)
    return start

def last_pt():
    last = []
    arr = x_de
    arr1 =y_ods
    pos = {'x': arr[8] ,'y':arr1[8] }
    last.append(pos)
    return last

def lasts_pt():
    last = []
    arr = x_de
    arr1 = y_ods
    pos = {'x': arr[9] ,'y':arr1[9] }
    last.append(pos)
    return last
#x_h = conex(x_de,y_ods)
#y_co = coney(y_ods)
#print(x_h)
#print(y_co)
#mo_cone = cone()
#print(mo_cone)
#mo_bump = bump()
#print(mo_bump)
#mo_cylinder = cylinder()
#print(mo_cylinder)
#mo_cube = cube()
#print(mo_cube)

#plt.plot(x_de,y_ods)
#plt.show()

def xml_temp():
    laneSegments = create_la()
    cubes = cube()
    cylinders = cylinder()
    cones = cone()
    bumps = bump()
    xml = temp_ev.get_template(XML_File).render(laneSegments = laneSegments  ,cube =cubes ,cylinder =cylinders,cone = cones,bump = bumps)
    return xml

def criteria():
    last = last_pt()
    lasty = lasts_pt()
    start = start_pt()
    xml = temp_ev.get_template(CRITERIA_File).render(start = start, lasts = last, lasty = lasty)
    return xml

class write:
    def getTest(self):
        xml_w = xml_temp()
        test_file_paths = []
        save_path_file = os.path.join(CURRENT_DIR, "Swamin01_environment.dbe.xml")
        test_file_paths.append(save_path_file)
        with open(save_path_file,"w") as f:
            f.write(xml_w)
        criteria_w = criteria()
        save_path =  os.path.join(CURRENT_DIR, "Swamin01_crite.dbc.xml")
        test_file_paths.append(save_path)
        with open(save_path,"w") as f:
            f.write(criteria_w)
        return test_file_paths
