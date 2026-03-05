#!/bin/bash
# 自动备份脚本 - 每小时检查并备份workspace更改

set -e

# 工作区目录
WORKSPACE_DIR="/root/.openclaw/workspace-researcher"
cd "$WORKSPACE_DIR"

echo "=========================================="
echo "自动备份脚本 - $(date '+%Y-%m-%d %H:%M:%S')"
echo "=========================================="

# 检查git状态
echo "检查git状态..."
git status

# 检查是否有更改
if git diff --quiet && git diff --cached --quiet; then
    echo "✅ 没有更改，跳过备份"
    exit 0
fi

echo "📝 发现更改，开始备份..."

# 添加所有更改
git add .

# 生成提交信息
COMMIT_MSG="自动备份 - $(date '+%Y-%m-%d %H:%M:%S')"

# 提交
echo "提交更改: $COMMIT_MSG"
git commit -m "$COMMIT_MSG"

# 推送到GitHub
echo "推送到GitHub..."
git push

echo "✅ 备份完成！"
echo "=========================================="
