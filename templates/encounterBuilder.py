# !pip install html5tagger

from html5tagger import Document, E

# Document is for full page html
# E is a way to add small snippets of html

# Create a document
doc = Document(
    E.TitleText_,           # The first argument is for <title>, adding variable TitleText
    lang="en",              # Keyword arguments for <html> attributes

    # Just list the resources you need, no need to remember link/script tags
    _urls=[ "style.css", "favicon.png", "manifest.json" ]
)

# Upper case names are template variables. You can modify them later.
doc.Head_
doc.h1.TitleText_("Demo")   # Goes inside <h1> and updates <title> as well

# This has been a hard problem for DOM other such generators:
doc.p("A paragraph with ").a("a link", href="/files")(" and ").em("formatting")

# Use with for complex nesting (not often needed)
with doc.table(id="data"):
    doc.tr.th("First").th("Second").th("Third")
    doc.TableRows_

# Let's add something to the template variables
doc.Head._script("console.log('</script> escaping is weird')")

table = doc.TableRows
for row in range(10):
    table.tr
    for col in range(3):
        table.td(row * col)

# Or remove the table data we just added
doc.TableRows = None