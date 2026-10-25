#!/bin/zsh
# Установка слэш-команд Job Hunt в OpenClaw.
#
# Вариант без установки: если фреймворк распакован В КОРЕНЬ воркспейса
# (т.е. его skills/ — это <workspace>/skills/), команды регистрируются сами.
# Этот скрипт нужен, когда фреймворк лежит в подпапке: он копирует skills/
# в воркспейс одной командой.
#
# Использование: ./install.sh [путь к воркспейсу]
set -euo pipefail

SRC="$(cd "$(dirname "$0")" && pwd)"
DEST="${1:-${OPENCLAW_WORKSPACE:-$HOME/.openclaw/workspace}}"

[ -d "$DEST" ] || { echo "✗ не найден воркспейс: $DEST (передай путь: ./install.sh /путь/к/воркспейсу)"; exit 1; }
[ -d "$SRC/skills" ] || { echo "✗ в $SRC нет папки skills/"; exit 1; }

mkdir -p "$DEST/skills"
for s in "$SRC"/skills/*/; do
  name="$(basename "$s")"
  mkdir -p "$DEST/skills/$name"
  cp -R "$s"/. "$DEST/skills/$name/"
done

echo "✓ команды установлены в $DEST/skills:"
echo "    /init-job-hunt  /vacancy-flow  /company-flow  /job-status"
echo "  проверка: openclaw skills list | grep -i 'init\\|vacancy-flow\\|company-flow\\|job-status'"
