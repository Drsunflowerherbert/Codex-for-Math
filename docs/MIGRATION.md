# Branch and clone migration

[Repository home](../README.md) · [Branch roles](BRANCHES.md) · [Project catalog](CATALOG.md)

The directory is on `main`; the default branch is still `codex/tangent-limit`
because the integration's default-change request was denied by GitHub. Thirteen
topic branches now have stable names: recommended
branches use `research/<topic>` and earlier source checkpoints use
`archive/<topic>-source`. All previous heads and research snapshots remain
accessible through their full commit IDs.

## Old-to-new names

| Old name | Current name | Status |
| --- | --- | --- |
| `codex/certified-roots-2026-10-15` | [`research/certified-roots`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/certified-roots) | Renamed |
| `codex/contest-library-2026-10-13` | [`research/contest-library`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/contest-library) | Renamed |
| `codex/critical-points-2026-10-15` | [`research/critical-points`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/critical-points) | Renamed |
| `codex/evidence-hardening-2026-10-13` | [`archive/evidence-hardening-source`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/archive/evidence-hardening-source) | Renamed |
| `codex/hadamard-study-2026-10-15` | [`research/hadamard-study`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/hadamard-study) | Renamed |
| `codex/holomorphic-anosov-review-2026-10-16` | [`research/holomorphic-anosov-review`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/holomorphic-anosov-review) | Renamed |
| `codex/integral-examples-2026-10-15` | [`research/integral-examples`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/integral-examples) | Renamed |
| `codex/lp-certificates-2026-10-13` | [`archive/lp-certificates-source`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/archive/lp-certificates-source) | Renamed |
| `codex/lp-paper-2026-10-13` | [`research/lp-paper`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/lp-paper) | Renamed |
| `codex/lp-sparse-discovery-2026-10-13` | [`archive/lp-sparse-discovery-source`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/archive/lp-sparse-discovery-source) | Renamed |
| `codex/research-2026-10-11` | [`research/integrated`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/integrated) | Renamed |
| `codex/research-map-2026-10-13` | [`research/research-map`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/research-map) | Renamed |
| `codex/tangent-limit` | [`codex/tangent-limit`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/codex/tangent-limit) | Rename to research/tangent-limit pending |
| `codex/transport-sharpness-2026-10-13` | [`archive/transport-sharpness-source`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/archive/transport-sharpness-source) | Renamed |

Also available as [JSON](branch-map.json).

## Existing links

The 13 completed renames use GitHub's supported mechanism. Old GitHub browser `tree` and
`blob` URLs redirect to the renamed branch. The tangent catalog paths
remain as compatibility pointer pages on `codex/tangent-limit`, leading to
the current catalog on main. Newly maintained navigation uses current names.

Full commit-pinned research links are unchanged. Historical project prose may
still name the branch used when it was written; this table resolves it without
altering evidence-covered research documents.

GitHub does not redirect raw file URLs or Git fetch/pull requests for an old
branch name. Update bookmarks and consumers that use those names. See
[GitHub's branch-rename documentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-branches-in-your-repository/renaming-a-branch).

## Existing local clones

First inspect the remote's fetch mapping:

```sh
git config --get-all remote.origin.fetch
```

If it was restricted to an old branch name, update that mapping **before**
setting upstreams or creating tracking branches. Git needs a configured mapping
for the new remote branches, not just a one-off fetch. For an ordinary clone
with an obsolete single-branch mapping, use:

```sh
git config --replace-all remote.origin.fetch '+refs/heads/*:refs/remotes/origin/*'
```

If you intentionally maintain custom fetch rules, preserve those rules and add
equivalent mappings for `main` and the renamed branches you use instead of
replacing them wholesale. If your existing mapping already covers all branches,
no configuration change is needed.

Then fetch and refresh the remote default:

```sh
git fetch origin
git remote set-head origin -a
```

If you already have a local topic branch, rename it and update its upstream.
For example, when neither destination name already exists locally:

```sh
git branch -m codex/integral-examples-2026-10-15 research/integral-examples
git branch --set-upstream-to=origin/research/integral-examples research/integral-examples
```

Repeat with completed rows for your other local branches. Keep the tangent
branch tracking `origin/codex/tangent-limit` until its pending rename exists.
Commit or otherwise preserve local edits before switching. To create a local
directory branch when no local `main` exists:

```sh
git switch --track origin/main
```

Do not rename an existing topic branch to main: main has its own directory
commit, while the topic branch preserves the project tree. Stale local tracking
refs can be pruned later after you have checked the new names and upstreams.

## Preservation boundary

The new main directory is a connected single-parent child of the previous
default commit. Its current tree omits research files to keep the homepage
small. The original tangent tree remains byte-identical on `codex/tangent-limit`; every other project stays on its own renamed branch. No topic history
is rewritten and no unrelated projects are merged. Topic follow-up commits
edit root/navigation documentation only.

## Remaining administration actions

Completed: create the connected five-file main directory and rename 13 ordinary
branches, preserving their heads and research contents.

Denied by GitHub: `PATCH /repos/Drsunflowerherbert/Codex-for-Math` with
`default_branch=main` returned HTTP 403, `Resource not accessible by integration`.
Main was created successfully, but that settings request did not execute.
The authenticated account is a repository administrator; the integration's
authorization does not permit this settings action. No new credentials or
permission expansion was attempted, and the denied action was not retried.

A repository administrator with settings access still needs to:

1. Select the existing `main` branch as the repository default in GitHub.
2. Use GitHub's supported rename mechanism to rename `codex/tangent-limit` to
   `research/tangent-limit` after it is no longer the default.
3. Update this pending row and its moving tangent links, then refresh local
   remote-default and upstream tracking as described above.

The second rename was left unattempted because default-branch renaming requires
administration permission too. All current navigation uses the existing tangent
name so it remains usable while these actions are pending.
