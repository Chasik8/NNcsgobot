import torch
from ultralytics import YOLO


def main():
    # print(torch.cuda.is_available())
    # model = YOLO("yolov8n.yaml")
    model = YOLO("D:\\Project\\Python\\Neroset_cs1\\runs\\detect\\yolov8n4\\weights\\best.pt")
    # model.val()
    model.to('cuda:0')
    # results = model.predict(
    #     data='D:\\Project\\Python\\Neroset_cs1\\cs1.yaml',
    #     source="ob2.mp4"
    # )
    # results=model.val(
    #     data='D:\\Project\\Python\\Neroset_cs1\\cs1.yaml',
    #     imgsz=640,
    #     batch=26,)
    # results = model.train(
    #     data='D:\\Project\\Python\\Neroset_cs1\\cs1.yaml',
    #     imgsz=640,
    #     epochs=400,
    #     batch=26,
    #     name='yolov8n'),
    # print(results)



    # # Load a model
    # model = YOLO("yolov8n.yaml")  # build a new model from scratch
    # # model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
    #
    # # Use the model
    # # model.cuda('cuda0')
    # model.train(data="coco128.yaml", epochs=3)  # train the model
    # metrics = model.val()  # evaluate model performance on the validation set
    # results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
    #
    # success = model.export(format="onnx")  # export the model to ONNX format


if __name__ == '__main__':
    main()
