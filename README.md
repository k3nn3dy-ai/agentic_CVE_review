# Agentic CVE Review Tool 🛡️

An intelligent security analysis platform powered by [crewAI](https://crewai.com) that automates CVE (Common Vulnerabilities and Exposures) monitoring and analysis. This tool leverages AI agents to process, analyze, and generate comprehensive security reports from the National Vulnerability Database (NVD).

![Security Analysis](https://img.shields.io/badge/Security-Analysis-blue)
![AI Powered](https://img.shields.io/badge/AI-Powered-green)
![Python](https://img.shields.io/badge/Python-3.10_|_3.11_|_3.12_|_3.13-blue)

## 🎯 Key Features

- **Automated CVE Intelligence**
  - Real-time fetching from National Vulnerability Database (NVD)
  - Smart filtering of vulnerabilities based on severity
  - Comprehensive coverage of CRITICAL and HIGH severity CVEs (7-day window)
  - Tracking of Known Exploited Vulnerabilities (KEV) (14-day window)

- **AI-Powered Analysis**
  - Intelligent vulnerability assessment
  - Impact analysis and risk scoring
  - Exploitation potential evaluation
  - Customisable analysis parameters

- **Advanced Reporting**
  - Detailed vulnerability descriptions
  - Technical impact assessments
  - Actionable mitigation strategies
  - JSON output for integration with security tools
  - Markdown reports for easy sharing

## 🚀 Quick Start

### Prerequisites

- Python >=3.10 <=3.13
- [UV](https://docs.astral.sh/uv/) package manager
- Anthropic API key for this set up, but can be configured to use the LLM of your choice

### Installation

1. Install UV package manager:
```bash
pip install uv
```

2. Clone and install dependencies:
```bash
git clone https://github.com/k3nn3dy-ai/agentic_CVE_review.git
cd cve-review-tool
crewai install
```

## 📊 Usage

Run the analysis:
```bash
crewai run
```

This will:
1. Fetch recent CVEs based on configured criteria
2. Analyze vulnerabilities using AI agents
3. Generate comprehensive reports in both JSON and Markdown formats

## 📋 Output

The tool generates several output files:

- `critical_cve_results_{date}.json`: Critical severity vulnerabilities
- `high_cve_results_{date}.json`: High severity vulnerabilities
- `known_exploits_cve_results_{date}.json`: Known exploited vulnerabilities
- `report.md`: Comprehensive security advisory report

## 🤖 AI Agents

The tool employs two specialized AI agents:

1. **CVE Researcher**
   - Specializes in vulnerability analysis
   - Assesses technical impact
   - Identifies exploitation risks

2. **Security Advisory Analyst**
   - Creates detailed vulnerability reports
   - Prioritizes threats based on CVSS scores
   - Provides actionable recommendations

## 🔄 Workflow

1. CVE data collection from NVD
2. AI-powered analysis of vulnerabilities
3. Risk assessment and prioritization
4. Comprehensive report generation
5. JSON output for integration

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests.

## Acknowledgments

Special thanks to:
- [CISA](https://www.cisa.gov/) for their cybersecurity resources and guidance
- [CrewAI](https://github.com/joaomdmoura/crewAI) for their innovative AI agent framework

Built with ❤️ using [crewAI](https://crewai.com)
