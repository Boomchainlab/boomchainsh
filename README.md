# boomchainsh
A Web3-native extensible shell for iSH and Alpine. Plugin-ready, remote-controlled, token-gated
# 🔗 BoomchainSH

> A lightweight, plugin-based Web3 shell for iSH (Alpine on iOS).  
> Built for extensibility, rewards, loyalty tracking, and chain ops.

## 🚀 Features
- ✅ Remote plugin install via URL
- 🔌 Enable/disable plugins dynamically
- 🔐 `.secrets.env` support
- 🧠 Tab autocompletion
- ⚙️ `.boomchainshrc` execution at launch

## ⚡ Installation (on iSH / Alpine)
```sh
apk add python3 py3-pip curl git
curl -O https://raw.githubusercontent.com/Boomchainlab/boomchainsh/main/boomchainsh.py
chmod +x boomchainsh.py
echo 'alias boomchainsh="python3 ~/boomchainsh.py"' >> ~/.profile
source ~/.profile
boomchainsh


📦 Install Plugin Pack
curl -LO https://raw.githubusercontent.com/Boomchainlab/boomchainsh/main/archive/boomchainsh-plugins.tar.gz
mkdir -p ~/.boomchainsh/plugins
tar -xvzf boomchainsh-plugins.tar.gz -C ~/.boomchainsh/plugins --strip-components=1


🧩 Plugin Example
plugin new greet
nano ~/.boomchainsh/plugins/greet.py


📜 License

MIT © Boomchainlab


---

## 🧪 `.github/workflows/test.yml`

```yaml
name: Lint Python

on: [push, pull_request]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: 3.10
      - run: pip install flake8
      - run: flake8 boomchainsh.py plugins/

📜 .secrets.env.example
ETH_RPC_URL=
WALLET_ADDRESS=
CHONK9K_PRIVATE_KEY=


🚢 Manual Push Instructions
git init
git remote add origin https://github.com/Boomchainlab/boomchainsh.git
git add .
git commit -m "🚀 Initial commit of BoomchainSH v0.5"
git branch -M main
git push -u origin main

Then:
git tag v0.5
git push origin v0.5
