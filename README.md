# Ai_Webscraper
## About the Project 🤖
<div align="center"> <br/><img src="https://your-screenshot-url.com/main.png" alt="screenshot" /><br/><br/> <p align="justify"> This AI Webscraper captures content from any website by scraping all the DOM elements. It then allows users to input queries that are intelligently handled by a language model (LLM), offering relevant and structured responses based on the scraped content. Whether for automated data extraction or dynamic analysis, the tool simplifies how users interact with web data. </p> </div>
```markdown

## Scope 🌐
i. Extract all elements from a web page and convert them into structured formats (HTML, CSV, JSON).  
ii. Enable intelligent querying of scraped data through a connected language model (LLM) for deeper insights.  
iii. Help automate tasks such as content monitoring, SEO auditing, and competitive analysis.  
iv. Provide real-time data parsing for content-heavy websites, enhancing data-driven decision-making.  
v. Useful for students, researchers, and developers working with web automation and scraping tools.  

---

## Tech Stack 🛠️
<details>  
<summary>Frontend</summary>  
<ul>  
<li><a href="https://streamlit.io/">Streamlit</a></li>  
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/HTML">HTML</a></li>  
<li><a href="https://developer.mozilla.org/en-US/docs/Web/CSS">CSS</a></li>  
<li><a href="https://developer.mozilla.org/en-US/docs/Learn/JavaScript">JavaScript</a></li>  
</ul>  
</details>  

<details>  
<summary>Backend</summary>  
<ul>  
<li><a href="https://www.python.org/">Python</a></li>  
<li><a href="https://flask.palletsprojects.com/">Flask</a></li>  
</ul>  
</details>  

<details>  
<summary>Modules</summary>  
<ul>  
<li><a href="https://beautiful-soup-4.readthedocs.io/">BeautifulSoup</a></li>  
<li><a href="https://pandas.pydata.org/">pandas</a></li>  
<li><a href="https://www.selenium.dev/">Selenium</a></li>  
<li><a href="https://www.openai.com/">OpenAI API</a></li>  
</ul>  
</details>  

---

## Features ⚙️

### User Functions:
- Input any website URL for scraping.  
- Parse and display the entire DOM structure.  
- Query specific content via LLM-powered prompt.  
- Export scraped data into various formats (CSV/JSON).  

### Admin Functions:
- Monitor scraped data usage and query logs.  
- View user statistics and feedback.  
- Download query and usage reports in CSV.  

---

## Requirements 📋
1. **Python 3.10+**: [Download](https://www.python.org/downloads/).  
2. **ChromeDriver**: [Install Selenium Driver](https://chromedriver.chromium.org/downloads).  
3. **Visual Studio Code**: [Download](https://code.visualstudio.com/Download).  

# Setup & Installation 🚀

```bash
# Clone the repository
git clone https://github.com/your-username/AI-WebScraper.git
cd AI-WebScraper

# Create and activate a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Set up MongoDB and configure credentials in config.py

# Start the web app
streamlit run app.py
```
## Known Issues 🚧
- If encountering `Selenium WebDriverException`, ensure ChromeDriver matches your browser version.  
- Internet connectivity is required for querying the LLM.  

---

## Usage 🎯
1. Enter a URL in the input field and click **Scrape**.  
2. View parsed elements in the **DOM Viewer**.  
3. Ask questions about the content using the **LLM Query** feature.  
4. Download results in **CSV** or **JSON** format.  

---

## Roadmap 🚀
- [ ] Add support for CSV/JSON exports.  
- [ ] Integrate OpenAI’s GPT for query handling.  
- [ ] Add OAuth-based user login.  
- [ ] Enhance UI for mobile devices.  

---

## Contributing 🤝
Pull requests are welcome! For major changes, please open an issue to discuss proposed changes.  

---

## Preview 👀
![image](https://github.com/user-attachments/assets/189aab8e-5e3c-40d4-b6de-77641380fe80)

---

## Acknowledgements 🎉
- [Your Mentor’s Name] for project guidance  
- [BeautifulSoup Documentation](https://beautiful-soup-4.readthedocs.io/)  
- [Selenium Documentation](https://www.selenium.dev/documentation/)  

---

## License 📄
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

