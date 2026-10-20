# Branch and clone migration

[Repository home](../README.md) · [Branch roles](BRANCHES.md) · [Project catalog](CATALOG.md)

The default branch is `main`. Topic branches now have stable names: recommended
branches use `research/<topic>` and earlier source checkpoints use
`archive/<topic>-source`. All previous heads and research snapshots remain
accessible through their full commit IDs.

## Old-to-new names

| Old name | New name |
| --- | --- |
| `codex/certified-roots-2026-10-15` | [`research/certified-roots`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/certified-roots) |
| `codex/contest-library-2026-10-13` | [`research/contest-library`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/contest-library) |
| `codex/critical-points-2026-10-15` | [`research/critical-points`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/critical-points) |
| `codex/evidence-hardening-2026-10-13` | [`archive/evidence-hardening-source`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/archive/evidence-hardening-source) |
| `codex/hadamard-study-2026-10-15` | [`research/hadamard-study`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/hadamard-study) |
| `codex/holomorphic-anosov-review-2026-10-16` | [`research/holomorphic-anosov-review`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/holomorphic-anosov-review) |
| `codex/integral-examples-2026-10-15` | [`research/integral-examples`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/integral-examples) |
| `codex/lp-certificates-2026-10-13` | [`archive/lp-certificates-source`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/archive/lp-certificates-source) |
| `codex/lp-paper-2026-10-13` | [`research/lp-paper`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/lp-paper) |
| `codex/lp-sparse-discovery-2026-10-13` | [`archive/lp-sparse-discovery-source`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/archive/lp-sparse-discovery-source) |
| `codex/research-2026-10-11` | [`research/integrated`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/integrated) |
| `codex/research-map-2026-10-13` | [`research/research-map`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/research-map) |
| `codex/tangent-limit` | [`research/tangent-limit`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/research/tangent-limit) |
| `codex/transport-sharpness-2026-10-13` | [`archive/transport-sharpness-source`](https://github.com/Drsunflowerherbert/Codex-for-Math/tree/archive/transport-sharpness-source) |

Also available as [JSON](branch-map.json).

## Existing links

The rename uses GitHub's supported mechanism. Old GitHub browser `tree` and
`blob` URLs redirect to the renamed branch. The former tangent catalog paths
remain as compatibility pointer pages on `research/tangent-limit`, leading to
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
git branch -m codex/tangent-limit research/tangent-limit
git branch --set-upstream-to=origin/research/tangent-limit research/tangent-limit
```

Repeat with the relevant row from the table for your other local branches.
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
small. The original tangent tree remains byte-identical on its renamed topic
branch; every other project stays on its own renamed branch. No topic history
is rewritten and no unrelated projects are merged. Topic follow-up commits
edit root/navigation documentation only.
