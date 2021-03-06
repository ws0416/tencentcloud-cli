**Example 1: 查询指定任务流模板**

查询名为“我的任务流A”的任务流模板的详情

Input: 

```
tccli vod DescribeProcedureTemplates --cli-unfold-argument  \
    --Names 我的任务流A
```

Output: 
```
{
    "Response": {
        "TotalCount": 1,
        "ProcedureTemplateSet": [
            {
                "Name": "我的任务流A",
                "Type": "Custom",
                "AiContentReviewTask": null,
                "AiAnalysisTask": null,
                "AiRecognitionTask": null,
                "MiniProgramPublishTask": null
            }
        ],
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

**Example 2: 查询所有的任务流模板**

查询所有的任务流模板的详情，共查到3个任务流模板

Input: 

```
tccli vod DescribeProcedureTemplates --cli-unfold-argument ```

Output: 
```
{
    "Response": {
        "TotalCount": 3,
        "ProcedureTemplateSet": [
            {
                "Name": "我的任务流A",
                "Type": "Custom",
                "AiContentReviewTask": null,
                "AiAnalysisTask": null,
                "AiRecognitionTask": null,
                "MiniProgramPublishTask": null
            },
            {
                "Name": "我的任务流B",
                "Type": "Custom",
                "AiContentReviewTask": null,
                "AiAnalysisTask": null,
                "AiRecognitionTask": null,
                "MiniProgramPublishTask": null
            },
            {
                "Name": "我的任务流C",
                "Type": "Custom",
                "AiContentReviewTask": {
                    "Definition": 10
                },
                "AiAnalysisTask": null,
                "AiRecognitionTask": null,
                "MiniProgramPublishTask": null
            }
        ],
        "RequestId": "6ca31e3a-6b8e-4b4e-9256-fdc700064ef3"
    }
}
```

