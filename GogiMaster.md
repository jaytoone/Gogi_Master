## Idea

애매한 요리

크라우드 웍스 https://www.kdata.or.kr/busi/busi_01_03.html

로딩이 길게 (인공지능을 분석하는 시간으로 대체)

수익 모델 : 광고로는 한계가 있다. 

**고기 사장**을 대상으로 게이미피케이션 : **수익을 극대화시키는 방법**

<u>메뉴 서비스</u> 

**인건비를 줄이는 걸 목표로**



## Dataset

* 라벨링은 퍼센트를 결과로 나타내기 위해, 2개로 나눈다.
* 데이터셋 구성을 잘해야한다.
* 결국 고객이 요구하는 서비스는 익음의 기준이 애매하기 때문
  * 애매한 고기부터 잘익은 고기로만 데이터를 구성해준다면, 좀 더 첨예하게 잘 익은 고기를 분류할 수 있다.
* 화질 중요함



## Masking

1. Detect된 고기를 넣으면 
2. rect를 roi로 잡고 crop해서 warp시켜 수직/수평이 되도록 한다. 
3. **<u>데이터를 회전시키고 늘이는 과정에서 blur가 생긴다.</u>**



### 모델 정확도 올리는 방법 

* 고기 **결을 고려한** 이미지 cropping
* **좋은 해상도** 사용하기
* 고기 **데이터수** 늘리기
* 고기 **사이즈** 변경
* 고기 **이상치** 제거 : 색의 영역을 벗어난 고기 데이터를 제거한다.
  * 평균이 200? 이상 제거 
* **전처리된 이미지를 학습시킨다.**



## Application

1. **이미지 서버 업로드**
   * https://docs.aws.amazon.com/ko_kr/aws-mobile/latest/developerguide/mobile-hub-add-aws-mobile-user-data-storage.html
   * Server_Upload_None_Cognito : file 객체 수정해서 업로드해보기
   * uri -> path 변환 : https://crystalcube.co.kr/184
   * /storage/emulated/0/GoMaWo/1588149843652.jpg
2. **프리뷰 스탑 모션이 안돼네..**





Android 개발 강의 : [https://www.inflearn.com/course/%EC%95%88%EB%93%9C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%8A%A4%ED%8A%9C%EB%94%94%EC%98%A4-%EC%95%88%EB%93%9C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%95%B1-%EB%A7%8C%EB%93%A4%EA%B8%B0/lecture/5723](https://www.inflearn.com/course/안드로이드-스튜디오-안드로이드-앱-만들기/lecture/5723)

홍 드로이드 카메라 만들기 : https://www.youtube.com/watch?v=MAB8LEfRIG8

카메라 어플 만들기 : https://loveiskey.tistory.com/192

좀더 깔끔한 예제 : http://blog.naver.com/PostView.nhn?blogId=whdals0&logNo=221408855795&categoryNo=29&parentCategoryNo=0&viewDate=&currentPage=1&postListTopCurrentPage=1&from=search



## Reference

* IMAGE PREPROCESSING : https://machinelearningmastery.com/how-to-manually-scale-image-pixel-data-for-deep-learning/
* VIA : http://www.robots.ox.ac.uk/~vgg/software/via/via-1.0.6.html
* 이미지 저장 : Imwrite('...jpg', frame)
* 일지 공유 폴더 : https://drive.google.com/file/d/1jR_a8M0A8ZX7jyTKPpNMCLbNlTcQ0IIm/view?usp=sharing
* Zoom : https://j.mp/3dXsGVH  
* 카메라 썸네일 : https://blog.naver.com/PostView.nhn?blogId=luku756&logNo=221127941797&parentCategoryNo=&categoryNo=31&viewDate=&isShowPopularPosts=true&from=search
* 완성도 있는 카메라 프리뷰 코드 : https://webnautes.tistory.com/822
* CAMERA_EASY : https://one-delay.tistory.com/40
* CAMERA2 : https://webnautes.tistory.com/822
* camera_preview : http://android-er.blogspot.com/2010/12/camera-preview-on-surfaceview.html

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