## Idea

애매한 요리

크라우드 웍스 https://www.kdata.or.kr/busi/busi_01_03.html

로딩이 길게 (인공지능을 분석하는 시간으로 대체)

수익 모델 : 광고로는 한계가 있다. 

**고기 사장**을 대상으로 게이미피케이션 : **수익을 극대화시키는 방법**

<u>메뉴 서비스</u> 

**인건비를 줄이는 걸 목표로**

Abmob app id : ca-app-pub-8407073558274950~6869020597

ad unit id : ca-app-pub-8407073558274950/2013523009



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
   * **퍼미션까지 있는 것 : https://www.simplifiedcoding.net/android-upload-image-to-server/**
     * **이게 잘됀다.**
   * /storage/emulated/0/GoMaWo/1588149843652.jpg
   * Server Callback (response) : https://github.com/gotev/android-upload-service/issues/104
2. 앱 광고 달기 : [https://deumdroid.tistory.com/entry/%EC%95%88%EB%93%9C%EB%A1%9C%EC%9D%B4%EB%93%9C-%EC%8A%A4%ED%8A%9C%EB%94%94%EC%98%A4-Google-AdMob-%EB%B0%B0%EB%84%88-%EA%B4%91%EA%B3%A0-%EB%84%A3%EA%B8%B0-%EB%AA%A8%EB%B0%94%EC%9D%BC-%EA%B4%91%EA%B3%A0](https://deumdroid.tistory.com/entry/안드로이드-스튜디오-Google-AdMob-배너-광고-넣기-모바일-광고)
   
   * **<u>종료 화면에 광고 넣기</u>**
3. **광고 배너 크기 키우기 (프리뷰 화면이 너무 내려가있다.)**
   * https://tech.yandex.com/mobile-ads/doc/android/quick-start/banner-docpage/
     * 300 x 250
4. **The application may be doing too much work on its main thread.**

   * https://okky.kr/article/469713
5. AsyncTask : https://youngest-programming.tistory.com/11
6. **촬영 뷰 상하로 해상도**
   * 가로 세로 비율 조정 (<u>포커싱은 되는데 화면이 축소되는 경우</u>)
   * https://gist.github.com/chittaranjan-khuntia/f9177d1698b6a80ff5b2ef2fdeaf0ef0
   * https://stackoverflow.com/questions/17804309/android-camera-preview-wrong-aspect-ratio
7. 카메라 focusing
   1. SurfaceView Auto Focusing : https://es1015.tistory.com/167 
   2. view size를 조정해보기
   3. Auto Focus 구현 : https://webnautes.tistory.com/822
8. **예측값 출력**
9. **앱디자인**

   * 버튼
   * 뷰
10. 배포 : https://imweb.me/faq?mode=view&category=29&category2=55&idx=210

   * https://here4you.tistory.com/198?category=787559
   * https://layers7.tistory.com/36?category=723289
   * app bundle 		

   * 처리방침 : https://layers7.tistory.com/39



## TODO

`+` **Android 측**

3. **쓰레드 관리**

4. **서버 로딩 화면 구현**

   * 영상 광고
   * **버퍼링 화면 : dialog https://mixup.tistory.com/36**

5. **배포**

   * app bundle 생성 : https://eso0609.tistory.com/68

   

**`+` Server 측**

1. 예측값 반환 속도 개선
   * extract rectangle 왜 오래걸리나



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