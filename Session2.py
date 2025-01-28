import cv2 


cap = cv2.VideoCapture(0)
faceCascade = cv2.CascadeClassifier('C:/Users/ramy/miniconda3/envs/myenv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml')


while True : 
    succes , image = cap.read()
    image = cv2.resize(image , (0,0) , None , 0.5 ,0.5)
    results = faceCascade.detectMultiScale(image , 1.5 , 3)
    print(len(results))
    if len(results) > 0 :
        x , y , w , h = results[0]
        x1 , y1 = x+w , y+h
        cv2.rectangle(image , (x,y) , (x1 , y1) , (0,255,0) , 3)
        cv2.imshow('my image' , image)
    if cv2.waitKey(1) == ord('q'):
        break 
cv2.destroyAllWindows()







#-------------------------------------------------------------------------------------------------------------------------
# import cv2 

# image = cv2.imread('/Users/ramy/Desktop/Ressources/ramy.jpg')
# resized_image = cv2.resize(image , (0,0) , None , 0.6 , 0.6 )
# hsv = cv2.cvtColor(resized_image , cv2.COLOR_BGR2HSV)


# cv2.rectangle(resized_image , (40,40) , (140,140) , ( 0 , 0 , 255) , 5  )
# cv2.circle(resized_image  , (200,500) ,70 ,(255 , 0 , 0) , -1       )
# cv2.putText(resized_image , 'Person' ,(40 , 30) , cv2.FONT_ITALIC , 1 ,( 0 , 0 , 255) , 3 )

# cv2.line(resized_image ,(100,100) , (200,200) , (0,255,0) , 7 )


# cv2.imshow('resized ' , resized_image)

# cv2.waitKey(0)
