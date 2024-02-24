title_of_an_article = input()
content_of_that_article = input()
print("<h1>")
print(f"    {title_of_an_article}")
print("</h1>")
print("<article>")
print(f"    {content_of_that_article}")
print("</article>")
while True:
    comments = input()
    if comments == "end of comments":
        break
    print('<div>')
    print(f'    {comments}')
    print('</div>')