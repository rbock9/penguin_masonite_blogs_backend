"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog


class BlogTableSeeder(Seeder):
    def run(self):
        Blog.create({"title": "Blog 1", "body": "This is Blog 1"})
        Blog.create({"title": "Blog 2", "body": "This is Blog 2"})
        Blog.create({"title": "Blog 3", "body": "This is Blog 3"})
