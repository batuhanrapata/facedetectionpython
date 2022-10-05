import face_recognition 
from PIL import Image, ImageDraw
import numpy

image_of_rdj=face_recognition.load_image_file('./known/Robert_Downey_Jr.jpg')
rdj_face_encoding=face_recognition.face_encodings(image_of_rdj)[0]
image_of_crs=face_recognition.load_image_file('./known/chrisevans.jpg')
crs_face_encoding=face_recognition.face_encodings(image_of_crs)[0]

#resimlerin kodlamasını içeren array
known_face_encodings=[rdj_face_encoding,crs_face_encoding]
known_face_names=["robert downey jr","chris evans"]

test_image=face_recognition.load_image_file('./group/avengers.jpg')

#resimdeki yüzleri bulma
face_locations=face_recognition.face_locations(test_image)
face_encodings=face_recognition.face_encodings(test_image,face_locations)







face_distances = face_recognition.face_distance(known_face_encodings, test_image)

pil_image=Image.fromarray(test_image)

draw=ImageDraw.Draw(pil_image)

for(top,right,bottom,left),face_encoding in zip(face_locations,face_encodings):
    matches=face_recognition.compare_faces(known_face_encodings,face_encoding)
    name="unknown person"
    if True in matches:
        first_match_index=matches.index(True)
        name=known_face_names[first_match_index]

    draw.rectangle(((left,top),(right,bottom)),outline=(0,0,0))
    text_width,text_height=draw.textsize(name)
    draw.rectangle(((left,bottom-text_height-10),(right,bottom)),fill=(0,0,0),outline=(0,0,0))  
    draw.text((left+6,bottom-text_height-5),name ,fill=(255,255,255))  
del draw

pil_image.show()
pil_image.save(f'{top}.jpg')
