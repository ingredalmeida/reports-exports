## Main Branch Types

- **feature/**: Used for developing new features or functionality.
    - *Example: feature/social-login or feature/issue-123*

- **bugfix/**: Aimed at fixing bugs in the development environment or non-critical issues.
    - *Example: bugfix/mobile-layout-adjustment*

- **hotfix/**: Used for critical and urgent fixes in production. These are branched directly from main/master and merged back into it.
    - *Example: hotfix/payment-error*

- **release/**: Acts as a preparation branch for a new release. This is where final adjustments and testing happen before the code goes to production.
    - *Example: release/v1.2.0*

- **docs/**: Exclusive changes to the project documentation.
    - *Example: docs/update-readme*

- **refactor/**: Code refactoring that doesn't change functionality or fix bugs (cleaning up the code).
    - *Example: refactor/clean-up-auth-service*

- **chore/**: Used for environment configurations, tool setups, dependency updates, or stack adjustments.
    - *Example: chore/docker-config or chore/update-node-version*


## Conventional Commits Patterns

- **test**: Any creation or modification of test code, such as unit tests.

- **feat**: Development of a new feature or functionality, such as a new service, endpoint, or capability.

- **refactor**: Code refactoring that has no impact on business logic or system rules.

- **style**: Code formatting and style changes that don't affect system functionality, such as lint adjustments or indentation fixes.

- **fix**: Bug fixes that address errors causing system malfunctions.

- **chore**: Project changes that don't affect the system or test files, such as linter rule updates or .gitignore modifications.

- **docs**: Changes to project documentation, such as API documentation or README updates.

- **build**: Changes affecting the build process or external dependencies, such as npm package updates.

- **perf**: Improvements to system performance, such as optimizing algorithms or database queries.

- **ci**: Changes to CI configuration files, such as Circle CI or Travis CI setups.

- **revert**: Reverting a previous commit.