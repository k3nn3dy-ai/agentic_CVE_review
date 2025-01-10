# CVE Review Tool

A powerful tool for automated CVE (Common Vulnerabilities and Exposures) analysis and reporting, built with [crewAI](https://crewai.com). This tool helps security professionals and developers stay informed about critical vulnerabilities by automatically fetching, analyzing, and generating comprehensive reports about recent CVEs.

## Features

- Automated fetching of CVEs from the National Vulnerability Database (NVD)
- Support for different severity levels (CRITICAL, HIGH, KNOWN_EXPLOITS)
- Intelligent analysis using AI agents
- Comprehensive report generation
- Configurable time ranges for vulnerability scanning
- Automatic JSON file generation for further analysis

## Prerequisites

- Python >=3.10 <=3.13
- [UV](https://docs.astral.sh/uv/) package manager
- OpenAI API key

## Installation

1. Install UV if you haven't already:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/cve_review/config/agents.yaml` to define your agents
- Modify `src/cve_review/config/tasks.yaml` to define your tasks
- Modify `src/cve_review/crew.py` to add your own logic, tools and specific args
- Modify `src/cve_review/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the cve_review Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The cve_review Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the CveReview Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
