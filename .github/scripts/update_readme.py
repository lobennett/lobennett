import yaml
import pytz
from datetime import datetime, timedelta

def calculate_streak(papers):
    """Calculate the number of consecutive days papers have been read."""
    if not papers:
        return 0
    
    # Convert to PST timezone
    pst = pytz.timezone('America/Los_Angeles')
    today = datetime.now(pst).date()
    
    # Sort papers by read date
    read_dates = [datetime.strptime(p['read_on'], '%Y-%m-%d').date() 
                  for p in sorted(papers, key=lambda x: x['read_on'], reverse=True)]
    
    if (today - read_dates[0]).days > 1:  # If no paper read yesterday or today
        return 0
    
    streak = 1
    for i in range(len(read_dates) - 1):
        if (read_dates[i] - read_dates[i + 1]).days == 1:
            streak += 1
        else:
            break
    
    return streak

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
    
    recent_papers = [
        {"title": paper["title"], "authors": paper["authors"]} 
        for paper in sorted_papers[:5]
    ]

    # Read current README
    with open("README.md", "r") as file:
        readme_content = file.read()

    # Find the end of the YAML block
    yaml_end = readme_content.find("```", readme_content.find("```yaml") + 7)

    # Format the papers as YAML using yaml.dump for proper YAML formatting
    papers_yaml = "\ndays_read_consecutively: " + str(streak) + "\nrecent_reads:\n"
    for paper in recent_papers:
        papers_yaml += f"  - title: {yaml.dump(paper['title'], default_style='\"').strip()}\n"
        papers_yaml += f"    authors: {yaml.dump(paper['authors'], default_style='\"').strip()}\n"

    # Insert the papers list before the end of the YAML block
    new_content = readme_content[:yaml_end] + papers_yaml + readme_content[yaml_end:]

    # Write updated README
    with open("README.md", "w") as file:
        file.write(new_content)


if __name__ == "__main__":
    main()
