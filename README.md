# Brew & Bake Lab

面向厨房实操的参数化饮品与烘焙手册。当前首个完整详情页为瑞士卷，包含配方切换、参数、步骤、状态判断、失败排查、版本记录和专注跟做模式。

## 本地预览

项目是无构建依赖的静态站点。在项目目录运行：

```bash
python3 -m http.server 4173
```

然后访问 `http://localhost:4173/`。

不要直接双击 HTML 作为最终验证方式；部署前应通过 HTTP 地址检查资源路径、本地存储和手机布局。

## 部署

### Vercel

1. 将此目录推送到独立 GitHub 仓库。
2. 在 Vercel 中导入该仓库。
3. Framework Preset 选择 `Other`。
4. 不填写 Build Command，Output Directory 保持项目根目录。
5. 部署后访问生产域名。

### GitHub Pages

也可在仓库设置中启用 Pages，并选择从 `main` 分支根目录发布。站点入口是根目录的 `index.html`。

## 当前数据边界

- 配方编辑和跟做进度保存在当前浏览器的本地存储中。
- 上传图片经过浏览器压缩后保存到当前设备。
- 换设备或清理浏览器数据前，请使用页面侧栏的“配方备份”导出 JSON。
- 当前版本尚未提供账号登录、跨设备同步或云端菜谱管理。

## 目录

```text
index.html              正式站点入口
assets/swiss-roll/      瑞士卷过程与状态图片
PROJECT_BRIEF.md        产品定位与信息架构
```
