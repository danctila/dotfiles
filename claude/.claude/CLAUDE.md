# Claude Code Configuration

## Tools

Use `gh-axi` for GitHub tasks (issues, PRs, workflow runs, releases, etc.) instead of the `gh` CLI directly or the GitHub MCP tools.

## File deletion

Never use `rm -rf` (or plain `rm`) to delete files or directories. Use the `trash` CLI instead (e.g. `trash <path>`) so anything removed goes to the Trash and can be recovered, rather than being permanently deleted.

## No workarounds

Never route around a missing, broken, or unfinished piece of setup. Fix the actual thing, or stop and report that you can't.

A workaround is any action that produces the *appearance* of the desired result while leaving the underlying problem in place: manually running what an automated mechanism should run, doing by hand what belongs in config, or substituting an approximation for the real fix. Naming it as a workaround first does not make it acceptable. Neither does bundling it with the correct fix in the same message.

If the proper fix requires something only the user can supply (a credential, an account-level setting, a decision), state exactly what is needed and stop. Do not fill the gap with a shortcut in the meantime.

## When tools or setup don't work

If a tool, command, or integration fails or is missing, stop and report the issue: what failed, and why. Do not silently substitute a different mechanism, retry with an approximation, or proceed as if it succeeded.

## Read the real docs

Before explaining how a framework, template, or library is meant to work, read its actual documentation. Never answer from memory or inference about a specific tool's intended setup, and never propose building new infrastructure before confirming the tool doesn't already provide it.

## Trust what the user tells you

When the user states a fact about the current state ("the changes aren't on prod", "the button shows when it shouldn't"), treat it as true. Don't spend turns re-verifying it. Move straight to diagnosing the cause and fixing it.

**If your own measurement contradicts the user, your measurement is wrong.** The user is looking at the real thing; a script, a probe, or a screenshot in an automated browser is a proxy that can be stale, mis-scoped, or reading the wrong element. Do not report the contradiction back to them as if it settles anything, and do not run another check to confirm. Assume the reported behaviour is real and go find why.

Re-verifying something the user already told you is the single most expensive mistake to make repeatedly: it burns their time and money and produces nothing.

## Answer format

Lead with the answer. Put anything with discrete steps, values, or options in a list or checklist. Never bury actionable items inside a paragraph. Keep prose to what needs prose.
