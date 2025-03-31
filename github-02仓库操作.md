##### 列出仓库

```shell
gh repo list <用户名>
```

### 添加仓库

###### 公开仓库

例如，创建一个名为 `new-public-repo` 的公开仓库，命令如下：

```bash
gh repo create new-public-repo --public
```

###### 私有仓库

例如，创建一个名为 `new-private-repo` 的私有仓库，命令如下：

```bash
gh repo create new-private-repo --private
```

###### 带有描述的仓库

如果你想在创建仓库时添加描述信息，可以使用 `--description` 参数。示例如下，创建一个名为 `new-desc-repo` 且带有描述信息的公开仓库：

bash

```bash
gh repo create new-desc-repo --public --description "这是一个带有描述的新仓库"
```

### 删除仓库

```shell
gh repo delete <用户名>/<仓库名称>
```

### 修改仓库描述

你可以使用 `gh repo edit` 命令修改仓库的描述信息。具体命令格式如下：

```bash
gh repo edit <用户名>/<仓库名> --description "新的描述信息"
```

###### 修改仓库的可见性

若要把仓库从公开变为私有，或者从私有变为公开，可使用 `--visibility` 参数。公开仓库使用 `public`，私有仓库使用 `private`。示例如下：

- 将 `wzl-GitHubs/ubuntu-ssh` 仓库变为私有：

```bash
gh repo edit wzl-GitHubs/ubuntu-ssh --visibility private
```

- 将 `wzl-GitHubs/ubuntu-ssh` 仓库变为公开：

```bash
gh repo edit wzl-GitHubs/ubuntu-ssh --visibility public
```

###### 启用或禁用仓库的某些功能

- **启用或禁用 Issues 功能**：使用 `--enable-issues` 或 `--disable-issues` 参数。例如，启用 `wzl-GitHubs/ubuntu-ssh` 仓库的 Issues 功能：

```bash
gh repo edit wzl-GitHubs/ubuntu-ssh --enable-issues
```

- **启用或禁用 Wiki 功能**：使用 `--enable-wiki` 或 `--disable-wiki` 参数。例如，禁用 `wzl-GitHubs/ubuntu-ssh` 仓库的 Wiki 功能：

```bash
gh repo edit wzl-GitHubs/ubuntu-ssh --disable-wiki
```

###### 添加或修改仓库主页链接

使用 `--homepage` 参数可以添加或修改仓库的主页链接。示例如下，为 `wzl-GitHubs/ubuntu-ssh` 仓库添加主页链接：

```bash
gh repo edit wzl-GitHubs/ubuntu-ssh --homepage "https://example.com"
```
