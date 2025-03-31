#### 安装`git`

在终端输入

```shell
sudo apt-get install git
```

#### 测试`ssh`

在终端输入

```shell
ssh -T git@github.com
```

`git@github.com: Permission denied (publickey).`

这时候需要建立公钥

#### 创建公钥

```shell
ssh-keygen -C "xx@xx.com" -f ~/.ssh/github
```

#### 查看公钥

```shell
cat ~/.ssh/github.pub
```

#### 上传公钥

登陆`github`操作

```shell
gh auth login
```

**过程需要手机验证**

`? What account do you want to log into? GitHub.com `****`选择ssh`****
`? What is your preferred protocol for Git operations on this host? SSH
? Upload your SSH public key to your GitHub account? /home/wzl/.ssh/github.pub
? Title for your SSH key: GitHub CLI
? How would you like to authenticate GitHub CLI? Paste an authentication token`
Tip: you can generate a Personal Access Token here https://github.com/settings/tokens `点击生成token`
`The minimum required scopes are 'repo', 'read:org', 'admin:public_key'.选择token
? Paste your authentication token: `

#### 登陆成功

`? Paste your authentication token: ********************************************************************- gh config set -h github.com git_protocol ssh
✓ Configured git protocol
✓ SSH key already existed on your GitHub account: /home/wzl/.ssh/github.pub
✓ Logged in as wzl-GitHubs`

#### 账号验证

```shell
ssh -T git@github.com
```

`Hi wzl-GitHubs! You've successfully authenticated, but GitHub does not provide shell access.`

#### 列出你自己的所有仓库

```bash
gh repo list --owner <你的用户名>
```
