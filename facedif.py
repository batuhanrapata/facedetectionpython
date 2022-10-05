import face_recognition

known_image = face_recognition.load_image_file("deneme\hbendeneme.PNG")

face_encoding = face_recognition.face_encodings(known_image)[0]

known_encodings = [
    face_encoding]

image_to_test = face_recognition.load_image_file("deneme\8spidermin.PNG")
image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]

face_distances = face_recognition.face_distance(known_encodings, image_to_test_encoding)

for i, face_distance in enumerate(face_distances):
    print("fotografin orjinal fotografa olan uzakligi {:.2} #{}".format(face_distance, i))
    print("yuzde ",100-(face_distance*100)," benzerlik var")
    print()