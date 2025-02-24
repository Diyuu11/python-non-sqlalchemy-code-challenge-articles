class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")

        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)

        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def title(self):
        return self._title

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be an instance of Magazine.")
        self._magazine = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be an instance of Author.")
        self._author = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def articles(self):
        return self._articles

    def add_article(self, magazine, title):
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of Magazine.")
        return Article(self, magazine, title)

    def magazines(self):
        return list({article.magazine for article in self.articles})

    def topic_areas(self):
        if not self.articles:
            return None
        return list({magazine.category for magazine in self.magazines()})


class Magazine:
    all = []

    def __init__(self, name, category):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._name = name
        self._category = category
        self._articles = []
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be between 2 and 16 characters.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    @property
    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self.articles})

    def article_titles(self):
        return [article.title for article in self.articles] if self.articles else None

    def contributing_authors(self):
        from collections import Counter
        author_counts = Counter(article.author for article in self.articles)
        contributors = [author for author, count in author_counts.items() if count > 2]
        return contributors if contributors else None

    @classmethod
    def top_publisher(cls):
        return max(cls.all, key=lambda mag: len(mag.articles), default=None)


author = Author("Abdullahi Aden")
print(author.name)


mag = Magazine("Tech Weekly", "Technology")
print(mag.name)
print(mag.category)

article = Article(author, mag, "The Future of AI")
print(article.title)

print(article.author.name)
print(article.magazine.name)

# invalid_author = Author("") # Name validation

print(author.topic_areas())



