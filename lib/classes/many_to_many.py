class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title_value: str):
        if hasattr(self, '_title'):
            print("Title cannot be changed after being instantiated.")
        if isinstance(title_value, str) and 5 <= len(title_value) <= 50:
            self._title = title_value
        else:
            print("Title must be a str and have between 5 and 50 characters.")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author_value):
        if isinstance(author_value, Author):
            self._author = author_value
        else:
            raise TypeError("Author must be an instance of Author")

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, magazine_value):
        if isinstance(magazine_value, Magazine):
            self._magazine = magazine_value
        else:
            raise TypeError("Magazine must be an instance of Magazine")


class Author:
    def __init__(self, name):
        if not isinstance(name, str) :
            raise TypeError("Name must be a str.")
        if len(name) == 0:
            raise ValueError("Name must have more than 0 characters.")
        self._name = name

    @property
    def name(self):
        return self._name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = set(magazine.category for magazine in self.magazines())
        return list(categories) if categories else None


class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name_value: str):
        if isinstance(name_value, str) and 2 <= len(name_value) <= 16:
            self._name = name_value
        else:
            print("Magazine name must be a str and have between 2 and 16 characters.")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category_value: str):
        if isinstance(category_value, str) and len(category_value) > 0:
            self._category = category_value
        else:
            print("Category must be a str with more than 0 characters.")

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            if article.author in author_count:
                author_count[article.author] += 1
            else:
                author_count[article.author] = 1
        result = [author for author, count in author_count.items() if count > 2]
        return result if result else None

    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        magazine_article_count = {magazine: 0 for magazine in cls.all_magazines}
        for article in Article.all:
            if article.magazine in magazine_article_count:
                magazine_article_count[article.magazine] += 1
        top_magazine = max(magazine_article_count, key=magazine_article_count.get, default=None)
        return top_magazine if magazine_article_count[top_magazine] > 0 else None
