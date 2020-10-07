#Flag for checking null values
$checkifexists = $null

$installdir = "c:\installer\"
$url = "https://www.7-zip.org/download.html"
$web_content = Invoke-WebRequest $url 

#Find Version and format into string
[string]$line = $web_content.ToString() -split "[`r`n]" | Select-String "Download"
$ver = [string]$line.Substring(198,5) 
$ver = $ver.replace(".","")


If (Test-Path -Path $installdir -PathType Container)
{ Write-Host "install directory exists" -ForegroundColor Yellow}
ELSE
{ New-Item -Path $installdir  -ItemType directory }

Write-Host "Checking for the latest version of 7-zip..." -ForegroundColor Yellow
# Download the installer
Write-Host "Newest Version of 32 and 64 bit is $ver" -ForegroundColor Yellow
$page = "https://www.7-zip.org/a/7z$ver-x64.msi"
$pagetwo = "https://www.7-zip.org/a/7z$ver.msi"

$destination = "$installdir\7-Zip.msi"
$destinationtwo = "$installdir\7-Zip32.msi"

if (Get-Command 'Invoke-Webrequest')
{
     Invoke-WebRequest $page -OutFile $destination
Invoke-WebRequest $pagetwo -OutFile $destinationtwo
 
}
else
{
    $WebClient = New-Object System.Net.WebClient
    $webclient.DownloadFile($page, $destination)
$webclient.DownloadFile($pagetwo, $destinationtwo)
}


$checkifexists = Get-ChildItem -Path C:\installer\* -Include *.msi
if ($checkifexists -eq $null)
{
Invoke-WebRequest $page -OutFile $destination 
Start-Sleep -s 2
Invoke-WebRequest $pagetwo -OutFile $destinationtwo
}

# Start the installation
Write-Host "Now installing Latest Version Please wait..." -ForegroundColor Yellow
msiexec.exe /i "$installdir\7-Zip.msi" /qb

#Waits two seconds before starting other installation
Start-Sleep -s 2
msiexec.exe /i "$installdir\7-Zip32.msi" /qb

Write-Host "7 more seconds..." -ForegroundColor Yellow
Start-Sleep -s 7
#Removes the installer after 7 seconds is up.
rm -Force $installdir\7*