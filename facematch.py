import face_recognition
image_of_rdj=face_recognition.load_image_file('./known/Robert_Downey_Jr.jpg')
rdj_face_encoding=face_recognition.face_encodings(image_of_rdj)[0]

unknown_image=face_recognition.load_image_file('./group/rdj.jpg')
unknown_face_encoding=face_recognition.face_encodings(unknown_image)[0]

results=face_recognition.compare_faces([rdj_face_encoding],unknown_face_encoding)

if results[0]:
    print('rdj var')
else :
    print('rdj yok')    