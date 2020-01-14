# -*- coding: utf-8 -*-
DESC = "fmu-2019-12-13"
INFO = {
  "CreateModel": {
    "params": [
      {
        "name": "LUTFile",
        "desc": "LUT文件。 用于试唇色。须为 512*512的PNG图片。"
      },
      {
        "name": "Description",
        "desc": "文件描述信息，可用于备注。"
      }
    ],
    "desc": "上传 LUT 格式文件注册唇色ID。最多允许上传1万张素材。"
  },
  "DeleteModel": {
    "params": [
      {
        "name": "ModelId",
        "desc": "素材ID。"
      }
    ],
    "desc": "删除已注册的唇色素材。"
  },
  "GetModelList": {
    "params": [
      {
        "name": "Offset",
        "desc": "起始序号，默认值为0。"
      },
      {
        "name": "Limit",
        "desc": "返回数量，默认值为10，最大值为100。"
      }
    ],
    "desc": "查询已注册的唇色素材。"
  },
  "TryLipstickPic": {
    "params": [
      {
        "name": "LipColorInfos",
        "desc": "唇色信息。 \n您可以输入最多3个 LipColorInfo 来实现给一张图中的最多3张人脸试唇色。"
      },
      {
        "name": "Image",
        "desc": "图片 base64 数据，base64 编码后大小不可超过6M。 \n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "Url",
        "desc": "图片的 Url ，对应图片 base64 编码后大小不可超过6M。 \n图片的 Url、Image必须提供一个，如果都提供，只使用 Url。 \n图片存储于腾讯云的 Url 可保障更高下载速度和稳定性，建议图片存储于腾讯云。 \n非腾讯云存储的Url速度和稳定性可能受一定影响。 \n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      }
    ],
    "desc": "对图片中的人脸嘴唇进行着色，最多支持同时对一张图中的3张人脸进行试唇色。\n\n您可以通过事先注册在腾讯云的唇色素材（LUT文件）改变图片中的人脸唇色，也可以输入RGBA模型数值。\n\n为了更好的效果，建议您使用事先注册在腾讯云的唇色素材（LUT文件）。\n\n>     \n- 公共参数中的签名方式请使用V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。"
  },
  "BeautifyPic": {
    "params": [
      {
        "name": "Image",
        "desc": "图片 base64 数据，base64 编码后大小不可超过5M。 \n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "Url",
        "desc": "图片的 Url 。对应图片 base64 编码后大小不可超过5M。 \nUrl、Image必须提供一个，如果都提供，只使用 Url。  \n图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。  \n非腾讯云存储的Url速度和稳定性可能受一定影响。 \n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "Whitening",
        "desc": "美白程度，取值范围[0,100]。0不美白，100代表最高程度。默认值30。"
      },
      {
        "name": "Smoothing",
        "desc": "磨皮程度，取值范围[0,100]。0不磨皮，100代表最高程度。默认值10。"
      },
      {
        "name": "FaceLifting",
        "desc": "瘦脸程度，取值范围[0,100]。0不瘦脸，100代表最高程度。默认值70。"
      },
      {
        "name": "EyeEnlarging",
        "desc": "大眼程度，取值范围[0,100]。0不大眼，100代表最高程度。默认值70。"
      }
    ],
    "desc": "输入人脸图片，输出美颜后的人脸图片。"
  }
}