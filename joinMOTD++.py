import requests
import json
import os
from utils.rtext import *


configPath = 'config/joinMOTD++.json'
# 以下内容请不要更改，需要更改配置文件请在加载一次后到configPath设定的配置文件路径进行修改。
# --------
defultConfig = '''
{
    "display-days": true,
    "one-text": true,
    "display-bungee-list": true,
    "motd": "%player%,欢迎回到服务器!",
    "one-text-api": "https://v1.hitokoto.cn/?encode=text",
    "bungee-list":{
        "测试1": "test1",
        "测试2": "test2"
    },
    "day-text": "今天是服务器开服的第%day%天。"
}'''
# --------


def get_config():  # 加载配置文件
    if not os.path.exists(configPath):  # 若文件不存在则写入默认值
        with open(configPath, 'w+', encoding='UTF-8') as f:
            f.write(defultConfig)
    with open('config/joinMOTD++.json', 'r', encoding='UTF-8') as f:
        config = json.load(f, encoding='UTF-8')
    return config


def format_text(player):  # 加载MOTD内容
    config = get_config()
    output = ['-'*40, config['motd'].replace('%player%', player), '']  # 分割线、主MOTD、换行
    if config['one-text']:  # 如果启用了一言则获取一言并加入输出列表
        output.append(requests.get(config['one-text-api']).text)
        output.append('')
    if config['display-days']:  # 如果启用了daycount则获取天数并加入输出列表
        from plugins.daycount import getday
        day_text = config['day-text'].replace('%day%', getday())
        output.append(day_text)
        output.append('')
    if config['display-bungee-list']:  # 如果启用了BUNGEE列表则获取BUNGEE列表并加入输出列表
        output.append('子服务器列表：')
        temp = config['bungee-list']
        bungee_list = []
        for i in temp:
            bungee_list.append(
                RText(f'[§6{i}§r] ', color=RColor.white).h(f'点击加入至§6{temp[i]}§r服务器').c(RAction.run_command, f'/server {temp[i]}')
            )
        output.append(RTextList(*bungee_list))
    output.append('-'*40)  # 分割线
    return output


def is_chinese(string):
    for char in string:
        if u'\u4e00' <= char <= u'\u9fff':
            return True
    return False


def on_player_joined(server, player):  # 玩家加入时显示MOTD
    try:
        if is_chinese(player):  # 检查玩家名是否有中文
            return
        elif player.startswith('bot_'):  # 检查玩家名是否以bot_开头
            return
        else:
            text = format_text(player)  # 获取MOTD
            for i in text:  # 输出
                if i == '':
                    server.tell(player, ' '*5)
                else:
                    server.tell(player, r' ' + i)
    except Exception as e:
        server.tell(player, 'MOTD++出现错误！麻烦让服务器管理者到控制台瞅一眼')
        print(e)


