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

