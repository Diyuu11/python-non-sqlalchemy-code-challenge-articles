class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author) or not isinstance(magazine, Magazine):
            raise Exception("Author and Magazine must be valid instances.")
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise Exception("The title must be a string between 5 and 50 characters.")

        self.author = author
        self.magazine = magazine
        self.title = title

        # Register the article with the author's and magazine's list of articles
        author._articles.append(self)
        magazine._articles.append(self)

        def name():
            return self.name


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Author name must be a non-empty string.")
        self.name = name
        self._articles = []

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise Exception("The magazine must be an instance of the Magazine class.")
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise Exception("The title must be a string between 5 and 50 characters.")
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise Exception("Magazine name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Category must be a non-empty string.")

        self.name = name
        self._category = category
        self._articles = []

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise Exception("Category must be a non-empty string.")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        author_count = {}
        for article in self._articles:
            author_count[article.author] = author_count.get(article.author, 0) + 1
        contributing_authors = [author for author, count in author_count.items() if count > 2]
        return contributing_authors if contributing_authors else None

    author_1=Author("hamdi")
    print(author_1.name)