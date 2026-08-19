PS C:\Users\Administrator> $py = "C:\Users\Administrator\AppData\Local\Programs\Python\Python312" $cur = [Environment]::GetEnvironmentVariable("Path","User") [Environment]::SetEnvironmentVariable("Path", "$py;$py\Scripts;$cur", "User") $env:Path = "$py;$py\Scripts;$env:Path" # 当前会话立即生效
>>
>> python -c "import struct, sys; print(struct.calcsize('P')*8, sys.version)"
At line:1 char:72
+ ... s\Administrator\AppData\Local\Programs\Python\Python312" $cur = [Envi ...
+                                                              ~~~~
Unexpected token '$cur' in expression or statement.
At line:1 char:132
+ ... Variable("Path","User") [Environment]::SetEnvironmentVariable("Path", ...
+                             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unexpected token '[Environment]::SetEnvironmentVariable' in expression or statement.
At line:1 char:210
+ ... entVariable("Path", "$py;$py\Scripts;$cur", "User") $env:Path = "$py; ...
+                                                         ~~~~~~~~~
Unexpected token '$env:Path' in expression or statement.
    + CategoryInfo          : ParserError: (:) [], ParentContainsErrorRecordException
    + FullyQualifiedErrorId : UnexpectedToken
