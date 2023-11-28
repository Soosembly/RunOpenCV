import os
import sys
import glob
import cv2


# 이미지 파일을 모두 img_files 리스트에 추가

# 특정 폴더에 있는 이미지 파일(*jpg)목록 읽기
# os.listdir() 
# file_list = os.listdir('.\\images')
# img_files = [os.path.join('.\\images', file) for file in file_list if file.endswith('.jpg')]

# glob.glob() 사용 방법
# 특정 패턴의 문자이름 또는 파일이름을 불러 올 수 있음
img_files = glob.glob('.\\images\\*.jpg') # .\\:현재 폴더 밑에, imges\\ 밑에, .jpg로 끝나는 파일을 모두 불러와

for f in img_files:
    print(f)


if not img_files:
    print("There are no jpg files in 'images' folder")
    sys.exit()

# 전체 화면으로 'image' 창 생성
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

# 무한 루프
cnt = len(img_files)
idx = 0

while True:
    img = cv2.imread(img_files[idx]) # idx=0

    if img is None:
        print('Image load failed!')
        break

    cv2.imshow('image', img)
    if cv2.waitKey(1000) >= 0: 
        break

    idx += 1
    if idx >= cnt:
        idx = 0

cv2.destroyAllWindows()
