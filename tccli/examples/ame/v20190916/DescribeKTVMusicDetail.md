**Example 1: 查询 KTV 曲目详情**



Input: 

```
tccli ame DescribeKTVMusicDetail --cli-unfold-argument  \
    --MusicId ame-78d2xxx
```

Output: 
```
{
    "Response": {
        "PlayToken": "DUE3344xxxxxx",
        "KTVMusicBaseInfo": {
            "ComposerSet": [
                "周杰伦"
            ],
            "MusicId": "ame-78d2xxx",
            "SingerSet": [
                "周杰伦"
            ],
            "Name": "七里香",
            "LyricistSet": [
                "方文山"
            ],
            "TagSet": [
                "华语",
                "流行"
            ]
        },
        "RequestId": "xx"
    }
}
```

