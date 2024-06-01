<h1 align="center">Mail Scrapper Telegram Bot</h1>

<p align="center">
  <a href="https://github.com/bisnuray/Mail-Scrapper/stargazers"><img src="https://img.shields.io/github/stars/bisnuray/Mail-Scrapper?color=blue&style=flat" alt="GitHub Repo stars"></a>
  <a href="https://github.com/bisnuray/Mail-Scrapper/issues"><img src="https://img.shields.io/github/issues/bisnuray/Mail-Scrapper" alt="GitHub issues"></a>
  <a href="https://github.com/bisnuray/Mail-Scrapper/pulls"><img src="https://img.shields.io/github/issues-pr/bisnuray/Mail-Scrapper" alt="GitHub pull requests"></a>
  <a href="https://github.com/bisnuray/Mail-Scrapper/graphs/contributors"><img src="https://img.shields.io/github/contributors/bisnuray/Mail-Scrapper?style=flat" alt="GitHub contributors"></a>
  <a href="https://github.com/bisnuray/Mail-Scrapper/network/members"><img src="https://img.shields.io/github/forks/bisnuray/Mail-Scrapper?style=flat" alt="GitHub forks"></a>
</p>

<p align="center">
  <em>Mail Scrapper an Advance Telegram Bot Script to scrape email and password combinations from specified Telegram groups and channels</em>
</p>
<hr>

## Features

- Scrape email and password combinations from Private/Public Telegram Groups/channels.
- Supported Format Group/Channel username/link
- Scraping Speed Super Fester.

## Requirements

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher.
- `pyrogram` and `aiogram==2.6` libraries.

## Installation

To install Squid and necessary utilities, run the following commands:

```bash
pip install pyrogram
pip install aiogram==2.6
```

## Configuration

1. Replace the placeholders in the script with your actual values:

    - `api_id` and `api_hash`: Obtain these from [my.telegram.org](https://my.telegram.org).
    - `phone_number`: Your phone number registered with Telegram.
    - `BOT_TOKEN`: Your Telegram bot token from [BotFather](https://t.me/BotFather).
    - `YOUR_ADMIN_USER_ID`: Your Telegram user ID for authorization.

## Deploy the Bot

```sh
git clone https://github.com/bisnuray/Mail-Scrapper
cd Mail-Scrapper
python3 mailscr.py
```

## Usage

1. Interact with your bot on Telegram using the `/scrmail` command:

    ```plaintext
    /scrmail <channel_identifier> <amount>
    ```

    - `<channel_identifier>`: The username or invite link of the channel.
    - `<amount>`: The number of email and password combinations to collect.


✨ **Note**: Fork this repo, & Star ☀️ the repo if you liked it. and Share this repo with Proper Credit

## Author

- Name: Bisnu Ray
- Telegram: [@itsSmartDev](https://t.me/itsSmartDev)

Feel free to reach out if you have any questions or feedback.
