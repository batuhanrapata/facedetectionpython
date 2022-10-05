import face_recognition
import numpy
known_face=face_recognition.load_image_file('./known/Robert_Downey_Jr.jpg')
known_face_enc=face_recognition.face_encodings(known_face)[0]


test_imagee=face_recognition.load_image_file('./known/chrisevans.jpg')
test_image_encoding=face_recognition.face_encodings(test_imagee)[0]

face_distances=face_recognition.face_distance(known_face_enc,test_image_encoding)[0]

for i,face_distance in enumerate(face_distances):
    print("test image look {:.2} from known #{}".format(face_distance,i))
    print("0.6 altinda {}".format(face_distance<0.6))
    print("0.5 altinda {}".format(face_distance<0.5))
    print()