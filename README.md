# build2019
Presentation for Build 2019

## code

- [helloworld.c](https://github.com/WhitewaterFoundry/build2019/blob/master/helloworld.c) - Sample C code
- [demo.py](https://github.com/WhitewaterFoundry/build2019/blob/master/demo.py) - Sample Python3 script
- [Dockerfile](https://github.com/WhitewaterFoundry/build2019/blob/master/Dockerfile) - Sample Dockerfile
- [deploy_container.yml](https://github.com/WhitewaterFoundry/build2019/blob/master/deploy_container.yml) - Sample Ansible Playbook that deploys our docker container
- [install_fedorawsl.yml](https://github.com/WhitewaterFoundry/build2019/blob/master/install_fedorawsl.yml) - Sample Ansible Playbook that installs Fedora Remix for WSL on Windows

## demo requirements

- Windows 10
    - WSL pre-enabled
- Visual Studio 2019
- Visual Studio Code
- Docker for Desktop
- Pengwin
    - Azure CLI via pengwin-setup
    - Ansible via pengwin-setup
    - Python and pip via pengwin-setup
    - .NET Core via pengwin-setup
    - Docker Bridge via pengwin-setup
    - GUI libraries via pengwin-setup
    - sudo apt-get update -y
    - sudo apt-get install build-essential gcc-mingw-w64 geany -y
    - pengwin-setup modified to skip update/upgrade:
        - `$ sudo nano /usr/local/bin/pengwin-setup` and comment out line 133
        - `$ sudo nano /usr/local/pengwin-setup.d/common.sh` and comment out lines 40 and 42
- X410

## DEV DEMOS

### Getting acquainted with WSL

#### Lets quickly review the basics of WSL and then explore some of it's capabilities. The intent of this section is to get developers thinking in this new hybrid environment.

- Demonstrate Enabling WSL
    - *Enable WSL*
    - Manually
        - *Start -> Settings -> Apps & Features -> Programs and Features -> Turn Windows features on or off -> Windows Subsystem for Linux -> OK*
        *or*
        - WIN + "Turn Windows Features On and Off"
    - PowerShell (as Administrator)
        - `PS Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux`
    - Reboot
- Install Pengwin from Microsoft Store
    - *Where to install Pengwin and other Linux distirbutions*
    - *[Store Link](https://www.microsoft.com/en-us/p/pengwin/9nv1gv1pxz6p)*
- Launch Pengwin
    - *How to start Pengwin*
- Install unzip
    - *We're going to add some packages using the apt package manager*
    - `$ sudo apt-get install unzip -y`
- Git clone our working folder
    - *We're going to our Windows Desktop folder*
    - `$ cd ~/winhome/OneDrive/Desktop/`
    - *Git clone our Build 2019 sample project*
    - `$ git clone https://github.com/WhitewaterFoundry/build2019`
    - `$ cd build2019`
- Open nano to show some simple C code we've written
    - `$ nano helloworld.c`
- Build helloworld.c for Linux
    - `$ gcc helloworld.c -o helloworld`
- Run helloworld for Linux
    - `$ ./helloworld`
- Build helloworld.c for Windows using MinGW packages
    - `$ x86_64-w64-mingw32-gcc helloworld.c -o helloworld.exe`
- Test helloworld for Windows
    - `$ cmd.exe`
    - `> helloworld.exe`
    - `> exit`
- Install Geany, a GUI code editor
    - `$ sudo apt-get install geany`
- Show how to install and run X410 *[Store Link](https://www.microsoft.com/en-us/p/x410/9nlp712zmn9q)*.
- Open file in Geany
    - `$ geany helloworld.c`

### Build a simple development environment

#### We are going to build a simple cross-compatible development environment with Python on WSL and Code on Windows. We are going to see how they can integrate to make dependency management easy.

##### Here is the old way:

- Demonstrate installing Python
    - `$ pengwin-setup` *-> Programming -> Python*
- Open Code
- Configure Code to connect to WSL:
    - *Ctrl + ,*
    - Find `terminal.integrated.shell.windows`
    - Paste `pengwin.exe`
- Open Terminal in Code
- So we can do things like install dependencies with pip
    - `$ sudo pip3 install flask`

##### Here is the new way:

- Search for and show Remote WSL extension in Code
- Demonstrate usage of new extension
    - *F1 -> Remote WSL> -> New Window*
    - Show 'Open Folder'
    - Show 'New Terminal'

### Build a quick web app

#### We can quickly build a small web app right here in this hybrid environment.

- Open Terminal in Code 
- Run script
    - `$ python3 demo.py`
- Open another Terminal in Code
    - `$ wslview http://127.0.0.1:5000`

### Debug running Linux code using Visual Studio

#### Let's build a more robust web app, based on ASP.NET Core, something you might build in-house or get contracted to develop for enterprise.

- Start sshd on WSL
    - `$ sudo service ssh start`
- Install .NET Core in Pengwin
    - `$ pengwin-setup` *-> Programming -> .NET* **Note: NuGet is not required for this demo.**
- Open Visual Studio 2019
- Create a new project -> ASP.NET Core Web Application -> Create
- Select
    - ".NET Core"
    - "ASP.NET Core 2.1"
    - "Web Application"
    - "Create"
    - **Note: Do not enable HTTPS or Docker features**
- Select Web Application template

#### Because ASP.NET Core is cross-platform we can deploy to Windows and Linux.

- Run .NET app in Windows
    - *Click 'IIS Express'*
- While building, open Pengwin and:
    - `$ cd ~/winhome/source/repos/WebApplication1/`
- Show app in Edge
- Stop .NET app in Windows
    - *Debug ->  Stop Debugging*
- Run .NET app in Pengwin
    - `$ dotnet restore`
    - `$ dotnet run`
- Open new console
    - *Middle-click Pengwin icon in taskbar*
- Verify in browser
    - `$ wslview http://127.0.0.1:5000`

#### When deploying ASP.NET Core apps to IIS, to remotely debug you have to enable IIS Management Scripts and Tools, Configure Web Deploy Publishing, and then Import into Visual Studio. On Linux we just use SSH.

- Attach to local process from Visual Studio
    - *Debug -> Attach to Process -> Default*
    - *Select* "dotnet.exe Automatic: Managed (CoreCLR) code"
- Attach to remote process from Visual Studio
    - *Debug -> Attach to Process -> SSH*
    - "localhost" *in Connection target*
    - *Refresh*
    - "pengwin" *in User name*
    - "pengwin" *in Password* **NOTE: In production we recommend using SSH keys.**
    - *Connect*
    - *Select* "dotnet exec /mnt/c/Users..."
    - *Attach*
    - *Check* "Managed (.NET Core for UNIX)" -> OK
    - *View -> Output -> Select* "Debug" **From here you can set breakpoints and monitor debug output just as you would on Windows.**
- Detach from Visual Studio
    - *Switch to Pengwin terminal and type Ctrl-C*

    *Note: On .NET Core apps on bare metal (and on WSL in future) you can use native debugging with GDB.

## OPS DEMOS

### Containerizing our app

- Install how to install Docker bridge
    - *Demonstrate* `$ pengwin-setup` *-> Tools -> Docker*
- Install a third-party tool `dive`
    - Download the latest .deb from [here](https://github.com/wagoodman/dive/releases)
        - `$ cd ~`
        - `$ wget https://github.com/wagoodman/dive/releases/download/v0.7.2/dive_0.7.2_linux_amd64.deb`
    - Install using
        - `$ sudo apt install ./dive_*.deb`
- Get to our working folder
    - `$ cd ~/winhome/source/repos/WebApplication1/`
- Create Dockerfile
    - `$ nano Dockerfile`
- Copy and paste from Dockerfile, explaining the Dockerfile.
    - Use official ASP.NET Core Docker container
    - Just 10 lines of actual code
- Create .dockerignore:
```
bin\
obj\
```
- Build Docker image and analyze it
    - `$ dive build -t webapplication1 .`
- Test locally then stop
    - `$ docker run -d -p 8080:80 --name localtest2 webapplication1`
    - `$ wslview http://localhost:8080/`
    - `$ docker stop localtest2`

### Deploy container to cloud​

- Install Azure CLU **NOTE: Pre-installed for this demo.**
    - `$ pengwin-setup` *-> Tools -> Cloud CLI -> Azure*
- Login into Azure
    - `$ az login`
- Create a Resource Group
    - `$ az group create --name Build2019ResourceGroup --location eastus`
- Create an Azure container registry
    - `$ az acr create --resource-group Build2019ResourceGroup --name build2019dcr --sku Basic`
- Log into Azure container registry
    - `$ az acr login --name build2019dcr`
- Get Azure Image Registry URI
    - `$ registry_uri=$(az acr show --name build2019dcr --query loginServer)`
- Remove double quotes, show results
    - `$ eval registry_uri=$registry_uri`
    - `$ echo $registry_uri`
- Tag our Docker image
    - `$ docker tag webapplication1 $registry_uri/webapplication1:v1`
- Push Docker image to Azure registry
    - `$ docker push $registry_uri/webapplication1:v1`
- Enable administrative rights on registry
    - `$ az acr update -n build2019dcr --admin-enabled true`
- Get our registry passphrase **NOTE: In production we recommend using Azure Key Vault.**
    - `$ registry_password=$(az acr credential show --name build2019dcr --query "passwords[0].value")   `
- Remove double quotes, do not show results
    - `$ eval registry_password=$registry_password  `
- Deploy our container
    ```
    $ az container create --resource-group Build2019ResourceGroup --name build2019dcr --image $registry_uri/webapplication1:v1 \
    --cpu 1 --memory 1 --ip-address public --ports 80 --registry-username build2019dcr --registry-password $registry_password
    ```
- Get our container's IP address by listing contents and piping through json parser jq, like sed for json, we pre-install with the Azure CLI tools
    - `$ ipaddr=$(az container list --resource-group Build2019ResourceGroup | jq '.[].ipAddress.ip')`
- Test
    - `$ wslview http://$ipaddr`

### Deploy container to on-site Linux server with Ansible

- Install Ansible on Pengwin
    - `$ pengwin-setup` *-> Tools -> Ansible* **Feature in pengwin-setup SOON.**
    - For now: `$ curl https://raw.githubusercontent.com/WhitewaterFoundry/pengwin-setup/development/pengwin-setup.d/ansible.sh | bash`
- Move up in our working path
    - `$ cd ..`
- Create hosts file
    - `$ echo "[webserver]" > hosts`
    - `$ echo "155.138.214.242" >> hosts`
- Generate and copy SSH Keys **Note: Only necessary first time connecting.**
    - `$ ssh-keygen -t rsa -C "name@example.org"`
    - `$ ssh-copy-id root@155.138.214.242`
- Test connection
    - `$ ansible webserver -m ping -u root -i hosts`
- Write Ansible Playbook
    - `$ nano deploy_container.yml`
- Copy and paste contents of deploy_container.yml, explaining each step:
    - Installs Docker dependencies, if needed
    - Installs Docker from official sources, if neded
    - Installs Ansible client dependencies
    - Configures to pull image from Azure container registry, uses environmental variables already created
- Run playbook
    - `$ ansible-playbook -i hosts deploy_container.yml --extra-vars '{"registry_uri":'$registry_uri',"registry_password":'$registry_password',"application_name":"webapplication1"}'  `
    - *NOTE: Several environmental variables defined and used earlier are carried over into our Ansible playbook using the --extra-vars option.*
- Verify running
    - `$ wslview http://155.138.214.242`

### Configuring remote devices​

#### We aren't simply limited to administering Linux devices.

- RDP to remote Windows 10
- Enable WSL (as Administrator) **Note: Already enabled for this demo.**
    - `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux`
- Enable WinRM (as Administrator)
    - `Winrm quickconfig`
- Enable basic authentication
    - `cmd /C 'winrm set winrm/config/service @{AllowUnencrypted="true"}' `
    - `cmd /C 'winrm set winrm/config/service/auth @{Basic="true"}' `
- Return to WSL on local device
- Change to root directory
    - `$ cd ~`
- Create new directory
    - `$ mkdir winclients`
    - `$ cd winclients`
- Create hosts file
    - `$ echo "[winclient]" > hosts`
    - `$ echo "149.248.34.228" >> hosts`
    - `$ echo "[winclient:vars]" >> hosts`
    - `$ echo "ansible_port=5985" >> hosts`
- Write Ansible Playbook
    - `$ nano install_fedorawsl.yml`
- Copy and paste contents of install_fedorawsl.yml, explaining contents, insert password
- Run playbook
    - `$ ansible-playbook -i hosts install_fedorawsl.yml`
- Return to RDP to remote Windows 10, confirm Fedora installed and dnf updated
