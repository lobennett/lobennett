import yaml
import pytz
from datetime import datetime


def calculate_streak(papers):
    """Calculate the number of consecutive days papers have been read."""
    if not papers:
        return 0

    # Convert to PST timezone
    pst = pytz.timezone("America/Los_Angeles")
    today = datetime.now(pst).date()

    # Extract unique read dates and sort them in descending order
    read_dates = sorted(
        {datetime.strptime(p["read_on"], "%Y-%m-%d").date() for p in papers},
        reverse=True,
    )

    if not read_dates:  # If no valid dates
        return 0

    # If the most recent paper is not from today, streak is broken
    if read_dates[0] != today:
        return 0

    streak = 1
    for i in range(len(read_dates) - 1):
        if (read_dates[i] - read_dates[i + 1]).days == 1:
            streak += 1
        else:
            break

    return streak


def papers_this_month(papers):
    """Calculate the number of papers read in the current month."""
    if not papers:
        return 0

    pst = pytz.timezone("America/Los_Angeles")
    today = datetime.now(pst)
    current_month = today.month
    current_year = today.year

    monthly_papers = [
        p
        for p in papers
        if datetime.strptime(p["read_on"], "%Y-%m-%d").month == current_month
        and datetime.strptime(p["read_on"], "%Y-%m-%d").year == current_year
    ]

    return len(monthly_papers)


def main():
    """
    Update the README.md file with the most recent papers from papers.yml.
    """

    # Read papers.yml
    with open("papers.yml", "r") as file:
        papers_data = yaml.safe_load(file)

    # Get the 5 most recent papers with title and authors
    sorted_papers = sorted(
        papers_data["recent_reads"], key=lambda x: x["read_on"], reverse=True
    )

    # Calculate streak
    streak = calculate_streak(papers_data["recent_reads"])

    # Calculate papers read this month
    monthly_count = papers_this_month(papers_data["recent_reads"])

    recent_papers = [
        {"title": paper["title"], "authors": paper["authors"]}
        for paper in sorted_papers[:5]
    ]

    # Read current README
    with open("README.md", "r") as file:
        readme_content = file.read()

    # Find the scholarship section boundaries
    scholarship_start = readme_content.find("papers_this_month:")
    scholarship_end = readme_content.find("```", scholarship_start)

    # Get the content before and after the scholarship section
    before_scholarship = readme_content[:scholarship_start]
    after_scholarship = readme_content[scholarship_end:]

    # Format the papers as YAML
    papers_yaml = (
        f"papers_this_month: {monthly_count}\n"
        f"days_read_consecutively: {streak}\n"
        "recent_reads:\n"
    )
    for i, paper in enumerate(recent_papers):
        papers_yaml += f"  - title: '{paper['title']}'\n"
        papers_yaml += f"    authors: {paper['authors']}" + (
            "\n" if i < len(recent_papers) - 1 else ""
        )

    # Combine all parts with the new content
    new_content = before_scholarship + papers_yaml + after_scholarship

    # Write updated README
    with open("README.md", "w") as file:
        file.write(new_content)


if __name__ == "__main__":
    main()
