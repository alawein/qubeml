---
type: canonical
source: none
sync: none
sla: none
---

# Contributing to QubeML

Thank you for your interest in contributing to QubeML. This project follows the [alawein org contributing standards](https://github.com/alawein/alawein/blob/main/CONTRIBUTING.md). This document outlines the development process and guidelines.

## Development Workflow

### Making Changes
1. **Small, focused changes**: Work on one feature, bug fix, or improvement at a time
2. **Commit frequently**: Make commits after completing each logical unit of work
3. **Clear commit messages**: Use descriptive messages that explain what and why
4. **Test before committing**: Ensure all tests pass before making commits
5. **One feature per commit**: Avoid bundling multiple unrelated changes
6. **Pull regularly**: Use `git pull` to sync with remote changes

### Code Quality
- Follow existing code style and conventions
- Add tests for new functionality
- Update documentation as needed
- Run the test suite: `python3 -m pytest tests/ -v`

### Project Structure
- `src/`: Core utilities and shared functions
- `quantum_computing/`: Quantum computing tutorials and examples
- `materials_informatics/`: Materials science ML approaches
- `integrative_projects/`: Combined quantum-materials applications
- `tests/`: Unit tests for all modules
- `data/`: Example datasets and samples

### Getting Started
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run tests to ensure setup works: `python3 -m pytest tests/ -v`
4. Start with small improvements or bug fixes
5. Follow the established workflow for contributions

### Best Practices
- Keep changes atomic and reversible
- Write clear, self-documenting code
- Add docstrings for new functions and classes
- Include type hints where appropriate
- Update relevant documentation

## Questions?
Feel free to open an issue for questions about the codebase or development process.