---
description: Security, privacy, data handling, and support information for Quandora users.
content_status: handoff
content_owner: researcher
---

# Security, Privacy And Support

Quandora uses browser OAuth through the host-managed agent connection. Do not
paste exchange keys, API keys, bearer tokens, authorization codes, access or
refresh tokens, passwords, or other credentials into an agent prompt.

## Verified Connection Facts

* The host stores and refreshes the Quandora connection; the agent should not
  inspect or copy credentials.
* Access tokens are valid for seven days and rotating refresh tokens for 30
  days, subject to account and authorization state.
* An older authorization does not gain newly granted Paper permissions through
  token refresh alone. Complete fresh browser consent when the safe connection
  response requires it.
* Result Bundle downloads use short-lived, single-use transfer URLs. The agent
  consumes them immediately and must not print, store, or reconstruct them.
* Factor and Strategy Analysis use owner-scoped server evidence and do not need
  local archives or credentials.

Reviewed policies for data retention, research-data handling, account deletion,
service support, and incident reporting require separate owner approval. This
page does not invent those commitments.

For installation-specific authorization guidance, including what to do if a
tool asks for an API key, see the
[Installation Guide](../getting-started/installation-guide.md).
