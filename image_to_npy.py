import os
import numpy as np
import cv2
import matplotlib.pyplot as plt


cooked_path = './cooked/'
uncooked_path = './uncooked/'
raw_path = './raw'
cooked_list = os.listdir(cooked_path)
uncooked_list = os.listdir(uncooked_path)
raw_list = os.listdir(raw_path)
# print(cooked_list)
# quit()

gogi_to_np = list()
y_label = list()

for image_name in cooked_list:
    img = cv2.imread(cooked_path + image_name)
    img = cv2.resize(img, (80, 300))
    # plt.imshow(img)
    # plt.show()
    pixel = np.array(img)
    rgb = cv2.cvtColor(pixel, cv2.COLOR_RGBA2RGB)
    print(rgb.shape)
    gogi_to_np.append(rgb)
    y_label.append(1)

# for image_name in uncooked_list:
#     img = cv2.imread(uncooked_path + image_name)
#     img = cv2.resize(img, (80, 300))
#     # plt.imshow(img)
#     # plt.show()
#     pixel = np.array(img)
#     rgb = cv2.cvtColor(pixel, cv2.COLOR_RGBA2RGB)
#     print(rgb.shape)
#     gogi_to_np.append(rgb)
#     y_label.append(0)

for image_name in uncooked_list:
    img = cv2.imread(uncooked_path + image_name)
    img = cv2.resize(img, (80, 300))
    # plt.imshow(img)
    # plt.show()
    pixel = np.array(img)
    rgb = cv2.cvtColor(pixel, cv2.COLOR_RGBA2RGB)
    print(rgb.shape)
    gogi_to_np.append(rgb)
    y_label.append(0)

print(y_label)

np.save('gogi_to_np', np.array(gogi_to_np))
np.save('y_label', np.array(y_label))