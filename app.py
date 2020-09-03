from models.blog import Blog
from models.post import Post
from database import Database

Database.initialize()

blog =Blog(
    author ="pasindu",
    title ="Sample",
    description ="Sample Discrption"
)

blog.new_post()

blog.save_to_mongo()

from_database=Blog.from_mongo(blog.id)

print(blog.get_posts())
