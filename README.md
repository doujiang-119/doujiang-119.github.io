# Samantha 个人网站 · 发布说明

零依赖静态站：只有 `index.html`、`favicon.svg` 和 `assets/` 里的图片，没有构建步骤，不需要安装任何开发环境。

```
site/
├── index.html        页面本体（样式内联，无需额外文件）
├── favicon.svg       浏览器标签页图标
└── assets/
    ├── photo.jpg     个人照片（大图 820px 宽）
    └── photo-s.jpg   个人照片（手机用小图 540px 宽）
```

---

## 一、在电脑上预览

**方法 1（最简单）：直接双击 `index.html`**，会用默认浏览器打开。所有功能都能用。

**方法 2（推荐，更接近线上效果）：起一个本地服务**

Windows（PowerShell）：
```powershell
cd site
python -m http.server 8000
```
macOS（终端）：
```bash
cd site
python3 -m http.server 8000
```
然后浏览器打开 `http://localhost:8000`。

**检查手机效果**：浏览器按 `F12` → 点设备图标（或按 `Ctrl+Shift+M`）→ 顶部选 `iPhone SE` 或把宽度调成 **375**。

---

## 二、发布到 GitHub Pages（全程网页操作，不用装 Git）

1. 登录 [github.com](https://github.com)，右上角 **+** → **New repository**
2. 仓库名随意（比如 `about-me`），选 **Public**（免费账号 Pages 只支持公开仓库），点 **Create repository**
3. 仓库页里点 **uploading an existing file**（或 Add file → Upload files）
4. 把 `site` 文件夹里的**所有内容**拖进去：`index.html`、`favicon.svg`、`assets` 整个文件夹
   - 注意：上传的是 site 文件夹**里面的**文件，`index.html` 必须在仓库根目录
5. 点 **Commit changes**，等上传完成
6. 仓库页 → **Settings** → 左侧 **Pages**
7. Source 选 **Deploy from a branch**；Branch 选 **main** + **/(root)**；点 **Save**
8. 等一两分钟，刷新该页，顶部会出现网址：
   `https://你的用户名.github.io/仓库名/`
   —— 这就是你的正式网址，手机电脑都能访问

**以后更新**：仓库页里重新 Upload files 覆盖同名文件，再 Commit 即可，一分多钟后自动生效。

**可选：用 GitHub Desktop 或命令行**（`git push`）也完全可以，效果一样。

---

## 三、还差的两件事（上线前必须处理）

| 事项 | 做法 |
|---|---|
| **微信二维码** | 把二维码图片存为 `assets/wechat-qr.jpg`，然后把 `index.html` 里搜 `【待确认】微信入口`，把整个虚线占位块换成 `<img src="assets/wechat-qr.jpg" alt="Samantha 的微信二维码" width="240">`；底部固定条和"想聊，加微信"按钮链接保持指向 `#contact` |
| **第三方授权确认** | 页面目前写的是"一家心理咨询培训公司"，没有出现公司名；公司经营数据（投诉率、满意度）未放上去。若想公开公司名或数据，先取得公司同意 |

## 四、以后可以加的（等你确认事实再动）

- 经历时间线：做成"章节卡片"横滑（版式已备好），需要你补年份和节点
- 行业年限"将近十年"：确认入行年份后可写具体（如"自 20XX 年"）
- 读者常见问题区：以后把微信里被问得多的问题沉淀上去
