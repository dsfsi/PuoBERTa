# Contributing to PuoBERTa

Thank you for your interest in contributing to PuoBERTa! This document provides guidelines and instructions for contributing to the project.

## Table of Contents

- [Ways to Contribute](#ways-to-contribute)
- [Getting Started](#getting-started)
- [Development Guidelines](#development-guidelines)
- [Submitting Contributions](#submitting-contributions)
- [Code of Conduct](#code-of-conduct)
- [Questions and Support](#questions-and-support)

## Ways to Contribute

There are many ways you can contribute to PuoBERTa:

### 1. Code Contributions
- Add new usage examples
- Improve documentation
- Fix bugs in example scripts
- Add support for new downstream tasks
- Optimize existing code

### 2. Dataset Contributions
- Report issues with the Daily News Dikgang dataset
- Suggest new datasets for Setswana NLP tasks
- Help with data cleaning and validation

### 3. Documentation
- Improve README files
- Add tutorials and guides
- Translate documentation
- Fix typos and clarify instructions

### 4. Model Improvements
- Fine-tune PuoBERTa for new tasks
- Share your trained models
- Report model performance on different tasks
- Suggest improvements to training procedures

### 5. Community Support
- Answer questions in issues
- Share your use cases
- Provide feedback on the model
- Help others get started

## Getting Started

### Prerequisites

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/PuoBERTa.git
   cd PuoBERTa
   ```

3. **Set up the development environment**:
   ```bash
   # Create a conda environment (recommended)
   make create_environment

   # Or use pip with virtualenv
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   # Install dependencies
   make requirements
   # Or: pip install -r requirements.txt
   ```

4. **Add upstream remote**:
   ```bash
   git remote add upstream https://github.com/dsfsi/PuoBERTa.git
   ```

### Setting Up Your Branch

1. **Update your fork** with the latest changes:
   ```bash
   git checkout master
   git pull upstream master
   ```

2. **Create a new branch** for your contribution:
   ```bash
   git checkout -b feature/your-feature-name
   # Or for bug fixes:
   git checkout -b fix/issue-description
   ```

## Development Guidelines

### Code Style

- Follow **PEP 8** style guidelines for Python code
- Use meaningful variable and function names
- Add comments to explain complex logic
- Keep functions focused and modular

### Testing

Before submitting your contribution:

1. **Test your code**:
   ```bash
   # Run the test environment script
   python test_environment.py

   # Test your specific example/script
   python examples/your_example.py
   ```

2. **Lint your code**:
   ```bash
   make lint
   ```

### Documentation

- Update relevant README files when adding new features
- Add docstrings to new functions and classes
- Include usage examples for new functionality
- Keep documentation clear and concise

## Submitting Contributions

### Pull Request Process

1. **Commit your changes** with clear, descriptive messages:
   ```bash
   git add .
   git commit -m "Add: Brief description of your changes"
   ```

   Use conventional commit prefixes:
   - `Add:` for new features
   - `Fix:` for bug fixes
   - `Update:` for improvements to existing features
   - `Docs:` for documentation changes
   - `Refactor:` for code refactoring

2. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Open a Pull Request**:
   - Go to the original PuoBERTa repository on GitHub
   - Click "New Pull Request"
   - Select your branch
   - Fill in the PR template with:
     - Description of changes
     - Related issue numbers (if applicable)
     - Testing performed
     - Screenshots (if UI changes)

### Pull Request Guidelines

- **One feature per PR**: Keep PRs focused on a single feature or fix
- **Clear description**: Explain what changes you made and why
- **Reference issues**: Link to related issues using `Fixes #123` or `Relates to #456`
- **Update documentation**: Include relevant documentation updates
- **Test your changes**: Ensure all examples and tests work
- **Be responsive**: Respond to review feedback promptly

## Example Contributions

### Adding a New Example

1. Create your example script in the `examples/` directory:
   ```python
   # examples/05_your_example.py
   """
   Brief description of what this example demonstrates.
   """

   def main():
       # Your example code
       pass

   if __name__ == "__main__":
       main()
   ```

2. Update `examples/README.md` to include your example:
   ```markdown
   ### 5. Your Example Title (`05_your_example.py`)

   Description of what this example does.

   \```bash
   python examples/05_your_example.py
   \```
   ```

3. Test your example thoroughly
4. Submit a PR with your changes

### Improving Documentation

1. Identify the documentation that needs improvement
2. Make your changes
3. Preview markdown files to ensure formatting is correct
4. Submit a PR with clear description of improvements

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inclusive environment for all contributors, regardless of:
- Background
- Identity
- Experience level
- Nationality
- Language proficiency

### Expected Behavior

- Be respectful and considerate
- Provide constructive feedback
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior

- Harassment or discrimination
- Trolling or insulting comments
- Personal or political attacks
- Publishing others' private information
- Other unethical or unprofessional conduct

### Enforcement

Instances of unacceptable behavior may be reported to the project maintainers. All complaints will be reviewed and investigated promptly and fairly.

## Questions and Support

### Getting Help

- **Issues**: Open an issue for bugs or feature requests
- **Discussions**: Use GitHub Discussions for questions
- **Email**: Contact the maintainers at vukosi.marivate@cs.up.ac.za
- **Feedback Form**: [DSFSI Resource Feedback Form](https://docs.google.com/forms/d/e/1FAIpQLSf7S36dyAUPx2egmXbFpnTBuzoRulhL5Elu-N1eoMhaO7v10w/formResponse)

### Useful Resources

- [Main README](README.md)
- [HuggingFace Model](https://huggingface.co/dsfsi/PuoBERTa)
- [Research Paper](https://arxiv.org/abs/2310.09141)
- [Interactive Demo](https://huggingface.co/spaces/dsfsi/PuoBERTaSpace)
- [Transformers Documentation](https://huggingface.co/docs/transformers/)

## Recognition

Contributors will be:
- Listed in release notes
- Acknowledged in relevant documentation
- Recognized for significant contributions

Thank you for contributing to PuoBERTa and advancing Setswana NLP!

---

**Note**: By contributing to this project, you agree that your contributions will be licensed under the same license as the project (CC BY 4.0 for the model).
