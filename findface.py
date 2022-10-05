import face_recognition
image =face_recognition.load_image_file('./group/avengers.jpg')
face_location=face_recognition.face_locations(image)
print(face_location)
print(f'there are {len(face_location)} people in this image')