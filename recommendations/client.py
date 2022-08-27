from pydoc import cli
import grpc
import recommendations_pb2_grpc
import recommendations_pb2
from recommendations_pb2 import BookCategory
from enum import Enum

# class BookCategory(Enum):
#      MYSTERY = 0
#      SCIENCE_FICTION = 1
#      SELF_HELP = 2



channel = grpc.insecure_channel("localhost:50051")
client = recommendations_pb2_grpc.RecommendationsStub(channel)
request = recommendations_pb2.RecommendationRequest(user_id=1, category=BookCategory.MYSTERY, max_results=3)
print(client.Recommend(request))

