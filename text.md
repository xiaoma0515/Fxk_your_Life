node --version
npm --version


npm install -g @anthropic-ai/claude-code



PS C:\Users\Administrator> node --version
>> npm --version
node : The term 'node' is not recognized as the name of a cmdlet, function, script file, or operable program. Check
the spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:1 char:1
+ node --version
+ ~~~~
    + CategoryInfo          : ObjectNotFound: (node:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException

npm : The term 'npm' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
spelling of the name, or if a path was included, verify that the path is correct and try again.
At line:2 char:1
+ npm --version
+ ~~~
    + CategoryInfo          : ObjectNotFound: (npm:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException



$url = "https://nodejs.org/dist/v22.14.0/node-v22.14.0-x64.msi"
$out = "$env:USERPROFILE\Downloads\node-lts.msi"
Invoke-WebRequest -Uri $url -OutFile $out
