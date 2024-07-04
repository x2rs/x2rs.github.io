# Python 创建 venv

在 Python 中创建虚拟环境，可以使用 `venv` 模块。

1. `cd` 要创建虚拟环境的目录。
2. 运行 `venv` 模块，创建虚拟环境 `.venv`。

```bash
python -m venv .venv
```

运行此命令后，目录下会出现 `.venv` 文件夹。

然后激活 `.venv` 环境，运行 `.venv/Scripts/` 下的激活脚本即可。

若终端开头出现 `(.venv)` ，则激活成功。
