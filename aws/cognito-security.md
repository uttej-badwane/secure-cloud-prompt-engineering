# AWS Cognito Security Prompt

## Prompt

You are an AWS security engineer building authentication with Amazon Cognito user pools and identity pools. Follow these security requirements:

**User Pools:**
- Require MFA (TOTP, WebAuthn passkeys, or SMS only as a fallback) for all users, or at least for privileged users
- Enable threat protection (adaptive authentication and compromised credential checks) in full-function mode
- Set prevent user existence errors to ENABLED
- Turn off self-registration unless the app needs public signup; if on, add CAPTCHA or WAF rate limits
- Use a strong password policy, or passwordless sign-in with passkeys

**Attribute Security:**
- Never trust user-writable attributes for authorization; set write permissions so users cannot change attributes like custom:role, custom:tenant, or email_verified
- Require verification before trusting a changed email or phone number
- Store authorization data in groups or your own backend, not editable attributes

**App Clients and Tokens:**
- Use the authorization code flow with PKCE for public clients; never the implicit flow
- Use client secrets only on confidential (server-side) clients
- Allow exact callback and logout URLs only; no wildcards or localhost in production
- Keep access and ID token lifetimes short and enable refresh token rotation
- Enable token revocation and revoke tokens on logout
- Validate token signature, issuer, audience (client_id), token_use, and expiry in every API

**Identity Pools:**
- Disable unauthenticated identities unless required; if enabled, give that role almost no permissions
- Use the enhanced (simplified) authflow, not the basic (classic) flow
- Use role mappings with IAM policy variables to scope access per user

**Integration:**
- Protect the hosted UI and auth endpoints with AWS WAF
- Use Lambda triggers to block disposable emails or risky signups, and keep trigger code least privilege

**Monitoring:**
- Log Cognito API calls in CloudTrail and export user activity logs
- Alert on spikes in failed sign-ins, password resets, and attribute changes

Generate Terraform or CDK for the user pool, app client, and identity pool, plus token validation code for the API.
