# How to setup:

## *nix
```sh
$ python -m venv venv
$ source ./venv/bin/activate
$ pip install --upgrade pip
$ pip install -r ./requirements.txt
```

## Windows
Ensure RemoteSigned execution policy is enabled for CurrentUser
```powershell
PS> Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

```powershell
PS> python -m venv venv
PS> .\venv\Scripts\Activate.ps1
PS> python -m pip install --upgrade pip
PS> pip install -r .\requirements.txt
```