# Driving-video-semantic-segmentation

下载pretrained models: [Dropbox](https://www.dropbox.com/sh/w3z9z8lqpi8b2w7/AAB0vkl4F5vy6HdIhmRCTKHSa?dl=0), [Tencent Weiyun](https://share.weiyun.com/qqx78Pv5)
将下载的预训练模型DeepLabV3Plus-MobileNet放入chekpoints中


测试单张图片:
```bash
python predict.py --input 图片地址  --dataset cityscapes --model deeplabv3plus_mobilenet --ckpt checkpoints/best_deeplabv3plus_mobilenet_cityscapes_os16.pth --save_val_results_to test_results
```

测试文件夹中的所有图片:
```bash
python predict.py --input 文件夹地址  --dataset cityscapes --model deeplabv3plus_mobilenet --ckpt checkpoints/best_deeplabv3plus_mobilenet_cityscapes_os16.pth --save_val_results_to test_results
```


Github 代码链接：https://github.com/ivorytan/Driving-video-semantic-segmentation
视频下载网盘链接：https://pan.baidu.com/s/1R1UzxpSvOi1tihW3hY_O6g 提取码：u8qn
