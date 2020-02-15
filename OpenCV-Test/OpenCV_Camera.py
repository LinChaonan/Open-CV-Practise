import cv2
# 创建一个 VideoCapture 对象，参数是设备的索引即摄像机的编号或者 Video 的文件名
# 这里的 0 是指第一台摄像机，以此类推
cap = cv2.VideoCapture(0)
while (True):
    # while cap.isOpened():
    # 一帧一帧的捕获
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 显示
    cv2.imshow("frame", gray)  # 窗口名为 frame
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()  # 关闭视频文件或设备
cv2.destroyAllWindows()