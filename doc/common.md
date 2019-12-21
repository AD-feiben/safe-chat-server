POST 请求使用 JSON 传参，`Content-Type` 为 `application/json`

如有错误信息，则返回 `error` 字段

error 实例
```json
{
    "error": {
        "code": 10015,
        "message": "invalid validation code"
    }
}
```



## 1. 发送邮件验证码

#### POST: `/send-email`

```
[http|https]://host:port/v1/api/common/send-email
```

#### Params:
|参数|类型|必须|描述|
|---|---|---|---|
|email|string|Y|邮箱|

#### Response:
|参数|类型|必须|描述|
|---|---|---|---|
|code_token|string|Y|验证码 token，用于验证|
|timeout|int|Y|有效时间，单位（s）|

#### 实例：

```json
{
    "code_token": "U2L3wzNbQeuAXRmZHZMrlg",
    "timeout": 600
}
```