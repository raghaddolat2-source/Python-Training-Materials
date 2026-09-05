# Security Policy

Thank you for contributing to this Python learning repository! While this project is primarily educational and not a production application, we take security and open-source best practices seriously.

## Supported Versions

Currently, only the `main` branch of this repository is actively maintained with security updates.

| Branch/Version | Supported          |
| -------------- | ------------------ |
| `main`         | :white_check_mark: |
| Older forks    | :x:                |

## Scope of Security for this Repository

Because this is a curriculum repository, "bugs" in the practice tasks (e.g., being able to withdraw negative money in the ATM Simulator) are considered **educational bugs**, not security vulnerabilities. Please report those using the standard GitHub Issue templates.

**True security vulnerabilities include:**

* Malicious code hidden inside a Pull Request.
* Vulnerable third-party dependencies introduced in a `requirements.txt` file.
* Exposed credentials, API keys, or `.env` files accidentally committed to the repository.

## Reporting a Vulnerability

**Please do not report security vulnerabilities through public GitHub issues.**

If you discover a security vulnerability, please report it privately. You can do this by:

1. Emailing the repository maintainer directly at: **`engahmadabukhuit@gmail.com`**
2. Using [GitHub's Private Vulnerability Reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing/privately-reporting-a-security-vulnerability) feature.

We will acknowledge receipt of your vulnerability report within 48 hours and strive to resolve it promptly.

## Best Practices for Students and Contributors

To maintain a secure learning environment, please adhere to the following when submitting code:

* **Never commit secrets:** Ensure your `.gitignore` is properly configured. Never commit `.env` files, API keys, or personal passwords to this repository.
* **Isolate your environment:** Always use a Virtual Environment (`venv`) when running code from this repository to protect your global system.
* **Do not execute untrusted code:** While we review Pull Requests, you should always review a script's source code before running it on your local machine.
