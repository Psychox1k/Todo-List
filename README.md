# Todo-List

A simple and intuitive task management web application built with Django. Organize your daily tasks, set deadlines, and track your progress efficiently.

## Features

- **Add Tasks** - Create new tasks with detailed descriptions
- **Tag System** - Organize tasks with custom tags
- **Task Completion** - Mark tasks as done/undone with one click
- **Deadlines** - Set and track task deadlines
- **Edit Tasks** - Update task content, tags, and deadlines
- **Delete Tasks** - Remove completed or unwanted tasks
- **Responsive Design** - Works on desktop and mobile devices

## Tech Stack

- **Backend**: Python 3.12, Django 5.2
- **Frontend**: HTML5, CSS3, Bootstrap 4
- **Forms**: Django Crispy Forms
- **Database**: SQLite (default)

## Getting Started

### Prerequisites

- Python 3.12+
- Git

## Installation

### Clone the repository
```bash
git clone https://github.com/Psychox1k/todo-list.git
cd todo-list
```

### Create virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```
### Install dependencies
```bash
pip install -r requirements.txt
```
### Run migrations
```bash
python manage.py migrate
```
### Start development server
```bash
python manage.py runserver
```
### Open your browser
Navigate to http://127.0.0.1:8000/

# Contributing

### Fork the project
- Create your feature branch 
    ```bash 
    git checkout -b feature/amazing-feature)
    ```
- Commit your changes
    ```bash
    git commit -m 'feat: add amazing feature'
    ```
Push to the branch (git push origin feature/amazing-feature)
Open a Pull Request

## License
This project is open source and available under the MIT License.
## Author
[Psychox1k](https://github.com/Psychox1k)(Kyrylo Zhyhariev)
