"""Generate AI summaries for news articles."""

from openai import OpenAI


def summarize_article(article: dict, api_key: str) -> dict:
    """
    Generate a "Why it matters" summary for an article using OpenAI.

    Args:
        article: Article dictionary with title, description, source, url
        api_key: OpenAI API key

    Returns:
        Article dictionary with added 'summary' field
    """
    if not api_key:
        return article

    client = OpenAI(api_key=api_key)

    prompt = f"""You are an AI news analyst. Generate a brief "Why it matters" summary for this news article.

Title: {article['title']}
Source: {article['source']}
Description: {article['description']}

Write 2-3 sentences explaining:
1. The significance of this news
2. How it might impact the AI industry, businesses, or everyday users

Be concise and insightful. Do not start with "Why it matters:" - just provide the summary directly."""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7,
        )

        summary = response.choices[0].message.content.strip()
        article_with_summary = article.copy()
        article_with_summary["summary"] = summary
        return article_with_summary

    except Exception as e:
        print(f"Warning: Could not generate summary: {e}")
        return article
