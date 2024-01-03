import cv2

#doc anh mau
image = cv2.imread("HaDo.jpg")
#doc anh xam
#image_gray = cv2.imread("ngua.jpg",cv2.IMREAD_GRAYSCALE)
#show anh
cv2.imshow("Anh mau",image)
#pause man hinh
cv2.waitKey()

image_rs = cv2.resize(image,dsize=None,fx=0.5,fy=0.5)
#cv2.imshow("size moi",image_rs)
#cv2.waitKey()

image_gray = cv2.cvtColor(image_rs, cv2.COLOR_RGB2GRAY )
cv2.imshow("anh BGR",image_gray)
cv2.waitKey()

#ap thresh
ret, thresh_binary = cv2.threshold(image_gray,80,255,cv2.THRESH_BINARY)
cv2.imshow("anh thresh", thresh_binary)
cv2.waitKey()

'''
cv2.imwrite('ngua2BGR.jpg',image_gray)
image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2XYZ )
cv2.imshow("anh XYZ",image_gray)
cv2.waitKey()
cv2.imwrite('ngua2XYZ.jpg',image_gray)

#change size
#image_rs = cv2.resize(image,dsize=(200,200))
image_rs = cv2.resize(image,dsize=None,fx=0.5,fy=0.5)
cv2.imshow("size moi",image_rs)
cv2.waitKey()
'''
#close cua so
cv2.destroyAllWindows()
'''
camera_id = 'testVideo.mp4'
#camera_id = 0
#open camera
cap = cv2.VideoCapture(camera_id)
#doc anh tu camera
while True:
    #doc anh
    ret, frame = cap.read()
    #hien anh
    cv2.imshow("cam",frame)
    #kiem tra neu bam Q thi thoat
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#giai phong camera
cap.release()
cv2.destroyAllWindows()

#Save anh
image = cv2.imread("HaDo.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imwrite("sample_gray.jpg",image)
'''