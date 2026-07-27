# GitBook Localization Runbook

## Current State

- Root Markdown remains a temporary mirror of `en/` so the existing English
  Space continues to publish during migration.
- `en/` is the future English Space project directory.
- `zh/` is the future Simplified Chinese Space project directory.
- Merging repository content does not configure GitBook Spaces or variants.

## Chinese Writing Style

- Write direct, natural product language for users.
- State the intended point positively. Avoid constructions that introduce an
  unnecessary rejection before the message, including “不是……而是……” and
  “并非……而是……”.
- Prefer short sentences and familiar verbs over literal translations of
  English abstractions.
- Preserve commands, code, paths, identifiers, metric names, and URLs exactly.

## Configure GitBook

After the bilingual repository PR is merged:

1. Confirm `make verify` passes on `main`.
2. In the existing English Space, disable Git Sync before changing its project
   directory.
3. Reconnect the same repository and branch with project directory `en`.
4. Import from GitHub to GitBook and confirm the English navigation and known
   page URLs remain correct.
5. Create a separate Simplified Chinese Space.
6. Connect it to the same repository and branch with project directory `zh`.
7. Import from GitHub to GitBook and verify Chinese navigation, assets, links,
   commands, and the visible notices on pending translations.
8. Add the Chinese Space to the published docs site as a Chinese language
   variant, keeping English as the default language.
9. Verify the language selector on desktop and mobile, search in both
   languages, the sign-in link, and representative deep links.

## Rollback

If the English Space is empty or its routes are incorrect, disable its Git Sync
and reconnect it to the repository root. Remove the Chinese language variant
from the published site if it routes users to incomplete or incorrect content.
Repository content can remain in place while the platform configuration is
corrected.

## Cleanup

After both Spaces and the language selector have been validated, create a
follow-up issue and PR to:

- remove the temporary root Markdown and root `.gitbook/assets` mirror;
- remove `compatibility` and `compatibility_mirror` from `docs-policy.json`;
- simplify CI to validate only `en/` and `zh/`;
- add redirects for any URL changed during the migration.
