# build2019
Presentation for Build 2019

## code

- [helloworld.c](https://github.com/WhitewaterFoundry/build2019/blob/master/helloworld.c)
- [demo.py](https://github.com/WhitewaterFoundry/build2019/blob/master/demo.py) - Sample Python3 script
- [deploy_container.yml](https://github.com/WhitewaterFoundry/build2019/blob/master/deploy_container.yml) - Sample Ansible Playbook that deploys our docker container to Azure
- [install_fedorawsl.yml](https://github.com/WhitewaterFoundry/build2019/blob/master/install_fedorawsl.yml) - Sample Ansible Playbook that installs Fedora Remix for WSL on Windows

## dev demos 

### Getting acquainted with WSL

- Enabling WSL
    - Manually
        - Start -> Settings -> Apps & Features -> Programs and Features -> Turn Windows features on or off -> Windows Subsystem for Linux -> OK
    - PowerShell (as Administrator)
        - `PS Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux`
- Install and run Pengwin from Microsoft Store
    - [Store Link](https://www.microsoft.com/en-us/p/pengwin/9nv1gv1pxz6p)
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
    - [Store Link](https://www.microsoft.com/en-us/p/x410/9nlp712zmn9q)
- Install Geany
    - `$ sudo apt-get install geany`
    - `$ geany helloworld.c`

### Build our development environment

### Script with Code

### Debug running Linux code using Visual Studio

## ops demos 

### Containerizing our app

### Deploy container to cloud​

### Deploy container to on-site Linux server​

### Configuring remote devices​