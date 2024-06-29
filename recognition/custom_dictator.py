




from threading import Thread
import face_recognition
import numpy as np
import cv2
import os
from attendance_system_facial_recognition.settings import BASE_DIR

face_cascade = cv2.CascadeClassifier(os.path.join(BASE_DIR,'static','face.xml'))
def fun(image_array):
    
    # define a video capture object
    vid = cv2.VideoCapture(0)
    names = []
    while(True):
       
        condition, frame = vid.read()
        if condition:
            position = {'x':0,"y":0}
            
            frame2 = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

            faces = face_cascade.detectMultiScale(frame2, 1.1, 4)

            
            
            if faces != ():
                # print(faces)
                for (x, y, w, h) in faces:
                    position['x'] = x                       #GETING FACE POSITION
                    position['y'] = y
                    
                    cropping_face_from_fame2 =  frame2[y:y + h, x:x + w]
                    if face_recognition.face_locations(cropping_face_from_fame2):
                        currentEncodedImage = face_recognition.face_encodings(cropping_face_from_fame2)         #CROPPING FACE SECTION AND ENCODE
                        
                        for student_data in image_array:
                            cheack = face_recognition.compare_faces(student_data["encode_img"],currentEncodedImage[0])          #MATCHING FACES
                            # print(currentEncodedImage[0])
                            # print(f"condition {cheack}")
                            if cheack[0]:
                                cv2.putText(frame, student_data['name'] , (position['x'], position['y']), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255,255,255),1)
                                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)                 #SETING KOWN FACE TO COLOR blue(text weight)
                                
                            else:
                                cv2.putText(frame, "Unknown" , (position['x'], position['y']), cv2.FONT_HERSHEY_DUPLEX, 0.8, (0,0,255),1)
                                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)                #SETING UNKOWN FACE TO COLOR RED
                                
                            if cheack[0] and  student_data['id'] not in  names:
                                names.append(student_data['id'])            #ADDING STUDENT TO ARRAY
                            
                    

                        
                
            cv2.imshow('frame', frame)
            key = cv2.waitKey(1)
            if key == 113:
                    vid.release()
                    cv2.destroyAllWindows()
                    return names            #RETURNING MULTIPLE STUDENT


import concurrent.futures
def FaceDetector(obj):
     
    encodec_image_array = []
    for student in obj:
        
        imagePath = os.path.join(BASE_DIR,"static\images",str(student.profile_pic))
        encoded_image = face_recognition.face_encodings(cv2.cvtColor(cv2.imread(imagePath),cv2.COLOR_BGR2RGB))
        if encoded_image:
            encodec_image_array.append({
                "id":student.registration_id,
                "encode_img":encoded_image,
                "name":student.full_name()
            })
    
    

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(fun,encodec_image_array)
        return future.result()
            
