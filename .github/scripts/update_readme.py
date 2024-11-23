import yaml


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
    papers_yaml = "\nrecent_reads:\n"
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
