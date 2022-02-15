import cv2
import HandTrackingModule as htm

capture = cv2.VideoCapture(0)

detect = htm.handDetector(detectionConfidence=0.85)

draw_list = []

while True:
    _,image = capture.read()
    image  = cv2.flip(image , 1)

    img = detect.findHands(image)
    userhands = detect.findPosition(image) #detects no of points available and marks them with id no. , index finger is marked as 8 


    for i in draw_list:
        cv2.circle(image , i  , 5 , (255,0,0) , -1)
    
    if len(userhands) != 0 :

        userX = userhands[8][1]
        userY = userhands[8][2]

        if  userhands[8][2] < userhands[6][2] and userhands[12][2] > userhands[10][2] : #when index finger only pointed 
            draw_list.append((userX, userY))

        if userhands[8][2] < userhands[6][2] and userhands[12][2] < userhands[10][2] :
            for (x,y) in draw_list :
                if (x > userX - 20 and x < userX + 20) and (y > userY - 20 and y < userY + 20):
                    draw_list.remove((x , y))


    cv2.imshow('Apna_Hath_Jagannath' , image)
    cv2.waitKey(1)
    

