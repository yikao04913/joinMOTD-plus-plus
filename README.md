# joinMOTD++  
一个MCDR的MOTD插件。在玩家加入服务器时显示。  

---

### 前置安装
**Windows**: `pip install requests` 
**Linux**: `pip3 install requests` 

### 插件效果  
![截图](https://i.loli.net/2020/07/07/ebdyGoVu5Tc2tsD.png)  
 
### 配置文件  
插件第一次被加载时会生成**joinMOTD++.json**。该文件内容如下：  
```json
{
    "display-days": true,
    "one-text": true,
    "display-bungee-list": true,
    "motd": "%player%,欢迎回到服务器!",
    "one-text-api": "https://v1.hitokoto.cn/?encode=text",
    "bungee-list":{
        "创造服": "creative",
        "生存服": "survival"
    },
    "day-text": "今天是服务器开服的第%day%天。"
}
```

### 配置项
`motd`：MOTD欢迎语内容。 **%player%** 代表玩家ID。

`display-days`：显示开服天数。需要[daycount](https://github.com/TISUnion/daycount)插件作为前置。  
`day-text`：开服天数的显示格式。 **%day%** 代表天数。  

`one-text`：显示一言。  
`one-text-api`：一言API接口。如需更换，请确保API返回值为纯文本。  

`display-bungee-list`：显示BC服务器列表。点击可以加入对应服务器。  
`bungee-list`：BC服务器列表。  
