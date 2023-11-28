import matplotlib.pyplot as plt
import cv2


# 컬러 영상 출력
imgBGR = cv2.imread('cat.bmp')
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB) # BGR -> RGB, 그냥 코드 자체를 외워야함

plt.axis('off') # 출력 plt의 가로세로 눈금 좌표 생략
plt.imshow(imgRGB) # imgBGR 아님
plt.show()

# 그레이스케일 영상 출력
imgGray = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

plt.axis('off') 
plt.imshow(imgGray, cmap='gray')
plt.show()

# 두 개의 영상을 함께 출력
# (121)의미, (몇 개의 행으로 할꺼냐:1, 몇 개의 열로 나눌것이냐:2, 그 중 어느 열에다가 그림을 그릴것인가:1)
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')
plt.show()
