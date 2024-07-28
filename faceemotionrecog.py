# -*- coding: utf-8 -*-
"""FaceEmotionRecog.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1a1xmGnpc4Aw_Kgu4g7VmRkMzlkvKfACq
"""

!pip install deepface &> /dev/null
print ("Deep Face installed sucessfully!!")

from deepface import DeepFace
##Load and display input image
import cv2
import matplotlib.pyplot as plt
img1=cv2.imread("/content/testingImage.jpeg")
plt.imshow(img1)
plt.show()

plt.imshow(img1[:, :, ::-1 ])
plt.show()

obj=DeepFace.analyze(img1, actions = ['age', 'gender', 'race', 'emotion'])
print(obj)

print(type(obj))

final_obj={}
for i in obj:
    final_obj.update(i)
print (final_obj)
print(type(final_obj))

print(range(len(final_obj)))
print(final_obj['age'])
print(final_obj['dominant_gender'])
print(final_obj['dominant_race'])
print(final_obj['dominant_emotion'])

print("Your age is",final_obj['age'],"and you are",final_obj['dominant_race'],
      "and current emotion is",final_obj['dominant_emotion'],
     "and your gender capture is", final_obj['dominant_gender'])