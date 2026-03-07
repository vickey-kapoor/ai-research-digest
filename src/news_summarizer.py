"""Generate ELI5 (Explain Like I'm 5) summaries for research papers."""

from openai import OpenAI


def summarize_research(research: dict, api_key: str) -> dict:
    """
    Generate a simple, jargon-free summary for a research paper.

    Summaries are written so a kid or grandma could understand them.

    Args:
        research: Research paper dictionary with title, description, source, url, authors
        api_key: OpenAI API key

    Returns:
        Research dictionary with added 'summary' field
    """
    if not api_key:
        return research

    client = OpenAI(api_key=api_key)

    authors = research.get("authors", "Unknown")

    prompt = f"""You explain AI research to someone with NO technical background - like a grandma or a kid.

Paper: {research['title']}
Authors: {authors}
Abstract: {research['description']}

Write 2-3 simple sentences explaining:
1. What did the scientists/researchers build or discover? (use simple analogies)
2. Why should a regular person care? How might this affect their life someday?

RULES:
- NO jargon (no "transformer", "architecture", "benchmark", "SOTA", "LLM", "neural network")
- Use everyday analogies (like teaching, cooking, organizing, etc.)
- Write like you're texting a friend who knows nothing about AI
- Keep it friendly and conversational

Example good summary:
"Scientists taught an AI to solve tricky math problems by breaking them into smaller steps - like how a teacher shows their work. This could help future AI assistants explain their thinking instead of just giving answers."

Now write the summary:"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7,
        )

        summary = response.choices[0].message.content.strip()
        research_with_summary = research.copy()
        research_with_summary["summary"] = summary
        return research_with_summary

    except Exception as e:
        print(f"Warning: Could not generate summary: {e}")
        return research
