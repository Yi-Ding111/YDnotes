# Bash



## bash commands



### Turn on/off error checking

```bash
set +e
```

用于关闭错误检查。在这个代码块中，如果有命令执行失败，脚本会继续执行，而不会中断.

Used to turn off error checking. If nay commands fails in this code block, the script will continue without interruption.

```bash
set -e
```

Turn on error checking.

```bash
function_name() {
		set +e
		kinds of commands
		set -e
}
```





## mkdir 



### -p

```bash
mkdir -p dir_name
```

-p 选项确保 dist 所需的任何父目录在不存在时也被创建。

The -p option ensures that any parent directories required for dist are also created if they don't exist.





## cp



### -r

Stand for `recursive`, enable the cp command to copy directories recursively.

```bash
cp -r /home/user/folder1 /home/user/folder2
```

会把folder里面所有的子目录和文件全部复制到folder2里面。

All subdirectories and files in folder will be copied to folder2.



