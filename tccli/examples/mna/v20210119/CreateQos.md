**Example 1: 移动网络发起加速**



Input: 

```
tccli mna CreateQos --cli-unfold-argument  \
    --QosMenu T100K \
    --Duration 30 \
    --SrcAddressInfo.SrcIpv4 192.168.2.11 \
    --SrcAddressInfo.SrcPublicIpv4 10.22.33.14 \
    --DestAddressInfo.DestIp 128.22.36.40 \
    --DeviceInfo.OS 1 \
    --DeviceInfo.Vendor 2 \
    --DeviceInfo.DeviceId 357315094232545 \
    --DeviceInfo.Wireless 1 \
    --DeviceInfo.PhoneNum 12847584945 \
    --Capacity.CTCCToken 177cc9c4ab0-7b93546 \
    --Capacity.Province 广东省
```

Output: 
```
{
    "Response": {
        "SessionId": "ZWViYzAwNzJmNjRkNGExMDgyMjkzZTY0YzU0ZjZhNDY=-1-0",
        "RequestId": "3c140219-cfe9-470e-b241-907877d6fb03",
        "Duration": 1790
    }
}
```

