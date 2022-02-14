# Copyright 2021-2022 nunopenim @github
# Copyright 2021-2022 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License


if ( ( ( Test-Path -Path ".\userbot\__init__.py" -PathType leaf ) -and
       ( Test-Path -Path ".\userbot\__main__.py" -PathType leaf ) ) -or
     ( ( Test-Path -Path ".\HyperUBot\*" ) -and
       ( Test-Path -Path ".\HyperUBot\userbot\__init__.py" -PathType leaf ) -and
       ( Test-Path -Path ".\HyperUBot\userbot\__main__.py" -PathType leaf ) ) ) {
    Write-Host -ForegroundColor Green "HyperUBot is installed already"
    exit 0
}

$ProgressPreference = "SilentlyContinue"
$win_info = Get-ComputerInfo | select WindowsProductName, OsVersion, WindowsVersion
$ProgressPreference = "Continue"

# Generated with ASCII Art Generator: http://patorjk.com/software/taag/
Write-Output " _   _                       _   _ ____        _   "
Write-Output "| | | |_   _ _ __   ___ _ __| | | | __ )  ___ | |_ "
Write-Output "| |_| | | | | '_ \ / _ \ '__| | | |  _ \ / _ \| __|"
Write-Output "|  _  | |_| | |_) |  __/ |  | |_| | |_) | (_) | |_ "
Write-Output "|_| |_|\__, | .__/ \___|_|   \___/|____/ \___/ \__|"
Write-Output "       |___/|_|                                    "
Write-Output "A customizable, modular Telegram userbot, with innovative components."
Write-Output ""

$win_name = $win_info.WindowsProductName
$win_release = $win_info.OsVersion
$win_ver = $win_info.WindowsVersion

Write-Output "Win edition: $win_name"
Write-Output "Release: $win_release"
Write-Output "Version: $win_ver"
Write-Output ""

# Python --version >=3.8
try {
    Write-Output "Checking for Python..."
    $py_ver_str = python --version
}
catch [System.Management.Automation.CommandNotFoundException] {
    throw "Python is not installed. Please install Python from 'https://www.python.org' or from Microsoft Store"
}

if ( -not $py_ver_str ) {
    throw "Python is not installed. Please install Python from 'https://www.python.org' or from Microsoft Store"
}

$py_ver_str = $py_ver_str.split(" ")[1]
$py_ver = [Version]::new($py_ver_str)

if ( $py_ver -lt [Version]::new(3, 8)) {
    Write-Host -ForegroundColor Yellow "HyperUBot requires at least Python v3.8! Current version is '$py_ver_str'"
    exit 1
}

Write-Output "Python $py_ver_str is installed!"

# Scoop Package Manager for Windows
try {
    Write-Output "Checking for Scoop Package Manager..."
    scoop | Out-Null
}
catch [System.Management.Automation.CommandNotFoundException] {
    Write-Output "Installing Scoop Package Manager..."
    try {
        # From https://scoop.sh/
        Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
    }
    catch {
        Write-Host -ForegroundColor Red "Failed to install the Scoop Package Manager"
        throw $PSItem.Exception.Message
    }
}

# Install scoop packages
Write-Output "Installing pre-requisites packages..."
scoop update
scoop install git neofetch ffmpeg-shared flac

try {
    Write-Output "Fetching latest release from HyperUBot's Repository..."
    $get_release = Invoke-WebRequest -Uri "https://api.github.com/repos/prototype74/HyperUBot/releases/latest"
}
catch [System.Net.WebException] {
    Write-Host -ForegroundColor Yellow "Failed to fetch release from HyperUBot's Repository"
    throw $PSItem.Exception.Message
}

$json_obj = ConvertFrom-Json $([String]::new($get_release.Content))
$tar_pkg = $json_obj.tarball_url
$release_ver = $json_obj.tag_name
$curr_path = (Get-Location).Path
$dir_name = "HyperUBot"

try {
    Write-Output "Downloading HyperUBot ($release_ver)..."
    Invoke-WebRequest $tar_pkg -OutFile .\HyperUBot.tar.gz
}
catch [System.Net.WebException] {
    Write-Host -ForegroundColor Yellow "Failed to download HyperUBot"
    throw $PSItem.Exception.Message
}

Write-Output "Creating HyperUBot's directory in '$curr_path'..."
New-Item -Path . -Name $dir_name -ItemType "directory" | Out-Null

Write-Output "Installing HyperUBot..."
tar -xf .\HyperUBot.tar.gz --directory .\$dir_name --strip-components=1

if ( $LASTEXITCODE -ne 0 ) {
    Write-Host -ForegroundColor Red "Installation failed!"
    exit 1
}
Remove-Item -Path .\HyperUBot.tar.gz -Force

if ( ( Test-Path -Path ".\$dir_name\*" ) -and
     ( Test-Path -Path ".\$dir_name\userbot\__init__.py" ) -and
     ( Test-Path -Path ".\$dir_name\userbot\__main__.py" ) ) {
    Write-Output "HyperUBot has been installed successfully!"
}
else {
    Write-Host -ForegroundColor Red "Installation was not successful!"
    exit 1
}

Set-Location $dir_name

Write-Output "Upgrading pip and setuptools..."
python -m pip install --upgrade pip setuptools

Write-Output "Installing required pip packages..."
while($true) {
    python -m pip install -r requirements.txt
    if ( $LASTEXITCODE -ne 0 ) {
        Write-Output ""
        Write-Host -ForegroundColor Yellow "pip installation was not successful. If pip is not installed, install it manually. For all other cases it may be possible that a pre-requisites package is missing. Install the package/lib/app the pip package does require. Finally, try the pip installation again..."
        Write-Output ""
        while($true) {
            $user_input = Read-Host -Prompt "Re-try pip installation? (y/n)"
            if ( $user_input.ToLower() -eq "y") {
                break
            }
            elseif ( $user_input.ToLower() -eq "n") {
                Write-Host -ForegroundColor Red "Installer cancelled"
                Set-Location ..
                Remove-Item -Path .\$dir_name -Recurse -Force
                exit 1
            }
            else {
                Write-Host -ForegroundColor Yellow "Invalid input. Try again..."
            }
        }
    }
    else {
        break
    }
}

Write-Host -ForegroundColor Green "Installer finished successfully!"
Write-Output ""

while($true) {
    $user_input = Read-Host -Prompt "Do you wish to start the Setup Assistant now? (y/n)"
    if ( $user_input.ToLower() -eq "y") {
        Write-Output "Starting Setup Assistant..."
        Write-Output ""
        python setup.py -nopip
        break
    }
    elseif ( $user_input.ToLower() -eq "n") {
        break
    }
    else {
        Write-Host -ForegroundColor Yellow "Invalid input. Try again..."
    }
}

exit 0
