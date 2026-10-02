# Xinzhen Yu — Academic Homepage

英文静态学术主页，用于 https://easonyxz.github.io/ 。页面包含 About、News、Education、Publications 和 Awards。无需 Jekyll、Ruby 或 npm；网站根目录中的 `.nojekyll` 让 GitHub Pages 直接发布 HTML。

## 文件结构

```text
githubio/
├── index.html                 # 生成的页面，不要直接维护内容
├── build.py                   # 根据 profile.json 生成 index.html
├── assets/
│   ├── profile.json           # 个人信息、简介、新闻、教育、论文、奖励
│   ├── style.css              # 布局、CVPR blue 配色和悬停效果
│   ├── main.js                # 论文图片放大弹窗
│   ├── avatar.jpg             # GitHub 头像
│   ├── favicon.png            # 浏览器图标
│   ├── szu-logo.png           # 深圳大学透明校徽
│   ├── shou-logo.png          # 上海海洋大学透明校徽
│   └── publications/          # 每篇的缩略图和大图 WebP
├── favicon.ico
├── 404.html
├── robots.txt
├── sitemap.xml
├── .nojekyll
├── .gitignore
└── README.md
```

## 本地更新与预览

用编辑器打开 `assets/profile.json`：`about` 是简介，`news` 是新闻，`education` 是教育经历，`publications` 是论文，`awards` 是奖励。`services` 暂时为空，填入真实记录后会显示 Academic Services。

论文图片用 `image` 指向缩略图、`image_large` 指向放大图。添加新论文时复制一条论文记录，修改标题、作者、venue、说明和链接。没有论文/代码链接时保留空字符串；没有图片时也保留空字符串。不要加虚构链接。作者中与 `name` 完全相同的姓名自动加粗。所有路径相对于网站根目录。

在 PowerShell 中运行：

```powershell
Set-Location 'C:\Users\eason\Desktop\academic-homepage\githubio'
python build.py
python -m http.server 8000 --bind 127.0.0.1
```

访问 http://127.0.0.1:8000/ ，Ctrl+C 停止服务。如果已有预览服务运行，只需要重新生成页面并刷新浏览器。修改 CSS/JavaScript 后可按 Ctrl+F5 强制刷新。

## 首次上传：推荐保留旧仓库历史

截至 2026-10-02，远程仓库 `Easonyxz/easonyxz.github.io` 的默认分支为 `main`，旧网站在仓库根目录。本地 `githubio` 目前不是 Git 仓库。不要在此直接 init 后强制推送；先克隆现有仓库，再复制新网站进去。

### 用 GitHub Desktop

1. 登录 GitHub Desktop，File → Clone repository，选择 `Easonyxz/easonyxz.github.io`；本地路径选 `C:\Users\eason\Desktop\academic-homepage\published-homepage`（不要选现有 githubio）。
2. 从 main 创建备份分支，例如 `old-site-20261002`，发布该分支，再切回 main。如果同名备份已存在，另取一个名字。
3. 把 githubio 中的文件和 assets 目录复制到 published-homepage 根目录，替换同名文件。确保 `.nojekyll`、`.gitignore` 也复制进去，不能变成 `published-homepage/githubio/index.html`。
4. 在 Desktop 的 Changes 中查看差异，提交为 `Update academic homepage`，点击 Push origin。旧的 css、js、fonts、images、blog-single.html 不影响新首页；如确认无需保留，可从 main 删除，备份分支仍保留原站点。保留仓库的 `.git` 目录。
5. 打开 GitHub 仓库 Settings → Pages → Build and deployment。Source 选择 **Deploy from a branch**，Branch 选择 **main**，Folder 选择 **/ (root)**，点 Save。
6. 等 Pages 构建完成，访问 https://easonyxz.github.io/ 。如显示旧页面，强制刷新；如构建失败，在 Actions 查看 Pages 的运行日志。

此方法通过正常提交更新现有仓库，无需新建仓库或更换网址。

### PowerShell 替代方式

安装并登录 Git 后可使用下面步骤；clone 目标须是尚不存在的文件夹。

```powershell
Set-Location 'C:\Users\eason\Desktop\academic-homepage'
git clone https://github.com/Easonyxz/easonyxz.github.io.git published-homepage
Set-Location published-homepage
git branch old-site-20261002
git push origin old-site-20261002
Get-ChildItem -LiteralPath '..\githubio' -Force | ForEach-Object {
    Copy-Item -LiteralPath $_.FullName -Destination '.' -Recurse -Force
}
git status --short
git diff --stat
git add .
git commit -m 'Update academic homepage'
git push origin main
```

随后按上面的 Settings → Pages 设置发布来源。如果备份分支已存在，换一个分支名。不要使用 force push。

## 以后如何更新

首次上传后，建议以 `published-homepage` 这个克隆目录作为唯一维护目录，后续不要同时修改两份文件。

1. 在 GitHub Desktop 的 main 分支点击 Fetch origin / Pull origin，取得最新内容。
2. 修改克隆目录中的 `assets/profile.json`（或 CSS、图片），在该目录运行 `python build.py`。
3. 本地预览确认；在 Desktop 写更新说明，Commit to main → Push origin。
4. Pages 自动重新发布，不必重新设置 Pages。

也可在克隆目录用 PowerShell：

```powershell
git pull --ff-only
# 编辑 profile.json、样式或图片后：
python build.py
git diff --stat
git add .
git commit -m 'Update publications and news'
git push origin main
```

GitHub Pages 不会替你运行 build.py，所以必须把生成后的 index.html 一起提交。若还没有克隆仓库，可临时用网页 Add file → Upload files 上传网站文件，确认选择 main 且文件位于根目录；长期更新建议用 Desktop。

## 资料与资源来源

个人信息来自提供的 CV/访问.tex 与 resume-zh_CN.tex；中文姓名为余欣震。News 年份及接受消息沿用简历。联系方式为学校邮箱、Scholar 和 GitHub，未发布手机号。CV、项目与开发经历暂不展示，也不包含在本次发布包中。

头像来自 GitHub @Easonyxz。校徽来自两所大学官网，独立透明 PNG 保留高分辨率。论文图来自用户提供的 HER2 PNG、FGA-MIL PDF 第一页和 Red Fuji JPG，WebP 缩略图最长边 800px、大图最长边 1800px，点击在页内放大。主色 #367DBD 来自简历 cvprblue。

参考设计：https://github.com/WD7ang/WowPage 和 https://github.com/luost26/academic-homepage 。本站独立实现，未复制模板源码。

部署依据：https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
