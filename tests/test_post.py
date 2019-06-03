import unittest
from app.models import Post
from app import db

class TestPost(unittest.TestCase):
    def setUp(self):
        self.new_post = Post(id=2, post='hellohello', user_id=12345, Comments='boom')

    def tearDown(self):
        Post.query.delete()
    def test_instance(self):
        self.assertTrue(isinstance(self.new_post, Post))

    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.id, 2)
        self.assertEquals(self.new_post.post, 'hellohello')
        self.assertEquals(self.new_post.user_id, 12345)
        self.assertEquals(self.new_post.Comments, 'boom')

    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all()) > 0)

    def test_get_post_by_id(self):
        self.new_post.save_post()
        got_posts = Post.get_posts(12345)
        self.assertTrue(len(got_posts) == 1)