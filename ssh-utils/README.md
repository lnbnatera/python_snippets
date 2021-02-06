# How to setup:

## *nix
```sh
$ python -m venv ssh-utils-venv
$ source ./ssh-utils-venv/bin/activate
$ pip install --upgrade pip
$ pip install -r ./requirements.txt
```

## Windows
Ensure RemoteSigned execution policy is enabled for CurrentUser
```powershell
PS> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

```powershell
PS> python -m venv ssh-utils-venv
PS> .\ssh-utils-venv\Scripts\Activate.ps1
PS> python -m pip install --upgrade pip
PS> pip install -r .\requirements.txt
```

## Sample run:
The script will create an id_rsa on the current directory and show the public key
```sh
$ python ./generate_ssh_key.py
0rtuUlAsNkaHJeEak3/W5Yx+8zJicVaf7N2XuGUW2dJdAtUqPpImVTeOVentww==
AAAAB3NzaC1yc2EAAAADAQABAAAAgQC5nrKRCO7XC/Sz5oitVlExnew4wn6qsu3nx1cJCvPxhp03Vo4GsBhzYKx0j5PAPp0s8ToJljJDK94VTqSdo9I2DsjREi0ZS+WWYeDOIJXIAeH30rtuUlAsNkaHJeEak3/W5Yx+8zJicVaf7N2XuGUW2dJdAtUqPpImVTeOVentww==
```