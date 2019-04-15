# build2019
Presentation for Build 2019

## code

demo.py - Sample Python3 script
deploy_container.yml - Sample Ansible Playbook that deploys our docker container to Azure
install_fedorawsl.yml - Sample Ansible Playbook that installs Fedora Remix for WSL on Windows

## demos 

### dev

#### Getting acquainted with WSL

- Enabling WSL
    - Manually
        - Start -> Settings -> Apps & Features -> Programs and Features -> Turn Windows features on or off -> Windows Subsystem for Linux -> OK
    - PowerShell (as Administrator)
        - `PS Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux`
- Install Pengwin from Microsoft Store
    - [Store Link](https://www.microsoft.com/en-us/p/pengwin/9nv1gv1pxz6p)
- Install ssh
    - `$ sudo apt-get install ssh`
- Install build-essential
    - `$ sudo apt-get install build-essential`
- Install vim
    - `$ sudo apt-get install vim`
- Install powershell
    - `$ pengwin-setup`
- Install X410
    - [Store Link](https://www.microsoft.com/en-us/p/x410/9nlp712zmn9q)
- Install Geany
    - `$ sudo apt-get install geany`

#### Build our development environment

#### Script with Code

#### Debug running Linux code using Visual Studio

### ops

#### Containerizing our app

#### Deploy container to cloud​

#### Deploy container to on-site Linux server​

#### Configuring remote devices​