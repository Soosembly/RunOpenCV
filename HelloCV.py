import sys
import cv2

print('Hello, OpenCV', cv2.__version__)

# cv2.imread(filename, flags=None), flags의 기본값이 None이라기 보다는.. 기본값은 IMREAD_COLOR임
# flags 3가지 옵션(IMREAD_COLOR, IMREAD_GRAYSCALE, IMREAD_UNCHANGED)
# img = cv2.imread('cat.bmp') <- 2번째 인자 컬러로 명시안해도 기본값으로 출력됨
img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE) 


# 연산이 제대로 되었는지 항상 확인하는 코드를 추가해주는 게 좋다.
if img is None:
    print('Image load falied!')
    sys.exit()

# cv2.imwrite(filename, img, params=None) # 대부분도 paramas 빼도 기본값으로 진행됨
cv2.imwrite('cat_gray.png', img)

# 새 창 띄우기
# cv2.namedWindow(winname, flags=None)
# 창 크기를 영상 크기에 맞게 변경 cv2.WINDOW_AUTOSIZE(기본값임)
# 영상 크기를 창 크기에 맞게 지정 cv2.WINDOW_NORMAL(마우스로 크기 변경시)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)

# 창 크기 변경
#cv2.resizeWindow(winname, width, height) <- WINDOW_NORMAL 함수를 써야 이 함수도 사용 가능

# 영상 출력하기(winname, mat), mat: 출력할 영상 데이터(numpy.ndarray), 데이터 타입은 uint8로 하는 게 좋다.
cv2.imshow('image', img) 
cv2.waitKey() # 키보드 입력을 기다리는 역할과 동시에 영상이 보여질 수 있게끔 작업을 함 
# cv2.waitKey(3000) 3초 이후 자동으로 닫혀짐

while True:
    if cv2.waitKey() == 27: # esc키의 아스키 코드(ASCII)/ 13(ENTER) / 9(TAB)
        break

# while True:
#     if cv2.waitKey() == ord('q'): # ord()사용해서 특정 키보드를 누르면 닫치게 할 수 있음
#         break


 
# cv2.destoryWindow(winname) 지정한 창 하나만 닫음
# cv2.destroyAllWindows() 열려있는 모든 창 닫기, 키보드 아무키나 누르면 됨, 일반적인 경우 프로그램 종료시 운영 체제에 의해 열려있는 모든 창이 자동으로 닫힘
cv2.destroyWindow('image')