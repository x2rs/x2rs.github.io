# Windows 10/11 禁用/启用笔记本自带键盘

## 禁用笔记本键盘

按 Win+R 快捷键打开运行窗口，输入cmd，然后按 Ctrl+Shift+Enter 组合键，以管理员身份运行cmd。

然后在cmd中输入以下命令，这将**禁用**笔记本键盘。

```cmd
sc config i8042prt start= disabled
```

重启电脑。

```cmd
shutdown -r -t 0
```

## 启用笔记本键盘

如果要重新启用笔记本键盘，需要将命令中的 `disabled` 替换为 `demand`。（或者 `auto`）

按 Win+R 快捷键打开运行窗口，输入cmd，然后按 Ctrl+Shift+Enter 组合键，以管理员身份运行cmd。

然后在cmd中输入以下命令，这将**启用**笔记本键盘。

```cmd
sc config i8042prt start= demand
```

重启电脑。

```cmd
shutdown -r -t 0
```