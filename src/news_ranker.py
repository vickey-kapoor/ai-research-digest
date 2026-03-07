"""Rank AI research by importance using OpenAI."""

from openai import OpenAI


def rank_research(research: list[dict], api_key: str) -> dict:
    """
    Use OpenAI to select the most important AI research paper.

    Focuses on AI Agents and Reasoning research.

    Args:
        research: List of research paper dictionaries
        api_key: OpenAI API key

    Returns:
        The most important research paper
    """
    if not research:
        raise ValueError("No research to rank")

    if len(research) == 1:
        return research[0]

    client = OpenAI(api_key=api_key)

    # Prepare research summary for the prompt
    research_text = "\n\n".join(
        f"[{i+1}] Title: {r['title']}\nSource: {r['source']}\nAuthors: {r.get('authors', 'Unknown')}\nAbstract: {r['description']}"
        for i, r in enumerate(research)
    )

    prompt = f"""You are an AI research curator specializing in AI Agents and Reasoning.

Select the ONE most important paper that would be most interesting to explain to a non-technical person.

Consider:
1. Relevance to AI Agents, autonomous systems, or reasoning
2. How groundbreaking or novel the approach is
3. Real-world impact potential (will regular people eventually feel this?)
4. How "explainable" the concept is to a general audience

Research Papers:
{research_text}

Respond with ONLY the number (e.g., "1" or "3"). No explanation."""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=10,
            temperature=0,
        )

        selected_index = int(response.choices[0].message.content.strip()) - 1
        if 0 <= selected_index < len(research):
            return research[selected_index]
    except (ValueError, IndexError):
        pass

    # Fallback to first paper if parsing fails
    return research[0]
