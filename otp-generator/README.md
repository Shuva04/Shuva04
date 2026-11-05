# Secure OTP Generator

A command-line numeric one-time-code generator using Python's cryptographically secure `secrets` module.

## Run
```bash
python otp_generator.py
```

## Security
- Uses `secrets`, not the predictable `random` module.
- Defaults to a six-digit code.
- This is a simple code generator, not a complete authentication system. Do not use it as a production TOTP service without expiry, replay prevention, secure delivery and rate limiting.

## Suggested caption
Developed a Python OTP generator using the secrets module to create cryptographically secure numeric codes, with configurable code length and input validation.