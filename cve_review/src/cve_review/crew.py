from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from cve_review.tools.crew_cve_tool import fetch_cve_data_tool
from crewai_tools import FileReadTool


@CrewBase
class CveReview():
	"""CveReview crew"""
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'
	
	fetch_cve_data_tool = fetch_cve_data_tool
	file_read_tool = FileReadTool()

	@agent
	def cve_researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['cve_researcher'],
			tools=[self.fetch_cve_data_tool],
			verbose=False
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			tools=[self.file_read_tool],
				verbose=False
		)

	@task
	def critical_cve_research_task(self) -> Task:
		return Task(
			config=self.tasks_config['critical_cve_research_task'],
		)

	@task
	def high_cve_research_task(self) -> Task:
		return Task(
			config=self.tasks_config['high_cve_research_task'],
		)

	@task
	def known_exploits_cve_research_task(self) -> Task:
		return Task(
			config=self.tasks_config['known_exploits_cve_research_task'],
		)

	@task
	def extract_critical_cve_task(self) -> Task:
		return Task(
			config=self.tasks_config['extract_critical_cve_task'],
			output_file='critical_cve_results.md'
		)

	@task
	def extract_high_cve_task(self) -> Task:
		return Task(
			config=self.tasks_config['extract_high_cve_task'],
			output_file='high_cve_results.md'
		)

	@task
	def extract_known_exploits_cve_task(self) -> Task:
		return Task(
			config=self.tasks_config['extract_known_exploits_cve_task'],
			output_file='known_exploits_cve_results.md'
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='Vulnerability_Report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the CveReview crew"""
		print("Starting crew creation...")  # Debug print
		
		crew_instance = Crew(
			agents=self.agents,
			tasks=self.tasks,
			process=Process.sequential,
			verbose=True,
			output_log_file='cve_logs.txt'
		)
		
		print("Crew created, starting execution...")  # Debug print
		result = crew_instance.kickoff()
		print(f"Crew execution completed with result: {result}")  # Debug print
		
		return result
