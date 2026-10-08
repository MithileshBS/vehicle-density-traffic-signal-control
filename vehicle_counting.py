import cv2
import glob
from vehicle_detector import VehicleDetector
def func(images_folder):
    for img_path in images_folder:
        print("Img path", img_path)
        img = cv2.imread(img_path)
        
        vehicle_boxes = vd.detect_vehicles(img)
        vehicle_count = len(vehicle_boxes)
        

        for box in vehicle_boxes:
            x, y, w, h = box

            cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

            cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)

        cv2.imshow("Cars", img)
        cv2.waitKey(1)
        return vehicle_count
def funk(value,arg1,arg2,arg3,arg4):
    if value<15:
        print('Lane-1:'+arg1 + " " + 'for 30 seconds')
        print('lane-2:'+arg2 + " " + 'for 30 seconds')
        print('lane-3:'+arg3 + " " + 'for 30 seconds')
        print('lane-4:'+arg4 + " " + 'for 30 seconds')
    elif 15 < value < 30:
        print('Lane-1:'+arg1 + " " + 'for 45 seconds')
        print('lane-2:'+arg2 + " " + 'for 45 seconds')
        print('lane-3:'+arg3 + " " + 'for 45 seconds')
        print('lane-4:'+arg4 + " " + 'for 45 seconds')
    elif 30< value<55:
        print('Lane-1:'+arg1 + " " + 'for 60 seconds')
        print('lane-2:'+arg2 + " " + 'for 60 seconds')
        print('lane-3:'+arg3 + " " + 'for 60 seconds')
        print('lane-4:'+arg4 + " " + 'for 60 seconds')

# Load Veichle Detector
vd = VehicleDetector()

# Load images from a folder
images_folder1 = glob.glob("test1/*.jpg")
a=func(images_folder1 )
print("lane1",a)
coln1="GREEN"
coln2="RED"
coln3="RED"
coln4="RED"

light1=funk(a,coln1,coln2,coln3,coln4)
images_folder2 = glob.glob("test2/*.jpg")
b=func(images_folder2)
print("lane2",b)
coln1="RED"
coln2="GREEN"
coln3="RED"
coln4="RED"
light2=funk(b,coln1,coln2,coln3,coln4)
images_folder3 = glob.glob("test3/*.jpg")
c=func(images_folder3)
print("lane3",c)
coln1="RED"
coln2="RED"
coln3="GREEN"
coln4="RED"
light3=funk(c,coln1,coln2,coln3,coln4)
images_folder4 = glob.glob("test4/*.jpg")
d=func(images_folder4)
print("lane4",d)
coln1="RED"
coln2="RED"
coln3="RED"
coln4="GREEN"
light4=funk(d,coln1,coln2,coln3,coln4)

