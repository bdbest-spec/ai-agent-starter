# Repository policy

`config/agent_policy.json` stores the application's local policy for repository changes. It does **not** grant GitHub permissions and cannot override GitHub authentication or platform-level confirmation.

The agent must:

1. Inspect the repository and requested scope.
2. Ask for explicit confirmation immediately before a write operation.
3. Never commit secrets.
4. Use least privilege and preserve unrelated files.
5. Report the commit and files changed.

The policy is enforced by `app/repository_policy.py` as a local validation layer. Actual authorization remains controlled by GitHub and the calling tool.
