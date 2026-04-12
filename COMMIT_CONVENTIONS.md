# Commit and Branch Naming Conventions

This document outlines the conventions for writing commit messages and naming branches in this project. Following these conventions ensures consistency, improves readability, and facilitates automated changelog generation.

## Commit Messages

We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification.

### Format
```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

### Commit Types
| Type | Description | Example |
|------|-------------|---------|
| `feat` | A new feature | `feat(auth): add OAuth2 support` |
| `fix` | A bug fix | `fix(api): handle 404 errors properly` |
| `docs` | Documentation changes | `docs(readme): update installation instructions` |
| `style` | Code style changes (formatting, missing semicolons, etc.) | `style: format code with ruff` |
| `refactor` | Code refactoring without changing functionality | `refactor(utils): optimize parsing function` |
| `perf` | Performance improvements | `perf(cache): implement LRU caching` |
| `test` | Adding or updating tests | `test(validator): add YAML validation tests` |
| `build` | Build system or dependency changes | `build(deps): update requests to v2.32` |
| `ci` | CI/CD configuration changes | `ci: add GitHub Actions workflow` |
| `chore` | Routine tasks, maintenance | `chore: update .gitignore` |
| `revert` | Revert a previous commit | `revert: revert faulty auth implementation` |

### Additional Types (Optional)
| Type | Description |
|------|-------------|
| `init` | Project initialization | `init: setup project structure` |
| `add` | Add new files or features | `add(api): create user endpoints` |
| `update` | Update existing functionality | `update(validator): improve error messages` |
| `remove` | Remove files or features | `remove: delete deprecated module` |
| `move` | Move or rename files | `move: relocate utils to shared directory` |
| `improve` | General improvements | `improve(ui): enhance button styling` |
| `security` | Security-related changes | `security: fix XSS vulnerability` |
| `hotfix` | Critical production fix | `hotfix: patch authentication bypass` |

### Scope
The scope is optional and should be a short description of the module or component affected:
- `auth` - Authentication module
- `api` - API endpoints
- `ui` - User interface
- `db` - Database related
- `docs` - Documentation
- `test` - Testing
- `ci` - Continuous Integration
- `build` - Build system

### Description
- Use imperative mood: "add" not "added" or "adds"
- Keep it short (50-72 characters recommended)
- No period at the end
- Lowercase (except for proper nouns)

### Body (Optional)
- Provide more detailed explanation
- Wrap at 72 characters
- Explain what and why, not how

### Footer (Optional)
- Reference issue numbers: `Fixes #123`
- Breaking changes: `BREAKING CHANGE: API response format changed`

## Examples

### Simple commit
```
feat(auth): implement JWT authentication
```

### Commit with scope
```
fix(api): correct status code for empty responses
```

### Commit with body
```
refactor(validator): simplify YAML parsing logic

The previous implementation had redundant checks that made the code hard to maintain. This refactor removes duplicate validation and improves error messages.
```

### Commit with footer
```
fix: resolve memory leak in request handler

Fixes #42
BREAKING CHANGE: Request timeout configuration moved to settings
```

## Branch Naming

### Format
```
<type>/<description>
```

### Branch Types
| Type | Description | Example |
|------|-------------|---------|
| `feature` | New feature development | `feature/user-profile` |
| `bugfix` | Bug fix | `bugfix/login-error` |
| `hotfix` | Urgent production fix | `hotfix/security-patch` |
| `release` | Release preparation | `release/v1.2.0` |
| `docs` | Documentation updates | `docs/api-reference` |
| `refactor` | Code refactoring | `refactor/auth-module` |
| `test` | Test-related work | `test/coverage-improvement` |
| `chore` | Maintenance tasks | `chore/deps-update` |

### Description Guidelines
- Use kebab-case (lowercase with hyphens)
- Be descriptive but concise
- Reference issue numbers if applicable
- Examples:
  - `feature/add-dark-mode`
  - `bugfix/fix-404-on-invalid-route`
  - `hotfix/patch-sql-injection`
  - `docs/update-api-examples`

### Branch Naming Examples
```
feature/oauth2-integration
bugfix/correct-response-format
hotfix/fix-authentication-bypass
release/v2.0.0
docs/add-contributing-guide
refactor/optimize-database-queries
test/add-integration-tests
```

## Best Practices

### For Commits
1. **One logical change per commit** - Don't mix unrelated changes
2. **Write clear, descriptive messages** - Future you will thank you
3. **Use the imperative mood** - "Fix bug" not "Fixed bug"
4. **Reference issues** - Use `Fixes #123` or `Closes #456`
5. **Keep commits small** - Easier to review and revert if needed
6. **Test before committing** - Ensure your changes work

### For Branches
1. **Create branches for features/fixes** - Don't work directly on main
2. **Keep branches short-lived** - Merge quickly to avoid conflicts
3. **Delete merged branches** - Keep repository clean
4. **Sync with main regularly** - Rebase to avoid big merge conflicts
5. **Use descriptive names** - Clear what the branch is for

## Tools

### Commit Linting
Consider using tools to enforce these conventions:
- [commitlint](https://commitlint.js.org/) - Lint commit messages
- [husky](https://typicode.github.io/husky/) - Git hooks
- [conventional-changelog](https://github.com/conventional-changelog/conventional-changelog) - Generate changelogs

### Branch Protection
Configure branch protection rules in your repository:
- Require pull request reviews
- Require status checks to pass
- Require linear history
- Prevent force pushes to main

## References
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Git Branching Strategies](https://nvie.com/posts/a-successful-git-branching-model/)
- [Git Commit Message Guidelines](https://chris.beams.io/posts/git-commit/)