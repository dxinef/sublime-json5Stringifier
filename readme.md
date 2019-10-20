# dxinefJson5Stringifier

基于JSON5，将类JSON字符串转换为标准JSON格式

![screen shoot](https://raw.githubusercontent.com/dxinef/sublime-json5Stringifier/master/screenshoot/1.gif)

## 安装

1. 直接将整个文件夹复制到sublime text3的插件安装目录下
2. 进入本插件目录，运行npm i

## 使用

1. 选中要转换的字符串，如未选中，默认为当前文件全文
2. ctrl + shift + p 调出命令菜单，选择JSON5 Stringify
3. 转换结果输出在新标签页中
4. 如希望设置快捷键调用，可在用户的快捷键设置中参考下方代码插入

```json
[
  {
    "keys": ["f5"],
    "command": "json5_stringifier"
  }
]

```

## 其他

该插件基于[JSON5](https://github.com/json5/json5)开发
