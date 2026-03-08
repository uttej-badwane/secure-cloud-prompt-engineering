#!/usr/bin/env bash
# install.sh — Install secure-cloud-prompt-engineering into Claude Code
#
# Usage:
#   ./install.sh            # Install everything
#   ./install.sh --skill    # Install only the IaC security review skill
#   ./install.sh --hooks    # Install only the session hooks
#   ./install.sh --dry-run  # Show what would be installed without copying

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_DIR="${HOME}/.claude"

INSTALL_SKILL=false
INSTALL_HOOKS=false
INSTALL_COMMANDS=false
INSTALL_AGENTS=false
INSTALL_RULES=false
INSTALL_ALL=true
DRY_RUN=false

# Parse arguments
for arg in "$@"; do
  case $arg in
    --skill)    INSTALL_SKILL=true;    INSTALL_ALL=false ;;
    --hooks)    INSTALL_HOOKS=true;    INSTALL_ALL=false ;;
    --commands) INSTALL_COMMANDS=true; INSTALL_ALL=false ;;
    --agents)   INSTALL_AGENTS=true;   INSTALL_ALL=false ;;
    --rules)    INSTALL_RULES=true;    INSTALL_ALL=false ;;
    --dry-run)  DRY_RUN=true ;;
    --help|-h)
      echo "Usage: ./install.sh [--skill] [--hooks] [--commands] [--agents] [--rules] [--dry-run]"
      echo ""
      echo "Options:"
      echo "  (no args)   Install everything"
      echo "  --skill     Install the IaC security review skill to ~/.claude/skills/"
      echo "  --hooks     Install session hooks to ~/.claude/hooks/"
      echo "  --commands  Install slash commands to ~/.claude/commands/"
      echo "  --agents    Install agent definitions to ~/.claude/agents/"
      echo "  --rules     Install always-follow rules to ~/.claude/rules/"
      echo "  --dry-run   Show what would be installed without copying files"
      exit 0
      ;;
    *)
      echo "Unknown argument: $arg. Use --help for usage." >&2
      exit 1
      ;;
  esac
done

if $INSTALL_ALL; then
  INSTALL_SKILL=true
  INSTALL_HOOKS=true
  INSTALL_COMMANDS=true
  INSTALL_AGENTS=true
  INSTALL_RULES=true
fi

log() { echo "  $1"; }
copy() {
  local src="$1" dst="$2"
  if $DRY_RUN; then
    log "[dry-run] cp -r $src -> $dst"
  else
    mkdir -p "$(dirname "$dst")"
    cp -r "$src" "$dst"
    log "Installed: $dst"
  fi
}

echo ""
echo "=== Secure Cloud Prompt Engineering — Installer ==="
echo ""

# --- Skill ---
if $INSTALL_SKILL; then
  echo "Installing IaC Security Review skill..."
  SKILL_SRC="${REPO_DIR}/skills/iac-security-review"
  SKILL_DST="${CLAUDE_DIR}/skills/iac-security-review"
  if [ -d "$SKILL_DST" ] && ! $DRY_RUN; then
    echo "  Existing skill found at ${SKILL_DST} — updating..."
    rm -rf "$SKILL_DST"
  fi
  copy "$SKILL_SRC" "$SKILL_DST"
  echo ""
fi

# --- Hooks ---
if $INSTALL_HOOKS; then
  echo "Installing session hooks..."
  HOOKS_SRC="${REPO_DIR}/hooks"
  HOOKS_DST="${CLAUDE_DIR}/hooks"
  for file in "${HOOKS_SRC}"/*.js "${HOOKS_SRC}/hooks.json"; do
    [ -f "$file" ] || continue
    copy "$file" "${HOOKS_DST}/$(basename "$file")"
  done
  echo ""
fi

# --- Commands ---
if $INSTALL_COMMANDS; then
  echo "Installing slash commands..."
  COMMANDS_SRC="${REPO_DIR}/commands"
  COMMANDS_DST="${CLAUDE_DIR}/commands"
  for file in "${COMMANDS_SRC}"/*.md; do
    [ -f "$file" ] || continue
    copy "$file" "${COMMANDS_DST}/$(basename "$file")"
  done
  echo ""
fi

# --- Agents ---
if $INSTALL_AGENTS; then
  echo "Installing agent definitions..."
  AGENTS_SRC="${REPO_DIR}/agents"
  AGENTS_DST="${CLAUDE_DIR}/agents"
  for file in "${AGENTS_SRC}"/*.md; do
    [ -f "$file" ] || continue
    copy "$file" "${AGENTS_DST}/$(basename "$file")"
  done
  echo ""
fi

# --- Rules ---
if $INSTALL_RULES; then
  echo "Installing always-follow rules..."
  RULES_SRC="${REPO_DIR}/rules"
  RULES_DST="${CLAUDE_DIR}/rules"
  for file in "${RULES_SRC}"/*.md; do
    [ -f "$file" ] || continue
    copy "$file" "${RULES_DST}/$(basename "$file")"
  done
  echo ""
fi

if $DRY_RUN; then
  echo "=== Dry run complete. No files were copied. ==="
else
  echo "=== Installation complete! ==="
  echo ""
  echo "What was installed to ${CLAUDE_DIR}/:"
  $INSTALL_SKILL    && echo "  skills/iac-security-review/  — IaC security review skill"
  $INSTALL_COMMANDS && echo "  commands/                    — slash commands (/iac-security-review, /compliance-check, ...)"
  $INSTALL_AGENTS   && echo "  agents/                      — security-reviewer, compliance-mapper, report-generator"
  $INSTALL_RULES    && echo "  rules/                       — security-first, iac-standards"
  $INSTALL_HOOKS    && echo "  hooks/                       — session-start, session-stop, pre-bash"
  echo ""
  echo "Try it out:"
  echo "  Open Claude Code in any project with IaC files and run:"
  echo "  > /iac-security-review"
fi
