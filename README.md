# AI Research WhatsApp Digest

Get the latest AI research delivered to your WhatsApp daily - explained simply, like talking to a friend.

## Features

- Fetches AI research from multiple sources (arXiv, Hugging Face, Papers With Code, AI lab blogs)
- Focuses on **AI Agents & Reasoning** research
- Uses AI to select the most impactful paper
- Generates **ELI5 summaries** (simple explanations anyone can understand)
- Sends to WhatsApp via Twilio
- Runs automatically via GitHub Actions (10:00 AM CST daily)

## Example Message

```
*Daily AI Research*

*Training Language Models to Reason Step by Step*
_Smith et al._

You know how it's easier to solve a math problem when you
write out each step? Researchers taught AI to do the same
thing - break down hard problems into smaller pieces. This
makes AI better at explaining its thinking, which could
help future assistants tutor kids or help you understand
complex topics.

https://arxiv.org/abs/...
_Source: arXiv_
```

## Setup

### 1. Get API Keys

**Twilio:**
- Sign up at [twilio.com](https://www.twilio.com/)
- Get Account SID and Auth Token from Console
- Set up WhatsApp Sandbox: [Twilio WhatsApp Sandbox](https://www.twilio.com/console/sms/whatsapp/sandbox)
- Send "join <sandbox-code>" from your WhatsApp to the Twilio number

**OpenAI:**
- Sign up at [platform.openai.com](https://platform.openai.com/)
- Create an API key

### 2. Configure GitHub Secrets

Go to your repository Settings > Secrets and variables > Actions, and add:

| Secret | Description |
|--------|-------------|
| `TWILIO_ACCOUNT_SID` | Twilio Account SID |
| `TWILIO_AUTH_TOKEN` | Twilio Auth Token |
| `TWILIO_WHATSAPP_NUMBER` | Twilio WhatsApp number (e.g., `whatsapp:+14155238886`) |
| `YOUR_WHATSAPP_NUMBER` | Your WhatsApp number (e.g., `whatsapp:+1234567890`) |
| `OPENAI_API_KEY` | OpenAI API key (required for ranking & summaries) |

### 3. Adjust Schedule (Optional)

Edit `.github/workflows/daily-news.yml` to change the time:

```yaml
schedule:
  - cron: '0 16 * * *'  # 10:00 AM CST (16:00 UTC) daily
```

Use [crontab.guru](https://crontab.guru/) to customize.

## Local Development

```bash
# Clone the repository
git clone https://github.com/vickey-kapoor/ai-research-whatsapp-digest.git
cd ai-research-whatsapp-digest

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file with your keys
echo "TWILIO_ACCOUNT_SID=your_sid" >> .env
echo "TWILIO_AUTH_TOKEN=your_token" >> .env
echo "TWILIO_WHATSAPP_NUMBER=whatsapp:+14155238886" >> .env
echo "YOUR_WHATSAPP_NUMBER=whatsapp:+1234567890" >> .env
echo "OPENAI_API_KEY=your_openai_key" >> .env

# Run
python main.py
```

## Project Structure

```
ai-research-whatsapp-digest/
├── .github/workflows/
│   └── daily-news.yml        # GitHub Actions (10 AM CST daily)
├── src/
│   ├── research_fetcher.py   # Aggregates research from all sources
│   ├── news_ranker.py        # AI-powered research ranking
│   ├── news_summarizer.py    # ELI5 summary generator
│   ├── whatsapp_sender.py    # Twilio WhatsApp integration
│   └── fetchers/
│       ├── arxiv_fetcher.py      # arXiv API
│       ├── huggingface_fetcher.py # Hugging Face Daily Papers
│       ├── pwc_fetcher.py        # Papers With Code
│       └── blog_fetcher.py       # AI lab blogs (Google, DeepMind, Meta)
├── main.py                   # Entry point
├── requirements.txt
├── CLAUDE.md                 # Development reference
└── README.md
```

## Research Sources

| Source | What it fetches |
|--------|-----------------|
| arXiv | Papers from cs.AI, cs.LG, cs.CL, cs.MA |
| Hugging Face | Daily trending papers |
| Papers With Code | Latest ML papers |
| AI Lab Blogs | Google AI, DeepMind, Meta AI |

## License

MIT
