$py = "C:\Users\Administrator\AppData\Local\Programs\Python\Python312"
$cur = [Environment]::GetEnvironmentVariable("Path","User")
[Environment]::SetEnvironmentVariable("Path", "$py;$py\Scripts;$cur", "User")
$env:Path = "$py;$py\Scripts;$env:Path"     # 当前会话立即生效

python -c "import struct, sys; print(struct.calcsize('P')*8, sys.version)"
