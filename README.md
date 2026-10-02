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

## 发布状态

新主页已于 2026-10-02 提交到 `Easonyxz/easonyxz.github.io` 的 `main` 分支，旧站点文件已从当前分支移除，没有创建旧站点备份分支。网站发布地址为 https://easonyxz.github.io/ 。

已连接 GitHub 的本地维护目录是 `C:\Users\eason\Desktop\academic-homepage\published-homepage`。后续以此目录为准，不必重新 clone 或从 githubio 复制文件。

GitHub Pages 发布 main 的仓库根目录，正常推送后会自动部署。若部署失败，在仓库 Actions 中查看 Pages 的运行日志；发布来源在 Settings → Pages 中查看。

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
