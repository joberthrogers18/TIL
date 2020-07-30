import wikipedia

result = wikipedia.page("Atari")
print(result.summary)


print('\n\n', result.title)
print(result.url)
print(result.content)

wikipedia.set_lang("fr")
print('\n\n',  wikipedia.page("Google").summary)

print('\n\n', wikipedia.WikipediaPage(title="Facebook").html())

print('\n\n Images:')
print(wikipedia.WikipediaPage(title="Facebook").images)

print('\n\n Parent Id:')
print(wikipedia.WikipediaPage(title="Facebook").parent_id)

print('\n\n  Sections:')
print(wikipedia.WikipediaPage(title="Facebook").sections)

