**Example 1: Sample request**



Input: 

```
tccli mdp DescribeMediaPackageChannels --cli-unfold-argument  \
    --PageNum 1 \
    --PageSize 10
```

Output: 
```
{
    "Response": {
        "Infos": [
            {
                "Id": "AEABF123954",
                "Name": "channelName",
                "Protocol": "HLS",
                "Points": {
                    "Inputs": [
                        {
                            "Url": "http://mediapackage.${region}-1.srclivepush.myqcloud.com/v1/017182d5d3c4647d244530760443/017182d5d3c4647d244530760444",
                            "AuthInfo": {
                                "Username": "",
                                "Password": ""
                            }
                        },
                        {
                            "Url": "http://mediapackage.${region}-2.srclivepush.myqcloud.com/v1/017182d5d3c4647d244530760443/017182d5d3c4647d244530760445",
                            "AuthInfo": {
                                "Username": "",
                                "Password": ""
                            }
                        }
                    ],
                    "Endpoints": [
                        {
                            "Name": "",
                            "Url": "",
                            "AuthInfo": {
                                "WhiteIpList:": [
                                    "1.2.3.4/24",
                                    "19.76.68.1/1"
                                ],
                                "BlackIpList:": [
                                    "1.2.3.4/24",
                                    "19.76.68.1/1"
                                ],
                                "AuthKey": ""
                            }
                        }
                    ]
                }
            }
        ],
        "PageNum": 1,
        "PageSize": 10,
        "TotalNum": 1,
        "TotalPage": 1,
        "RequestId": "11-222-333"
    }
}
```

