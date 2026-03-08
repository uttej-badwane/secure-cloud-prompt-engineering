#!/usr/bin/env node
/**
 * PreToolUse (Bash) hook — warns before running potentially destructive commands
 * in the context of an IaC security review workflow.
 *
 * This hook reads the command from stdin (JSON: { tool_input: { command } })
 * and can block execution by exiting with a non-zero code.
 */

let input = '';
process.stdin.on('data', chunk => { input += chunk; });
process.stdin.on('end', () => {
  let toolInput;
  try {
    toolInput = JSON.parse(input);
  } catch {
    process.exit(0); // allow if we can't parse
  }

  const command = (toolInput?.tool_input?.command || '').trim();

  // Warn on terraform apply/destroy without review
  const dangerous = [
    /terraform\s+apply/,
    /terraform\s+destroy/,
    /kubectl\s+delete/,
    /aws\s+.*\s+delete/,
    /rm\s+-rf/,
  ];

  for (const pattern of dangerous) {
    if (pattern.test(command)) {
      // Output warning to stderr (visible to user, not to Claude)
      process.stderr.write(
        `[security-hook] Potentially destructive command detected: ${command}\n` +
        `[security-hook] Ensure IaC security review is complete before applying changes.\n`
      );
      break;
    }
  }

  process.exit(0); // always allow — this is a warning hook, not a blocking hook
});
