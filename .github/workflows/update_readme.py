import yaml


def main():
    """
    Update the README.md file with the most recent papers from papers.yml.
    """

    # Read papers.yml
    with open("papers.yml", "r") as file:
        papers_data = yaml.safe_load(file)

    # Get the 5 most recent paper titles, sorted by read_on date from most recent to least
    sorted_papers = sorted(
        papers_data["recent_reads"], key=lambda x: x["read_on"], reverse=True
    )
    recent_titles = [paper["title"] for paper in sorted_papers[:5]]

    # Read current README
    with open("README.md", "r") as file:
        readme_content = file.read()

    # Find the end of the YAML block
    yaml_end = readme_content.find("```", readme_content.find("```yaml") + 7)

    # Format the paper titles as YAML
    papers_yaml = "\n  recent_reads: " + str(recent_titles).replace("'", '"')

    # Insert the papers list before the end of the YAML block
    new_content = readme_content[:yaml_end] + papers_yaml + readme_content[yaml_end:]

    # Write updated README
    with open("README.md", "w") as file:
        file.write(new_content)


if __name__ == "__main__":
    main()
