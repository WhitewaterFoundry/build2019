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
    - Azure CLI 
    - gcc-mingw-w64
- X410

## DEV DEMOS

### Getting acquainted with WSL

#### Lets quickly review the basics of WSL and then explore some of it's capabilities. The intent of this section is to get developers thinking in this new hybrid environment.

- Demonstrate Enabling WSL
    - Manually
        - *Start -> Settings -> Apps & Features -> Programs and Features -> Turn Windows features on or off -> Windows Subsystem for Linux -> OK*
    - PowerShell (as Administrator)
        - `PS Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux`
- Install and run Pengwin from Microsoft Store
    - *[Store Link](https://www.microsoft.com/en-us/p/pengwin/9nv1gv1pxz6p)*
- Install ssh and unzip
    - `$ sudo apt-get install ssh jq unzip -y`
- Install basic build tools
    - `$ sudo apt-get install build-essential gcc-mingw-w64 -y`
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

### Build a simple development environment

#### We are going to build a simple cross-compatible development environment with Python on WSL and Code on Windows. We are going to see how they can integrate to make dependency management easy.

- Install Python
    - `$ pengwin-setup` *-> Programming -> Python*
- Open Code
- Configure Code
    - *Ctrl + ,*
    - Find `terminal.integrated.shell.windows`
    - Paste `pengwin.exe`
- Open Terminal in Code
- So we can do things like install dependencies with pip
    - `$ pip3 install --upgrade pip`
    - `$ pip3 install flask --user`

### Build a quick web app

#### We can quickly build a small web app right here in this hybrid environment.

- Copy and paste demo.py into Code and save to Desktop as demo.py
- Open Terminal in Code 
- Run script
    - `$ cd /mnt/c/Users/Hayden/OneDrive/Desktop`
    - `$ python3 demo.py`
- Switch to Pengwin and show webpage
    - `$ wslview http://127.0.0.1:5000`

### Debug running Linux code using Visual Studio

#### Let's build a more sophisticated web app, based on ASP.NET Core.

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
    - **Note: Do not check HTTPS or Docker features**
- Select Web Application template

#### Because ASP.NET Core is cross-platform we can deploy to Windows and Linux.

- Run .NET app in Windows
    - *Click 'IIS Express'*
- Stop .NET app in Windows
    - *Debug ->  Stop Debugging*
- Run .NET app in Pengwin
    - `$ cd ~/winhome/source/repos/WebApplication1/WebApplication1/`
    - `$ dotnet restore`
    - `$ dotnet run`
- Open new console
    - *Middle-click Pengwin icon in taskbar*
- Verify in browser
    - `$ wslview http://127.0.0.1:5000`

#### When deploying ASP.NET Core apps to IIS, to remotely debug you have to enable IIS Management Scripts and Tools, Configure Web Deploy Publishing, and then Import into Visual Studio. On Linux we just use SSH.

- Attach to process from Visual Studio
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

## OPS DEMOS

### Containerizing our app

- Install Docker bridge
    - `$ pengwin-setup` *-> Tools -> Docker*
- Install a third-party tool `dive`: <https://github.com/wagoodman/dive/releases>
    - Download the latest .deb
    - install using `sudo apt install ./dive_*.deb`
- Get to our working folder
    - `$ cd ~/winhome/source/repos/WebApplication1/WebApplication1/`
- Create Dockerfile:
    ```
    FROM microsoft/dotnet:sdk AS build-env
    WORKDIR /app

    # Copy csproj and restore as distinct layers
    COPY *.csproj ./
    RUN dotnet restore

    # Copy everything else and build
    COPY . ./
    RUN dotnet publish -c Release -o out

    # Build runtime image
    FROM microsoft/dotnet:aspnetcore-runtime
    WORKDIR /app
    COPY --from=build-env /app/out .
    ENTRYPOINT ["dotnet", "WebApplication1.dll"]
    ```
- Create .dockerignore:
    ```
    bin\
    obj\
    ```
- Build Docker image and analyze it
    - `$ dive build -t webapplication1 .`
- Test locally then stop
    - `$ docker run -d -p 8080:80 --name localtest webapplication1`
    - `$ wslview http://localhost:8080/`
    - `$ docker stop localtest`

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
    - `$ registry_password=$(az acr credential show --name build2019dcr --query "passwords[0].value")`
- Remove double quotes, do not show results
    - `$ eval registry_password=$registry_password`
- Deploy our container
    ```
    $ az container create --resource-group Build2019ResourceGroup --name build2019dcr --image $registry_uri/webapplication1:v1 \
    --cpu 1 --memory 1 --ip-address public --ports 80 --registry-username build2019dcr --registry-password $registry_password
    ```
- Get IP address
    - `$ ipaddr=$(az container list --resource-group Build2019ResourceGroup | jq '.[].ipAddress.ip')`
- Test
    - `$ wslview http://$ipaddr`

### Deploy container to on-site Linux server with Ansible

- Install Ansible on Pengwin
    - `$ pengwin-setup` *-> Tools -> Ansible* **Feature in pengwin-setup development branch.**
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
- Copy and paste contents of deploy_container.yml
- Run playbook
    - `$ ansible-playbook -i hosts deploy_container.yml --extra-vars '{"registry_uri":'$registry_uri',"registry_password":'$registry_password',"application_name":"webapplication1"}'  `
    - *NOTE: Several environmental variables defined and used earlier are carried over into our Ansible playbook using the --extra-vars option.*
- Verify running
    - `$ wslview http://155.138.214.242`

### Configuring remote devices​

- RDP to remote Windows 10
- Enable WSL (as Administrator) **Note: Already enabled for this demo.**
    - `PS Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux`
- Enable WinRM (as Administrator)
    - `PS Winrm quickconfig`
- Enable basic authentication
    - `PS cmd /C 'winrm set winrm/config/service @{AllowUnencrypted="true"}' `
    - `PS cmd /C 'winrm set winrm/config/service/auth @{Basic="true"}' `
- Return to WSL on local device
- Change to root directory
    - `$ cd ~`
- Create new directory
    - `$ mkdir winclients`
    - `$ cd winclients`
- Create hosts file
    - `$ echo "[winclient]" > hosts`
    - `$ echo "66.42.70.150" >> hosts`
- Write Ansible Playbook
    - `$ nano install_fedorawsl.yml`
- Copy and paste contents of install_fedorawsl.yml
- Run playbook
    - `$ ansible-playbook -i hosts install_fedorawsl.yml`
- Return to RDP to remote Windows 10, confirm Fedora installed and dnf updated
