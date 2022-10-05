from PIL import Image
import face_recognition

image_of_avengers=face_recognition.load_image_file('./group/avengers.jpg')
face_locations=face_recognition.face_locations(image_of_avengers)

for face_location in face_locations:
    top,right,bottom,left=face_location
    face_image=image_of_avengers[top:bottom,left:right]
    pil_image=Image.fromarray(face_image)
    #pil_image.show() resimleri ekrana veriyor
    pil_image.save(f'{top}.jpg')

