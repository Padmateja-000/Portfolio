import os
import sys

# Set up Django environment manually
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from portfolio.models import Skill, Project, Certificate, Achievement, Education, Training
from datetime import date

# Clear existing data
Skill.objects.all().delete()
Project.objects.all().delete()
Certificate.objects.all().delete()
Achievement.objects.all().delete()
Education.objects.all().delete()
Training.objects.all().delete()

# Skills
Skill.objects.create(name='Cyber Security', proficiency=85, icon_class='fas fa-shield-alt')
Skill.objects.create(name='Python', proficiency=80, icon_class='fab fa-python')
Skill.objects.create(name='Bash', proficiency=85, icon_class='fas fa-terminal')
Skill.objects.create(name='C/C++', proficiency=75, icon_class='fas fa-code')
Skill.objects.create(name='Java', proficiency=75, icon_class='fab fa-java')
Skill.objects.create(name='HTML/CSS', proficiency=80, icon_class='fab fa-html5')
Skill.objects.create(name='Tools (Nmap, Wireshark, etc.)', proficiency=85, icon_class='fas fa-tools')

# Projects
Project.objects.create(
    title='Linux System Automation & Security ToolKit',
    description='Developed an automation toolkit using Bash for system monitoring, maintenance, and security. Implemented disk storage monitoring with automated email alerts triggered by threshold limits. Created periodic configuration backup scripts using cron for system integrity and recovery. Built SSH brute-force detection logic to automatically block malicious IP addresses. Developed CPU, memory, and RAID health monitoring scripts with alerting mechanisms.',
    technologies='Bash, Cron, Linux',
    github_link='https://github.com/Padmateja-000/Security-Tool-Kit',
    image='projects/linux_security_toolkit.png',
)

Project.objects.create(
    title='SSH Honeypot and Intrusion Detection System',
    description='Configured and deployed an SSH honeypot using Cowrie on Linux to simulate vulnerable services and capture unauthorized login attempts. Developed Bash scripts to parse honeypot log files and extract attacker IP, login attempts, and activity details. Implemented threshold-based detection logic to identify repeated brute-force login attempts from suspicious sources. Integrated firewall rules using iptables to automatically block malicious IP addresses detected from honeypot logs. Created automation scripts to generate reports, trigger alerts, and combine monitoring and response actions in a single workflow.',
    technologies='Bash, Linux, Cowrie, iptables',
    github_link='https://github.com/Padmateja-000/SSH-Honeypot-and-Intrusion-Detection-System',
    image='projects/ssh_honeypot.png',
)

# Education
Education.objects.create(
    degree='Bachelor of Technology - Computer Science and Engineering',
    institution='Lovely Professional University',
    start_date=date(2023, 8, 1),
    description='CGPA: 6.80 | Punjab, India'
)

Education.objects.create(
    degree='Intermediate - MPC',
    institution='Vamsi Jr College',
    start_date=date(2021, 6, 1),
    end_date=date(2023, 3, 1),
    description='Percentage: 91 | Andhra Pradesh, India'
)

Education.objects.create(
    degree='Matriculation',
    institution='Sri Swamy Vivekananda School',
    start_date=date(2020, 3, 1),
    end_date=date(2021, 4, 1),
    description='Percentage: 100 | Andhra Pradesh, India'
)

# Training
Training.objects.create(
    title='Red Hat System Administration Summer Training',
    organization='Red Hat',
    start_date=date(2025, 6, 1),
    end_date=date(2025, 7, 1),
    description='Completed comprehensive training in Red Hat Linux system administration, covering user management, permissions, networking and SELinux. Gained hands-on experience in troubleshooting system issues and managing core Linux services. Learned system security fundamentals, including access control, process management, and log analysis. Developed shell scripting skills to automate administrative tasks and improve system efficiency. Worked with service configuration, cron jobs, and essential RHL administration tools in practical lab environments.'
)

# Certificates
Certificate.objects.create(title='Cyber Security 101', issuer='TryHackMe', date_issued=date(2026, 10, 1))
Certificate.objects.create(title='Google Cybersecurity Professional Certificate', issuer='Coursera', date_issued=date(2026, 9, 1))
Certificate.objects.create(title='Red Hat System Administration (RH124)', issuer='RedHat', date_issued=date(2025, 7, 1))
Certificate.objects.create(title='Red Hat System Administration (RH134)', issuer='RedHat', date_issued=date(2025, 7, 1))

# Achievements
Achievement.objects.create(
    title='TryHackMe - Top 4% Globally',
    description='Ranked Top 4% Globally among 4M+ participants. Achieved 20 badges and Completed 125+ rooms.',
    date=date(2025, 2, 1)
)

print("Database populated successfully with CV data!")
