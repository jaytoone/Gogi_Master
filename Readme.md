## Gogi_Master

Mask-RCNN을 이용해 사진 데이터로부터 **육류 이미지를 분별**하고 사전에 학습된 CNN모델을 사용해 **육류의 익힘 정도 및 부위를 판별**한다. (부위 판별 서비스는 향후 개발 계획 중)



## Mask-RCNN for meat detection

https://github.com/jaytoone/Nuggi



## Check the doneness of meat with CNN

* image_preprocessing_with_labeling.ipynb : Mask-RCNN을 통해 전처리된 육류 이미지 데이터를 CNN모델에 학습시키기 위해 사전에 라벨링해주는 파일

* Make_model_Gogi.ipynb : 라벨링 된 데이터를 학습하여 익힘을 판단하는 모델을 만드는 파일



## Android

https://github.com/jaytoone/Android_GoMaWo



## Reference

* IMAGE PREPROCESSING : https://machinelearningmastery.com/how-to-manually-scale-image-pixel-data-for-deep-learning/
* VIA : http://www.robots.ox.ac.uk/~vgg/software/via/via-1.0.6.html
* 이미지 저장 : Imwrite('...jpg', frame)

|           속성            |         의미          |         비고          |
| :-----------------------: | :-------------------: | :-------------------: |
| cv2.CAP_PROP_FRAME_WIDTH  |     프레임의 너비     |           -           |
| cv2.CAP_PROP_FRAME_HEIGHT |     프레임의 높이     |           -           |
| cv2.CAP_PROP_FRAME_COUNT  |   프레임의 총 개수    |           -           |
|     cv2.CAP_PROP_FPS      |      프레임 속도      |           -           |
|    cv2.CAP_PROP_FOURCC    |       코덱 코드       |           -           |
|  cv2.CAP_PROP_BRIGHTNESS  |      이미지 밝기      |     카메라만 해당     |
|   cv2.CAP_PROP_CONTRAST   |      이미지 대비      |     카메라만 해당     |
|  cv2.CAP_PROP_SATURATION  |      이미지 채도      |     카메라만 해당     |
|     cv2.CAP_PROP_HUE      |      이미지 색상      |     카메라만 해당     |
|     cv2.CAP_PROP_GAIN     |      이미지 게인      |     카메라만 해당     |
|   cv2.CAP_PROP_EXPOSURE   |      이미지 노출      |     카메라만 해당     |
|   cv2.CAP_PROP_POS_MSEC   |   프레임 재생 시간    |        ms 반환        |
|  cv2.CAP_PROP_POS_FRAMES  |      현재 프레임      | 프레임의 총 개수 미만 |
|  CAP_PROP_POS_AVI_RATIO   | 비디오 파일 상대 위치 |   0 = 시작, 1 = 끝    |