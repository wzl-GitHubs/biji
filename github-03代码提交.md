### 创建带有描述的仓库

如果你想在创建仓库时添加描述信息，可以使用 `--description` 参数。示例如下，创建一个名为 `new-desc-repo` 且带有描述信息的公开仓库：

bash

```bash
gh repo create new-desc-repo --public --description "这是一个带有描述的新仓库"
```

### 删除仓库

```shell
gh repo delete <用户名>/<仓库名称>
```

### 提交代码

```bash
# 初始化本地仓库
cd test-project
git init

# 关联远程仓库
git remote add origin git@github.com:wzl-GitHubs/test-project.git
# 例如
git remote add origin 'https://github.com/wzl-GitHubs/biji.git'

# 编写代码...

# 修改编码
git config --global core.quotepath
git config --global core.quotepath false

# 查看文件状态
git status

# 暂存所有修改的文件
git add .

# 配置全局作者信息
git config --global user.email "you@example.com"
git config --global user.name "Your Name"

# 提交到本地仓库
git commit -m "完成项目初始搭建"

# 首次提交需要创建主分支
git checkout -b main
# 将本地的 main 分支推送到远程
git push -u origin main
# 然后需要选择提交方式

输入创建的token名
Username for 'https://github.com': https://github.com
输入token
Password for 'https://https%3A%2F%2Fgithub.com@github.com': 
```

### 示例流程

假设你要对 `main` 分支进行二次提交，操作步骤如下：

bash

```bash
# 查看文件状态
git status

# 添加所有更改的文件到暂存区
git add .

# 提交暂存区的文件到本地仓库
git commit -m "更新 bug"

# 拉取远程仓库的最新代码
git pull origin main

# 推送本地代码到远程仓库
git push origin main
```
