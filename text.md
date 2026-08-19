$url = "https://nodejs.org/dist/v22.14.0/node-v22.14.0-x64.msi"
$out = "$env:USERPROFILE\Downloads\node-lts.msi"
Invoke-WebRequest -Uri $url -OutFile $out
Start-Process $out
