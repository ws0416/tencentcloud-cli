**Example 1: 成功发送单条消息**



Input: 

```
tccli tdmq SendMessages --cli-unfold-argument  \
    --Topic persistent://tenant/namespace/topic \
    --Payload '"hello TDMQ"' \
    --StringToken xxxxxx
```

Output: 
```
{
    "Response": {
        "RequestId": "36713f94-d07d-4b96-babf-42d139276f23",
        "MessageId": "71:11:0:0",
        "ErrorMsg": ""
    }
}
```

