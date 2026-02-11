from factory.toy import Toy
from factory.book import Book
from factory.videoGame import VideoGame

class GiftFactory:
   @staticmethod
   def create_gift(gift_type):
     if gift_type == "toy":
       return Toy()
     if gift_type == "book":
        return Book()
     if gift_type == "video game":
        return VideoGame()
     raise ValueError("Unknown gift type")