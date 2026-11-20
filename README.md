# Vibe Coding + GitOps 入门实验

这是一个适合初学者的端到端小项目：Python 标准库 Web 应用 → 单元测试 → Docker 镜像 → GitHub Actions → GHCR → Flux → 本机 kind。

详细的 Windows 11 + WSL2 操作步骤见配套学习指南。先按指南替换以下占位内容，再提交到 GitHub：

* `clusters/kind-demo/flux-system/source-sync.yaml` 中的 `CHANGE_ME/CHANGE_ME` 改成个人 GitHub 的 `用户名/仓库名`。
* `clusters/kind-demo/apps/demo/deployment.yaml` 中的 `ghcr.io/CHANGE_ME/CHANGE_ME:CHANGE_ME` 改成已发布的 GHCR 镜像及其真实 commit SHA 标签。

## 本地测试

```bash
python3 -m unittest discover -s tests -v
```

## 本地构建并试跑容器

```bash
docker build -t vibe-demo:local .
docker run --rm -p 8080:8080 vibe-demo:local
```

浏览器打开 `http://localhost:8080`。健康检查地址为 `http://localhost:8080/healthz`。
