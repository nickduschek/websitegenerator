import os
import frontmatter
from jinja2 import Environment, FileSystemLoader
from markdown2 import markdown

def converterenMarkdownToHTML(content, template):
    content1 = markdown(content)

    env = Environment(loader = FileSystemLoader("templates"))
    template = env.get_template(template)
    return template.render(content=content1)


def proces():
    if not os.path.exists("docs"):
        os.makedirs("docs")
    
    for file in os.listdir("pages"):
        template = "template.html"
        with open(os.path.join("pages", file), "r") as f:
            content = f.read()
            inhoud = converterenMarkdownToHTML(content, template)
        
        with open(os.path.join("docs", os.path.splitext(file)[0] + ".html"), "w") as f:
            f.write(inhoud)


def main():
    proces()

if __name__ == "__main__":
    main()