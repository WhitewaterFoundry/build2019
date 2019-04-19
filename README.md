# build2019
Presentation for Build 2019

## code

- [helloworld.c](https://github.com/WhitewaterFoundry/build2019/blob/master/helloworld.c)
- [demo.py](https://github.com/WhitewaterFoundry/build2019/blob/master/demo.py) - Sample Python3 script
- [deploy_container.yml](https://github.com/WhitewaterFoundry/build2019/blob/master/deploy_container.yml) - Sample Ansible Playbook that deploys our docker container to Azure
- [install_fedorawsl.yml](https://github.com/WhitewaterFoundry/build2019/blob/master/install_fedorawsl.yml) - Sample Ansible Playbook that installs Fedora Remix for WSL on Windows

## demo requirements

- Windows 10
    - WSL pre-enabled
- Visual Studio 2019
- Visual Studio Code
- Docker for Desktop
- Pengwin
    - Azure CLI pre-installed
    - Azure 
- X410

## dev demos 

### Getting acquainted with WSL

- Demonstrate Enabling WSL
    - Manually
        - *Start -> Settings -> Apps & Features -> Programs and Features -> Turn Windows features on or off -> Windows Subsystem for Linux -> OK*
    - PowerShell (as Administrator)
        - `PS Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux`
- Install and run Pengwin from Microsoft Store
    - *[Store Link](https://www.microsoft.com/en-us/p/pengwin/9nv1gv1pxz6p)*
- Install ssh
    - `$ sudo apt-get install ssh -y`
- Install basic build tools
    - `$ sudo apt-get install build-essential gcc-mingw-w64 -y`
- Install nano
    - `$ sudo apt-get install nano -y`
- Run nano
    - `$ nano helloworld.c`
- Copy and paste helloworld.c into nano and save
- Build helloworld.c for Linux
    - `$ gcc helloworld.c -o helloworld`
- Run helloworld for Linux
    - `$ ./helloworld`
- Build helloworld.c for Windows
    - `$ x86_64-w64-mingw32-gcc helloworld.c -o helloworld.exe`
- Run helloworld for Windows
    - `$ cp helloworld.exe /mnt/c/Users/Pengwin/Desktop/`
    - `$ cmd.exe`
    - `> cd c:\Users\Pengwin\Desktop\`
    - `> helloworld.exe`
    - `> exit`
- Install PowerShell
    - `$ pengwin-setup` -> Tools -> PowerShell
    - `$ pwsh`
- Install and run X410
    - *[Store Link](https://www.microsoft.com/en-us/p/x410/9nlp712zmn9q)*
- Install Geany
    - `$ sudo apt-get install geany`
    - `$ geany helloworld.c`

### Build our development environment

- Install Python
    - `$ pengwin-setup` *-> Programming -> Python*
- Open Code
- Configure Code
    - *Ctrl + ,*
    - Find `terminal.integrated.shell.windows`
    - Paste `pengwin.exe`
- Open Terminal in Code

### Script with Code

- Copy and paste demo.py into Code and save to Desktop as demo.py
- Open Terminal in Code
- Install dependencies 
    - `$ pip3 install --upgrade pip`
    - `$ pip3 install flask` 
- Run script
    - `$ cd /mnt/c/Users/Pengwin/Desktop`
    - `$ python3 demo.py`
- Show webpage
    - `$ wslview http://127.0.0.1:5000`

### Debug running Linux code using Visual Studio

- Start sshd on WSL
    - `$ sudo service ssh start`
- Install .NET Core
    - `$ pengwin-setup` *-> Programming -> .NET*
- Create new ASP.NET Core project in Visual Studio 2019
- Select Web Application template
- Run .NET app in Windows
    - *Click 'IIS Express'*
- Run .NET app in Pengwin
    - `$ cd ~/winhome/source/repos/WebApplication1/`
    - `$ dotnet restore`
    - `$ dotnet run`
- Open new console
    - *Middle-click Pengwin icon in taskbar*
- Verify in browser
    - `$ wslview http://127.0.0.1:5000`
- Attach to process from Visual Studio
    - *Debug -> Attach to Process -> SSH*
    - "localhost1" *in Connection target*
    - *Refresh*
    - "pengwin" *in User name*
    - "pengwin" *in Password* **In production we recommend using SSH keys.**
    - *Connect*
    - *Select* "dotnet exec /mnt/c/Users..."
    - *Attach*
    - *Check* "Managed (.NET Core for UNIX)" -> OK
    - *View -> Output -> Select* "Debug" **From here you can set breakpoints just as you would on Windows.**

## ops demos 

### Containerizing our app

- Install Docker bridge
    - `$ pengwin-setup` *-> Tools -> Docker*
- Compile web app
    - `$ dotnet publish -c Release`
- Confirm
    - `$ ls bin/Release/netcoreapp2.1/publish`
- Prepare
    - `$ cd ..`
    - `$ nano Dockerfile`
    - *Copy and paste the following:*
        ```
        FROM mcr.microsoft.com/dotnet/core/runtime:2.1
        COPY WebApplication1/bin/Release/netcoreapp2.1/publish/ WebApplication1/
        ENTRYPOINT ["dotnet", "WebApplication1/WebApplication1.dll"]
        ```
- Build Docker container
    - `$ docker build -t myimage .`
    - `$ docker create myimage --name webapp`
    - `$ docker ps -A`
    - 

### Deploy container to cloud​

- Install Azure CLU **Pre-installed for this demo.**
    - `$ pengwin-setup` *-> Tools -> Cloud CLI -> Azure*
- Create a Resource Group
    - `$ az group create --name myResourceGroup --location eastus`

### Deploy container to on-site Linux server​

### Configuring remote devices​