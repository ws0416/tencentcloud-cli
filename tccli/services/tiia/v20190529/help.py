# -*- coding: utf-8 -*-
DESC = "tiia-2019-05-29"
INFO = {
  "RecognizeCar": {
    "params": [
      {
        "name": "ImageUrl",
        "desc": "图片URL地址。 \n图片限制： \n• 图片格式：PNG、JPG、JPEG。 \n• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 \n建议：\n• 图片像素：大于50*50像素，否则影响识别效果； \n• 长宽比：长边：短边<5； \n接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。"
      },
      {
        "name": "ImageBase64",
        "desc": "图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。\n\n图片URL地址。支持的图片格式：PNG、JPG、JPEG、BMP，暂不支持GIF格式。支持的图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。"
      }
    ],
    "desc": "腾讯云车辆属性识别可对汽车车身及车辆属性进行检测与识别，目前支持11种车身颜色、20多种车型、300多种品牌、4000多种车系+年款的识别，同时支持对车标的位置进行检测。\n>     \n- 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。"
  },
  "DetectLabel": {
    "params": [
      {
        "name": "ImageUrl",
        "desc": "图片URL地址。 \n图片限制： \n• 图片格式：PNG、JPG、JPEG。 \n• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 \n建议：\n• 图片像素：大于50*50像素，否则影响识别效果； \n• 长宽比：长边：短边<5； \n接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。"
      },
      {
        "name": "ImageBase64",
        "desc": "图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。"
      },
      {
        "name": "Scenes",
        "desc": "本次调用支持的识别场景，可选值如下：\nWEB，针对网络图片优化;\nCAMERA，针对手机摄像头拍摄图片优化;\nALBUM，针对手机相册、网盘产品优化;\n如果不传此参数，则默认为WEB。\n\n支持多场景（Scenes）一起检测。例如，使用 Scenes=[\"WEB\", \"CAMERA\"]，即对一张图片使用两个模型同时检测，输出两套识别结果。"
      }
    ],
    "desc": "图像标签利用深度学习技术、海量训练数据，可以对图片进行智能分类、物体识别等。\n\n目前支持8个大类、六十多个子类、数千个标签。涵盖各种日常场景、动植物、物品、美食、卡证等。具体分类请见图像分析常见问题功能和限制部分（https://cloud.tencent.com/document/product/865/17629 ）\n\n图像标签提供三个版本供选择：\n\n• 摄像头版：针对搜索、手机摄像头照片进行优化，涵盖大量卡证、日常物品、二维码条形码。\n\n• 相册版：针对手机相册、网盘进行优化，去除相册和网盘中不常见的标签，针对相册常见图片类型（人像、日常活动、日常物品等）识别效果更好。\n\n• 网络版：针对网络图片进行优化，涵盖标签更多，满足长尾识别需求。\n\n每个产品的图像类型都有独特性，建议在接入初期，对三个版本进行对比评估后选择合适的版本使用。\n\n为了方便使用、减少图片传输次数，图像标签包装成多合一接口，实际上是多个服务。\n\n图像标签按照服务的实际使用数量进行收费。例如一张图片同时调用相册版、摄像头版两个服务，那么此次调用按照两次计费。\n>     \n- 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。"
  },
  "AssessQuality": {
    "params": [
      {
        "name": "ImageUrl",
        "desc": "图片URL地址。 \n图片限制： \n• 图片格式：PNG、JPG、JPEG。 \n• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 \n建议：\n• 图片像素：大于50*50像素，否则影响识别效果； \n• 长宽比：长边：短边<5； \n接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。"
      },
      {
        "name": "ImageBase64",
        "desc": "图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。"
      }
    ],
    "desc": "评估输入图片在视觉上的质量，从多个方面评估，并同时给出综合的、客观的清晰度评分，和主观的美观度评分。\n>     \n- 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。"
  },
  "DetectDisgust": {
    "params": [
      {
        "name": "ImageUrl",
        "desc": "图片URL地址。 \n图片限制： \n• 图片格式：PNG、JPG、JPEG。 \n• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 \n建议：\n• 图片像素：大于50*50像素，否则影响识别效果； \n• 长宽比：长边：短边<5； \n接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。"
      },
      {
        "name": "ImageBase64",
        "desc": "图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。"
      }
    ],
    "desc": "输入一张图片，返回AI针对一张图片是否是恶心的一系列判断值。\n\n通过恶心图片识别, 可以判断一张图片是否令人恶心, 同时给出它属于的潜在类别, 让您能够过滤掉使人不愉快的图片。\n>     \n- 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。"
  },
  "CropImage": {
    "params": [
      {
        "name": "Width",
        "desc": "需要裁剪区域的宽度，与Height共同组成所需裁剪的图片宽高比例；\n输入数字请大于0、小于图片宽度的像素值；"
      },
      {
        "name": "Height",
        "desc": "需要裁剪区域的高度，与Width共同组成所需裁剪的图片宽高比例；\n输入数字请请大于0、小于图片高度的像素值；\n宽高比例（Width : Height）会简化为最简分数，即如果Width输入10、Height输入20，会简化为1：2。\nWidth : Height建议取值在[1, 2.5]之间，超过这个范围可能会影响效果；"
      },
      {
        "name": "ImageUrl",
        "desc": "图片URL地址。 \n图片限制： \n• 图片格式：PNG、JPG、JPEG。 \n• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 \n建议：\n• 图片像素：大于50*50像素，否则影响识别效果； \n• 长宽比：长边：短边<5； \n接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。"
      },
      {
        "name": "ImageBase64",
        "desc": "图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。"
      }
    ],
    "desc": "根据输入的裁剪比例，智能判断一张图片的最佳裁剪区域，确保原图的主体区域不受影响。\n\n可以自动裁剪图片，适应不同平台、设备的展示要求，避免简单拉伸带来的变形。\n>     \n- 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。"
  },
  "DetectMisbehavior": {
    "params": [
      {
        "name": "ImageUrl",
        "desc": "图片URL地址。 \n图片限制： \n• 图片格式：PNG、JPG、JPEG。 \n• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 \n建议：\n• 图片像素：大于50*50像素，否则影响识别效果； \n• 长宽比：长边：短边<5； \n接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。"
      },
      {
        "name": "ImageBase64",
        "desc": "图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。"
      }
    ],
    "desc": "可以识别输入的图片中是否包含不良行为，例如打架斗殴、赌博、抽烟等，可以应用于广告图、直播截图、短视频截图等审核，减少不良行为对平台内容质量的影响，维护健康向上的互联网环境。\n>     \n- 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。"
  },
  "DetectProduct": {
    "params": [
      {
        "name": "ImageUrl",
        "desc": "图片URL地址。 \n图片限制： \n• 图片格式：PNG、JPG、JPEG。 \n• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 \n建议：\n• 图片像素：大于50*50像素，否则影响识别效果； \n• 长宽比：长边：短边<5； \n接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。"
      },
      {
        "name": "ImageBase64",
        "desc": "图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。"
      }
    ],
    "desc": "本接口支持识别图片中包含的商品，能够输出商品的品类名称、类别，还可以输出商品在图片中的位置。支持一张图片多个商品的识别。\n>     \n- 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。"
  },
  "ImageModeration": {
    "params": [
      {
        "name": "Scenes",
        "desc": "本次调用支持的识别场景，可选值如下：\n1. PORN，即色情识别\n2. TERRORISM，即暴恐识别\n3. POLITICS，即政治敏感识别\n4. TEXT, 即图像文本识别\n\n支持多场景（Scenes）一起检测。例如，使用 Scenes=[\"PORN\", \"TERRORISM\"]，即对一张图片同时进行色情识别和暴恐识别。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片URL地址。 \n图片限制： \n • 图片格式：PNG、JPG、JPEG。 \n • 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 TEXT场景要求图片经Base64编码后不超过3M。\n • 图片像素：大于50*50像素，否则影响识别效果； \n • 长宽比：长边：短边<5； \n接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。"
      },
      {
        "name": "Config",
        "desc": "预留字段，后期用于展示更多识别信息。"
      },
      {
        "name": "Extra",
        "desc": "透传字段，透传简单信息。"
      },
      {
        "name": "ImageBase64",
        "desc": "图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。"
      }
    ],
    "desc": "图像审核包含鉴黄、政治敏感识别、暴恐识别、图文审核等服务。\n\n• 鉴黄：识别图片中是否存在涉黄内容，将图片分为正常、性感、色情三类，并输出分类的置信度。\n\n• 政治敏感识别：识别图片中是否存在政治人物、政治恶搞、著名政治事件照片等内容。\n\n• 暴恐识别：识别图片中的暴力恐怖元素，例如武器、管制刀具、血腥、恐怖主义等。\n\n• 图文审核：结合OCR、NLP和二维码识别算法，分析图片中的文字是否违规，或是否存在二维码等营销内容，并输出违规内容的类别（涉黄、涉政、谩骂、广告营销、暴恐等）。\n\n为了方便使用、减少图片传输次数，图像审核包装成多合一接口，实际上是多个服务。\n\n图像审核根据服务的调用次数收费。例如一张图片同时调用鉴黄、图文审核两个服务，那么此次调用按照两次计费。\n>     \n- 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。"
  },
  "EnhanceImage": {
    "params": [
      {
        "name": "ImageUrl",
        "desc": "图片URL地址。 \n图片限制： \n• 图片格式：PNG、JPG、JPEG。 \n• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 \n建议：\n• 图片像素：大于50*50像素，否则影响识别效果； \n• 长宽比：长边：短边<5； \n接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。"
      },
      {
        "name": "ImageBase64",
        "desc": "支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段"
      }
    ],
    "desc": "传入一张图片，输出清晰度提升后的图片。\n\n可以消除图片有损压缩导致的噪声，和使用滤镜、拍摄失焦导致的模糊。让图片的边缘和细节更加清晰自然。\n>     \n- 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。"
  },
  "DetectCelebrity": {
    "params": [
      {
        "name": "ImageUrl",
        "desc": "图片URL地址。 \n图片限制： \n• 图片格式：PNG、JPG、JPEG。 \n• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 \n建议：\n• 图片像素：大于50*50像素，否则影响识别效果； \n• 长宽比：长边：短边<5； \n接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。"
      },
      {
        "name": "ImageBase64",
        "desc": "图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。"
      }
    ],
    "desc": "传入一张图片，可以识别图片中包含的人物是否为公众人物，如果是，输出人物的姓名、基本信息、脸部坐标。\n\n支持识别一张图片中存在的多个人脸，针对每个人脸，会给出与之最相似的公众人物。\n>     \n- 公共参数中的签名方式必须指定为V3版本，即配置SignatureMethod参数为TC3-HMAC-SHA256。"
  }
}